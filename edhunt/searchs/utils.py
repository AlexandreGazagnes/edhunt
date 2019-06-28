from edhunt.users.utils import UsersEnums


class SearchsEnums():

    prefix = ["-", "Indifférent", 'Tous', ]
    booleen = prefix + UsersEnums.booleen
    mob = UsersEnums.mob[1:]
    contract = prefix + UsersEnums.contract[1:]
    employer = prefix + UsersEnums.employer[1:]
    status = prefix + UsersEnums.status[1:]
    rem = prefix + UsersEnums.rem[1:]
    currency = UsersEnums.currency
    management = prefix + UsersEnums.booleen
    company_size = prefix + UsersEnums.company_size[1:]
    sector = prefix + UsersEnums.sector[1:]
    function = prefix + UsersEnums.function[1:]
    position = prefix + UsersEnums.position[1:]
    english_mandatory = prefix + ["100%", "75%", "50%", "25%", "0%"]

    @staticmethod
    def choices(item):
        return [(i, i) for i in SearchsEnums.__dict__.get(item)]
