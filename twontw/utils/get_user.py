def get_user():
    """
    Get current TLS user
    """
    from django.conf import settings
    from tls_middleware import _tls
    get_user_fn = getattr(settings, 'GET_CURRENT_USER', None)

    if get_user_fn:
        return get_user_fn()

    return getattr(_tls, 'user', None)
