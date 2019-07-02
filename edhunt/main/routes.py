from secrets import token_hex
from flask import render_template, url_for, flash, redirect, request
from flask_login import (current_user, login_required)

from edhunt import db
from edhunt.utils.routes import (handle_authentication,
                                 flash_all_errors, extract_fields, load_user)

from edhunt.utils.gzip import gzipped
from edhunt.main.text import MainText
from edhunt.main.model import Questionnaire, Contact, Post
from edhunt.main.forms import MainForms

from edhunt.users.model import User
from edhunt.searchs.model import Search
from edhunt.opportunities.model import Opportunity
from edhunt.plateforms import Plateforms

from flask import Blueprint
main = Blueprint('main', __name__)


@main.route("/edhunt/")
@main.route("/edhunt")
@login_required
def edhunt():

  # handle connections problems
  handle_authentication(False)

  # for funct, plat in [(current_user.filed_info, "profile filling"),
  #                     (current_user.filed_joboard, "plateform connection")]:
  #     if int(funct()) > 80:
  #         _flash = "success"
  #     elif int(funct()) < 40:
  #         _flash = "danger"
  #     else:
  #         _flash = "warning"
  #     flash(f"Your {plat} is scored to {funct()}%", _flash)

  search_list = Search.query.filter_by(user_id=current_user.id).all()

  opp_list = Opportunity.query.filter_by(user_id=current_user.id).all()

  plate_list = list()
  for p in Plateforms.list_all:
    plate_list.append(getattr(Plateforms.tables, p).query.filter_by(user_id=current_user.id).first())

  plate_list = [i for i in plate_list if i]
  [setattr(opp, "search_name", Search.query.filter_by(id=opp.search_id).first().name)
   for opp in opp_list]
  db.session.commit()

  return render_template('main/edhunt2.html',
                         title="edhunt",
                         search_list=search_list,
                         opp_list=opp_list,
                         plate_list=plate_list)


@main.route("/", defaults={"token": None}, methods=["GET", "POST"])
@main.route("/home/<string:token>", methods=["GET", "POST"])
@gzipped
def home(token):
  """main page with latest posts"""
  if current_user.is_authenticated:
    return redirect(url_for("main.edhunt"))

  form = MainForms.Form_0()
  fields = extract_fields(form)

  if request.method == 'GET':
    pass
  else:
    if form.validate_on_submit():
      if not token:
        token = token_hex(16)
        quest = Questionnaire(token=token)
        db.session.add(quest)
        db.session.commit()
      else:
        quest = Questionnaire.query.filter_by(token=token).first()
        if not quest:
          flash("Désolé, une erreur c'est produite", "danger")
          return redirect(url_for("main.home"))

      for field in fields:
        setattr(quest, field, getattr(form, field).data)
      db.session.commit()

      return redirect(url_for("main.questionnaire_1", token=token))
    else:
      flash_all_errors(form)

  return render_template('main/home2.html',
                         form=form,
                         text=MainText.home)


@main.route("/apropos/", methods=["GET"])
@main.route("/apropos", methods=["GET"])
@gzipped
def apropos():
  return render_template('main/apropos.html',
                         title="A propos",
                         text=MainText.apropos)


@main.route("/loffre2/", methods=["GET"])
@main.route("/loffre2", methods=["GET"])
@gzipped
def loffre2():
  return render_template('main/loffre.html',
                         title="L'offre",
                         text=MainText.offre)


@main.route("/loffre/", methods=["GET"])
@main.route("/loffre", methods=["GET"])
@gzipped
def loffre():
  return render_template('main/loffre2.html',
                         title="L'offre",
                         text=MainText.offre2)


@main.route("/blog/", methods=["GET"])
@main.route("/blog", methods=["GET"])
@gzipped
def blog():
  posts = Post.query.all()
  return render_template('main/blog.html',
                         title="Blog",
                         text=MainText.blog,
                         posts=posts)


@main.route("/post/<string:post_id>", methods=["GET"])
@gzipped
def post(post_id):
  post = Post.query.filter_by(id=post_id).first()
  if not post:
    flash("Error with post", "danger")
    return redirect(url_for('main.home'))

  # nav
  post_id_next = post_id_past = None
  posts = Post.query.all()
  idx = posts.index(post)
  if idx > 0 and (len(posts) > 1):
    post_id_past = posts[idx - 1].id
  if (not (idx + 1 == len(posts))):
    post_id_next = posts[idx + 1].id
  nav = {"post_id_next": post_id_next,
         "post_id_past": post_id_past}

  # flash(post, "info")
  # for k, v in nav.items():
  #     flash(f"{k} : {v}", "info")

  return render_template('main/post.html',
                         title="Post",
                         post=post,
                         nav=nav,
                         text=MainText.post)


