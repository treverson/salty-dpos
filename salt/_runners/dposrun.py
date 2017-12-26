# -*- coding: utf-8 -*-
"""
DPOS Runner
==================

:codeauthor: slasheks <slasheks@protonmail.com>

To use this runner, set up the secret in pillar data
and make that available to the minion where you want to
enable foriging. 

.. code-block:: yaml
    secret: <delegate pass>

To use forge notify you will need a slack api key accessible
to the minion on the master.

.. code-block:: yaml
    slack_api: <api_key>

.. note::
    Best practice would be to use gpg to encrypt the secret and 
    have salt decrypt at runtime
"""
import time
import datetime
import logging
import salt.client
import salt.runner

log = logging.getLogger(__name__)

def _client_bootstrap():
    """
    """
    # __opts__ adds _master to the id
    return salt.client.LocalClient(__opts__['conf_file']), __opts__.get('id').split('_')[0]

def _runner_bootstrap():
    """
    """
    opts = __opts__
    opts['quiet'] = True
    return salt.runner.RunnerClient(opts)

def forging_notify(dpos_coin, delegate, channel='autopost', from_name='salt-slacker'):
    """
    Notify via slack if delegate is not forging

    CLI Example:

    .. code-block:: bash

        salt-run dposrun.forging_notify lisk slasheks
    """
    response = is_forging(dpos_coin, delegate)
    forging = any(y == True for y in response.values())


    if forging is False:

        client, master_id = _client_bootstrap()
        message = 'Hey @{0} ! No one is forging for {1}'.format(delegate,
                                                                dpos_coin)
        key = client.cmd(master_id, 'pillar.get', ['slack_api'])
        api_key = key.get(master_id).strip()

        if not api_key:

            return "Slack API key not defined in Pillar data."

        test = client.cmd(master_id, 'slack.post_message',
                          [channel, message, from_name, api_key])

        return test

    else:

        return response

def missed_block_notify(dpos_coin, delegate, channel='autopost', from_name='salt-slacker'):
    """
    Notify via slack if last block was generated more than 20m ago

    CLI Example:

    .. code-block:: bash

        salt-run dposrun.missed_block_notify lisk slasheks
    """
    #TODO catch when someone misstypes delegate name

    allm = []

    # Get the nodes
    response = is_forging(dpos_coin, delegate)

    client, master_id = _client_bootstrap()

    # Get the highest height node?
    for minion in response:
        test = client.cmd(minion, 'salty_dpos_get.height')
        allm.append(test)

    highest_node = max(allm, key=lambda x:x).keys()[0]

    test = client.cmd(highest_node,
                      'salty_dpos_get.last_forged_block',
                      [delegate])

    time_now = time.time()

    block_time = int(test[highest_node]['timestamp']) + 1464109200
    time_diff = time_now - block_time

    # 20 minutes is 1200 seconds
    if time_diff > 1200:

        human_time = datetime.datetime.fromtimestamp(block_time)\
                .strftime('%Y-%m-%d %H:%M:%S')

        message = 'Hey @{} ! Last block forged at: {}'.format(delegate,
                                                              human_time)

        key = client.cmd(master_id, 'pillar.get', ['slack_api'])
        api_key = key.get(master_id)

        if not api_key:
            return "Slack API key not defined in Pillar data."

        test = client.cmd(master_id, 'slack.post_message',
                          [channel, message, from_name, api_key])

        return test

    else:

        return "No diff", time_diff



    return response

def is_forging(dpos_coin, delegate, blacklist=[]):
    """
    Check if a delegate is forging based on DPOS system and delegate name

    CLI Example:

    .. code-block:: bash

        salt-run dposrun.is_forging lisk slasheks
    """
    allm = {}
    minions_by_grains = []

    runner = _runner_bootstrap()
    client, _ = _client_bootstrap()

    # Get cached grains. env is set in the begginig. Safe bet. 
    resp = runner.cmd('cache.grains', ['*'])

    for r,asd in resp.iteritems():
        if asd.get('{}env'.format(dpos_coin)):
            minions_by_grains.append(asd.get('id'))

    # pop blacklist minions from minion list
    filtered_minions = [x for x in minions_by_grains if x not in blacklist]

    for minion in filtered_minions:

        test = client.cmd(minion, 'salty_dpos_get.forging_status', [delegate])

        if test[minion] is True or test[minion] is False:

            allm[minion] = test[minion]

    return allm

