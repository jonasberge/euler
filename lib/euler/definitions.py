from os import path


UTIL_DIR = path.dirname(path.abspath(__file__))
ROOT_DIR = path.abspath(path.join(UTIL_DIR, '..', '..'))

DATA_DIR = path.abspath(path.join(ROOT_DIR, 'data'))
CACHE_DIR = path.abspath(path.join(ROOT_DIR, 'cache'))
