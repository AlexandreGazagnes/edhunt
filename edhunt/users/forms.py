from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import (StringField, PasswordField, SubmitField, BooleanField,
                     TextAreaField, SelectField)
from wtforms.validators import (DataRequired, Length, Email, EqualTo,
                                ValidationError)

from edhunt.main.model import Country
from edhunt.utils.forms import Validator, HelpMessages
from edhunt.users.model import User
from edhunt.users.utils import UsersEnums


class _RegistrationForm(FlaskForm):

  username = StringField('Utilisateur',
                         render_kw={"placeholder": "MonIdentifiant"})
  email = StringField("Email",
                      render_kw={"placeholder": "email@email.com"},
                      validators=[Email()])
  password = PasswordField("Mot de Passe",
                           render_kw={"placeholder": "********"})
  confirm_password = PasswordField("Confirmez Mot de Passe",
                                   render_kw={"placeholder": "********"})
  submit = SubmitField("S'inscrire")

  def validate_username(self, username):
    Validator.required(username)
    Validator.length(username, 6, 40)
    user = User.query.filter_by(username=username.data).first()
    if user:
      raise ValidationError(f"{username.data} : Ce nom d'utilisateur est déja pris, veuillez en choisir un autre.")

  def validate_email(self, email):
    Validator.required(email)
    Validator.length(email, 5, 40)
    user = User.query.filter_by(email=email.data).first()
    if user:
      raise ValidationError(f"{email.data} : Cet email est déja pris, veuillez en choisir un autre.")

  def validate_password(self, password):
    Validator.required(password)
    Validator.length(password, 8, 40)
    Validator.password_hard(password)

  def validate_confirm_password(self, confirm_password):
    Validator.required(confirm_password)
    Validator.length(confirm_password, 8, 40)
    if not self.password.data == confirm_password.data:
      raise ValidationError(f"Les mots de passe ne sont pas identiques.")


class _LoginForm(FlaskForm):

  email = StringField("Email",
                      render_kw={"placeholder": "email@email.com"},
                      validators=[Email()])
  password = PasswordField("Mot de Passe",
                           render_kw={"placeholder": "********"})
  remember = BooleanField('Se souvenir de moi')
  submit = SubmitField("Connexion")

  def validate_email(self, email):
    Validator.required(email)
    Validator.length(email, 5, 40)

  def validate_password(self, password):
    Validator.required(password)
    Validator.length(password, 8, 40)
    Validator.password_hard(password)


class _UpdateAccountForm(FlaskForm):
  """form to update user infos"""

  username = StringField('Utilisateur',
                         render_kw={"placeholder": "MonIdentifiant"})
  email = StringField("Email",
                      render_kw={"placeholder": "email@email.com"},
                      validators=[DataRequired(),
                                  Length(min=5, max=40), Email()])
  password = PasswordField("Mot de Passe",
                           render_kw={"placeholder": "********"},
                           validators=[DataRequired(),
                                       Length(min=8, max=40)])
  confirm_password = PasswordField("Confirmez Mot de Passe",
                                   render_kw={"placeholder": "********"},
                                   validators=[DataRequired(),
                                               Length(min=8, max=40),
                                               EqualTo('password')])
  submit = SubmitField("Modifier")

  def validate_username(self, username):
    Validator.required(username)
    Validator.length(username, 6, 40)
    user = User.query.filter_by(username=username.data).first()
    if user:
      raise ValidationError(f"{username.data} : Ce nom d'utilisateur est déja pris, veuillez en choisir un autre.")

  def validate_email(self, email):
    Validator.required(email)
    Validator.length(email, 5, 40)
    user = User.query.filter_by(email=email.data).first()
    if user:
      raise ValidationError(f"{email.data} : Cet email est déja pris, veuillez en choisir un autre.")

  def validate_password(self, password):
    Validator.required(password)
    Validator.length(password, 8, 40)
    Validator.password_hard(password)

  def validate_confirm_password(self, confirm_password):
    Validator.required(confirm_password)
    Validator.length(confirm_password, 8, 40)
    if not confirm_password.data == self.password.data:
      raise ValidationError(f"Les mots de passe ne sont pas identiques.")


