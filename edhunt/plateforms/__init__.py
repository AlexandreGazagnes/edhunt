from edhunt.plateforms.text import PlateformsText
from edhunt.plateforms.forms import PlateformsForms
from edhunt.plateforms.model import PlateformsTables
from edhunt.plateforms.utils import PlateformsEnums
from edhunt.plateforms.webdriver import WebDriver


class Plateforms:
    text = PlateformsText
    forms = PlateformsForms
    tables = PlateformsTables
    enums = PlateformsEnums
    list_all = ["apec", "cadremploi", 'indeed', 'jobintree', 'keljob',
                'lesjeudis', 'meteojob', 'monster', 'regionjob']
    WebDriver = WebDriver
