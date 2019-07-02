from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import (StringField, PasswordField, SubmitField, BooleanField,
                     TextAreaField, SelectField, SelectMultipleField)
from wtforms.validators import (DataRequired, Length, Email, EqualTo,
                                ValidationError)

from edhunt.utils.forms import HelpMessages, Validator, _handle_tous_indiff
from edhunt.users.utils import UsersEnums
from edhunt.main.utils import QuestionnaireEnums
from edhunt.config import Params


class _Form_0(FlaskForm):

  search = SelectField("Niveau d'écoute du marché",
                       description=HelpMessages.unique_select,
                       choices=UsersEnums.choices('search'))

  employed = SelectField('En poste actuellement',
                         description=HelpMessages.unique_select,
                         choices=UsersEnums.choices('trooleen'))

  function = SelectField('Fonction',
                         description=HelpMessages.unique_select,
                         choices=UsersEnums.choices('function'))

  xp_at_work = StringField('Experience professionnelle',
                           render_kw={"placeholder": "12"})

  zip_code = StringField('Code postal',)

  rem = SelectField('Rémuneration actuelle',
                    description=HelpMessages.unique_select,
                    choices=UsersEnums.choices("small_rem"))

  submit = SubmitField("s'inscrire")


class _Form_1(FlaskForm):

  # freeHunt
  feat_1 = SelectField("recherche et centralise toutes les offres d'emploi qui m'intéressent",
                       description=HelpMessages.unique_select,
                       choices=UsersEnums.choices('trooleen'))

  feat_2 = SelectField("me permette de candidater à n'importe quelle offre en un clic",
                       description=HelpMessages.unique_select,
                       choices=UsersEnums.choices('trooleen'))

  feat_3 = SelectField("me fournisse un outil de gestion et de suivi de mes différentes pistes",
                       description=HelpMessages.unique_select,
                       choices=UsersEnums.choices('trooleen'))

  # smartHunt
  feat_4 = SelectField("diffuse et mette à jour mon CV ou mon profil sur les différentes plateformes d'emploi",
                       description=HelpMessages.unique_select,
                       choices=UsersEnums.choices('trooleen'))

  feat_5 = SelectField("candidate pour moi automatiquement sur les offres d'emploi qui m'intéressent *",
                       description=HelpMessages.unique_select,
                       choices=UsersEnums.choices('trooleen'))

  feat_6 = SelectField("identifie pour moi les décisionnaires RH / opérationnels sur les postes qui m'intéressent * ",
                       description=HelpMessages.unique_select,
                       choices=UsersEnums.choices('trooleen'))

  # bigHunt
  feat_7 = SelectField("accède pour moi à tout site/interface externe nécessitant des actions d’enregistrement spécifique (site d'entreprise, jobboard, cabinet de recrutement...) **",
                       description=HelpMessages.unique_select,
                       choices=UsersEnums.choices('trooleen'))

  feat_8 = SelectField("gère automatiquement les mails de retour de candidatures et les intègre à l'outil de gestion de mes pistes d'emploi **",
                       description=HelpMessages.unique_select,
                       choices=UsersEnums.choices('trooleen'))

  feat_9 = SelectField("appuie ma candidature par l'envoi d'un message personnalisé aux décisionnaires RH / opérationnels, en plus de mon CV **",
                       description=HelpMessages.unique_select,
                       choices=UsersEnums.choices('trooleen'))

  # proHunt
  feat_10 = SelectField("m'aide pour la définition de mon projet professionnel et dans  la selections des offres sur lesquelles candidater - via un consultant edhunt ***",
                        description=HelpMessages.unique_select,
                        choices=UsersEnums.choices('trooleen'))

  feat_11 = SelectField("m'aide pour la rédaction ou l'amélioration de mon CV, rédige automatiquement ou manuellement ma/mes lettre(s) de motivations - via un consultant edhunt ***",
                        description=HelpMessages.unique_select,
                        choices=UsersEnums.choices('trooleen'))

  feat_12 = SelectField("m'accompagne dans les différentes phases opérationnelles de mes process de recrutement : brief avant les entretiens, débrief après les entretiens, choix parmi les différentes pistes... - via un consultant edhunt ***",
                        description=HelpMessages.unique_select,
                        choices=UsersEnums.choices('trooleen'))

  feat_13 = SelectField("aille chercher pour moi des postes sur mesure en appellant ou en rencontrant en direct les décisionnaires RH / opérationnels pour défendre ma candidature - via un consultant edhunt ***",
                        description=HelpMessages.unique_select,
                        choices=UsersEnums.choices('trooleen'))

  feat_14 = SelectField("m'accompagne lors de la négociation salariale, la signature de mon contrat de travail et ma période d'essai - via un consultant edhunt ***",
                        description=HelpMessages.unique_select,
                        choices=UsersEnums.choices('trooleen'))

  submit = SubmitField("Suivant")

  def validate_feat_1(self, feat_1):
    Validator.required(feat_1)
    Validator.choice_not_null(feat_1)

  def validate_feat_2(self, feat_2):
    Validator.required(feat_2)
    Validator.choice_not_null(feat_2)

  def validate_feat_3(self, feat_3):
    Validator.required(feat_3)
    Validator.choice_not_null(feat_3)

  # def validate_feat_4(self, feat_4):
  #     Validator.required(feat_4)
  #     Validator.choice_not_null(feat_4)

  # def validate_feat_5(self, feat_5):
  #     Validator.required(feat_5)
  #     Validator.choice_not_null(feat_5)

  # def validate_feat_6(self, feat_6):
  #     Validator.required(feat_6)
  #     Validator.choice_not_null(feat_6)

  # def validate_feat_7(self, feat_7):
  #     Validator.required(feat_7)
  #     Validator.choice_not_null(feat_7)

  # def validate_feat_8(self, feat_8):
  #     Validator.required(feat_8)
  #     Validator.choice_not_null(feat_8)

  # def validate_feat_9(self, feat_9):
  #     Validator.required(feat_9)
  #     Validator.choice_not_null(feat_9)

  # def validate_feat_10(self, feat_10):
  #     Validator.required(feat_10)
  #     Validator.choice_not_null(feat_10)

  # def validate_feat_11(self, feat_11):
  #     Validator.required(feat_11)
  #     Validator.choice_not_null(feat_11)

  # def validate_feat_12(self, feat_12):
  #     Validator.required(feat_12)
  #     Validator.choice_not_null(feat_12)

  # def validate_feat_13(self, feat_13):
  #     Validator.required(feat_13)
  #     Validator.choice_not_null(feat_13)

  # def validate_feat_14(self, feat_14):
  #     Validator.required(feat_14)
  #     Validator.choice_not_null(feat_14)


