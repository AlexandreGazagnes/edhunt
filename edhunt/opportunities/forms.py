from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import (StringField, PasswordField, SubmitField, BooleanField,
                     TextAreaField, SelectField, SelectMultipleField)
from wtforms.validators import (DataRequired, Length, Email, EqualTo,
                                ValidationError)

from edhunt.utils.forms import HelpMessages, Validator, _handle_tous_indiff


class _DeleteForm(FlaskForm):

    submit = SubmitField("Suppr.")


class OpportunitiesForms():

    Delete = _DeleteForm
