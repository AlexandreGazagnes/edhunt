from flask import url_for, flash, redirect
from flask_login import current_user
from edhunt import db, login_manager
from edhunt.users.model import User
from edhunt.config import Params


def handle_authentication(expected):

    if (not expected) and (not current_user.is_authenticated):
        flash("something went wrong you have to be authetifiacted, please login first", "danger")
        return redirect(url_for('login'))

    elif expected and current_user.is_authenticated:
        flash("you are already authetified", "danger")
        return redirect(url_for('manage_account'))


def commit_flash_redirect(where='account'):
    db.session.commit()
    flash("info updated successfuly", "success")
    return redirect(url_for(where))


def flash_all_errors(form):

    if form.errors and Params.TEST_MODE:
        [flash(f"{k} : {' '.join(v)}", 'danger')
         for k, v in form.errors.items()]
    if form.errors and not Params.TEST_MODE:
        flash("Désolé, le formulaire n'est pas complet ou est invalide", "danger")


def extract_fields(form):

    drop_fields = ['meta', '_prefix', '_errors', '_fields', '_csrf',
                   'submit', 'csrf_token']
    fields = [i for i in form.__dict__.keys() if (i not in drop_fields)]

    return fields


@login_manager.user_loader
def load_user(user_id):
    """load an user when logged"""
    return User.query.get(int(user_id))