class _Form_2(FlaskForm):

  contract = SelectField('Contrat de travail actuel',
                         description=HelpMessages.unique_select,
                         choices=UsersEnums.choices("contract"))

  status = SelectField('Statut actuel',
                       description=HelpMessages.unique_select,
                       choices=UsersEnums.choices('status'))

  sector = SelectField('Secteur actuel',
                       description=HelpMessages.unique_select,
                       choices=UsersEnums.choices('sector'))

  # function = SelectField('Fonction',
  #                        description=HelpMessages.unique_select,
  #                        choices=UsersEnums.choices('function'))

  position = SelectField('Position hiérachique actuelle',
                         description=HelpMessages.unique_select,
                         choices=UsersEnums.choices('position'))

  # management = SelectField('Management',
  #                          description=HelpMessages.unique_select,
  #                          choices=UsersEnums.choices('management'))

  diploma_level = SelectField('Niveau de diplôme',
                              description=HelpMessages.unique_select,
                              choices=UsersEnums.choices('diploma_level'))

  # rem = SelectField('Rémuneration (annuelle brute fixe - en Euros)',
  #                   description=HelpMessages.unique_select,
  #                   choices=UsersEnums.choices("small_rem"))

  # xp_at_work = StringField('Experience professionnelle',
  #                          render_kw={"placeholder": "12"})

  # diploma_type = SelectField('Type de diplôme',
  #                            description=HelpMessages.unique_select,
  #                            choices=UsersEnums.choices('diploma_type'))
  diploma_year = StringField('Année d\'obtention')

  # zip_code = StringField('Code postal',)

  submit = SubmitField("Suivant")

  def validate_status(self, status):
    Validator.required(status)
    Validator.choice_not_null(status)

  def validate_sector(self, sector):
    Validator.required(sector)
    Validator.choice_not_null(sector)

  def validate_function(self, function):
    Validator.required(function)
    Validator.choice_not_null(function)

  # def validate_position(self, position):
  #     Validator.required(position)
  #     Validator.choice_not_null(position)

  # def validate_management(self, management):
  #     Validator.required(management)
  #     Validator.choice_not_null(management)

  def validate_rem(self, rem):
    Validator.required(rem)
    Validator.choice_not_null(rem)

  # def validate_xp_at_work(self, xp_at_work):
  #     Validator.required(xp_at_work)
  #     Validator.length(xp_at_work, 1, 2)
  #     Validator.xp(xp_at_work)

  def validate_diploma_level(self, diploma_level):
    Validator.required(diploma_level)
    Validator.choice_not_null(diploma_level)

  # def validate_diploma_type(self, diploma_type):
  #     Validator.required(diploma_type)
  #     Validator.choice_not_null(diploma_type)

  def validate_diploma_year(self, diploma_year):
    Validator.required(diploma_year)
    Validator.length(diploma_year, 4, 4)
    Validator.numerical(diploma_year)
    if not (2025 >= int(str(diploma_year.data).strip()) >= 1969):
      raise ValidationError('Humm... Vous êtes trop jeune ou trop agé pour travailler, non?')

  def validate_zip_code(self, zip_code):
    Validator.required(zip_code)
    Validator.length(zip_code, 5, 5)
    Validator.numerical(zip_code)


