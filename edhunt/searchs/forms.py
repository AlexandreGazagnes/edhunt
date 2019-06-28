from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import (StringField, PasswordField, SubmitField, BooleanField,
                     TextAreaField, SelectField, SelectMultipleField)
from wtforms.validators import (DataRequired, Length, Email, EqualTo,
                                ValidationError)


from edhunt.utils.forms import HelpMessages, Validator, _handle_tous_indiff
from edhunt.searchs.utils import SearchsEnums


class _CreateSearchForm(FlaskForm):

  name = StringField('Nom',
                     render_kw={"placeholder": "Ma Recherche 1"},
                     )
  mob = SelectField('Périmètre géographique',
                    description=HelpMessages.unique_select,
                    choices=SearchsEnums.choices('mob'),
                    validators=[DataRequired()])

  country_1 = StringField("Pays 1 (jusqu'à 5 possibles)", render_kw={"placeholder": "ex : 'France"})
  country_2 = StringField('Pays 2', render_kw={"placeholder": "ex : 'Japon"})
  country_3 = StringField('Pays 3', render_kw={"placeholder": "ex : 'France"})
  country_4 = StringField('Pays 4', render_kw={"placeholder": "ex : 'France"})
  country_5 = StringField('Pays 5', render_kw={"placeholder": "ex : France"})

  region_1 = StringField("Région 1 (jusqu'à 5 possibles)", render_kw={"placeholder": "ex : Bretagne"})
  region_2 = StringField('Région 2', render_kw={"placeholder": "ex : Bretagne"})
  region_3 = StringField('Région 3', render_kw={"placeholder": "ex : Bretagne"})
  region_4 = StringField('Région 4', render_kw={"placeholder": "ex : Bretagne"})
  region_5 = StringField('Région 5', render_kw={"placeholder": "ex : Bretagne"})

  departement_1 = StringField("Département 1 (jusqu'à 5 possibles)",
                              render_kw={"placeholder": "ex : Aveyron"})
  departement_2 = StringField('Département 2',
                              render_kw={"placeholder": "ex : Aveyron"})
  departement_3 = StringField('Département 3',
                              render_kw={"placeholder": "ex : Aveyron"})
  departement_4 = StringField('Département 4',
                              render_kw={"placeholder": "ex : Aveyron"})
  departement_5 = StringField('Département 5',
                              render_kw={"placeholder": "ex : Aveyron"})

  town_1 = StringField("Ville 1 (jusqu'à 5 possibles)", render_kw={"placeholder": "ex : Grenoble"})
  town_2 = StringField('Ville 2', render_kw={"placeholder": "ex : Grenoble"})
  town_3 = StringField('Ville 3', render_kw={"placeholder": "ex : Grenoble"})
  town_4 = StringField('Ville 4', render_kw={"placeholder": "ex : Grenoble"})
  town_5 = StringField('Ville 5', render_kw={"placeholder": "ex : Grenoble"})

  key_words = TextAreaField('Mots clés ou compétences (minimum 3)',
                            render_kw={"placeholder": str(
                                "mots clés séparés par une "
                                "virgule \nex : ' vente, architecture, contrôle de gestion '")},
                            description=HelpMessages.comma_sep)
  submit = SubmitField("Créer")

  def validate_name(self, name):
    Validator.required(name)
    Validator.length(name, 3, 40)

  def validate_country_1(self, country_1):
    if self.mob.data == "Pays":
      Validator.required(country_1)
      Validator.country(country_1)

  def validate_country_2(self, country_2):
    if (self.mob.data == "Pays") and country_2.data:
      Validator.country(country_2)

  def validate_country_3(self, country_3):
    if (self.mob.data == "Pays") and country_3.data:
      Validator.country(country_3)

  def validate_country_4(self, country_4):
    if (self.mob.data == "Pays") and country_4.data:
      Validator.country(country_4)

  def validate_country_5(self, country_5):
    if (self.mob.data == "Pays") and country_5.data:
      Validator.country(country_5)

  def validate_region_1(self, region_1):
    if self.mob.data == "Région":
      Validator.required(region_1)
      Validator.region(region_1)

  def validate_region_2(self, region_2):
    if (self.mob.data == "Région") and region_2.data:
      Validator.region(region_2)

  def validate_region_3(self, region_3):
    if (self.mob.data == "Région") and region_3.data:
      Validator.region(region_3)

  def validate_region_4(self, region_4):
    if (self.mob.data == "Région") and region_4.data:
      Validator.region(region_4)

  def validate_region_5(self, region_5):
    if (self.mob.data == "Région") and region_5.data:
      Validator.region(region_5)

  def validate_departement_1(self, departement_1):
    if self.mob.data == "Département":
      Validator.required(departement_1)
      Validator.departement(departement_1)

  def validate_departement_2(self, departement_2):
    if (self.mob.data == "Département") and departement_2.data:
      Validator.departement(departement_2)

  def validate_departement_3(self, departement_3):
    if (self.mob.data == "Département") and departement_3.data:
      Validator.departement(departement_3)

  def validate_departement_4(self, departement_4):
    if (self.mob.data == "Département") and departement_4.data:
      Validator.departement(departement_4)

  def validate_departement_5(self, departement_5):
    if (self.mob.data == "Département") and departement_5.data:
      Validator.departement(departement_5)

  def validate_town_1(self, town_1):
    if (self.mob.data == "Ville") and (not self.town_1.data):
      raise ValidationError('Data Required')

  def validate_key_words(self, key_words):
    Validator.required(key_words)
    Validator.length(key_words, 6, 300)
    _key_words = key_words.data.split(",")
    if not len(_key_words) >= 3:
      raise ValidationError('minimum 3 mots')
    _key_words = [i.lower().strip().replace("  ", " ")
                  .replace("-", " ").replace("  ", " ").strip()
                  for i in _key_words]
    _key_words = ", ".join(_key_words)
    self.key_words.data = key_words.data = _key_words


