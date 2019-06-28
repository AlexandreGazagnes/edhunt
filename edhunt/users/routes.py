from flask import render_template, url_for, flash, redirect, request, Markup
from flask_login import (LoginManager, current_user, UserMixin, login_user,
                         logout_user, login_required)
from edhunt import db, bcrypt
from edhunt.users.utils import save_resume, create_image
from edhunt.plateforms import Plateforms

from edhunt.users import Users

from edhunt.config import Params
from edhunt.main.model import (Town, Country, ZipCode, School, Job, Company)
from edhunt.utils.routes import (extract_fields, handle_authentication,
                                 flash_all_errors, commit_flash_redirect, load_user)

# from edhunt.main.text import MainText
from edhunt.main.model import Questionnaire, Contact, Post
# from edhunt.main.forms import MainForms

# from edhunt.searchs.model import Search
# from edhunt.opportunities.model import Opportunity


from flask import Blueprint
users = Blueprint('users', __name__)


@users.route("/register_user", methods=['GET', 'POST'])
def register_user():

    if Params.FORCE_QUESTIONNAIRE:
        return redirect(url_for('main.questionnaire_1'))

    if Params.DISABLE_REGISTER:
        try:
            logout_user()
        except:
            pass
        return redirect(url_for('main.connection', token="error"))

    handle_authentication(True)
    form = Users.forms.Register()
    fields = extract_fields(form)
    if form.validate_on_submit():
        # create user
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Users.table(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        # CREATE PLATEFORMS
        for p in Plateforms.list_all:
            Plate = getattr(Plateforms.tables, p)
            db.session.add(Plate(user_id=user.id))
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))

    return render_template('user/register_user.html',
                           title='Inscription',
                           fields=fields,
                           form=form)


@users.route("/_register_user/<token>", methods=['GET', 'POST'])
def _register_user(token):

    if Params.FORCE_QUESTIONNAIRE:
        q = Questionnaire.query.filter_by(token=token).first()
        if not q:
            flash("Hummmm, petite futée, tu t'es crue la plus maline?")
            return redirect(url_for('main.questionnaire_1'))

    if Params.DISABLE_REGISTER:
        try:
            logout_user()
        except:
            pass
        return redirect(url_for('main.connection', token=token))

    handle_authentication(True)
    form = Users.forms.Register()
    fields = extract_fields(form)
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Users.table(username=form.username.data, email=form.email.data, password=hashed_password)
        previous_fields = ["search", "employed", "contract", "diploma_type", "xp_at_work", "status",
                           "diploma_year", "search", "sector", "zip_code",
                           "function", "position", "management", "rem",
                           "diploma_level"]

        for field in previous_fields:
            setattr(user, field, getattr(q, field))
        db.session.add(user)
        db.session.commit()

        # CREATE PLATEFORMS
        for p in Plateforms.list_all:
            Plate = getattr(Plateforms.tables, p)
            db.session.add(Plate(user_id=user.id))
        db.session.commit()

        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))

    return render_template('user/register_user.html',
                           title='Inscription',
                           fields=fields,
                           form=form)


@users.route("/login", methods=['GET', 'POST'])
def login():

    handle_authentication(True)
    form = Users.forms.Login()
    fields = extract_fields(form)

    if Params.DISABLE_LOGIN:
        try:
            logout_user()
        except:
            pass
        return redirect(url_for('main.connection', token="error"))

    if form.validate_on_submit():
        user = Users.table.query.filter_by(email=form.email.data).first()
        if not user:
            flash('Login Unsuccessful. Please check email', 'danger')
            return redirect(url_for('users.login'))

        good_passwd = bcrypt.check_password_hash(user.password, form.password.data)

        if not good_passwd:
            flash('Login Unsuccessful. Please check password', 'danger')
            return redirect(url_for('users.login'))
        if user and good_passwd:
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash('You have been logged in!', 'success')

            return redirect(next_page) if next_page else redirect(url_for('users.manage_user'))
        else:
            raise AttributeError("something went wrong with login")

    return render_template('user/login_user.html',
                           title='Connexion',
                           form=form,
                           fields=fields,)


@users.route("/logout")
@login_required
def logout():

    handle_authentication(False)
    logout_user()
    flash("successfuly logged out", 'success')

    return redirect(url_for('main.home'))


