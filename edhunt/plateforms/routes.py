from flask import render_template, url_for, flash, redirect, request, Markup
from flask_login import (LoginManager, current_user, UserMixin, login_user,
                         logout_user, login_required)
from edhunt import db, bcrypt, warning
from edhunt.main.model import (Town, Country, ZipCode, School, Job, Company)
from edhunt.users import Users
from edhunt.plateforms import Plateforms
from edhunt.utils.routes import (extract_fields, handle_authentication,
                                 flash_all_errors, commit_flash_redirect, load_user)
from edhunt.users.utils import save_resume, create_image
from edhunt.config import Params
from edhunt.opportunities.model import Opportunity

from edhunt.plateforms.webdriver import WebDriver

from flask import Blueprint
plateforms = Blueprint('plateforms', __name__)


# @plateforms.route("/manage_plateforms", methods=['GET'])
# @login_required
# def manage_plateforms():

#     handle_authentication(False)

#     plateform_list = Plateforms.list_all
#     plateform_list = [(plateform,
#                        getattr(Plateforms.tables, plateform).query.filter_by(user_id=current_user.id).first(),
#                        url_for('plateforms.update_plateform', plateform=plateform),
#                        url_for(f'plateforms.test_plateform', plateform=plateform))
#                       for plateform in plateform_list]

#     plateform_list = [(i, (j.connexion if j else "Off"), k, l) for i, j, k, l in plateform_list]

#     return render_template('plateform/manage_plateforms.html',
#                            title='Plateformes',
#                            text=Plateforms.text.manage_plateforms(),
#                            plateform_list=plateform_list)


@plateforms.route("/manage_plateforms/", defaults={"opt": None})
@plateforms.route("/manage_plateforms/<string:opt>", methods=['GET'])
@login_required
def manage_plateforms(opt):

    handle_authentication(False)

    plateform_list = Plateforms.list_all
    plateform_list = [(plateform,
                       getattr(Plateforms.tables, plateform).query.filter_by(user_id=current_user.id).first(),
                       url_for('plateforms.update_plateform', plateform=plateform),
                       url_for(f'plateforms.test_plateform', plateform=plateform))
                      for plateform in plateform_list]

    # plateform_list = [(i, j, k, l) for i, j, k, l in plateform_list]

    nav = {"opt": opt}

    return render_template('plateform/manage_plateforms2.html',
                           title='Plateformes',
                           text=Plateforms.text.manage_plateforms(),
                           plateform_list=plateform_list,
                           nav=nav)


@plateforms.route("/update_<string:plateform>", methods=['GET', 'POST'])
@login_required
def update_plateform(plateform):

    plateform_name = plateform
    # handle authetication problems
    handle_authentication(False)

    form = Plateforms.forms.Update()
    fields = extract_fields(form)
    plateform = getattr(Plateforms.tables, plateform_name).query.filter_by(user_id=current_user.id).first()
    if request.method == 'GET':
        if plateform:
            for field in fields:
                getattr(form, field).data = getattr(plateform, field)
    else:
        if form.validate_on_submit():

            if not plateform:
                plateform = getattr(Plateforms.tables, plateform_name)(user_id=current_user.id)
                db.session.add(plateform)
                db.session.commit()
            if form.account.data == "Oui":
                form.sub_account.data = "Oui"
            plateform = getattr(Plateforms.tables, plateform_name).query.filter_by(user_id=current_user.id).first()
            for field in fields:
                setattr(plateform, field, getattr(form, field).data)
                db.session.commit()
            # if form.connection.data != "On":
            #     flash(f"Sorry  did not allow to login to {plateform}",
            #           "danger")
            #     return redirect(url_for("users.manage_user"))
            for i in ["autorisation", "good_user", "edhunt_integrity"]:
                if getattr(form, i).data != "Oui":
                    flash(f"Sorry you must accept credentials to login to {plateform_name}",
                          "danger")
                    return redirect(url_for("plateforms.manage_plateforms"))
            return commit_flash_redirect('plateforms.manage_plateforms')
        else:
            flash_all_errors(form)

    return render_template('plateform/update_plateform.html',
                           title=plateform_name,
                           form=form, fields=fields)


@plateforms.route("/test_<string:plateform>", methods=['GET'])
@login_required
def test_plateform(plateform):

    plateform_name = plateform
    # handle authetication problems
    handle_authentication(False)
    plateform = getattr(Plateforms.tables, plateform_name).query.filter_by(user_id=current_user.id).first()

    msg = ""
    if not plateform:
        msg = f"Sorry but you do not have set you plateform info {plateform_name}"
    if (not plateform.email) or (not plateform.password):
        msg = f"Sorry but you do not have set you plateform email/password for {plateform_name}"
    if msg:
        flash(msg, "danger")
        return redirect(
            url_for("plateforms.update_plateform", plateform=plateform_name))

    res, msg, color = WebDriver.test_connexion(plateform)
    flash(msg, color)
    if res:
        plateform.connexion = "On"
    else:
        plateform.connexion = "Off"
    db.session.commit()

    return redirect(url_for("plateforms.manage_plateforms"))


@plateforms.route("/search/<string:plateform>/<string:words>/<string:loc>/", methods=['GET'])
@login_required
def search_light(plateform, words, loc):

    plateform_name = plateform
    handle_authentication(False)
    plateform = getattr(Plateforms.tables, plateform_name).query.filter_by(user_id=current_user.id).first()

    msg = ""
    if not plateform:
        msg = f"Sorry but you do not have set you plateform info {plateform_name}"
    if (not plateform.email) or (not plateform.password):
        msg = f"Sorry but you do not have set you plateform email/password for {plateform_name}"
    if msg:
        flash(msg, "danger")
        return redirect(
            url_for("plateforms.update_plateform", plateform=plateform_name))

    res, msg, color = WebDriver.search_light(plateform_name, plateform, words, loc)

    # flash(msg, color)
    # if res:
    #     plateform.connexion = "On"
    #     db.session.commit()
    #     return redirect(url_for("plateforms.manage_plateforms"))
    # else:
    #     plateform.connexion = "Off"
    #     db.session.commit()
    #     redirect(url_for("plateforms.update_plateform", plateform=plateform_name))

    return redirect(url_for("plateforms.update_plateform", plateform=plateform_name))


@plateforms.route("/candidate/<string:opp_id>", methods=['GET'])
@login_required
def candidate(opp_id):

    handle_authentication(False)
    opp = Opportunity.query.filter_by(id=opp_id).first()
    if not opp:
        raise AttributeError("pb with opp")

    if current_user.id != opp.user_id:
        flash("sorry this is not your search, you are not allowed", "danger")
        return redirect(url_for("main.edhunt"))

    plateform = getattr(Plateforms.tables, opp.plateform).query.filter_by(user_id=current_user.id).first()

    msg = ""
    if not plateform:
        msg = f"Sorry but you do not have set you plateform info {plateform_name}"
    if (not plateform.email) or (not plateform.password):
        msg = f"Sorry but you do not have set you plateform email/password for {plateform_name}"
    if msg:
        flash(msg, "danger")
        return redirect(
            url_for("plateforms.update_plateform", plateform=plateform_name))

    res, msg, color = WebDriver.candidate(plateform, opp.url)

    flash(msg, "info")
    flash("donne", info)

    return redirect(url_for("main.edhunt"))
