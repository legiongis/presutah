from arches.app.models.system_settings import settings
from arches.app.utils.betterJSONSerializer import JSONSerializer
from arches.app.search.components.base import BaseSearchFilter

details = {
    "searchcomponentid": "",
    "name": "Preservation Directory",
    "icon": "fa fa-bank",
    "modulename": "directory_search.py",
    "classname": "DirectorySearch",
    "type": "popup",
    "componentpath": "views/components/search/directory-search",
    "componentname": "directory-search",
    "sortorder": "0",
    "enabled": True,
}


class DirectorySearch(BaseSearchFilter):
    def view_data(self):
        ret = {}
        ret["saved_searches"] = settings.SAVED_SEARCHES
        return ret