# @main.route("/manifeste/", methods=["GET"])
# @main.route("/manifeste", methods=["GET"])
# @gzipped
# def manifeste():
#     return render_template('main/faq2.html',
#                            title="Manifeste",
#                            text=MainText.faq,
#                            text2=MainText.apropos)


@main.route("/faq/", methods=["GET"])
@main.route("/faq", methods=["GET"])
@gzipped
def faq():
  return render_template('main/faq.html',
                         title="FAQ",
                         text=MainText.faq,
                         text2=MainText.apropos)


@main.route("/manifeste/", methods=["GET"])
@main.route("/manifeste", methods=["GET"])
@gzipped
def manifeste():
  return render_template('main/faq.html',
                         title="FAQ",
                         text=MainText.faq,
                         text2=MainText.apropos)


@main.route("/contact/", methods=["GET", "POST"])
@main.route("/contact", methods=["GET", "POST"])
@gzipped
def contact():
  form = MainForms.Contact()
  fields = extract_fields(form)

  if request.method == 'GET':
    pass
  else:
    if form.validate_on_submit():
      contact = Contact()
      for field in fields:
        setattr(contact, field, getattr(form, field).data)
      db.session.add(contact)
      db.session.commit()

      flash("Message envoyé !", "success")
      return redirect(url_for("main.home"))
    else:
      flash_all_errors(form)

  return render_template('main/contact.html',
                         title="Contact",
                         form=form,
                         text=MainText.contact)


@main.route("/questionnaire_0/<string:token>", methods=["GET", "POST"])
@gzipped
def questionnaire_0(token):

  return redirect(url_for("main.home", token=token))


@main.route("/questionnaire_1/", defaults={"token": None}, methods=["GET", "POST"])
@main.route("/questionnaire_1/<string:token>", methods=["GET", "POST"])
@gzipped
def questionnaire_1(token):

  quest = Questionnaire.query.filter_by(token=token).first()
  if not quest:
    flash("Désolé, une erreur c'est produite", "danger")
    return redirect(url_for("main.home"))

  form = MainForms.Form_1()
  fields = extract_fields(form)

  if request.method == 'GET':
    pass
  else:
    if form.validate_on_submit():
      for field in fields:
        setattr(quest, field, getattr(form, field).data)
      db.session.commit()

      return redirect(url_for("main.questionnaire_2", token=token))
    else:
      flash_all_errors(form)

  return render_template('main/questionnaire_1.html',
                         title="Inscription 1/3",
                         form=form, token=token,
                         text=MainText.questionnaire.q1,
                         back="0")


@main.route("/questionnaire_2/<string:token>", methods=["GET", "POST"])
@gzipped
def questionnaire_2(token):

  quest = Questionnaire.query.filter_by(token=token).first()
  if not quest:
    flash("Désolé, une erreur c'est produite", "danger")
    return redirect(url_for("main.home"))

  form = MainForms.Form_2()
  fields = extract_fields(form)

  if request.method == 'GET':
    pass
  else:
    if form.validate_on_submit():
      for field in fields:
        setattr(quest, field, getattr(form, field).data)
      db.session.commit()

      return redirect(url_for("main.questionnaire_3", token=token))
    else:
      flash_all_errors(form)

  return render_template('main/questionnaire_2.html',
                         title="Inscription 2/3",
                         form=form, token=token,
                         text=MainText.questionnaire.q2,
                         back="1")


@main.route("/questionnaire_3/<string:token>", methods=["GET", "POST"])
@gzipped
def questionnaire_3(token):

  quest = Questionnaire.query.filter_by(token=token).first()
  if not quest:
    flash("Désolé, une erreur c'est produite", "danger")
    return redirect(url_for("main.home"))

  form = MainForms.Form_3()
  fields = extract_fields(form)

  if request.method == 'GET':
    pass
  else:
    if form.validate_on_submit():
      for field in fields:
        setattr(quest, field, getattr(form, field).data)
      db.session.commit()

      return redirect(url_for('main.questionnaire_4', token=token))
    else:
      flash_all_errors(form)

  return render_template('main/questionnaire_3.html',
                         title="Inscription 3/3",
                         form=form, token=token,
                         text=MainText.questionnaire.q3,
                         back="2")


