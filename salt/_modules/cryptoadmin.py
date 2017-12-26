"""
"""

log = logging.getLogger(__name__)

def _run_crypto_cmd(cmd):
    """

    """

    working_dir = __pillar__.get('app_dir') 
    user = __pillar__.get('username')
    cmd_response = __salt__['cmd.run_all'](cmd,
                                           cwd='{0}'.format(working_dir),
                                           runas='{0}'.format(user))

    return cmd_response

def status():
    """
    Get the status of the process

    CLI Example::

        salt 'crypto-delegate1' cryptoadmin.status
    """

    if __grains__.get('liskenv'):
        cmd_run = 'bash lisk.sh status'
    elif __grains__.get('shiftenv'):
        cmd_run = 'bash shift_manager.bash status'
    elif __grains__.get('oxyenv'):
        cmd_run = 'bash oxy_manager.bash status'
    elif __grains__.get('lwfenv'):
        cmd_run = 'bash lwf_manager.bash status'
    else:
        return 'Platform not supported'

    response = _run_crypto_cmd(cmd_run)

    return response

def help():
    """
    Get the help messages from the platform shell tool

    CLI Example::

        salt 'crypto-delegate1' cryptoadmin.help
    """
    if __grains__.get('liskenv'):
        cmd_run = 'bash lisk.sh help'
    elif __grains__.get('shiftenv'):
        cmd_run = 'bash shift_manager.bash'
    elif __grains__.get('oxyenv'):
        cmd_run = 'bash oxy_manager.bash'
    elif __grains__.get('lwfenv'):
        cmd_run = 'bash lwf_manager.bash'
    else:
        return 'Platform not supported'

    response = _run_crypto_cmd(cmd_run)

    return response

def stop():
    """
    Stop the crypto platform process

    CLI Example::

        salt 'crypto-delegate1' cryptoadmin.stop
    """
    if __grains__.get('liskenv'):
        cmd_run = 'bash lisk.sh stop'
    elif __grains__.get('shiftenv'):
        cmd_run = 'bash shift_manager.bash stop'
    elif __grains__.get('oxyenv'):
        cmd_run = 'bash oxy_manager.bash stop'
    elif __grains__.get('lwfenv'):
        cmd_run = 'bash lwf_manager.bash stop'
    else:
        return 'Platform not supported'

    response = _run_crypto_cmd(cmd_run)

    return response

def start():
    """
    Start the crypto platform process

    CLI Example::

        salt 'crypto-delegate1' cryptoadmin.start
    """
    if __grains__.get('liskenv'):
        cmd_run = 'bash lisk.sh start'
    elif __grains__.get('shiftenv'):
        cmd_run = 'bash shift_manager.bash start'
    elif __grains__.get('oxyenv'):
        cmd_run = 'bash oxy_manager.bash start'
    elif __grains__.get('lwfenv'):
        cmd_run = 'bash lwf_manager.bash start'
    else:
        return 'Platform not supported'

    response = _run_crypto_cmd(cmd_run)

    return response

def reload():
    """
    Reload the crypto platform process

    CLI Example::

        salt 'crypto-delegate1' cryptoadmin.reload
    """
    if __grains__.get('liskenv'):
        cmd_run = 'bash lisk.sh reload'
    elif __grains__.get('shiftenv'):
        cmd_run = 'bash shift_manager.bash reload'
    elif __grains__.get('oxyenv'):
        cmd_run = 'bash oxy_manager.bash reload'
    elif __grains__.get('lwfenv'):
        cmd_run = 'bash lwf_manager.bash reload'
    else:
        return 'Platform not supported'

    response = _run_crypto_cmd(cmd_run)

    return response

def rebuild():
    """
    Rebuild the DPOS crypto process

    CLI Example::

        salt '*' cryptoadmin.rebuild
    """

    if __grains__.get('shiftenv'):
        cmd_run = 'echo "y" | bash shift_manager.bash rebuild'
    elif __grains__.get('oxyenv'):
        cmd_run = 'echo "y" | bash oxy_manager.bash rebuild'
    elif __grains__.get('lwfenv'):
        cmd_run = 'echo "y" | bash lwf_manager.bash rebuild'
    elif __grains__.get('liskenv') and __grains__.get('liskenv') == 'main':
        cmd_run = 'bash lisk.sh rebuild {0}'.format(__pillar__.get('snapshot_service_main'))
    else:
        return 'Platform not supported'

    response = _run_crypto_cmd(cmd_run)

    return response

def update():
    """
    Update the DPOS crypto process

    CLI Example::

        salt '*' cryptoadmin.update
    """

    if __grains__.get('shiftenv'):
        cmd_run = 'bash shift_manager.bash update_client'
    elif __grains__.get('oxyenv'):
        cmd_run = 'bash oxy_manager.bash update_client'
    elif __grains__.get('lwfenv'):
        cmd_run = 'bash lwf_manager.bash update_client'
    else:
        return 'Platform not supported'

    response = _run_crypto_cmd(cmd_run)

    return response

def update_wallet():
    """
    Update the shift wallet on a given node

    CLI Example::

        salt '*' cryptoadmin.update_wallet
    """

    if __grains__.get('shiftenv'):
        cmd_run = 'bash shift_manager.bash update_wallet'
    else:
        return 'Platform not supported'

    response = _run_crypto_cmd(cmd_run)

    return response