@users.route("/update_user", methods=['GET', 'POST'])
@login_required
def update_user():

    handle_authentication(False)

    form = Users.forms.Update()
    fields = extract_fields(form)
    if request.method == 'GET':
        # prefill the form
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.password.data = ""
        form.confirm_password.data = ""
    else:
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            current_user.username = form.username.data
            current_user.email = form.email.data
            current_user.password = hashed_password
            db.session.commit()
            flash('Your account has been modified! Please re-log in', 'success')
            logout_user()
            return redirect(url_for('users.login'))
        else:
            flash_all_errors(form)

    return render_template('user/update/update_user.html',
                           title='Compte',
                           fields=fields,
                           form=form)


@users.route("/delete_user", methods=['GET', 'POST'])
@login_required
def delete_user():

    handle_authentication(False)

    form = Users.forms.Delete()
    fields = extract_fields(form)
    if form.validate_on_submit():
        user_id = current_user.id
        logout_user()
        user = Users.table.query.filter_by(id=user_id).first()
        db.session.delete(user)
        db.session.commit()
        flash("User deleted", "success")
        return redirect(url_for('main.home'))

    return render_template('user/delete_user.html',
                           title="Suppression du compte",
                           fields=fields,
                           text=Users.text.delete_user,
                           form=form)


# @users.route("/manage_user", methods=['GET'])
# @login_required
# def manage_user():

#     handle_authentication(False)

#     resume_list = [(f"{n}",
#                     getattr(current_user, f"resume{n}_name"),
#                     getattr(current_user, f"resume{n}_doc"))
#                    for n in range(1, 4)]

#     return render_template('user/manage_user.html',
#                            title='Profil',
#                            text=Users.text.manage_user(),
#                            resume_list=resume_list)


@users.route("/manage_user/", defaults={"opt": None})
@users.route("/manage_user/<string:opt>", methods=['GET'])
@login_required
def manage_user(opt):

    handle_authentication(False)

    resume_list = [(f"{n}",
                    getattr(current_user, f"resume{n}_name"),
                    getattr(current_user, f"resume{n}_doc"))
                   for n in range(1, 4)]

    nav = {"opt": opt}

    return render_template('user/manage_user2.html',
                           title='Profil',
                           text=Users.text.manage_user(),
                           resume_list=resume_list,
                           nav=nav)


# @users.route("/manage_plateforms", methods=['GET'])
# @login_required
# def manage_plateforms():

#     handle_authentication(False)

#     plateform_list = Plateforms.list_all
#     plateform_list = [(plateform,
#                        getattr(Plateforms.tables, plateform).query.filter_by(user_id=current_user.id).first(),
#                        url_for('users.update_plateform', plateform=plateform))
#                       for plateform in plateform_list]

#     plateform_list = [(i, (j.connexion if j else "Off"), k) for i, j, k in plateform_list]

#     return render_template('user/manage_plateforms.html',
#                            title='Plateformes',
#                            text=Users.text.manage_plateforms(),
#                            plateform_list=plateform_list)


@users.route("/update_expectation", methods=['GET', 'POST'])
@login_required
def update_expectation():

    # handle authetication problems
    handle_authentication(False)

    form = Users.forms.Expectation()
    fields = extract_fields(form)
    if request.method == 'GET':
        # prefill the form
        form.employed.data = current_user.employed
        form.search.data = current_user.search
        form.order.data = current_user.order
        form.automation.data = current_user.automation
    else:
        if form.validate_on_submit():
            # update user info
            current_user.employed = form.employed.data
            current_user.sub_employed = form.sub_employed.data

            current_user.search = form.search.data
            current_user.order = form.order.data
            current_user.automation = form.automation.data
            return commit_flash_redirect('users.manage_user')
        else:
            flash_all_errors(form)

    return render_template('user/update/update_expectation.html',
                           title="Attentes",
                           fields=fields,
                           form=form)


@users.route("/update_resume/<n>", methods=['GET', 'POST'])
@login_required
def update_resume(n):

    # handle authetication problems
    handle_authentication(False)

    form = Users.forms.Resume()
    fields = extract_fields(form)
    if request.method == 'GET':
        # prefill the form
        pass
    else:
        if form.validate_on_submit():
            # update user info
            _resume_doc = save_resume(form.resume_doc.data)
            setattr(current_user, f"resume{n}_doc", _resume_doc)
            if form.resume_name.data:
                setattr(current_user, f"resume{n}_name", form.resume_name.data)
            else:
                setattr(current_user, f"resume{n}_name", f"my_resume_{n}")
            return commit_flash_redirect('users.manage_user')
        else:
            if form.errors:
                flash_all_errors(form)

    return render_template('user/update/update_resume.html',
                           title="CVs",
                           fields=fields,
                           form=form)


