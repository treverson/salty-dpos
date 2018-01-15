cryptoadmin.app_log_find:

    Find string in the logs of the application process

    CLI Example::

        salt 'crypto-delegate1' cryptoadmin.app_log_find forged
        salt 'crypto-delegate1' cryptoadmin.app_log_find forged amount=15
    

cryptoadmin.app_logs:

    Tail the logs of the application process

    CLI Example::

        salt 'crypto-delegate1' cryptoadmin.app_logs
        salt 'crypto-delegate1' cryptoadmin.app_logs amount=15
    

cryptoadmin.db_log_find:

    Find string in the logs of the database

    CLI Example::

        salt 'crypto-delegate1' cryptoadmin.db_log_find err
        salt 'crypto-delegate1' cryptoadmin.db_log_find err amount=15
    

cryptoadmin.db_logs:

    Tail the logs of the application process

    CLI Example::

        salt 'crypto-delegate1' cryptoadmin.db_logs
        salt 'crypto-delegate1' cryptoadmin.db_logs amount=15
    

cryptoadmin.help:

    Get the help messages from the platform shell tool

    CLI Example::

        salt 'crypto-delegate1' cryptoadmin.help
    

cryptoadmin.rebuild:

    Rebuild the DPOS crypto process

    CLI Example::

        salt '*' cryptoadmin.rebuild
        salt '*' cryptoadmin.rebuild url="https://testnet-snapshot.lisknode.io"
        salt '*' cryptoadmin.rebuild local="/path/to/chain.gz"
    

cryptoadmin.reload:

    Reload the crypto platform process

    CLI Example::

        salt 'crypto-delegate1' cryptoadmin.reload
    

cryptoadmin.start:

    Start the crypto platform process

    CLI Example::

        salt 'crypto-delegate1' cryptoadmin.start
    

cryptoadmin.start_db:

    Start the crypto platform database process

    CLI Example::

        salt 'crypto-delegate1' cryptoadmin.start_db
    

cryptoadmin.start_node:

    Start the crypto platform process

    CLI Example::

        salt 'crypto-delegate1' cryptoadmin.start_node
    

cryptoadmin.status:

    Get the status of the process

    CLI Example::

        salt 'crypto-delegate1' cryptoadmin.status
    

cryptoadmin.stop:

    Stop all the crypto platform processes

    CLI Example::

        salt 'crypto-delegate1' cryptoadmin.stop
    

cryptoadmin.stop_db:

    Stop the crypto platform database process

    CLI Example::

        salt 'crypto-delegate1' cryptoadmin.stop_db
    

cryptoadmin.stop_node:

    Stop the crypto platform application process

    CLI Example::

        salt 'crypto-delegate1' cryptoadmin.stop_node
    

cryptoadmin.update:

    Update the DPOS crypto process

    CLI Example::

        salt '*' cryptoadmin.update
    

cryptoadmin.update_wallet:

    Update the shift wallet on a given node

    CLI Example::

        salt '*' cryptoadmin.update_wallet
    