class _UpdateWorkStatusForm(FlaskForm):

  contract = SelectMultipleField('Type de Contrat',
                                 description=HelpMessages.multiple_select,
                                 choices=SearchsEnums.choices('contract'),
                                 validators=[DataRequired()])
  employer = SelectMultipleField("Type d'employeur",
                                 description=HelpMessages.multiple_select,
                                 choices=SearchsEnums.choices('employer'),
                                 validators=[DataRequired()])
  status = SelectMultipleField("Statut",
                               description=HelpMessages.multiple_select,
                               choices=SearchsEnums.choices('status'),
                               validators=[DataRequired()])
  rem = SelectMultipleField("Rémunération annuelle brute",
                            description=HelpMessages.multiple_select,
                            choices=SearchsEnums.choices('rem'),
                            validators=[DataRequired()])
  currency = SelectField("Monnaie",
                         description=HelpMessages.unique_select,
                         choices=SearchsEnums.choices('currency'),
                         validators=[DataRequired()],
                         default="Euro")
  management = SelectField("Management",
                           description=HelpMessages.unique_select,
                           choices=SearchsEnums.choices('booleen'),
                           validators=[DataRequired()])
  submit = SubmitField("Modifier")

  def validate_contract(self, contract):
    Validator.required(contract)
    _handle_tous_indiff(self, 'contract')

  def validate_employer(self, employer):
    Validator.required(employer)
    _handle_tous_indiff(self, 'employer')

  def validate_status(self, status):
    Validator.required(status)
    _handle_tous_indiff(self, 'status')

  def validate_rem(self, rem):
    Validator.required(rem)
    _handle_tous_indiff(self, 'rem')