@users.route("/view_resume/<filename>_<n>", methods=['GET'])
@login_required
def view_resume(filename, n):

    # handle authetication problems
    handle_authentication(False)
    img = create_image(filename)
    img = url_for('static', filename="resumes/" + img)

    return render_template('user/view_resume.html',
                           title="CV",
                           filename=filename,
                           img=img,
                           n=n)


@users.route("/update_identification", methods=['GET', 'POST'])
@login_required
def update_identification():

    # handle authetication problems
    handle_authentication(False)
    form = Users.forms.Identification()
    fields = extract_fields(form)
    if request.method == 'GET':
        # pre fill all fields
        for field in fields:
            k = getattr(form, field)
            k.data = getattr(current_user, field)
    else:
        if form.validate_on_submit():
            if form.firstname.data:
                form.firstname.data = form.firstname.data.title()
            if form.lastname.data:
                form.lastname.data = form.lastname.data.capitalize()
            # if needed add the town to Town table
            if form.birth_town.data not in Town.list_all():
                form.birth_town.data = form.birth_town.data.capitalize()\
                    .strip().replace("  ", " ").replace("  ", " ")
                db.session.add(Town(town=form.birth_town.data))
            # upadte user attrs
            for field in fields:
                setattr(current_user, field, getattr(form, field).data)
            return commit_flash_redirect('users.manage_user')
        else:
            flash_all_errors(form)

    return render_template('user/update/update_identification.html',
                           title="Identification",
                           form=form, fields=fields,
                           country_list=Country.list_all(),
                           town_list=Town.list_all(),
                           zip_code_list=ZipCode.list_all())


@users.route("/update_localisation", methods=['GET', 'POST'])
@login_required
def update_localisation():

    # handle authetication problems
    handle_authentication(False)

    form = Users.forms.Localisation()
    fields = extract_fields(form)
    if request.method == 'GET':
        # pre fill all fields
        for field in fields:
            k = getattr(form, field)
            k.data = getattr(current_user, field)
    else:
        if form.validate_on_submit():
            # if needed add the town to Town table
            if form.town.data not in Town.list_all():
                form.town.data = form.town.data.capitalize()\
                    .strip().replace("  ", " ").replace("  ", " ")
                db.session.add(Town(town=form.town.data))
            # update User attrs
            for field in fields:
                setattr(current_user, field, getattr(form, field).data)
            return commit_flash_redirect('users.manage_user')
        else:
            flash_all_errors(form)

    return render_template('user/update/update_localisation.html',
                           title="Localisation",
                           form=form,
                           fields=fields,
                           country_list=Country.list_all(),
                           town_list=Town.list_all())


@users.route("/update_diploma", methods=['GET', 'POST'])
@login_required
def update_diploma():

    # handle authetication problems
    handle_authentication(False)

    form = Users.forms.Diploma()
    fields = extract_fields(form)
    if request.method == 'GET':
        # pre fill all fields
        for field in fields:
            k = getattr(form, field)
            k.data = getattr(current_user, field)
    else:
        if form.validate_on_submit():
            # handle town and school if needed
            if form.diploma_town.data not in Town.list_all():
                form.diploma_town.data = form.diploma_town.data.capitalize()\
                    .strip().replace("  ", " ").replace("  ", " ")
                db.session.add(Town(town=form.diploma_town.data))
            if form.diploma_school.data not in School.list_all():
                form.diploma_school.data = form.diploma_school.data.capitalize()\
                    .strip().replace("  ", " ").replace("  ", " ")
                db.session.add(School(school=form.diploma_school.data))
            # update User attrs
            for field in fields:
                setattr(current_user, field, getattr(form, field).data)
            return commit_flash_redirect('users.manage_user')
        else:
            flash_all_errors(form)

    return render_template('user/update/update_diploma.html',
                           title="Diplôma",
                           form=form,
                           fields=fields,
                           town_list=Town.list_all(),
                           school_list=School.list_all())


