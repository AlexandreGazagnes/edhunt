from flask import render_template, url_for, flash, redirect, request
from flask_login import (current_user, login_required)

from edhunt import db, warning
from edhunt.utils.routes import (handle_authentication,
                                 flash_all_errors, extract_fields, load_user)

from edhunt.searchs.model import Search
from edhunt.searchs.forms import SearchsForms

from edhunt.opportunities.model import Opportunity
from edhunt.main.model import (Town, Country, Job, Company, Region, Departement)

from edhunt.plateforms import Plateforms
from flask import Blueprint
searchs = Blueprint('searchs', __name__)


@searchs.route("/create_search", methods=["GET", "POST"])
@login_required
def create_search():

    # handle connections problems
    handle_authentication(False)
    # form and fields
    form = SearchsForms.Create()
    # fields = extract_fields(form)
    if request.method == 'GET':
        pass
    else:
        if form.validate_on_submit():
            # if needed add the town to Town table
            for i in (1, 2, 3, 4, 5):
                town = getattr(form, f"town_{i}").data
                if town not in Town.list_all():
                    town = town.capitalize()\
                        .strip().replace("  ", " ").replace("  ", " ")
                    db.session.add(Town(town=town))

            search = Search(user_id=current_user.id)
            # upadte user attrs
            search.name = form.name.data
            search.mob = form.mob.data
            for feat in ["country", "departement", "region", "town"]:
                _data = [getattr(form, f"{feat}_{i}").data for i in [1, 2, 3, 4, 5]]
                setattr(search, feat, ", ".join([i for i in _data if i]))
            form.key_words.data = form.key_words.data.strip().upper()\
                .replace("-", " ").replace("  ", " ").replace("  ", " ")
            if form.key_words.data:
                kwords = form.key_words.data
                kwords = kwords.lower().strip()\
                    .replace("-", " ").replace("  ", " ").replace("  ", " ")
                kwords = ", ".join([i.strip() for i in kwords.split(",")])
                form.key_words.data = kwords
            search.key_words = form.key_words.data
            db.session.add(search)
            db.session.commit()
            flash("search updated", "success")
            return redirect(url_for("searchs.manage_search", search_id=search.id))
        else:
            flash_all_errors(form)

    form.submit.label.text = "Create"
    return render_template('search/create_search.html',
                           title="Create Search",
                           mode="Create",
                           form=form,
                           country_list=Country.list_all(),
                           town_list=Town.list_all(),
                           departement_list=Departement.list_all(),
                           region_list=Region.list_all())


@searchs.route("/update_search/<search_id>", methods=["GET", "POST"])
@login_required
def update_search(search_id):

    # handle connections problems
    handle_authentication(False)
    # form and fields
    form = SearchsForms.Update()
    search = Search.query.filter_by(id=search_id).first()
    # authetication problem
    if current_user.id != search.user_id:
        flash("sorry this is not your search, you are not allowed", "danger")
        return redirect(url_for("main.edhunt"))

    if request.method == 'GET':
        # prefill the form
        form.name.data = search.name
        form.mob.data = search.mob
        for feat in ['country', 'town', 'departement', 'region']:
            if getattr(search, feat) is None:
                setattr(search, feat, "")
            _data = [i.strip() for i in getattr(search, feat).split(",")]
            _data = _data + (["", ] * (5 - len(_data)))
            [setattr(getattr(form, f"{feat}_{i+1}"), "data", j)
             for i, j in enumerate(_data)]
        form.key_words.data = search.key_words
    else:
        if form.validate_on_submit():
            # if needed add the town to Town table
            for i in (1, 2, 3, 4, 5):
                town = getattr(form, f"town_{i}").data
                if town not in Town.list_all():
                    town = town.capitalize()\
                        .strip().replace("  ", " ").replace("  ", " ")
                    db.session.add(Town(town=town))
            # upadte user attrs
            search.name = form.name.data
            search.mob = form.mob.data
            for feat in ["country", "departement", "region", "town"]:
                _data = [getattr(form, f"{feat}_{i}").data for i in [1, 2, 3, 4, 5]]
                setattr(search, feat, ", ".join([i for i in _data if i]))
            form.key_words.data = form.key_words.data.strip().upper()\
                .replace("-", " ").replace("  ", " ").replace("  ", " ")
            if form.key_words.data:
                kwords = form.key_words.data
                kwords = kwords.lower().strip()\
                    .replace("-", " ").replace("  ", " ").replace("  ", " ")
                kwords = ", ".join([i.strip() for i in kwords.split(",")])
                form.key_words.data = kwords
            search.key_words = form.key_words.data
            db.session.commit()
            flash("search updated", "success")
            return redirect(url_for("searchs.manage_search", search_id=search.id))
        else:
            flash_all_errors(form)

    form.submit.label.text = "Update"
    return render_template('search/update/update_search.html',
                           title="Update Search",
                           mode="Update",
                           form=form,
                           country_list=Country.list_all(),
                           town_list=Town.list_all(),
                           region_list=Region.list_all(),
                           departement_list=Departement.list_all(),
                           search_id=search.id)