class _UpdateExpectationForm(FlaskForm):
  """form to update expectation level of user"""

  employed = SelectField('En poste actuellement',
                         description=HelpMessages.unique_select,
                         choices=UsersEnums.choices('trooleen'))
  sub_employed = SelectField('Situation',
                             description=HelpMessages.unique_select,
                             choices=UsersEnums.choices('sub_employed'))
  search = SelectField('Recherche',
                       description=HelpMessages.unique_select,
                       choices=UsersEnums.choices('search'))
  order = SelectField('Attentes',
                      description=HelpMessages.unique_select,
                      choices=UsersEnums.choices('order'))
  automation = SelectField('Candidatures',
                           description=HelpMessages.unique_select,
                           choices=UsersEnums.choices('automation'))
  submit = SubmitField("Modifier")


class _UpdateResumeForm(FlaskForm):

  resume_doc = FileField("Document (pdf uniquement)",
                         validators=[FileRequired(), FileAllowed(['pdf'])])
  resume_name = StringField("Nom du CV",
                            render_kw={"placeholder": "Mon-CV-2019"})
  submit = SubmitField("Modifier")

  def validate_resume_name(self, resume_name):
    Validator.required(resume_name)
    Validator.length(resume_name, 3, 40)


class _UpdateIdentificationForm(FlaskForm):
  """fzeioz"""

  firstname = StringField('Prénom',
                          render_kw={"placeholder": "Prénom"})
  lastname = StringField('Nom',
                         render_kw={"placeholder": "Nom"})
  sex = SelectField('Sexe',
                    description=HelpMessages.unique_select,
                    choices=UsersEnums.choices('sex'))
  birthdate = StringField('Date de naissance',
                          render_kw={"placeholder": "JJ/MM/AAAA"})
  nationality = StringField('Nationalité',
                            render_kw={"placeholder": "par pays : 'France' pour 'Francais'"})
  birth_country = StringField('Pays de naissance',
                              render_kw={"placeholder": "France"})
  birth_zip_code = StringField('Code postal de naissance',
                               render_kw={"placeholder": "38000"})
  birth_town = StringField('Ville de naissance',
                           render_kw={"placeholder": "Grenoble"})
  submit = SubmitField("Modifier")

  def validate_firstname(self, firstname):
    Validator.required(firstname)
    Validator.length(firstname, 2, 40)

  def validate_lastname(self, lastname):
    Validator.required(lastname)
    Validator.length(lastname, 2, 40)

  def validate_birthdate(self, birthdate):
    Validator.required(birthdate)
    Validator.length(birthdate, 8, 12)
    Validator.date(birthdate)

  def validate_nationality(self, nationality):
    Validator.required(nationality)
    if nationality.data not in Country.list_all():
      raise ValidationError('Ce pays est inconnu')

  def validate_birth_country(self, birth_country):
    Validator.required(birth_country)
    if birth_country.data not in Country.list_all():
      raise ValidationError('Ce pays est inconnu')

  def validate_birth_zip_code(self, birth_zip_code):
    Validator.required(birth_zip_code)
    Validator.length(birth_zip_code, 5, 5)
    Validator.numerical(birth_zip_code)

  def validate_birth_town(self, birth_town):
    Validator.required(birth_town)
    Validator.length(birth_town, 2, 50)


class _UpdateLocalisationForm(FlaskForm):

  town = StringField('Ville',
                     render_kw={"placeholder": "Bordeaux"})
  zip_code = StringField('Code postal',
                         render_kw={"placeholder": "33000"})
  country = StringField('Pays',
                        render_kw={"placeholder": "France"})
  driver_licence = SelectField('Permis de conduire (Auto/Moto)',
                               description=HelpMessages.unique_select,
                               choices=UsersEnums.choices('trooleen'))
  vehicule = SelectField('Véhicule',
                         description=HelpMessages.unique_select,
                         choices=UsersEnums.choices('trooleen'))
  submit = SubmitField("Modifier")

  def validate_town(self, town):
    Validator.required(town)
    Validator.length(town, 2, 50)

  def validate_zip_code(self, zip_code):
    Validator.required(zip_code)
    Validator.length(zip_code, 5, 5)
    Validator.numerical(zip_code)

  def validate_country(self, country):
    Validator.required(country)
    if country.data not in Country.list_all():
      raise ValidationError('Ce pays est inconnu')


class _UpdateDiplomaForm(FlaskForm):

  diploma_name = StringField('Diplôme',
                             render_kw={"placeholder": "Architecte Monuments Historiques"})
  diploma_school = StringField('Ecole, université, institut',
                               render_kw={"placeholder": "Ecole Superieure d'Architecture de Versailles"})
  diploma_town = StringField('Ville',
                             render_kw={"placeholder": "Versailles"})
  diploma_level = SelectField('Niveau',
                              description=HelpMessages.unique_select,
                              choices=UsersEnums.choices('diploma_level'))
  diploma_type = SelectField('Type',
                             description=HelpMessages.unique_select,
                             choices=UsersEnums.choices('diploma_type'))
  diploma_year = StringField('Année d\'obtention',
                             validators=[DataRequired(), Length(min=4, max=4)])
  submit = SubmitField("Modifier")

  def validate_diploma_name(self, diploma_name):
    Validator.required(diploma_name)
    Validator.length(diploma_name, 2, 50)

  def validate_diploma_school(self, diploma_school):
    Validator.required(diploma_school)
    Validator.length(diploma_school, 2, 50)

  def _validate_diploma_town(diploma_town):
    Validator.required(diploma_town)
    Validator.length(diploma_town, 2, 50)

  def validate_diploma_year(self, diploma_year):
    Validator.required(diploma_year)
    Validator.length(diploma_year, 4, 4)
    Validator.numerical(diploma_year)
    if not (2020 >= int(str(diploma_year.data).strip()) >= 1969):
      raise ValidationError('Humm... Vous êtes trop jeune ou trop agé pour travailler, non?')


class _UpdateWorkExperienceForm(FlaskForm):

  company = StringField('Entreprise',
                        render_kw={"placeholder": "TonSanto"})
  xp_at_company = StringField('Ancienneté dans l\'entreprise',
                              render_kw={"placeholder": "12"})
  company_size = SelectField('Taille (nombre de salariés)',
                             description=HelpMessages.unique_select,
                             choices=UsersEnums.choices('company_size'))
  sector = SelectField('Secteur',
                       description=HelpMessages.unique_select,
                       choices=UsersEnums.choices('sector'))
  job = StringField('Poste',
                    render_kw={"placeholder": "Responsable du lobying"})
  xp_at_job = StringField('Ancienneté à ce poste',
                          render_kw={"placeholder": "6"},
                          validators=[DataRequired(), Length(min=1, max=2)])
  function = SelectField('Fonction',
                         description=HelpMessages.unique_select,
                         choices=UsersEnums.choices('function'))
  position = SelectField('Position hiérachique',
                         description=HelpMessages.unique_select,
                         choices=UsersEnums.choices('position'))
  mob = SelectField('Mobilité',
                    description=HelpMessages.unique_select,
                    choices=UsersEnums.choices('mob'))
  key_words = TextAreaField('Mots clés ou compétences (minimum : 3)',
                            render_kw={"placeholder": str(
                                "mots clés séparés par une "
                                "virgule \nex : ' déontologie, santé publique"
                                ", respect de l'environnement '")},
                            validators=[DataRequired(), Length(min=5)])
  submit = SubmitField("Modifier")

  def validate_company(self, company):
    Validator.required(company)
    Validator.length(company, 2, 50)

  def validate_xp_at_company(self, xp_at_company):
    Validator.required(xp_at_company)
    Validator.length(xp_at_company, 1, 2)
    Validator.xp(xp_at_company)

  def validate_job(self, job):
    Validator.required(job)
    Validator.length(job, 3, 50)

  def validate_xp_at_job(self, xp_at_job):
    Validator.required(xp_at_job)
    Validator.length(xp_at_job, 1, 2)
    Validator.xp(xp_at_job)

  def validate_key_words(self, key_words):
    Validator.required(key_words)
    Validator.length(key_words, 6, 300)
    _key_words = key_words.data.split(",")
    if not len(_key_words) >= 3:
      raise ValidationError('3 or more words')


class _UpdateWorkStatusForm(FlaskForm):
  contract = SelectField('Contrat',
                         description=HelpMessages.unique_select,
                         choices=UsersEnums.choices("contract"))
  employer = SelectField('Type d\'emloyeur',
                         description=HelpMessages.unique_select,
                         choices=UsersEnums.choices("employer"))
  status = SelectField('Statut',
                       description=HelpMessages.unique_select,
                       choices=UsersEnums.choices('status'))
  rem = SelectField('Remuneration (annuelle brute fixe)',
                    description=HelpMessages.unique_select,
                    choices=UsersEnums.choices("small_rem"))
  currency = SelectField('Monnaie', description=HelpMessages.unique_select,
                         choices=UsersEnums.choices("currency"))
  management = SelectField('Management',
                           description=HelpMessages.unique_select,
                           choices=UsersEnums.choices('management'))
  xp_at_work = StringField('Experience professionnelle totale',
                           render_kw={"placeholder": "12"})
  submit = SubmitField("Modifier")

  def validate_xp_at_work(self, xp_at_work):
    Validator.required(xp_at_work)
    Validator.length(xp_at_work, 1, 2)
    Validator.xp(xp_at_work)


class _UpdateLanguagesForm(FlaskForm):

  english = SelectField('Niveau d\'Anglais', choices=UsersEnums.choices('english'))
  others = StringField('Autres Langues',
                       render_kw={"placeholder":
                                  str("Espagnol : scolaire, "
                                      "Italien : natif, Espéranto : fluent")},
                       validators=[Length(max=50)])
  submit = SubmitField("Modifier")


class _RequestResetForm(FlaskForm):
  """ reset password request"""

  email = StringField("Email",
                      render_kw={"placeholder": "email@email.com"},
                      validators=[DataRequired(),
                                  Length(min=5, max=40),
                                  Email()])
  submit = SubmitField('Demander un nouveau mot de passe')

  def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user is None:
      raise ValidationError('There is no account with email, \
                                Please register first')


class _ResetPasswordForm(FlaskForm):
  """reset password execution """

  password = PasswordField("Mot de Passe",
                           validators=[DataRequired(), Length(min=6, max=40)])
  confirm_password = PasswordField("Confirmez Mot de Passe",
                                   render_kw={"placeholder": "********"},
                                   validators=[DataRequired(), Length(min=6, max=40),
                                               EqualTo('password')])
  submit = SubmitField("Reset password")


class _DeleteForm(FlaskForm):

  submit = SubmitField("Supprimer")


class UsersForms(FlaskForm):

  Register = _RegistrationForm
  Login = _LoginForm
  Update = _UpdateAccountForm
  Expectation = _UpdateExpectationForm
  Resume = _UpdateResumeForm
  Identification = _UpdateIdentificationForm
  Localisation = _UpdateLocalisationForm
  Diploma = _UpdateDiplomaForm
  WorkExperience = _UpdateWorkExperienceForm
  WorkStatus = _UpdateWorkStatusForm
  Languages = _UpdateLanguagesForm
  Request = _RequestResetForm
  Reset = _ResetPasswordForm
  Delete = _DeleteForm
