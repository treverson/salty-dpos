"""
"""
import logging

log = logging.getLogger(__name__)

def _run_crypto_cmd(cmd, working_dir=None, user=None):
    """

    """

    if working_dir is None:
        working_dir = __pillar__.get('app_dir') 

    if user is None:
        user = __pillar__.get('username')

    allowed_users = ['postgres', __pillar__.get('username')]

    if user not in allowed_users:
        return "User not allowed"

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

def app_logs(amount=10):
    """
    Tail the logs of the application process

    CLI Example::

        salt 'crypto-delegate1' cryptoadmin.app_logs
        salt 'crypto-delegate1' cryptoadmin.app_logs amount=15
    """
    try:
        amount = int(amount)
    except ValueError:
        return '{} amount is not supported'.format(amount)

    if __grains__.get('liskenv'):
        cmd_run = 'tail -{} logs/lisk.log'
    elif __grains__.get('shiftenv'):
        cmd_run = 'tail -{} logs/shift.log'
    else:
        return 'Platform not supported'

    response = _run_crypto_cmd(cmd_run.format(amount))

    return response

def app_log_find(term, amount=15):
    """
    Find string in the logs of the application process

    CLI Example::

        salt 'crypto-delegate1' cryptoadmin.app_log_find forged
        salt 'crypto-delegate1' cryptoadmin.app_log_find forged amount=15
    """
    try:
        amount = int(amount)
    except ValueError:
        return '{} amount is not supported'.format(amount)

    file_path = __pillar__.get('app_dir') + 'logs/'

    if __grains__.get('liskenv'):
        response = __salt__['file.grep'](file_path + 'lisk.log', term, '-i')
    elif __grains__.get('shiftenv'):
        response = __salt__['file.grep'](file_path + 'shift.log', term, '-i')
    else:
        return 'Platform not supported'

    response['stdout'] = response['stdout'].split('\n')[-amount:]

    return response

def db_logs(amount=10):
    """
    Tail the logs of the application process

    CLI Example::

        salt 'crypto-delegate1' cryptoadmin.db_logs
        salt 'crypto-delegate1' cryptoadmin.db_logs amount=15
    """
    try:
        amount = int(amount)
    except ValueError:
        return '{} amount is not supported'.format(amount)

    working_dir = None
    user = None

    if __grains__.get('liskenv'):
        cmd_run = 'tail -{} logs/pgsql.log'
    elif __grains__.get('shiftenv'):
        cmd_run = 'tail -{} postgresql-9.6-main.log'
        working_dir = '/var/log/postgresql/'
        user = 'postgres'
    else:
        return 'Platform not supported'

    response = _run_crypto_cmd(cmd_run.format(amount), working_dir, user)

    return response

def db_log_find(term, amount=15):
    """
    Find string in the logs of the database

    CLI Example::

        salt 'crypto-delegate1' cryptoadmin.db_log_find err
        salt 'crypto-delegate1' cryptoadmin.db_log_find err amount=15
    """
    try:
        amount = int(amount)
    except ValueError:
        return '{} amount is not supported'.format(amount)

    if __grains__.get('liskenv'):
        working_dir = __pillar__.get('app_dir')
        response = __salt__['file.grep'](working_dir+ 'logs/pgsql.log', term, '-i')
    elif __grains__.get('shiftenv'):
        working_dir = '/var/log/postgresql/postgresql-9.6-main.log'
        response = __salt__['file.grep'](working_dir, term, '-i')
    else:
        return 'Platform not supported'

    response['stdout'] = response['stdout'].split('\n')[-amount:]

    return response

def stop():
    """
    Stop all the crypto platform processes

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

def stop_node():
    """
    Stop the crypto platform application process

    CLI Example::

        salt 'crypto-delegate1' cryptoadmin.stop_node
    """
    if __grains__.get('liskenv'):
        cmd_run = 'bash lisk.sh stop_node'
    else:
        return 'Platform not supported'

    response = _run_crypto_cmd(cmd_run)

    return response

def stop_db():
    """
    Stop the crypto platform database process

    CLI Example::

        salt 'crypto-delegate1' cryptoadmin.stop_db
    """
    if __grains__.get('liskenv'):
        cmd_run = 'bash lisk.sh stop_db'
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

def start_db():
    """
    Start the crypto platform database process

    CLI Example::

        salt 'crypto-delegate1' cryptoadmin.start_db
    """
    if __grains__.get('liskenv'):
        cmd_run = 'bash lisk.sh start_db'
    else:
        return 'Platform not supported'

    response = _run_crypto_cmd(cmd_run)

    return response

def start_node():
    """
    Start the crypto platform process

    CLI Example::

        salt 'crypto-delegate1' cryptoadmin.start_node
    """
    if __grains__.get('liskenv'):
        cmd_run = 'bash lisk.sh start_node'
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

def rebuild(url=None,local=None):
    """
    Rebuild the DPOS crypto process

    CLI Example::

        salt '*' cryptoadmin.rebuild
        salt '*' cryptoadmin.rebuild url="https://testnet-snapshot.lisknode.io"
        salt '*' cryptoadmin.rebuild local="/path/to/chain.gz"
    """

    if __grains__.get('shiftenv'):
        cmd_run = 'echo "y" | bash shift_manager.bash rebuild'
    elif __grains__.get('oxyenv'):
        cmd_run = 'echo "y" | bash oxy_manager.bash rebuild'
    elif __grains__.get('lwfenv'):
        cmd_run = 'echo "y" | bash lwf_manager.bash rebuild'
    elif __grains__.get('liskenv') and __grains__.get('liskenv') == 'main':
        cmd_run = 'bash lisk.sh rebuild {0}'.format(__pillar__.get('snapshot_service_main'))
    elif __grains__.get('liskenv') and __grains__.get('liskenv') == 'test':
        if url:
            cmd_run = 'bash lisk.sh rebuild -u {}'.format(url)
        elif local:
            cmd_run = 'bash lisk.sh rebuild -f {}'.format(local)
        else:
            cmd_run = 'bash lisk.sh rebuild'
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