class _Form_3(FlaskForm):
  email = StringField("Email ",
                      render_kw={"placeholder": "email@email.com"})
  phone = StringField("Téléphone",
                      render_kw={"placeholder": "06.06.06.06.06"})
  hour = StringField("Disponibilités ",
                     render_kw={"placeholder": "entre 12 et 14h, toute la journée..."})
  device_type = SelectField("Type d'appareil utilisé ",
                            choices=QuestionnaireEnums.choices('device_type'))
  submit = SubmitField("Valider")


class _Form_4(FlaskForm):

  offer_timing = SelectField("lu / regardé une offre d'emploi c'était il y a : ",
                             description=HelpMessages.unique_select,
                             choices=QuestionnaireEnums.choices('timing'))

  candidature_timing = SelectField("candidaté / envoyé mon CV pour une offre d'emploi c'était il y a : ",
                                   description=HelpMessages.unique_select,
                                   choices=QuestionnaireEnums.choices('timing'))

  call_timing = SelectField("reçu un appel (cabinet de recrutement, SSII, service RH) pour une offre d'emploi c'était il y a : ",
                            description=HelpMessages.unique_select,
                            choices=QuestionnaireEnums.choices('timing'))

  interview_timing = SelectField("passé un entretien d'embauche, c'était il y a :",
                                 description=HelpMessages.unique_select,
                                 choices=QuestionnaireEnums.choices('timing'))

  submit = SubmitField("Suivant")


