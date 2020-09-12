from mezmorize import Cache

from .definitions import CACHE_DIR


def disk_cached(function):
    cache = Cache(CACHE_TYPE='filesystem',
                  CACHE_DIR=CACHE_DIR,
                  CACHE_DEFAULT_TIMEOUT=0,
                  CACHE_THRESHOLD=0)

    @cache.memoize()
    def wrapped(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapped
