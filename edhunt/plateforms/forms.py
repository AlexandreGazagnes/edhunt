from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import (StringField, PasswordField, SubmitField, BooleanField,
                     TextAreaField, SelectField)
from wtforms.validators import (DataRequired, Length, Email, EqualTo,
                                ValidationError)

from edhunt.utils.forms import Validator, HelpMessages
from edhunt.plateforms.utils import PlateformsEnums


class _UpdatePlateformForm(FlaskForm):
    """change plateform for user"""

    # connexion = SelectField('Connexion',
    #                         description=HelpMessages.unique_select,
    #                         choices=PlateformsEnums.choices('connexion'))

    account = SelectField('Compte déja existant sur cette plateforme',
                          description=HelpMessages.unique_select,
                          choices=PlateformsEnums.choices('trooleen'))

    sub_account = SelectField('si Non, en créer un?',
                              description=HelpMessages.unique_select,
                              choices=PlateformsEnums.choices('trooleen'))
    email = StringField("Email",
                        render_kw={"placeholder": "email@email.com"},
                        validators=[Email()])
    password = PasswordField("Mot de Passe",
                             render_kw={"placeholder": "********"})
    _autorisation = "J'accepte que edhunt se connecte à la plateforme."
    _resume = "J'accepte que edhunt mette en ligne mon/mes CV(s) sur cette plateforme."
    _candidature = "J'accepte que edhunt puisse candidater directement en mon nom sur cette plateforme."
    _good_user = "Je suis bien la personne associée à ce compte, atteste ne pas usurper d'identié en me connectant avec ces identifiants, je dispose de l'ensemble des droits de ce compte."
    _edhunt_integrity = "J'interdit à edhunt d'exploiter, de vendre ou d'utiliser mes données personnelles à/auprès de tiers. J'exige que mes données servent expressement et uniquement à la gestion de mes candidatures et/ou ma recherche d'emploi."

    autorisation = SelectField(_autorisation,
                               description=HelpMessages.unique_select,
                               choices=PlateformsEnums.choices('trooleen'))
    resume = SelectField(_resume,
                         description=HelpMessages.unique_select,
                         choices=PlateformsEnums.choices('trooleen'))
    candidature = SelectField(_candidature,
                              description=HelpMessages.unique_select,
                              choices=PlateformsEnums.choices('trooleen'))

    good_user = SelectField(_good_user,
                            description=HelpMessages.unique_select,
                            choices=PlateformsEnums.choices('trooleen'))
    edhunt_integrity = SelectField(_edhunt_integrity,
                                   description=HelpMessages.unique_select,
                                   choices=PlateformsEnums.choices('trooleen'))
    submit = SubmitField("Modifier")

    def validate_connexion(self, connexion):
        Validator.required(connexion)
        Validator.choice_not_null(connexion)

    def validate_account(self, account):
        Validator.required(account)
        Validator.choice_not_null(account)

    def validate_sub_account(self, sub_account):
        if self.account.data == "Non":
            Validator.required(sub_account)
            Validator.choice_not_null(sub_account)

    def validate_connected(self, connected):
        Validator.required(connected)
        Validator.choice_not_null(connected)

    def validate_email(self, email):
        Validator.required(email)
        Validator.length(email, 5, 40)

    def validate_password(self, password):
        Validator.required(password)
        Validator.length(password, 4, 40)

    def validate_autorisation(self, autorisation):
        Validator.required(autorisation)
        Validator.choice_not_null(autorisation)

    def validate_resume(self, resume):
        Validator.required(resume)
        Validator.choice_not_null(resume)

    def validate_candidature(self, candidature):
        Validator.required(candidature)
        Validator.choice_not_null(candidature)

    def validate_good_user(self, good_user):
        Validator.required(good_user)
        Validator.choice_not_null(good_user)

    def validate_edhunt_integrity(self, edhunt_integrity):
        Validator.required(edhunt_integrity)
        Validator.choice_not_null(edhunt_integrity)


class PlateformsForms:
    Update = _UpdatePlateformForm
