import logging
import dposutils

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

    return dposutils.dposAPI(url)

def enable_forging():
    """
    Enable forging on a node based on delegate name

    CLI Example::

        salt 'dpos-delegate1' salty_dpos_post.enable_forging

    """
    if not __pillar__.get('secret'):

        return "No secret set in pillar data"

    else:

        secret = __pillar__.get('secret').strip()
        payload = {'secret': secret}

        return _get_api().delegates('enable_forging',
                                    payload)

def disable_forging():
    """
    Disable forging on a node based on delegate name

    CLI Example::

        salt 'dpos-delegate1' salty_dpos_post.disable_forging

    """
    if not __pillar__.get('secret'):

        return "No secret set in pillar data"

    else:

        secret = __pillar__.get('secret').strip()
        payload = {'secret': secret}

        return _get_api().delegates('disable_forging',
                                    payload)