class _UpdateJobForm(FlaskForm):

  company = StringField('Entreprise recherchées',
                        render_kw={"placeholder": "Orange, "
                                   "Google, SauverLaPlanete.com, "
                                   "AmisDesAnimauxSA "},
                        description=HelpMessages.comma_sep)
  not_company = StringField('Entreprise évitées',
                            render_kw={"placeholder": "TonSanto, EsclavagismeSA"
                                       ", Lehmann Brother"},
                            description=HelpMessages.comma_sep)
  company_size = SelectMultipleField("Taille de l'entreprise",
                                     description=HelpMessages.multiple_select,
                                     choices=SearchsEnums.choices("company_size"),
                                     validators=[DataRequired()],
                                     default="-")
  job = StringField('Postes',
                    render_kw={"placeholder": "Responsable Recrutement, "
                               "Developpeur Web, Notaire"},
                    description=HelpMessages.comma_sep)
  sector = SelectMultipleField("Secteur",
                               description=HelpMessages.multiple_select,
                               choices=SearchsEnums.choices("sector"),
                               validators=[DataRequired()],
                               default="-")
  function = SelectMultipleField("Fonction",
                                 description=HelpMessages.multiple_select,
                                 choices=SearchsEnums.choices("function"),
                                 validators=[DataRequired()],
                                 default="-")
  position = SelectMultipleField("Position",
                                 description=HelpMessages.multiple_select,
                                 choices=SearchsEnums.choices("position"),
                                 default="-")
  not_key_words = TextAreaField("Mots clés à bannir",
                                render_kw={"placeholder": "torture, massacre de bébés phoques, travailler tout nu"},
                                description=HelpMessages.comma_sep)
  submit = SubmitField("Modifier")

  def validate_company(self, company):
    if company.data:
      Validator.length(company, 2, 200)

  def validate_not_company(self, not_company):
    if not_company.data:
      Validator.length(not_company, 2, 200)

  def validate_job(self, job):
    Validator.required(job)
    Validator.length(job, 2, 200)

  def validate_company_size(self, company_size):
    Validator.required(company_size)
    _handle_tous_indiff(self, 'company_size')

  def validate_sector(self, sector):
    Validator.required(sector)
    _handle_tous_indiff(self, 'sector')

  def validate_function(self, function):
    Validator.required(function)
    _handle_tous_indiff(self, 'function')

  def validate_position(self, position):
    Validator.required(position)
    _handle_tous_indiff(self, 'position')

  def validate_not_key_words(self, not_key_words):
    if not_key_words.data:
      Validator.length(not_key_words, 0, 300)
      _not_key_words = not_key_words.data.split(",")
      _not_key_words = [i.lower().strip().replace("  ", " ")
                        .replace("-", " ").replace("  ", " ").strip()
                        for i in _not_key_words]
      _not_key_words = ", ".join(_not_key_words)
      self.not_key_words.data = not_key_words.data = _not_key_words


class _UpdateLanguagesForm(FlaskForm):

  english_mandatory = SelectMultipleField("% d'Anglais",
                                          description=HelpMessages.multiple_select,
                                          choices=SearchsEnums.choices("english_mandatory"),
                                          validators=[DataRequired()],
                                          default="-")
  other_languages = StringField('Autres Langues',
                                render_kw={"placeholder": "Italien, Espéranto"},
                                description=HelpMessages.comma_sep,
                                validators=[Length(max=50)])
  submit = SubmitField("Modifier")

  def validate_english_mandatory(self, english_mandatory):
    Validator.required(english_mandatory)
    _handle_tous_indiff(self, 'english_mandatory')

  def validate_other_languages(self, other_languages):
    if other_languages.data:
      Validator.length(other_languages, 0, 200)


class _DeleteForm(FlaskForm):

  submit = SubmitField("Supprimer")


class SearchsForms():

  Create = _CreateSearchForm
  Update = _CreateSearchForm
  Status = _UpdateWorkStatusForm
  Job = _UpdateJobForm
  Languages = _UpdateLanguagesForm
  Delete = _DeleteForm
