from edhunt.opportunities.text import OpportunitiesText
from edhunt.opportunities.forms import OpportunitiesForms
from edhunt.opportunities.model import Opportunity
from edhunt.opportunities.utils import Lorem


class Opportunities:
    text = OpportunitiesText
    forms = OpportunitiesForms
    table = Opportunity
    lorem = Lorem
