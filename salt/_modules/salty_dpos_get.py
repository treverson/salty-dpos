import requests
import logging
import dposutils

log = logging.getLogger(__name__)

def _get_url():
    """

    """
    if __pillar__.get('app_port'):
        url = 'http://localhost:{}'.format(__pillar__.get('app_port'))
    else:
        return None

    return url

def _get_api():
    """

    """
    url = _get_url()

    if not url:
        return None

    if __grains__.get('crypto_ver') == 1:
        return dposutils.dposAPIv1(url, 1)
    else:
        return dposutils.dposAPI(url, 0)

def constants():
    """
    GET constants information from the target API

    V1 Only

    CLI Example::

        salt '*' salty_dpos_get.constants
    """
    api = _get_api()
    if api.version == 1:
        return _get_api().loader('constants')
    else:
        return None

def sync():
    """
    GET sync information from the target API

    CLI Example::

        salt '*' salty_dpos_get.sync
    """

    return _get_api().loader('sync')

def height():
    """
    GET height information from the target API

    CLI Example::

        salt '*' salty_dpos_get.height
    """

    api = _get_api()
    if api.version == 1:
        return api.loader('status').get('height')
    else:
        return api.loader('sync').get('height')

def status():
    """
    GET status information from the dpos API

    CLI Example::

        salt '*' salty_dpos_get.status
    """

    return _get_api().loader('status')

def consensus():
    """
    GET consensus information from the target API

    CLI Example::

        salt '*' salty_dpos_get.consensus
    """
    return _get_api().loader('sync').get('consensus')

def version():
    """
    GET peer version information from the dpos API

    CLI Example::

        salt '*' salty_dpos_get.version
    """

    payload = {
        "ip" : "127.0.0.1",
        "port" : 7000,
        "parameters" : ""
    }

    api = _get_api()
    if api.version == 1:
        return _get_api().loader('constants').get('version')
    else:
        return _get_api().peers('peer_version', payload)

def peer_list():
    """
    GET peers information from the dpos API

    CLI Example::

        salt '*' salty_dpos_get.peer_list
    """

    payload = {
        "ip" : "127.0.0.1",
        "port" : 7000,
        "parameters" : ""
        }

    api = _get_api()
    if api.version == 1:
        return api.peers()
    else:
        return api.peers('peer_list', payload)

def delegate(delegate):
    """
    GET delegate information based on delegate name

    CLI Example::

        salt '*' salty_dpos_get.delegate slasheks

    .. code-block:: yaml
        dpos-delegate1:
        ----------
        address:
            6573868316532588354L
        approval:
            20.3
        missedblocks:
            1254
        producedblocks:
            44240
        productivity:
            97.24
        publicKey:
            7beb5f1e8592022fe5272b45eeeda6a1b6923a801af6e1790933cc6a78ed95a1
        rank:
            8
        rate:
            8
        username:
            slasheks
        vote:
            2417487588036848
    """
    api = _get_api()
    if api.version == 1:
        return api.delegate(delegate)
    else:
        return api.autoname(delegate).get('delegate')

def forging_status(username):
    """
    GET forging status based on a delegate name

    CLI Example::

        salt '*' salty_dpos_get.forging_status slasheks

    delegate:
        ----------
        enabled:
            False
        success:
            True

    """
    api = _get_api()
    if api.version == 1:
        return api.forge_check(username)
    else:
        return api.forge_check(username).get('enabled')

def forged_blocks(username, limit=5, order_by='height'):
    """
    GET forged blocks based on delegate name

    CLI Example::

        salt 'dpos-delegate1' salty_dpos_get.forged_blocks slasheks

    .. code-block:: yaml
        dpos-delegate1:
            ----------
            blocks:
                 |_
                   ----------
                   blockSignature:
                       fa25249eaf0dd27e4127ba246e9ba5bdd3202962e2cfc70a5396a295b5216b1bbf6edb13aca9eae8021f389a88d13b274ff980c5f27f8154cc1758cfe23c8108
                   confirmations:
                       95
                   generatorId:
                       6573868316532588354L
                   generatorPublicKey:
                       7beb5f1e8592022fe5272b45eeeda6a1b6923a801af6e1790933cc6a78ed95a1
                   height:
                       4020536
                   id:
                       10440143050652943624
                   numberOfTransactions:
                       2
                   payloadHash:
                       2443f0543a675cbb90a8db1d61f00997379897892d4073710b5f2e2a714f6ab1
                   payloadLength:
                       429
                   previousBlock:
                       11476759316531321694
                   reward:
                       400000000
                   timestamp:
                       50123130
                   totalAmount:
                       100000000
                   totalFee:
                       110000000
                   totalForged:
                       510000000
                   version:
                       0
    """
    delegate_info = delegate(username)

    query_string = '{}&limit={}&orderBy={}:desc'\
            .format(delegate_info['publicKey'], limit, order_by)

    payload = {
        'pubkey': query_string
    }

    return _get_api().blocks('my_blocks', payload)

def last_forged_block(username):
    """
    GET the last forged block based on delegate name

    CLI Example::

        salt 'dpos-delegate1' salty_dpos_get.last_forged_block slasheks

    .. code-block:: yaml
        dpos-delegate1:
            ----------
            blockSignature:
                f09975daef352bbca382463f4d7abf24f9c30ed0ee665fa846245da05a95690120c337c3550e842d4b950205aa551930f4d88f7cf439bc105c25e3d1833a3806
            confirmations:
                8
            generatorId:
                6573868316532588354L
            generatorPublicKey:
                7beb5f1e8592022fe5272b45eeeda6a1b6923a801af6e1790933cc6a78ed95a1
            height:
                4020632
            id:
                3268137026912411903
            numberOfTransactions:
                0
            payloadHash:
                e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
            payloadLength:
                0
            previousBlock:
                12279427697070199066
            reward:
                400000000
            timestamp:
                50124190
            totalAmount:
                0
            totalFee:
                0
            totalForged:
                400000000
            version:
                0
    """
    return forged_blocks(username).get('blocks')[0]


def network_height():
    """
    GET network height
    NOTE: This is an internal query of the DB

    CLI Example::

        salt '*' salty_dpos_get.network_height

        delegate:
            1913313
    """
    allpeers = []

    peerl = peer_list()

    if peerl.get('peers'):

        for peer in peerl['peers']:

            if peer['broadhash'] and peer['height']:

                allpeers.append(peer)

    max_peer_height = max([x['height'] for x in allpeers])

    return max_peer_height


def height_diff():
    """
    GET the difference between the heights in the DB and your node

    CLI Example::

        salt '*' salty_dpos_get.height_diff

        delegate:
            0
    """

    if __grains__.get('arkenv'):
        return 'Currently not supported on this platform'

    return network_height() - height()

def failover_candidate():
    """
    GET True response if the node has consensus greater than 80
    and height difference of less than one

    CLI Example::

        salt '*' salty_dpos_get.failover_candidate

        delegate1:
            True
        delegate2:
            False
    """

    if consensus() > 80 and height_diff() < 1:
        return True
    else:
        return False