class _Form_5(FlaskForm):

  fond_already = SelectField(
      "J'ai déjà eu connaissance d'un service similaire ou fortement complémentaire",
      description=HelpMessages.unique_select,
      choices=UsersEnums.choices('trooleen'))

  fond_concurency = TextAreaField("Si oui, lequel",
                                  render_kw={"placeholder": "Oui, j'emploie Pénélope Fillon depuis 1997 en CESU pour chercher un job à ma place"})

  # forme_choc_level = SelectField(
  #     "J'ai été globalement dérangé par la forme du site",
  #     description=HelpMessages.unique_select,
  #     choices=QuestionnaireEnums.choices('satisfaction'))

  # forme_cool_level = SelectField(
  #     "J'ai globalement trouvé la forme du site agréable",
  #     description=HelpMessages.unique_select,
  #     choices=QuestionnaireEnums.choices('satisfaction'))

  fond_compr_level = SelectField(
      "J'ai le sentiment d'avoir globalement compris les services proposés par edhunt",
      description=HelpMessages.unique_select,
      choices=QuestionnaireEnums.choices('satisfaction'))

  fond_painful_level = SelectField("J'ai déjà trouvé pénible la multiplicité des plateformes, avec autant de logins, de mots de passe, de connexions et d'interfaces différents",
                                   description=HelpMessages.unique_select,
                                   choices=QuestionnaireEnums.choices('satisfaction'))

  fond_interest_level = SelectField("Avoir une interface unique pour gérer et automatiser tous mes process de recrutement serait une bonne chose",
                                    description=HelpMessages.unique_select,
                                    choices=QuestionnaireEnums.choices('satisfaction'))

  # device_name = StringField("Type d'appareil utilisé ",
  #                           render_kw={"placeholder": "Optionnel - iphone3, PC portable, Nokia 3310, Minitel"})

  remarque = TextAreaField("Une dernière chose avant de se quitter?",
                           render_kw={"placeholder": "Une question, une remarque, un doute, un mot doux?"})

  submit = SubmitField("Suivant")

  #   def validate_fond_already(self, fond_already):
  #     Validator.required(fond_already)
  #     Validator.choice_not_null(fond_already)

  #   def validate_fond_concurency(self, fond_concurency):
  #     Validator.length(fond_concurency, 0, 300)

  #   def validate_forme_choc_level(self, forme_choc_level):
  #     Validator.required(forme_choc_level)
  #     Validator.choice_not_null(forme_choc_level)

  #   def validate_forme_cool_level(self, forme_cool_level):
  #     Validator.required(forme_cool_level)
  #     Validator.choice_not_null(forme_cool_level)

  #   def validate_fond_compr_level(self, fond_compr_level):
  #     Validator.required(fond_compr_level)
  #     Validator.choice_not_null(fond_compr_level)

  #   def validate_fond_painful_level(self, fond_painful_level):
  #     Validator.required(fond_painful_level)
  #     Validator.choice_not_null(fond_painful_level)

  #   def validate_fond_interest_level(self, fond_interest_level):
  #     Validator.required(fond_interest_level)
  #     Validator.choice_not_null(fond_interest_level)

  #   def validate_device_type(self, device_type):
  #     Validator.required(device_type)

  #   def validate_remarque(self, remarque):
  #     # Validator.required(remarque)
  #     pass

  # # class _Form_1(FlaskForm):

  # #   def validate_search(self, search):
  # #     Validator.required(search)
  # #     Validator.choice_not_null(search)

  # #   def validate_employed(self, employed):
  # #     Validator.required(employed)
  # #     Validator.choice_not_null(employed)

  # #   # def validate_contract(self, contract):
  # #   #   Validator.required(contract)
  # #   #   Validator.choice_not_null(contract)

  #   # submit = SubmitField("Suivant")

  # class _Form_12(FlaskForm):

  #   offer_timing = SelectField("lu / regardé une offre d'emploi c'était il y a : ",
  #                              description=HelpMessages.unique_select,
  #                              choices=QuestionnaireEnums.choices('timing'))

  #   candidature_timing = SelectField("candidaté / envoyé mon CV pour une offre d'emploi c'était il y a : ",
  #                                    description=HelpMessages.unique_select,
  #                                    choices=QuestionnaireEnums.choices('timing'))

  #   call_timing = SelectField("reçu un appel (cabinet de recrutement, SSII, service RH) pour une offre d'emploi c'était il y a : ",
  #                             description=HelpMessages.unique_select,
  #                             choices=QuestionnaireEnums.choices('timing'))

  #   interview_timing = SelectField("passé un entretien d'embauche, c'était il y a :",
  #                                  description=HelpMessages.unique_select,
  #                                  choices=QuestionnaireEnums.choices('timing'))

  #   submit = SubmitField("Suivant")

  #   def validate_offer_timing(self, offer_timing):
  #     Validator.required(offer_timing)
  #     Validator.choice_not_null(offer_timing)

  #   def validate_candidature_timing(self, candidature_timing):
  #     Validator.required(candidature_timing)
  #     Validator.choice_not_null(candidature_timing)

  #   def validate_call_timing(self, call_timing):
  #     Validator.required(call_timing)
  #     Validator.choice_not_null(call_timing)

  #   def validate_interview_timing(self, interview_timing):
  #     Validator.required(interview_timing)
  #     Validator.choice_not_null(interview_timing)

  # # class _EdhuntForm(FlaskForm):

  #   # forme
  #   # forme_generic = TextAreaField("Avis général sur la forme du site",
  #   #                               render_kw={"placeholder": "Obligatoire - commentaire sur la police, les fautes d'orthographe, problèmes d'affichage etc etc"})
  #   # forme_good = TextAreaField("Quelque chose de spécialement sympa/agréable sur la forme  du site?",
  #   #                            render_kw={"placeholder": "Facultatif"})

  #   # forme_bad = TextAreaField("Quelque chose de spécialement bizarre/génant sur la forme du site?",
  #   #                           render_kw={"placeholder": "Facultatif"})

  #   # # fond
  #   # fond_generic = TextAreaField("Avis général sur le service proposé",
  #   #                              render_kw={"placeholder": "Obligatoire - bien/pas compris? déjà pensé à se type de service? réel/possible besoin pour toi?"})

  #   # fond_questions = TextAreaField("Questions/réticences/doutes/réflexions sur ce type de service",
  #   #                                render_kw={"placeholder": str("Facultatif - aurais-tu des réticences concernant ce type de services, est-ce qu'il faudrait spécifiquement ajouter une option, un service...")})

  #   # fond_already = SelectField(
  #   #     "As-tu déjà eu connaissance d'un service similaire ou fortement complémentaire",
  #   #     description=HelpMessages.unique_select,
  #   #     choices=UsersEnums.choices('trooleen'))

  #   # fond_concurency = TextAreaField("Si oui, lequel",
  #   #                                 render_kw={"placeholder": "Oui, j'emploie Pénélope Fillon depuis 1997 en CESU pour chercher un job à ma place"})

  #   #     # qcm
  #   #     forme_choc_level = SelectField(
  #   #         "J'ai été globalement dérangé par la forme du site",
  #   #         description=HelpMessages.unique_select,
  #   #         choices=QuestionnaireEnums.choices('satisfaction'))

  #   #     forme_cool_level = SelectField(
  #   #         "J'ai globalement trouvé la forme du site agréable",
  #   #         description=HelpMessages.unique_select,
  #   #         choices=QuestionnaireEnums.choices('satisfaction'))

  #   #     fond_compr_level = SelectField(
  #   #         "J'ai globalement compris le service proposé par edhunt",
  #   #         description=HelpMessages.unique_select,
  #   #         choices=QuestionnaireEnums.choices('satisfaction'))

  #   #     fond_painful_level = SelectField("J'ai déjà trouvé pénible la multiplicité des plateformes, avec autant de logins, de mots de passe, de connexions et d'interfaces différents",
  #   #                                      description=HelpMessages.unique_select,
  #   #                                      choices=QuestionnaireEnums.choices('satisfaction'))

  #   #     fond_interest_level = SelectField("Avoir une interface unique pour gérer et automatiser tous mes process de recrutement serait une bonne chose",
  #   #                                       description=HelpMessages.unique_select,
  #   #                                       choices=QuestionnaireEnums.choices('satisfaction'))

  #   #     # earth = SelectField("Je pense que la terre est creuse et qu'Élisabeth II est un réptile extraterrestre venu du futur pour asservir l'Humanité",
  #   #     #                     description=HelpMessages.unique_select,
  #   #     #                     choices=QuestionnaireEnums.choices('satisfaction'))

  #   #     # user
  #   #     # user = StringField("Utilisateur",
  #   #     #                    render_kw={"placeholder": "Facultatif - Provencal Le Gaulois"})

  #   #     device_type = SelectField("Type d'appareil utilisé ",
  #   #                               choices=[QuestionnaireEnums.choices('device_type')])

  #   #     # search
  #   #     search = SelectField("Niveau d'écoute du marché",
  #   #                          description=HelpMessages.unique_select,
  #   #                          choices=UsersEnums.choices('search'))

  #   #     # employed
  #   #     employed = SelectField('En poste actuellement',
  #   #                            description=HelpMessages.unique_select,
  #   #                            choices=UsersEnums.choices('trooleen'))

  #   #     remarque = TextAreaField("On t'écoute...",
  #   #                              render_kw={"placeholder": "Un champ oublié, une erreur dans les questions, un mot doux?"})

  #   #     submit = SubmitField("Soumettre")

  #   #     # def validate_forme_generic(self, forme_generic):
  #   #     #     Validator.required(forme_generic)
  #   #     #     Validator.length(forme_generic, 1, 1000)

  #   #     # def validate_forme_good(self, forme_good):
  #   #     #     Validator.length(forme_good, 0, 1000)

  #   #     # def validate_form_bad(self, form_bad):
  #   #     #     Validator.length(form_bad, 0, 1000)

  #   #     # def validate_fond_generic(self, fond_generic):
  #   #     #     Validator.required(fond_generic)
  #   #     #     Validator.length(fond_generic, 1, 1000)

  #   #     # def validate_fond_questions(self, fond_questions):
  #   #     #     Validator.length(fond_questions, 0, 1000)

  #   #     def validate_fond_already(self, fond_already):
  #   #         Validator.required(fond_already)
  #   #         Validator.choice_not_null(fond_already)

  #   #     def validate_fond_concurency(self, fond_concurency):
  #   #         Validator.length(fond_concurency, 0, 300)

  #   #     def validate_forme_choc_level(self, forme_choc_level):
  #   #         Validator.required(forme_choc_level)
  #   #         Validator.choice_not_null(forme_choc_level)

  #   #     def validate_forme_cool_level(self, forme_cool_level):
  #   #         Validator.required(forme_cool_level)
  #   #         Validator.choice_not_null(forme_cool_level)

  #   #     def validate_fond_compr_level(self, fond_compr_level):
  #   #         Validator.required(fond_compr_level)
  #   #         Validator.choice_not_null(fond_compr_level)

  #   #     def validate_fond_painful_level(self, fond_painful_level):
  #   #         Validator.required(fond_painful_level)
  #   #         Validator.choice_not_null(fond_painful_level)

  #   #     def validate_fond_interest_level(self, fond_interest_level):
  #   #         Validator.required(fond_interest_level)
  #   #         Validator.choice_not_null(fond_interest_level)

  #   #     def validate_device_type(self, device_type):
  #   #         Validator.required(device_type)

  #   # class _UserForm(FlaskForm):

  #   #     # work status
  #   #     # employed = SelectField('En poste actuellement',
  #   #     #                        description=HelpMessages.unique_select,
  #   #     #                        choices=UsersEnums.choices('trooleen'))

  #   #     contract = SelectField('Contrat de travail',
  #   #                            description=HelpMessages.unique_select,
  #   #                            choices=UsersEnums.choices("contract"))

  #   #     status = SelectField('Statut',
  #   #                          description=HelpMessages.unique_select,
  #   #                          choices=UsersEnums.choices('status'))

  #   #     sector = SelectField('Secteur',
  #   #                          description=HelpMessages.unique_select,
  #   #                          choices=UsersEnums.choices('sector'))

  #   #     function = SelectField('Fonction',
  #   #                            description=HelpMessages.unique_select,
  #   #                            choices=UsersEnums.choices('function'))

  #   #     position = SelectField('Position hiérachique',
  #   #                            description=HelpMessages.unique_select,
  #   #                            choices=UsersEnums.choices('position'))

  #   #     management = SelectField('Management',
  #   #                              description=HelpMessages.unique_select,
  #   #                              choices=UsersEnums.choices('management'))

  #   #     rem = SelectField('Rémuneration (annuelle brute fixe - en Euros)',
  #   #                       description=HelpMessages.unique_select,
  #   #                       choices=UsersEnums.choices("small_rem"))

  #   #     # xp_at_company = StringField('Ancienneté dans l\'entreprise',
  #   #     #                             render_kw={"placeholder": "12"})

  #   #     # xp_at_job = StringField('Ancienneté à ce poste',
  #   #     #                         render_kw={"placeholder": "12"})

  #   #     xp_at_work = StringField('Experience professionnelle totale',
  #   #                              render_kw={"placeholder": "12"})

  #   #     # marre = SelectField("Je commence à en avoir marre de répondre à des questions bizarres, mais comme je suis quelqu'un de sympa, j'irai jusqu'au bout de ce questionnaire",
  #   #     #                     description=HelpMessages.unique_select,
  #   #     #                     choices=QuestionnaireEnums.choices('satisfaction'))

  #   #     # search
  #   #     # search = SelectField("Niveau d'écoute du marché",
  #   #     #                      description=HelpMessages.unique_select,
  #   #     #                      choices=UsersEnums.choices('search'))

  #   #     offer_timing = SelectField("La dernière fois que j'ai lu/regardé une offre d'emploi c'était il y a : ",
  #   #                                description=HelpMessages.unique_select,
  #   #                                choices=QuestionnaireEnums.choices('timing'))

  #   #     candidature_timing = SelectField("La dernière fois que j'ai candidaté/envoyé mon CV pour une offre d'emploi c'était il y a : ",
  #   #                                      description=HelpMessages.unique_select,
  #   #                                      choices=QuestionnaireEnums.choices('timing'))

  #   #     call_timing = SelectField("La dernière fois que j'ai reçu un appel (cabinet de recrutement, SSII - entreprise) pour une offre d'emploi c'était il y a : ",
  #   #                               description=HelpMessages.unique_select,
  #   #                               choices=QuestionnaireEnums.choices('timing'))

  #   #     interview_timing = SelectField("La dernière que j'ai passé un entretien de recrutement, c'était il y a :",
  #   #                                    description=HelpMessages.unique_select,
  #   #                                    choices=QuestionnaireEnums.choices('timing'))

  #   #     # user
  #   #     diploma_level = SelectField('Niveau de Diplôme',
  #   #                                 description=HelpMessages.unique_select,
  #   #                                 choices=UsersEnums.choices('diploma_level'))

  #   #     diploma_type = SelectField('Type de diplôme',
  #   #                                description=HelpMessages.unique_select,
  #   #                                choices=UsersEnums.choices('diploma_type'))
  #   #     diploma_year = StringField('Année d\'obtention',
  #   #                                validators=[DataRequired(), Length(min=4, max=4)])

  #   #     zip_code = StringField('Code postal',
  #   #                            render_kw={"placeholder": "33000"})

  #   #     # moon = SelectField("Moi aussi je pense que les américains n'ont jamais mis le pied sur la Lune, que les pyramides ont été construites par des extraterrestre et que Michael Jackson est toujours vivant",
  #   #     #                    description=HelpMessages.unique_select,
  #   #     #                    choices=QuestionnaireEnums.choices('satisfaction'))

  #   #     remarque = TextAreaField("On t'écoute...",
  #   #                              render_kw={"placeholder": "Un champ oublié, une erreur dans les questions, un mot doux?"})

  #   #     submit = SubmitField("Soumettre")

  #   #     def validate_employed(self, employed):
  #   #         Validator.required(employed)
  #   #         Validator.choice_not_null(employed)

  #   #     def validate_contract(self, contract):
  #   #         Validator.required(contract)
  #   #         Validator.choice_not_null(contract)

  #   #     def validate_sector(self, sector):
  #   #         Validator.required(sector)
  #   #         Validator.choice_not_null(sector)

  #   #     def validate_function(self, function):
  #   #         Validator.required(function)
  #   #         Validator.choice_not_null(function)

  #   #     def validate_status(self, status):
  #   #         Validator.required(status)
  #   #         Validator.choice_not_null(status)

  #   #     def validate_position(self, position):
  #   #         Validator.required(position)
  #   #         Validator.choice_not_null(position)

  #   #     def validate_management(self, management):
  #   #         Validator.required(management)
  #   #         Validator.choice_not_null(management)

  #   #     def validate_rem(self, rem):
  #   #         Validator.required(rem)
  #   #         Validator.choice_not_null(rem)

  #   #     def validate_xp_at_work(self, xp_at_work):
  #   #         Validator.required(xp_at_work)
  #   #         Validator.length(xp_at_work, 1, 2)
  #   #         Validator.xp(xp_at_work)

  #   #     def validate_diploma_level(self, diploma_level):
  #   #         Validator.required(diploma_level)
  #   #         Validator.choice_not_null(diploma_level)

  #   #     def validate_diploma_type(self, diploma_type):
  #   #         Validator.required(diploma_type)
  #   #         Validator.choice_not_null(diploma_type)

  #   #     def validate_diploma_year(self, diploma_year):
  #   #         Validator.required(diploma_year)
  #   #         Validator.length(diploma_year, 4, 4)
  #   #         Validator.numerical(diploma_year)
  #   #         if not (2020 >= int(str(diploma_year.data).strip()) >= 1969):
  #   #             raise ValidationError('Humm... Vous êtes trop jeune ou trop agé pour travailler, non?')

  #   #     def validate_zip_code(self, zip_code):
  #   #         Validator.required(zip_code)
  #   #         Validator.length(zip_code, 5, 5)
  #   #         Validator.numerical(zip_code)

  #   #     # def validate_xp_at_job(self, xp_at_job):
  #   #     #     Validator.required(xp_at_job)
  #   #     #     Validator.length(xp_at_job, 1, 2)
  #   #     #     Validator.xp(xp_at_job)

  #   #     # def validate_xp_at_company(self, xp_at_company):
  #   #     #     Validator.required(xp_at_company)
  #   #     #     Validator.length(xp_at_company, 1, 2)
  #   #     #     Validator.xp(xp_at_company)

  #   #     # def validate_xp_at_work(self, xp_at_work):
  #   #     #     Validator.required(xp_at_work)
  #   #     #     Validator.length(xp_at_work, 1, 2)
  #   #     #     Validator.xp(xp_at_work)


