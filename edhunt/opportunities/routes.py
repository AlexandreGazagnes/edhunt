from flask import render_template, url_for, flash, redirect, request
from flask_login import (current_user, login_required)

from edhunt import db
from edhunt.utils.routes import (handle_authentication,
                                 flash_all_errors, extract_fields, load_user)

from edhunt.opportunities.model import Opportunity
from edhunt.opportunities.forms import OpportunitiesForms

from edhunt.searchs.model import Search
from edhunt.users.model import User

from edhunt.main.model import (Town, Country, Job, Company, Region, Departement)

from flask import Blueprint
opportunities = Blueprint('opportunities', __name__)


@opportunities.route("/visualize_opportunity/<opp_id>", methods=["GET"])
@login_required
def visualize_opportunity(opp_id):
    # handle connections problems
    handle_authentication(False)
    opp = Opportunity.query.filter_by(id=opp_id).first()
    # authetication problem
    if current_user.id != opp.user_id:
        flash("sorry this is not your opp, you are not allowed", "danger")
        return redirect(url_for("main.edhunt"))
    opp_id_next = opp_id_past = None
    opps = Opportunity.query.filter_by(search_id=opp.search_id).all()
    # nav
    idx = opps.index(opp)
    if idx > 0 and (len(opps) > 1):
        opp_id_past = opps[idx - 1].id
    if (not (idx + 1 == len(opps))):
        opp_id_next = opps[idx + 1].id
    nav = {"opp_id_next": opp_id_next,
           "opp_id_past": opp_id_past,
           "search_id": opp.search_id}

    return render_template('opportunity/visualize_opportunity.html',
                           title="Opportunity",
                           opp=opp, nav=nav)


@opportunities.route("/visualize_opportunities", methods=["GET"])
@login_required
def visualize_opportunities():
    # handle connections problems
    handle_authentication(False)
    opp_list = Opportunity.query.filter_by(user_id=int(current_user.id)).all()

    # # authetication problem
    # if current_user.id != int(user_id):
    #   flash("sorry this is not your opp, you are not allowed", "danger")
    #   return redirect(url_for("main.edhunt"))

    return render_template('opportunity/visualize_opportunities.html',
                           title="Opportunities",
                           opp_list=opp_list,
                           user=current_user)


@opportunities.route("/delete_opportunity/<opp_id>", methods=["GET", "POST"])
@login_required
def delete_opportunity(opp_id):

    # handle connections problems
    handle_authentication(False)
    opp = Opportunity.query.filter_by(id=opp_id).first()

    # authetication problem
    if current_user.id != opp.user_id:
        flash("sorry this is not your opp, you are not allowed", "danger")
        return redirect(url_for("main.edhunt"))

    form = OpportunitiesForms.Delete()

    if form.validate_on_submit():
        db.session.delete(opp)
        db.session.commit()
        flash("Opportunité supprimée", "success")
        return redirect(url_for('main.edhunt'))

    return render_template('opportunity/delete_opportunity.html',
                           title="Delete search",
                           form=form,
                           opp_id=opp.id)