@users.route("/update_work_experience", methods=['GET', 'POST'])
@login_required
def update_work_experience():

    # handle authetication problems
    handle_authentication(False)

    form = Users.forms.WorkExperience()
    fields = extract_fields(form)

    if request.method == 'GET':
        # pre fill all fields
        for field in fields:
            k = getattr(form, field)
            k.data = getattr(current_user, field)
    else:
        if form.validate_on_submit():
            # if needed add the comapny and job to relative tables
            if form.company.data not in Company.list_all():
                form.company.data = form.company.data.upper().strip()\
                    .replace("-", " ").replace("  ", " ").replace("  ", " ")
                db.session.add(Company(company=form.company.data))
                db.session.commit()
            if form.job.data not in Job.list_all():
                form.job.data = form.job.data.capitalize().strip()\
                    .replace("-", " ").replace("  ", " ").replace("  ", " ")
                db.session.add(Job(job=form.job.data))
                db.session.commit()
            if form.key_words.data:
                kwords = form.key_words.data
                kwords = kwords.lower().strip()\
                    .replace("-", " ").replace("  ", " ").replace("  ", " ")
                kwords = ", ".join([i.strip() for i in kwords.split(",")])
                form.key_words.data = kwords
            # update User attrs
            for field in fields:
                setattr(current_user, field, getattr(form, field).data)
                db.session.commit()
            return commit_flash_redirect('users.manage_user')
        else:
            flash_all_errors(form)

    return render_template('user/update/update_work_experience.html',
                           title="Experience professionnelle",
                           form=form,
                           fields=fields,
                           company_list=Company.list_all(),
                           job_list=Job.list_all())


@users.route("/update_work_status", methods=['GET', 'POST'])
@login_required
def update_work_status():

    # handle authetication problems
    handle_authentication(False)

    form = Users.forms.WorkStatus()
    fields = extract_fields(form)
    if request.method == 'GET':
        # prefill all fields
        for field in fields:
            k = getattr(form, field)
            k.data = getattr(current_user, field)
    else:
        if form.validate_on_submit():
            # update user attrs
            for field in fields:
                setattr(current_user, field, getattr(form, field).data)
            return commit_flash_redirect('users.manage_user')
        else:
            flash_all_errors(form)

    return render_template('user/update/update_work_status.html',
                           fields=fields,
                           title="Statut",
                           form=form)


@users.route("/update_language", methods=['GET', 'POST'])
@login_required
def update_language():

    # handle authetication problems
    handle_authentication(False)

    form = Users.forms.Languages()
    fields = extract_fields(form)
    if request.method == 'GET':
        # prefill all fields
        for field in fields:
            k = getattr(form, field)
            k.data = getattr(current_user, field)
    else:
        if form.validate_on_submit():
            # update user attrs
            for field in fields:
                setattr(current_user, field, getattr(form, field).data)
            return commit_flash_redirect('users.manage_user')
        else:
            flash_all_errors(form)

    return render_template('user/update/update_language.html',
                           title="Langues",
                           form=form,
                           fields=fields)


# @users.route("/update_<string:plateform>", methods=['GET', 'POST'])
# @login_required
# def update_plateform(plateform):
#     """Account page"""

#     # handle authetication problems
#     handle_authentication(False)

#     form = Users.forms.Plateform()
#     fields = extract_fields(form)
#     plateform = getattr(Plateforms.tables, plateform).query.filter_by(user_id=current_user.id).first()
#     if request.method == 'GET':
#         if plateform:
#             for field in fields:
#                 getattr(form, field).data = getattr(plateform, field)

#     else:
#         if form.validate_on_submit():
#             for field in fields:
#                 setattr(plateform, field, getattr(form, field).data)
#             if form.connection.data != "On":
#                 flash(f"Sorry  did not allow to login to {plateform}",
#                       "danger")
#                 return redirect(url_for("users.manage_user"))
#             for i in ["autorisation", "good_user", "edhunt_integrity"]:
#                 if getattr(form, i).data != "Oui":
#                     flash(f"Sorry you must accept credentials to login to {plateform}",
#                           "danger")
#                     return redirect(url_for("users.manage_user"))
#             return commit_flash_redirect('users.manage_user')
#         else:
#             flash_all_errors(form)

#     return render_template('user/update/update_plateform.html',
#                            title="Plateforme",
#                            form=form, fields=fields,
#                            plateform=plateform)
