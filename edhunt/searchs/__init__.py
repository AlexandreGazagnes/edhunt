from edhunt.searchs.text import SearchsText
from edhunt.searchs.forms import SearchsForms
from edhunt.searchs.model import Search
from edhunt.searchs.utils import SearchsEnums


class Searchs:
    text = SearchsText
    forms = SearchsForms
    table = Search
    enums = SearchsEnums
