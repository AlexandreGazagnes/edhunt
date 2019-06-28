from edhunt import db
from edhunt.plateforms.utils import *


class Apec(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    connexion = col_connexion()
    account = col_bool()
    status = db.Column(db.Enum(*["cadre", "jd"]),
                       unique=False, nullable=False, default="cadre")
    sub_account = col_bool()
    connected = col_connexion()
    email = col_email()
    password = col_password()
    autorisation = col_bool()
    resume = col_bool()
    candidature = col_bool()
    good_user = col_bool()
    edhunt_integrity = col_bool()
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True,
                        nullable=False)

    @property
    def fields(self):

        keys = ['connexion', 'account', 'connected', 'email',
                'autorisation', 'good_user', "edhunt_integrity", 'user_id']

        values = [getattr(self, k) for k in keys]

        labels = ["Status", "Compte", "Connexion", 'email', 'Autorisation',
                  'Utilisateur', 'Crédits']

        return zip(labels, values)

    def __repr__(self):
        keys = ['id', 'connexion', 'account', 'connected', 'email', 'password',
                'autorisation', 'good_user', "edhunt_integrity", 'user_id']
        txt = "\n".join([str(key.ljust(20, " ") + ": " +
                             str(self.__dict__[key])) for key in keys])
        return "\n" + txt

    @property
    def __name__(self):
        return "apec"


class Cadremploi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    connexion = col_connexion()
    account = col_bool()
    connected = col_bool()
    email = col_email()
    password = col_password()
    autorisation = col_bool()
    good_user = col_bool()
    edhunt_integrity = col_bool()
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True,
                        nullable=False)

    def __repr__(self):
        keys = ['id', 'connexion', 'account', 'connected', 'email', 'password',
                'autorisation', 'good_user', "edhunt_integrity", 'user_id']
        txt = "\n".join([str(key.ljust(20, " ") + ": " +
                             str(self.__dict__[key])) for key in keys])
        return "\n" + txt

    @property
    def __name__(self):
        return "cadremploi"


class Indeed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    connexion = col_connexion()
    account = col_bool()
    connected = col_bool()
    email = col_email()
    password = col_password()
    autorisation = col_bool()
    good_user = col_bool()
    edhunt_integrity = col_bool()
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True,
                        nullable=False)

    def __repr__(self):
        keys = ['id', 'connexion', 'account', 'connected', 'email', 'password',
                'autorisation', 'good_user', "edhunt_integrity", 'user_id']
        txt = "\n".join([str(key.ljust(20, " ") + ": " +
                             str(self.__dict__[key])) for key in keys])
        return "\n" + txt

    @property
    def __name__(self):
        return "indeed"


class Jobintree(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    connexion = col_connexion()
    account = col_bool()
    connected = col_bool()
    email = col_email()
    password = col_password()
    autorisation = col_bool()
    good_user = col_bool()
    edhunt_integrity = col_bool()
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True,
                        nullable=False)

    def __repr__(self):
        keys = ['id', 'connexion', 'account', 'connected', 'email', 'password',
                'autorisation', 'good_user', "edhunt_integrity", 'user_id']
        txt = "\n".join([str(key.ljust(20, " ") + ": " +
                             str(self.__dict__[key])) for key in keys])
        return "\n" + txt

    @property
    def __name__(self):
        return "jobintree"


class Keljob(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    connexion = col_connexion()
    account = col_bool()
    connected = col_bool()
    email = col_email()
    password = col_password()
    autorisation = col_bool()
    good_user = col_bool()
    edhunt_integrity = col_bool()
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True,
                        nullable=False)

    def __repr__(self):
        keys = ['id', 'connexion', 'account', 'connected', 'email', 'password',
                'autorisation', 'good_user', "edhunt_integrity", 'user_id']
        txt = "\n".join([str(key.ljust(20, " ") + ": " +
                             str(self.__dict__[key])) for key in keys])
        return "\n" + txt

    @property
    def __name__(self):
        return "keljob"

# class Leboncoin(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     connexion = col_connexion()
#     account = col_bool()
#     connected = col_bool()
#     email = col_email()
#     password = col_password()
#     autorisation = col_bool()
#     good_user = col_bool()
#     edhunt_integrity = col_bool()
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True,
#                         nullable=False)

    def __repr__(self):
        keys = ['id', 'connexion', 'account', 'connected', 'email', 'password',
                'autorisation', 'good_user', "edhunt_integrity", 'user_id']
        txt = "\n".join([str(key.ljust(20, " ") + ": " +
                             str(self.__dict__[key])) for key in keys])
        return "\n" + txt


class Lesjeudis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    connexion = col_connexion()
    account = col_bool()
    connected = col_bool()
    email = col_email()
    password = col_password()
    autorisation = col_bool()
    good_user = col_bool()
    edhunt_integrity = col_bool()
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True,
                        nullable=False)

    def __repr__(self):
        keys = ['id', 'connexion', 'account', 'connected', 'email', 'password',
                'autorisation', 'good_user', "edhunt_integrity", 'user_id']
        txt = "\n".join([str(key.ljust(20, " ") + ": " +
                             str(self.__dict__[key])) for key in keys])
        return "\n" + txt

    @property
    def __name__(self):
        return "lesjeudi"


class Meteojob(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    connexion = col_connexion()
    account = col_bool()
    connected = col_bool()
    email = col_email()
    password = col_password()
    autorisation = col_bool()
    good_user = col_bool()
    edhunt_integrity = col_bool()
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True,
                        nullable=False)

    def __repr__(self):
        keys = ['id', 'connexion', 'account', 'connected', 'email', 'password',
                'autorisation', 'good_user', "edhunt_integrity", 'user_id']
        txt = "\n".join([str(key.ljust(20, " ") + ": " +
                             str(self.__dict__[key])) for key in keys])
        return "\n" + txt

    @property
    def __name__(self):
        return "meteojob"


class Monster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    connexion = col_connexion()
    account = col_bool()
    connected = col_bool()
    email = col_email()
    password = col_password()
    autorisation = col_bool()
    good_user = col_bool()
    edhunt_integrity = col_bool()
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True,
                        nullable=False)

    def __repr__(self):
        keys = ['id', 'connexion', 'account', 'connected', 'email', 'password',
                'autorisation', 'good_user', "edhunt_integrity", 'user_id']
        txt = "\n".join([str(key.ljust(20, " ") + ": " +
                             str(self.__dict__[key])) for key in keys])
        return "\n" + txt

    @property
    def __name__(self):
        return "monster"


class Regionjob(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    connexion = col_connexion()
    account = col_bool()
    connected = col_bool()
    email = col_email()
    password = col_password()
    autorisation = col_bool()
    good_user = col_bool()
    edhunt_integrity = col_bool()
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True,
                        nullable=False)

    def __repr__(self):
        keys = ['id', 'connexion', 'account', 'connected', 'email', 'password',
                'autorisation', 'good_user', "edhunt_integrity", 'user_id']
        txt = "\n".join([str(key.ljust(20, " ") + ": " +
                             str(self.__dict__[key])) for key in keys])
        return "\n" + txt

    @property
    def __name__(self):
        return "regionjob"


class PlateformsTables:

    apec = Apec
    cadremploi = Cadremploi
    indeed = Indeed
    jobintree = Jobintree
    keljob = Keljob
    # leboncoin = Leboncoin
    lesjeudis = Lesjeudis
    meteojob = Meteojob
    monster = Monster
    regionjob = Regionjob
