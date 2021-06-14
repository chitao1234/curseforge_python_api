from requests import get, post
from json import loads as _loads
from json import dumps


BASE_URL = 'https://addons-ecs.forgesvc.net/api/v2/addon/'
BARE_BASE_URL = 'https://addons-ecs.forgesvc.net/api/v2/'
JSON_HEADER = {'Content-Type': 'application/json'}


def loads(s, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw):
    return s if _loads(s, cls=cls, object_hook=object_hook, parse_float=parse_float, parse_int=parse_int, parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw) \
    else None