def enable_forging(dpos_coin, delegate, node=False, force_enable=False, blacklist=[]):
    """
    Enable delegate forging based on DPOS system and delegate name

    CLI Example:

    .. code-block:: bash

        salt-run dposrun.enable_forging lisk slasheks
    """
    #TODO Need to know how many nodes to know if all are connected
    #TODO if given a node forge there
    #TODO Match key to delegate

    client, master_id = _client_bootstrap()

    runner_resp = {'success':False}

    # Check if forging is enabled on at least one node
    response = is_forging(dpos_coin, delegate, blacklist)
    forging = any(y == True for y in response.values())

    # If forging is enabled and not forging return
    if forging is True and force_enable is False:

        runner_resp['forging'] = [x for x,y in response.iteritems() if y is True]

        if len(runner_resp['forging']) == 2:

            runner_resp['message'] = "More than one. Need to disable somewhere... "

            #worse node is last node, not necessarily the worse
            worse_node = runner_resp['forging'][-1]

            # Try to disable forging on last node
            test = client.cmd(worse_node, 'salty_dpos_post.disable_forging')

            if test[worse_node].get('success'):
                runner_resp['message'] += "Disabled forging on {}".format(worse_node)
            else:
                runner_resp['message'] += "Failed to disable forging on {}".format(worse_node)

        elif len(runner_resp['forging']) > 2:

           runner_resp['message'] = "More than one. Need to disable somewhere... "
           result = disable_forging(dpos_coin, delegate, blacklist=blacklist)
           runner_resp['message'] += "Disabled forging on {}".format(" ".join(result))

        else:

            runner_resp['message'] = 'Already forging on one node'
            return runner_resp

    elif forging is True and force_enable is True:

        #TODO
        # disable forging on enabled host
        # enable forging on other host
        response['message'] = 'Failover from {} to {}'
        return response

    elif forging is False and force_enable is False:

        nodes = []
        for node in response:
            test = client.cmd(node, 'salty_dpos_get.failover_candidate')
            log.debug(test)
            nodes.append(client.cmd(node, 'salty_dpos_get.failover_candidate'))

        # Grab the first node if there are nodes
        # enable forging on best host
        if len(nodes) >= 1:

            forging_node = nodes[0].keys()[0]

            test = client.cmd(forging_node, 'salty_dpos_post.enable_forging')

            if test[forging_node].get('success'):
                runner_resp['message'] = 'Enabled forging on {}'.format(forging_node)
                runner_resp['success'] = True
            else:
                runner_resp['message'] = 'Failed to enable forging on {}'.format(forging_node)

        elif len(nodes) == 0:

            runner_resp['message'] = 'Could not find any failover candidates'

        return runner_resp

    else:

        #TODO
        response['message'] = 'Something else'
        return response


def disable_forging(dpos_coin, delegate, node=None, blacklist=[]):
    """
    Disable delegate forging based on DPOS system and delegate name

    CLI Example:

    .. code-block:: bash

        salt-run dposrun.disable_forging lisk slasheks
    """

    runner_resp = {}

    response = is_forging(dpos_coin, delegate, blacklist)

    client, master_id = _client_bootstrap()

    forging_nodes = [x for x, y in response.iteritems() if y is True]

    for node in forging_nodes:
        runner_resp[node] = client.cmd(node, 'salty_dpos_post.disable_forging')

    if not runner_resp:
        runner_resp['message'] = 'Could not find any nodes forging for delegate {}'\
            .format(delegate)

    return runner_resp

