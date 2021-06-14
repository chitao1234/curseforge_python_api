from typing import Union
from . import _utils


def file_info(addon_id: int, file_id: int) -> Union[dict, None]:
    return _utils.loads(_utils.get(_utils.BASE_URL + str(addon_id) + '/file/' + str(file_id)).text)


def file_url(addon_id: int, file_id: int) -> str:
    return _utils.get(_utils.BASE_URL + str(addon_id) + '/file/' + str(file_id) + '/download-url').text


def file_changelog(addon_id: int, file_id: int) -> str:
    return _utils.get(_utils.BASE_URL + str(addon_id) + '/file/' + str(file_id) + '/changelog').text
