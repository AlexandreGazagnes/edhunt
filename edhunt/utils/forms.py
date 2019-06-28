import string

from wtforms.validators import ValidationError
from edhunt.main.model import Country, Region, Departement


def _handle_tous_indiff(obj, feat):
    for val in ["-", "Tous", 'Indifférent']:
        if val in getattr(obj, feat).data:
            getattr(obj, feat).data = [val, ]


class HelpMessages:

    multiple_select = 'Maintenez Crtl et/ou Shift + option pour effectuer une selection multiple'
    comma_sep = 'Ecrivez les valeurs qui vous conviennent, séparées par une virgule'
    unique_select = "Une seule valeur possible"


class Validator():

    @staticmethod
    def required(arg):
        if not arg.data:
            raise ValidationError('Ce champ doit être rempli')

    @staticmethod
    def length(arg, _min=2, _max=40):
        if _min == _max:
            if not (_max >= len(arg.data) >= _min):
                raise ValidationError(f'Ce champ doit comporter {_max} caractères')
        else:
            if not (_max >= len(arg.data) >= _min):
                raise ValidationError(f'Ce champ doit comporter entre {_min} et {_max} caractères')

    @staticmethod
    def numerical(arg):
        try:
            int(str(arg.data).strip())
        except Exception as e:
            raise ValidationError('Ce champ doit être numérique')

    @staticmethod
    def xp(xp):
        Validator.numerical(xp)
        if not (42 >= int(str(xp.data).strip()) >= 0):
            raise ValidationError('Humm... Vous êtes trop jeune ou trop vieux pour ça...')

    @staticmethod
    def date(date):
        _date = date.data.split("/")
        if len(_date) != 3:
            raise ValidationError("Format invalide, utilisez '/' comme séparateur")
        if not (31 >= int(_date[0]) >= 1):
            raise ValidationError('le Jour doit être compris entre 01 et 31')
        if not (12 >= int(_date[1]) >= 1):
            raise ValidationError('le Mois doit être compris entre 01 et 12')
        if not (2004 >= int(_date[2]) >= 1949):
            raise ValidationError('Humm... Vous êtes trop jeune ou trop agé pour travailler, non?')

    @staticmethod
    def country(country):
        if country.data not in Country.list_all():
            raise ValidationError("Ce pays n'existe pas")

    @staticmethod
    def region(region):
        if region.data not in Region.list_all():
            raise ValidationError("Cette Région n'existe pas")

    @staticmethod
    def departement(departement):
        if departement.data not in Departement.list_all():
            raise ValidationError("Ce Département n'existe pas")

    @staticmethod
    def choice_not_null(var):
        if var.data.strip() == "-":
            raise ValidationError("Champ incorrect")

    @staticmethod
    def password_hard(var):
        p = var.data
        digs = [str(k) for k in range(10)]
        punct = ['!', '#', '$', '%', '&', '*', '+', '-', '.', '?', '@', '_']
        if not [i for i in p if (i == i.lower())]:
            raise ValidationError("Au moins une minuscule")
        if not [i for i in p if (i == i.upper())]:
            raise ValidationError("Au moins une majuscule")
        if not [i for i in p if (i in digs)]:
            raise ValidationError("Au moins un chiffre")
        if not [i for i in p if (i in punct)]:
            raise ValidationError(f"Au moins un caractère spécial de type : {' '.join(punct)}")
