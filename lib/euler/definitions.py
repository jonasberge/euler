from os import path


UTIL_DIR = path.dirname(path.abspath(__file__))
ROOT_DIR = path.abspath(path.join(UTIL_DIR, '..', '..'))

DATA_DIR = path.abspath(path.join(ROOT_DIR, 'data'))
CACHE_DIR = path.abspath(path.join(ROOT_DIR, 'cache'))

DESK_DIR = path.abspath(path.join(ROOT_DIR, 'desk'))
DRAWER_DIR = path.abspath(path.join(ROOT_DIR, 'drawer'))
SOLVED_DIR = path.abspath(path.join(ROOT_DIR, 'solved'))