@searchs.route("/maj_searchs", methods=["GET"])
@login_required
def maj_searchs():

    raise NotImplementedError("Not Implemented Error")


@searchs.route("/maj_search/<search_id>", methods=["GET"])
@login_required
def maj_search(search_id):

    # handle connections problems
    handle_authentication(False)
    # form and fields
    form = SearchsForms.Update()
    search = Search.query.filter_by(id=search_id).first()

    # authetication problem
    if current_user.id != search.user_id:
        flash("sorry this is not your search, you are not allowed", "danger")
        return redirect(url_for("main.edhunt"))

    avialable_plateforms = current_user.avialable_plateforms()

    key_words = search.key_words
    loc = search.town

    if "apec" in avialable_plateforms:
        plat = getattr(Plateforms.tables, "apec")\
            .query.filter_by(user_id=current_user.id).first()
        warning(plat)
        opportunities_list, msg, color = Plateforms.WebDriver.search_light(plat, key_words, loc)
    else:
        raise ValueError("Apec not connected")

    try:
        opportunities_list
    except Exception as e:
        raise e

    existing_opps = Opportunity.query.filter_by(search_id=search.id).all()
    old_len_existing_opps = len(existing_opps)
    existing_opps = [i.url for i in existing_opps]

    if not opportunities_list:
        flash("error with opportunities_list or opportunities_list url", "info")

    for opp_dict in opportunities_list:
        opp = Opportunity(user_id=current_user.id, search_id=search.id, **opp_dict)
        if opp.url not in existing_opps:
            db.session.add(opp)
            db.session.commit()

    existing_opps = Opportunity.query.filter_by(search_id=search.id).all()
    new_len_existing_opps = len(existing_opps)
    new_opps = new_len_existing_opps - old_len_existing_opps
    flash(f"{new_opps} new opps added", "info")

    return redirect(url_for("searchs.visualize_search", search_id=search.id))


@searchs.route("/delete_search/<search_id>", methods=["GET", "POST"])
@login_required
def delete_search(search_id):

    # handle connections problems
    handle_authentication(False)
    search = Search.query.filter_by(id=search_id).first()

    # authetication problem
    if current_user.id != search.user_id:
        flash("sorry this is not your search, you are not allowed", "danger")
        return redirect(url_for("main.edhunt"))

    form = SearchsForms.Delete()

    if form.validate_on_submit():
        db.session.delete(search)
        db.session.commit()
        flash("Search deleted", "success")
        return redirect(url_for('main.edhunt'))

    return render_template('search/delete_search.html',
                           title="Supprimer une search",
                           form=form,
                           search_id=search.id)


# @searchs.route("/manage_search/<search_id>", methods=["GET"])
# @login_required
# def manage_search(search_id):

#     # handle connections problems
#     handle_authentication(False)
#     search = Search.query.filter_by(id=search_id).first()
#     # authetication problem
#     if current_user.id != search.user_id:
#         flash("sorry this is not your search, you are not allowed", "danger")
#         return redirect(url_for("main.edhunt"))

#     return render_template('search/manage_search.html',
#                            title="Search",
# search=search)

@searchs.route("/manage_search/<search_id>", methods=["GET"])
@login_required
def manage_search(search_id):

    # handle connections problems
    handle_authentication(False)
    search = Search.query.filter_by(id=search_id).first()
    # authetication problem
    if current_user.id != search.user_id:
        flash("sorry this is not your search, you are not allowed", "danger")
        return redirect(url_for("main.edhunt"))

    return render_template('search/manage_search2.html',
                           title="Search",
                           search=search)


