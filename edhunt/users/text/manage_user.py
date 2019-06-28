from flask_login import (LoginManager, current_user, UserMixin, login_user,
                         logout_user, login_required)
from edhunt.utils.text import handle_none_values
from edhunt import warning
from flask import Markup


class _Page:

  def __init__(self, current_user):

    self.title = f"Profil de {current_user.username }"
    self.sub_title = ""
    self. head = "Vous trouverez et pourrez modifier ici l'ensemble informations relatives à votre compte et à votre profil Une astuce? plus votre score est élevé, meilleur c'est pour vous!"


class _Account:

  def __init__(self, current_user):

    self.title = 'Compte'
    self.head = "Commencons par l'essentiel avec les paramètres de votre compte : email, mot de passe et nom d'utilisateur. Si vous venez de vous inscrire, pas besoin de tout chambouler pour l'instant!"
    self._table = [('Utilisateur', current_user.username),
                   ('Email', current_user.email),
                   ('Mot de passe', '********'),
                   ('Création du compte', current_user.created.split(" ")[0])]

  @property
  def table(self):
    return handle_none_values(self._table)


class _Expectation:

  def __init__(self, current_user):

    self.title = 'Attentes'
    self.head = "Etes vous vraiment à l'écoute du marché, voulez vous juste voir les offres qui passent ou voulez-vous que edhunt candidate pour vous automatiquement sur le poste de vos rèves?"
    self._table = [('En poste', current_user.employed),
                   ('Disponible', current_user.sub_employed),
                   ('Situation', current_user.search),
                   ('Attentes', current_user.order),
                   ('Candidatures', current_user.automation)]

  @property
  def table(self):
    return handle_none_values(self._table)


class _Resume:

  def __init__(self, current_user):

    self.title = 'CV'
    self.head = "Le recrutement sans CV ? Oui, mais pas pour toute de suite. Il va falloir aider edhunt à vous aider. \n Si vous n'avez pas de CV, pas de soucis, edhunt en fera un tout spécialement pour vous."
    self._table = []

  @property
  def table(self):
    return handle_none_values(self._table)


class _Identification:

  def __init__(self, current_user):

    self.title = 'Identité'
    self.head = "edhunt a besoin de quelques informations sur vous. Qui êtes vous ? Quel est votre film préféré? Quelle est votre couleur préférée? Quelle note avez vous eu au Brevet des collèges en Histoire ?"
    self._table = [('Prénom', current_user.firstname),
                   ('Nome', current_user.lastname),
                   ('Sexe', current_user.sex),
                   ('Date de naissance', current_user.birthdate),
                   ('Nationalité', current_user.nationality),
                   ('Date de naissance', current_user.birth_country),
                   ('Code postal de naissance', current_user.birth_zip_code),
                   ('Ville de naissance', current_user.birth_town)]

  @property
  def table(self):
    return handle_none_values(self._table)


class _Localisation:

  def __init__(self, current_user):
    self.title = "Localisation (actuelle)"
    self.head = "Le permis et la voiture ca n'est pas nécessaire à Paris, mais si vous vivez dans la banlieue de Sévérac le Chateau dans l'Aveyron, ca peut dépanner!"
    self._table = [('Ville', current_user.town),
                   ('Code postal', current_user.zip_code),
                   ('Pays', current_user.country),
                   ('Permis', current_user.driver_licence),
                   ('Véhicule', current_user.vehicule)]

  @property
  def table(self):
    return handle_none_values(self._table)


class _Diploma:

  def __init__(self, current_user):
    self.title = "Diplôme"
    self.head = "Dans ton bureau, si t'as un diplôme, t'as l'air intelligent. Si t'as un climatiseur, t'as l'air conditionné. une citation égarée de Pierre Légaré. "
    self._table = [('Diplôme', current_user.diploma_name),
                   ('Ecole', current_user.diploma_school),
                   ('Ville', current_user.diploma_town),
                   ('Niveau', current_user.diploma_level),
                   ('Type', current_user.diploma_type),
                   ("Année d'obtention", current_user.diploma_year)]

  @property
  def table(self):
    return handle_none_values(self._table)


class _WorkExperience:

  def __init__(self, current_user):
    self.title = "Situation professionnelle (actuelle, dernière en date ou plus significative)"
    self.head = "20 années en tant que Président Directeur Général de Goldman Sachs ou 1 an comme charpentier chez Jojo Construction, ca n'est pas vraiment la même chose, quoique..."
    self._table = [('Entreprise', current_user.company),
                   ("Ancienneté dans l'entreprise", current_user.xp_at_company),
                   ('Taille', current_user.company_size),
                   ('Secteur', current_user.sector),
                   ('Poste', current_user.job),
                   ("Ancienneté à ce poste", current_user.xp_at_job),
                   ("Fonction", current_user.function),
                   ("Position hiérachique", current_user.position),
                   ("Déplacements professionnels", current_user.mob),
                   ("Mots clés, compétences", current_user.key_words)]

  @property
  def table(self):
    return handle_none_values(self._table)


class _WorkStatus:

  def __init__(self, current_user):
    self.title = "Statut professionnel (actuel ou dernier en date)"
    self.head = "Un emploi, oui, mais dans quelles conditions? CDI/CDD, cadre/non cadre, Junior/Expert voici des données essentielles, et ne parlons pas du point sensible : le salaire..."
    self._table = [('Contrat', current_user.contract),
                   ("Type d'employeur", current_user.employer),
                   ('Statut', current_user.status),
                   ('Remunération', current_user.rem),
                   ('Monnaie', current_user.currency),
                   ("Management", current_user.management),
                   ("Experience professionnelle", current_user.xp_at_work)]

  @property
  def table(self):
    return handle_none_values(self._table)


class _Language:

  def __init__(self, current_user):
    self.title = "Langues"
    self.head = "'My tailor is rich', cela parle à tout le monde, mais ca ne veut pas dire être billingue. Regarder la dernière saison de Games Of Thrones en VO non sous titré ? Cela peut être un point de départ..."
    self._table = [('Anglais', current_user.english),
                   ("Autres langues", current_user.others)]

  @property
  def table(self):
    return handle_none_values(self._table)


class ManageUsersText:

  def __init__(self):
    try:
      current_user
    except Exception as e:
      raise e

    self.page = _Page(current_user)
    self.account = _Account(current_user)
    self.expectation = _Expectation(current_user)
    self.resume = _Resume(current_user)
    self.identification = _Identification(current_user)
    self.localisation = _Localisation(current_user)
    self.diploma = _Diploma(current_user)
    self.work_experience = _WorkExperience(current_user)
    self.work_status = _WorkStatus(current_user)
    self.language = _Language(current_user)
