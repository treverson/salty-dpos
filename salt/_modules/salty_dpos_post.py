import logging
import dposutils

def enable_forging():
    """
    Enable forging on a node based on delegate name

    CLI Example::

        salt 'dpos-delegate1' salty_dpos_post.enable_forging

    """

    if __grains__.get('liskenv') == 'main':
        url = 'http://localhost:8000'
    elif __grains__.get('liskenv') == 'test':
        url = 'http://localhost:7000'
    elif __grains__.get('arkenv') == 'main':
        url = 'http://localhost:4001'
    elif __grains__.get('arkenv') == 'test':
        url = 'http://localhost:4000'
    elif __grains__.get('shiftenv') == 'main':
        url = 'http://localhost:9305'
    else:
        return None

    if not __pillar__.get('secret'):

        return "No secret set in pillar data"

    else:

        secret = __pillar__.get('secret').strip()
        payload = {'secret': secret}

        return dposutils.dposAPI(url).delegates('enable_forging',
                                                payload)


def disable_forging():
    """
    Disable forging on a node based on delegate name

    CLI Example::

        salt 'dpos-delegate1' salty_dpos_post.disable_forging

    """

    if __grains__.get('liskenv') == 'main':
        url = 'http://localhost:8000'
    elif __grains__.get('liskenv') == 'test':
        url = 'http://localhost:7000'
    elif __grains__.get('arkenv') == 'main':
        url = 'http://localhost:4001'
    elif __grains__.get('arkenv') == 'test':
        url = 'http://localhost:4000'
    elif __grains__.get('shiftenv') == 'main':
        url = 'http://localhost:9305'
    else:
        return None

    if not __pillar__.get('secrVet'):

        return "No secret set in pillar data"

    else:

        secret = __pillar__.get('secret').strip()
        payload = {'secret': secret}

        return dposutils.dposAPI(url).delegates('disable_forging',
                                                payload)