@searchs.route("/update_searched_status/<search_id>", methods=["GET", "POST"])
@login_required
def update_searched_status(search_id):

    # handle connections problems
    handle_authentication(False)
    search = Search.query.filter_by(id=search_id).first()
    # authetication problem
    if current_user.id != search.user_id:
        flash("sorry this is not your search, you are not allowed", "danger")
        return redirect(url_for("main.edhunt"))

    form = SearchsForms.Status()
    fields = extract_fields(form)
    if request.method == 'GET':
        # prefill all fields
        for field in fields:
            k = getattr(form, field)
            k.data = getattr(search, field)
    else:
        if form.validate_on_submit():
            # update user attrs
            for field in fields:
                d = getattr(form, field).data
                if isinstance(d, list):
                    d = ", ".join(d)
                setattr(search, field, d)
            db.session.commit()
            flash("Search updated", "success")
            return redirect(url_for('searchs.manage_search', search_id=search.id))
        else:
            flash_all_errors(form)
    return render_template('search/update/update_searched_status.html',
                           title="Update Statuts",
                           form=form,
                           search_id=search.id)


@searchs.route("/update_searched_job/<search_id>", methods=["GET", "POST"])
@login_required
def update_searched_job(search_id):

    # handle connections problems
    handle_authentication(False)
    search = Search.query.filter_by(id=search_id).first()
    # authetication problem
    if current_user.id != search.user_id:
        flash("sorry this is not your search, you are not allowed", "danger")
        return redirect(url_for("main.edhunt"))

    form = SearchsForms.Job()
    fields = extract_fields(form)
    if request.method == 'GET':
        # prefill all fields
        for field in fields:
            k = getattr(form, field)
            k.data = getattr(search, field)
    else:
        if form.validate_on_submit():
            # handle company (upper....)
            form.company.data = form.company.data.strip().upper()\
                .replace("-", " ").replace("  ", " ").replace("  ", " ")
            form.not_company.data = form.not_company.data.strip().upper()\
                .replace("-", " ").replace("  ", " ").replace("  ", " ")
            # if needed update Comany Table
            company_list = form.company.data.split(",")
            not_company_list = form.not_company.data.split(",")
            for comp_list in [company_list, not_company_list]:
                for _company in comp_list:
                    _company = _company.strip().upper().replace("-", " ")\
                        .replace("  ", " ").replace("  ", " ")
                    if _company not in Company.list_all():
                        db.session.add(Company(company=_company))
            if form.company.data:
                comps = form.company.data
                comps = comps.upper().strip()\
                    .replace("-", " ").replace("  ", " ").replace("  ", " ")
                comps = ", ".join([i.strip() for i in comps.split(",")])
                form.company.data = comps
            if form.not_company.data:
                comps = form.not_company.data
                comps = comps.upper().strip()\
                    .replace("-", " ").replace("  ", " ").replace("  ", " ")
                comps = ", ".join([i.strip() for i in comps.split(",")])
                form.not_company.data = comps
            if form.not_key_words.data:
                kwords = form.not_key_words.data
                kwords = kwords.lower().strip()\
                    .replace("-", " ").replace("  ", " ").replace("  ", " ")
                kwords = ", ".join([i.strip() for i in kwords.split(",")])
                form.not_key_words.data = kwords
            # update user attrs
            for field in fields:
                d = getattr(form, field).data
                if isinstance(d, list):
                    d = ", ".join(d)
                setattr(search, field, d)
            db.session.commit()
            flash("Search updated", "success")
            return redirect(url_for('searchs.manage_search', search_id=search.id))
        else:
            flash_all_errors(form)
    return render_template('search/update/update_searched_job.html',
                           title="Update Job",
                           form=form,
                           company_list=Company.list_all(),
                           search_id=search.id)


@searchs.route("/update_searched_language/<search_id>", methods=["GET", "POST"])
@login_required
def update_searched_language(search_id):

    # handle connections problems
    handle_authentication(False)
    search = Search.query.filter_by(id=search_id).first()

    # authetication problem
    if current_user.id != search.user_id:
        flash("sorry this is not your search, you are not allowed", "danger")
        return redirect(url_for("main.edhunt"))

    form = SearchsForms.Languages()
    fields = extract_fields(form)

    if request.method == 'GET':
        # prefill all fields
        form.other_languages.data = search.other_languages
    else:
        if form.validate_on_submit():
            # update user attrs
            if form.other_languages.data:
                langs = form.other_languages.data
                langs = langs.capitalize().strip()\
                    .replace("-", " ").replace("  ", " ").replace("  ", " ")
                langs = ", ".join([i.strip() for i in langs.split(",")])
                form.other_languages.data = langs
            for field in fields:
                d = getattr(form, field).data
                if isinstance(d, list):
                    d = ", ".join(d)
                setattr(search, field, d)
            db.session.commit()
            flash("Search updated", "success")
            return redirect(url_for('searchs.manage_search', search_id=search.id))
        else:
            flash_all_errors(form)
    return render_template('search/update/update_searched_language.html',
                           title="Update Languages",
                           form=form,
                           search_id=search.id)


