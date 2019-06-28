from flask import current_app
from edhunt import db, info, warning


class PlateformsEnums():

  booleen = ["Oui",
             "Non"]

  trooleen = ["-",
              "Oui",
              "Non"]

  connexion = ["-",
               "On",
               "Off",
               "Not available"]

  @staticmethod
  def choices(item):
    return [(i, i) for i in PlateformsEnums.__dict__.get(item)]


def col_connexion():
  return db.Column(db.Enum(*PlateformsEnums.connexion),
                   unique=False, nullable=False, default="Off")


def col_email():
  return db.Column(db.String(40), unique=True, nullable=True)


def col_password():
  return db.Column(db.String(40), unique=False, nullable=True)


def col_bool():
  return db.Column(db.Enum(*PlateformsEnums.booleen),
                   unique=False, nullable=True)
