from flask_login import (LoginManager, current_user, UserMixin, login_user,
                         logout_user, login_required)
from edhunt.utils.text import handle_none_values
from edhunt import warning
from flask import Markup


class _Page:

  def __init__(self, current_user):

    self.title = f"Plateformes"
    self.sub_title = ""
    self. head = "Vous trouverez et pourrez modifier ici l'ensemble connexions aux plateformes externes relatives à votre compte et à votre profil Une astuce? plus votre score est élevé, meilleur c'est pour vous!"


class ManagePlateformsText:

  def __init__(self):
    try:
      current_user
    except Exception as e:
      raise e

    self.page = _Page(current_user)
