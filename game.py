from typing import List, Union
from datetime import datetime
from . import _utils


def _process_time(iso_time: str) -> datetime:
    return datetime.strptime(iso_time, '%Y-%m-%dT%H:%M:%S.%fZ')


def featured_addon(game_id: int, featured_count: int, popular_count: int, updated_count: int, addon_ids: List[Union[int, None]] = []) -> dict:
    return _utils.post(_utils.BASE_URL + 'featured', headers=_utils.JSON_HEADER, data=_utils.dumps({"GameId": game_id, "addonIds": addon_ids, "featuredCount": featured_count, "popularCount": popular_count, "updatedCount": updated_count})).text


def database_timestamp() -> datetime:
    return _process_time(_utils.get(_utils.BASE_URL + 'timestamp').text)


def search(game_id: int, section_id: int, query: str = '', index: int = 0, sort: int = 0, page_size: int = 0, game_version: str = '', category_id: int = 0) -> list:
    url = _utils.BASE_URL + \
          'search?gameId={game_id}&sectionId={section_id}'.format(game_id=game_id, section_id=section_id) + \
          query if 'searchFilter=' + query else '' + \
          index if 'index=' + index else '' + \
          sort if 'sort=' + sort else '' + \
          page_size if 'pageSize=' + page_size else '' + \
          game_version if 'gameVersion=' + game_version else '' + \
          category_id if 'categoryId=' + category_id else ''
    return _utils.loads(_utils.get(url).text)


def game_database_timestamp() -> datetime:
    return _process_time(_utils.get(_utils.BARE_BASE_URL + 'game/timestamp').text)


def games_list(supports_addons: bool = False) -> list:
    return _utils.loads(_utils.get(_utils.BARE_BASE_URL + 'game?supportsAddons=' + str(supports_addons).lower()).text)


def game_info(game_id: int) -> dict:
    return _utils.loads(_utils.get(_utils.BARE_BASE_URL + 'game/' + str(game_id)))


def category_database_timestamp() -> datetime:
    return _process_time(_utils.get(_utils.BARE_BASE_URL + 'category/timestamp').text)


def categories_list() -> list:
    return _utils.loads(_utils.get(_utils.BARE_BASE_URL + 'category').text)


def category_info(category_id: int) -> dict:
    return _utils.loads(_utils.get(_utils.BARE_BASE_URL + 'category/' + str(category_id)).text)


def section_info(section_id: int) -> dict:
    return _utils.loads(_utils.get(_utils.BARE_BASE_URL + 'category/section/' + str(section_id)).text)


def minecraft_datebase_timestamp() -> datetime:
    return _process_time(_utils.get(_utils.BARE_BASE_URL + 'minecraft/version/timestamp').text)


def minecraft_versions() -> list:
    return _utils.loads(_utils.get(_utils.BARE_BASE_URL + 'minecraft/version').text)


def minecraft_version_info(version: str) -> dict:
    return _utils.loads(_utils.get(_utils.BARE_BASE_URL + 'minecraft/version/' + version).text)


def minecraft_modloader_datebase_timestamp() -> datetime:
    return _process_time(_utils.get(_utils.BARE_BASE_URL + 'minecraft/modloader/timestamp').text)


def minecraft_modloader_versions() -> list:
    return _utils.loads(_utils.get(_utils.BARE_BASE_URL + 'minecraft/modloader').text)


def minecraft_modloader_version_info(version: str) -> dict:
    return _utils.loads(_utils.get(_utils.BARE_BASE_URL + 'minecraft/modloader/' + version).text)