class _PostForm(FlaskForm):

  pass


class _CorporateForm(FlaskForm):
  password = PasswordField('Mot de Passe',
                           render_kw={"placeholder": "Obligatoire - azerty, ca fonctionne?"})
  submit = SubmitField("Envoyer")

  def validate_password(self, password):
    Validator.required(password)
    if password.data != Params.CORPORATE_PASSWORD:
      raise ValidationError("Désolé mais le mot de passe est incorrect")


class _ContactForm(FlaskForm):

  title = StringField('Titre du message',
                      render_kw={"placeholder": "Obligatoire - titre du message"})
  # topic = None
  text = TextAreaField("Votre message",
                       render_kw={"placeholder": "Obligatoire - votre message"})
  name = StringField('Prénom, Nom ou Pseudo',
                     render_kw={"placeholder": "Obligatoire - Elias de Kelliwic"})
  email = StringField('Email',
                      render_kw={"placeholder": "Obligatoire - prenom.nom@mail.com"})
  phone = StringField('Téléphone',
                      render_kw={"placeholder": "06.06.06.06.06 "})
  # user = StringField('Prénom',
  #                    render_kw={"placeholder": "Prénom"})

  submit = SubmitField("Envoyer")

  def validate_title(self, title):
    Validator.required(title)

  def validate_text(self, text):
    Validator.required(text)

  def validate_name(self, name):
    Validator.required(name)

  def validate_email(self, email):
    Validator.required(email)


class MainForms:

  # Edhunt = _EdhuntForm
  # User = _UserForm
  Post = _PostForm
  Corporate = _CorporateForm
  Contact = _ContactForm
  # Prospect = _ProspectForm
  Form_0 = _Form_0
  Form_1 = _Form_1
  Form_2 = _Form_2
  Form_3 = _Form_3
  Form_4 = _Form_4
  Form_5 = _Form_5
  Form_6 = None