# @searchs.route("/visualize_search/<search_id>", methods=["GET"])
# @login_required
# def visualize_search(search_id):
#     # handle connections problems
#     handle_authentication(False)
#     search = Search.query.filter_by(id=search_id).first()
#     opp_list = Opportunity.query.filter_by(search_id=int(search_id)).all()

#     # authetication problem
#     if (current_user.id != search.user_id):
#         flash("sorry this is not your opp, you are not allowed", "danger")
#         return redirect(url_for("main.edhunt"))

#     search_id_next = search_id_past = None
#     search_s = Search.query.filter_by(user_id=current_user.id).all()
#     # nav
#     idx = search_s.index(search)
#     if idx > 0 and (len(search_s) > 1):
#         search_id_past = search_s[idx - 1].id
#     if (not (idx + 1 == len(search_s))):
#         search_id_next = search_s[idx + 1].id
#     nav = {"search_id_next": search_id_next,
#            "search_id_past": search_id_past}

#     return render_template('search/visualize_search.html',
#                            title="Opportunity",
#                            opp_list=opp_list,
#                            user=current_user,
#                            search=search,
#                            nav=nav)


@searchs.route("/visualize_search/<search_id>", methods=["GET"])
@login_required
def visualize_search(search_id):
    # handle connections problems
    handle_authentication(False)
    search = Search.query.filter_by(id=search_id).first()
    opp_list = Opportunity.query.filter_by(search_id=int(search_id)).all()

    # authetication problem
    if (current_user.id != search.user_id):
        flash("sorry this is not your opp, you are not allowed", "danger")
        return redirect(url_for("main.edhunt"))

    search_id_next = search_id_past = None
    search_s = Search.query.filter_by(user_id=current_user.id).all()
    # nav
    idx = search_s.index(search)
    if idx > 0 and (len(search_s) > 1):
        search_id_past = search_s[idx - 1].id
    if (not (idx + 1 == len(search_s))):
        search_id_next = search_s[idx + 1].id
    nav = {"search_id_next": search_id_next,
           "search_id_past": search_id_past}

    return render_template('search/visualize_search2.html',
                           title="Opportunity",
                           opp_list=opp_list,
                           user=current_user,
                           search=search,
                           nav=nav)


# @searchs.route("/visualize_searchs/", methods=["GET"])
# @login_required
# def visualize_searchs():
#     # handle connections problems
#     handle_authentication(False)
#     search_list = Search.query.filter_by(user_id=current_user.id).all()
#     # opp_list = Opportunity.query.filter_by(search_id=int(search_id)).all()

#     # search_id_next = search_id_past = None
#     # search_s = Search.query.filter_by(user_id=current_user.id).all()
#     # # nav
#     # idx = search_s.index(search)
#     # if idx > 0 and (len(search_s) > 1):
#     #     search_id_past = search_s[idx - 1].id
#     # if (not (idx + 1 == len(search_s))):
#     #     search_id_next = search_s[idx + 1].id
#     # nav = {"search_id_next": search_id_next,
#     #        "search_id_past": search_id_past}

#     return render_template('search/visualize_searchs.html',
#                            title="Recherches",
#                            search_list=search_list)


@searchs.route("/visualize_searchs/<string:src>", methods=['GET'])
@searchs.route("/visualize_searchs/", defaults={"src": None})
@login_required
def visualize_searchs(src):
    # handle connections problems
    handle_authentication(False)
    search_list = Search.query.filter_by(user_id=current_user.id).all()
    # opp_list = Opportunity.query.filter_by(search_id=int(search_id)).all()

    # search_id_next = search_id_past = None
    # search_s = Search.query.filter_by(user_id=current_user.id).all()
    # # nav
    # idx = search_s.index(search)
    # if idx > 0 and (len(search_s) > 1):
    #     search_id_past = search_s[idx - 1].id
    # if (not (idx + 1 == len(search_s))):
    #     search_id_next = search_s[idx + 1].id
    # nav = {"search_id_next": search_id_next,
    #        "search_id_past": search_id_past}

    nav = {'src': src}

    return render_template('search/visualize_searchs.html',
                           title="Recherches",
                           search_list=search_list,
                           nav=nav)
