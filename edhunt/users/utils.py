import os
import secrets
# import PyPDF2
from flask import current_app
from edhunt import db, info, warning
from PIL import Image
from pdf2image import convert_from_path, convert_from_bytes


class UsersEnums():

  booleen = ["Oui",
             "Non"]

  trooleen = ["-",
              "Oui",
              "Non"]

  sub_employed = ["-",
                  "En période d'essai",
                  "En préavis de départ",
                  "Disponible"]

  search = ["-",
            "En recherche active",
            "En veille/A l'écoute",
            "Pas à l'écoute"]

  order = ["-",
           "Trouves moi le/un job",
           "Aides moi à benchmarker le marché"]

  automation = ["-",
                "edhunt, gères les candidatures automatiquement à ma place!",
                "edhunt, ne fait rien sans ma permission!"]

  mob = ["-",
         "Ville",
         "Département",
         "Région",
         "Pays"]

  sex = ["-",
         "Homme",
         "Femme",
         "Autre / Non genré"]

  diploma_level = ["-",
                   "Autodidacte",
                   "BAC",
                   "BAC+2",
                   "BAC+3/4",
                   "BAC+5",
                   "BAC+6",
                   "BAC+8/9"]

  diploma_type = ["-",
                  'Architecte',
                  'BAC',
                  'BEP/CAP',
                  'BTS/DUT',
                  'Doctorat',
                  'ESC',
                  'IAE',
                  'IEP',
                  'IUP',
                  'Ingenieur',
                  'Licence',
                  'MBA',
                  'MS/MSC',
                  'Master 1',
                  'Master 2',
                  'Mastère/Magistère',
                  'Science Po'
                  'Universitaire'
                  'Autre']

  company_size = ["-",
                  '0 - 10',
                  '10 - 20',
                  '20 - 50',
                  '50 - 100',
                  '100 - 200',
                  '200 - 500',
                  '500 - 1 000',
                  '1 000 - 5 000',
                  '5 000 - 10 000',
                  '10 000+']

  sector = ["-",
            'Administration',
            'Banque/Finance/Assurances',
            'Conseil/Audit',
            'Distribution/Commerce',
            "Enseignement/Formation",
            "Hotellerie/Restauration",
            'Immobilier/Construction',
            'Industrie',
            "Loisir/Tourisme",
            'Web/Digital/Tech',
            "Ingénierie/Bureau d'Etudes",
            'Services',
            'Presse/Media/Communication',
            'Santé/Social',
            'Secteur Public',
            "Télécommunications/Réseaux",
            "Autre"]

  function = ["-",
              'Achats',
              'Administratif',
              'Audit/Conseil',
              'Commerce/Vente',
              'Dev/IT/Tech',
              'Finance/Contrôle de gestion',
              'Import/Export/nternational',
              "Ingénierie/Bureau d'Etudes",
              'Juridique/Fiscal',
              'Logistique/Transport',
              'Maintenance/Entretien',
              'Management/Direction Général(e)',
              "Management/Direction de Projet",
              'Marketing/Communication',
              'Opérationnel/Production',
              'Qualité/RSE',
              'R&D/Enseignement',
              'Ressources Humaines',
              "Autre"]

  position = ["-",
              "Etudiant",
              "Junior",
              "Consultant",
              "Senior",
              "Expert",
              "Chef de Projet",
              "Manager",
              "Directeur",
              "Non significatif"]

  status = ["-",
            "Cadre fonction privé",
            "Cadre fonction publique",
            "Etudiant",
            "Non cadre",
            "Autre"]

  contract = ["-",
              "CDD",
              "CDI",
              "Freelance/Indépendant",
              "Interim/CDIC",
              "Stage/Alternance",
              "Autre"]

  employer = ["-",
              "Agence d'interim",
              "Cabinet de conseil",
              "Client final",
              "ESN/SSII",
              "Sous-traitant"]

  management = ["-",
                "Oui, hiéarchique",
                "Oui, fonctionnel/projet",
                "Non"]

  small_rem = ["-",
               "- de 20 000 €",
               "20 000 - 30 000 €",
               "30 000 - 40 000 €",
               "40 000 - 50 000 €",
               "50 000 - 60 000 €",
               "60 000 - 70 000 €",
               "70 000 - 80 000 €",
               "80 000 - 100 000 €",
               "+ de 100 000 €"]

  rem = ["-",
         "20 000-",
         "20 000 - 25 000",
         "25 000 - 30 000",
         "30 000 - 35 000",
         "35 000 - 40 000",
         "40 000 - 45 000",
         "45 000 - 50 000",
         "50 000 - 55 000",
         "55 000 - 60 000",
         "60 000 - 70 000",
         "70 000 - 80 000",
         "80 000 - 100 000",
         "100 000 - 120 000",
         "120 000 - 150 000",
         "150 000+"]

  currency = ["-",
              "Euro",
              "Dollar",
              "Livre",
              "Franc suisse"]

  english = ["-",
             'Natif',
             'Billingue',
             'Fluent',
             'Professionnel',
             'Notions',
             'Scolaire']

  joboard = ["-",
             "On",
             "Off",
             "Not available"]

  joboard_form = ["-",
                  "On",
                  "Off"]

  @staticmethod
  def choices(item):
    return [(i, i) for i in UsersEnums.__dict__.get(item)]


class Joboard():

  def status():
    return db.Column(db.Enum(*UsersEnums.joboard), unique=False,
                     nullable=False, default="Off")

  def email():
    return db.Column(db.String(40), unique=True, nullable=True)

  def password():
    return db.Column(db.String(40), unique=False, nullable=True)

  def autorisation():
    return db.Column(db.Enum(*UsersEnums.booleen), unique=False,
                     nullable=False, default="Non")

  def good_user():
    return db.Column(db.Enum(*UsersEnums.booleen), unique=False,
                     nullable=False, default="Non")

  def edhunt_integrity():
    return db.Column(db.Enum(*UsersEnums.booleen), unique=False,
                     nullable=False, default="Non")


def save_resume(form_resume):
  """save resume from user form"""

  info("\n\n\nsave resume called\n\n\n ")

  random_hex = secrets.token_hex(16)
  _, f_ext = os.path.splitext(form_resume.filename)
  resume_fn = random_hex + f_ext
  resume_path = os.path.join(current_app.root_path, 'static/resumes', resume_fn)
  form_resume.save(resume_path)

  # with open(resume_path, "wb") as f:
  #     f.write(form_resume)

  return resume_fn


def create_image(filename):

  img_path = os.path.join(current_app.root_path, 'static/resumes', filename)
  img = convert_from_path(img_path)[0]
  img_path = img_path.replace(".pdf", ".jpg")
  img.save(img_path)

  img = Image.open(img_path)
  basewidth = 600
  wpercent = (basewidth / float(img.size[0]))
  hsize = int((float(img.size[1]) * float(wpercent)))
  img = img.resize((basewidth, hsize), Image.ANTIALIAS)
  img.save(img_path)

  return filename.replace(".pdf", ".jpg")