@main.route("/questionnaire_4/<string:token>", methods=["GET", "POST"])
@gzipped
def questionnaire_4(token):

  quest = Questionnaire.query.filter_by(token=token).first()
  if not quest:
    flash("Désolé, une erreur c'est produite", "danger")
    return redirect(url_for("main.home"))

  form = MainForms.Form_4()
  fields = extract_fields(form)

  if request.method == 'GET':
    pass
  else:

    if form.validate_on_submit():
      for field in fields:
        setattr(quest, field, getattr(form, field).data)
      db.session.commit()

      return redirect(url_for("main.questionnaire_5", token=token))
    else:
      flash_all_errors(form)

  return render_template('main/questionnaire_4.html',
                         title="Bienvenue chez edhunt!",
                         form=form, token=token,
                         text=MainText.questionnaire.q4,
                         back="3")


@main.route("/questionnaire_5/<string:token>", methods=["GET", "POST"])
@gzipped
def questionnaire_5(token):

  quest = Questionnaire.query.filter_by(token=token).first()
  if not quest:
    flash("Désolé, une erreur c'est produite", "danger")
    return redirect(url_for("main.home"))
  form = MainForms.Form_5()
  fields = extract_fields(form)

  if request.method == 'GET':
    pass
  else:

    if form.validate_on_submit():
      for field in fields:
        setattr(quest, field, getattr(form, field).data)
      db.session.commit()

      # flash("Super Merci!", "success")
      return redirect(url_for("main.questionnaire_6", token=token))
    else:
      flash_all_errors(form)

  return render_template('main/questionnaire_5.html',
                         title="Inscription 5/6",
                         form=form, token=token,
                         text=MainText.questionnaire.q5,
                         back="4")


@main.route("/questionnaire_6/<string:token>", methods=["GET", "POST"])
@gzipped
def questionnaire_6(token):

  quest = Questionnaire.query.filter_by(token=token).first()
  if not quest:
    flash("Désolé, une erreur c'est produite", "danger")
    return redirect(url_for("main.home"))

  if token != "error":
    form = MainForms.Form_6()
    fields = extract_fields(form)
  else:
    form = None

  if request.method == 'GET':
    pass
  else:
    if form.validate_on_submit():
      # u = User.query.filter_by(email=form.email.data).all()
      # if u:
      #   flash("Vous avez déja un compte!", "success")
      #   return redirect(url_for("main.login_user"))
      # else:
      #   flash("Contact créé!", "success")
      #   quest.email = form.email.data
      #   quest.phone = form.phone.data
      #   quest.hour = form.hour.data
      #   db.session.commit()
      # return redirect(url_for('main.home'))
      # flash("success", "success")
      for field in fields:
        setattr(quest, field, getattr(form, field).data)
      db.session.commit()
      return redirect(url_for('main.bienvenue', token=token))

  return render_template('main/questionnaire_6.html',
                         title="Inscription 6/6",
                         text=MainText.questionnaire.q6,
                         form=form, token=token,
                         back="5")


@main.route("/bienvenue/", defaults={"token": None})
@main.route("/bienvenue/<string:token>", methods=["GET"])
def bienvenue(token):

  if not token:
    return redirect(url_for("main.home"))
  quest = Questionnaire.query.filter_by(token=token).first()
  if not quest:
    return redirect(url_for("main.home"))

  return render_template('main/bienvenue.html',
                         title="Bienvenue")


@main.route("/corporate_log", methods=["GET", "POST"])
def corporate_log():

  form = MainForms.Corporate()

  if request.method == 'GET':
    pass

  else:
    if form.validate_on_submit():
      flash("Super Merci!", "success")

      return render_template('main/corporate_data2.html',
                             title="Corporate",
                             text=MainText.home,
                             corpo=MainText.corporate)
    else:
      flash_all_errors(form)

  return render_template('main/corporate_log.html',
                         title="Corporate",
                         text=MainText.corporate,
                         form=form)


@main.errorhandler(404)
def error_404(error):
  return render_template('main/404.html')


@main.errorhandler(403)
def error_403(error):
  return render_template('main/403.html')


@main.errorhandler(500)
def error_500(error):
  return render_template('main/500.html')


@main.route("/test")
def test():
  return render_template('main/test.html',
                         title="Test")
