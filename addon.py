from typing import List
from . import _utils


def addon_info(addon_id: int) -> dict:
    return _utils.loads(_utils.get(_utils.BASE_URL + str(addon_id)).text)


def addon_description(addon_id: int) -> str:
    return _utils.get(_utils.BASE_URL + str(addon_id) + '/description').text


def multiple_addon_info(addon_ids: List[int]) -> list:
    return _utils.post(_utils.BASE_URL, data=_utils.dumps(addon_ids), headers=_utils.JSON_HEADER)


def addon_files(addon_id: int) -> list:
    return _utils.loads(_utils.get(_utils.BASE_URL + str(addon_id) + '/files').text)


def addon_by_fingerprint(fingerprint: List[int]) -> dict:
    return _utils.post(_utils.BARE_BASE_URL, data=_utils.dumps(fingerprint), headers=_utils.JSON_HEADER)
