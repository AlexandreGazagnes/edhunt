from edhunt.users.text import UsersText
from edhunt.users.forms import UsersForms
from edhunt.users.model import User
from edhunt.users.utils import UsersEnums


class Users():

    text = UsersText
    forms = UsersForms
    table = User
    enums = UsersEnums
