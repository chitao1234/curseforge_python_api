from requests import get as _get, post as _post
from json import loads as _loads
from json import dumps


BASE_URL = 'https://addons-ecs.forgesvc.net/api/v2/addon/'
BARE_BASE_URL = 'https://addons-ecs.forgesvc.net/api/v2/'
JSON_HEADER = {'Content-Type': 'application/json'}
UA_FIREFOX = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'


def get(url, params=None, **kwargs):
    return _get(url, params, verify=False, headers={'User-Agent': UA_FIREFOX}, **kwargs)


def post(url, params=None, **kwargs):
    return _post(url, params, verify=False, headers={'User-Agent': UA_FIREFOX}, **kwargs)


def loads(s, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw):
    result = _loads(s, cls=cls, object_hook=object_hook, parse_float=parse_float, parse_int=parse_int, parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw)
    return result if result else None
