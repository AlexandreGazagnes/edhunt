import sqlite3

import pandas as pd
import numpy as np

from edhunt import db, bcrypt, info
from edhunt.main.model import (School, Country, Town, Company,
                               Job, ZipCode, Departement, Region)
from edhunt.main.model import Post, Contact, Features
from edhunt.main.text.blog import BlogText
from edhunt.users.model import User
from edhunt.searchs.model import Search
from edhunt.opportunities.model import Opportunity
from edhunt.opportunities.utils import Lorem
from edhunt.config import Alex
from edhunt.plateforms import Plateforms


class _Admin:

  def _reboot(db=db):

    db.drop_all()
    db.create_all()

  def _make_features(db=db, verbose=False):

    _features = [{"name": "FreeHunt",
                  "searchs_max": "3",
                  "candidatures_max": "30",
                  "plateforms_max": "3",
                  "candidature_auto": False,
                  "opportunity_score": False,
                  "decideur_identification": False,
                  "edhunt_email": False,
                  "create_plateform_account": False,
                  "handle_external_app": False,
                  "decideur_contact": False,
                  "decideur_contact_auto": False,
                  "coach": False, },

                 {"name": "SmartHunt",
                  "searchs_max": "10",
                  "candidatures_max": "90",
                  "plateforms_max": "12",
                  "candidature_auto": True,
                  "opportunity_score": True,
                  "decideur_identification": True,
                  "edhunt_email": False,
                  "create_plateform_account": False,
                  "handle_external_app": False,
                  "decideur_contact": False,
                  "decideur_contact_auto": False,
                  "coach": False, },

                 {"name": "BigHunt",
                  "searchs_max": "illimites",
                  "candidatures_max": "illimites",
                  "plateforms_max": "illimites",
                  "candidature_auto": True,
                  "opportunity_score": True,
                  "decideur_identification": True,
                  "edhunt_email": True,
                  "create_plateform_account": True,
                  "handle_external_app": True,
                  "decideur_contact": True,
                  "decideur_contact_auto": True,
                  "coach": False, },

                 {"name": "ProHunt",
                  "searchs_max": "illimites",
                  "candidatures_max": "illimites",
                  "plateforms_max": "illimites",
                  "candidature_auto": True,
                  "opportunity_score": True,
                  "decideur_identification": True,
                  "edhunt_email": True,
                  "create_plateform_account": True,
                  "handle_external_app": True,
                  "decideur_contact": True,
                  "decideur_contact_auto": True,
                  "coach": True, }]

    for _feat in _features:
      feat = Features(**_feat)
      db.session.add(feat)
      db.session.commit()

  def _make_enums_tables(db=db, verbose=False):

    from edhunt.main.utils import (SCHOOL_LIST, COUNTRY_LIST,
                                   TOWN_LIST, COMPANY_LIST, ZIP_LIST,
                                   REGION_LIST, DEPARTEMENT_LIST)
    # reboot Enum tables
    [db.session.add(Country(country=country)) for country in COUNTRY_LIST]
    [db.session.add(Town(town=town)) for town in TOWN_LIST]
    [db.session.add(School(school=school)) for school in SCHOOL_LIST]
    [db.session.add(Company(company=company)) for company in COMPANY_LIST]
    [db.session.add(Region(region=region)) for region in REGION_LIST]
    [db.session.add(ZipCode(zip_code=zip_code)) for zip_code in ZIP_LIST]
    [db.session.add(Departement(departement=departement)) for departement in
     DEPARTEMENT_LIST]

    db.session.commit()

    if verbose:
      info(School.query.first())
      info(Country.query.first())
      info(Town.query.first())
      info(Company.query.first())
      info(Job.query.first())
      info(ZipCode.query.first())
      info(Departement.query.first())
      info(Region.query.first())

  def _make_fake_users(db=db, verbose=False):

    password = bcrypt.generate_password_hash("edhuntcesttr0pbien!").decode('utf-8')
    u_li = list()
    u_li.append(User(
        username="TestAdmin", email="test@edhunt.fr", password=password))
    u_li.append(User(
        username="fake_antoine", email="fake_antoine@admin.fr", password=password))
    u_li.append(User(
        username="fake_edouard", email="fake_edouard@admin.fr", password=password))

    db.session.add_all(u_li)
    db.session.commit()

    if verbose:
      info(User.query.all())

  def _make_fake_searchs(db=db, verbose=False):

    s_li = list()
    for town, words in zip(["Paris", "Rouen", "Marseille"],
                           ["python, pandas", "html, CSS", "C++"]):
      s_li.append(Search(name=f"fake_python {town}", mob="Ville", town=town,
                         key_words=words, user_id=1))

    for town, words in zip(["Paris", "Rouen", "Marseille"],
                           ["Paie RH", "RH recrutement", "GPEC HR"]):
      s_li.append(Search(name=f"fake_RH {town}", mob="Ville", town=town,
                         key_words=words, user_id=2))

    for town, words in zip(["Paris", "Rouen", "Marseille"],
                           ["solidity", "EOS", "C++"]):
      s_li.append(Search(name=f"fake_bitcoin {town}", mob="Ville", town=town,
                         key_words=words, user_id=3))

    db.session.add_all(s_li)
    db.session.commit()

    if verbose:
      info(Search.query.all())

  def _make_fake_oppotunities(db=db, verbose=False):

    o_li = list()
    for i, j, k in zip(["A", "B", "C"], [0, 1, 2], ["apec", 'regionjob', 'monster']):
      o_li.append(Opportunity(company=i, job=f"fake_dev{j}", text=Lorem.three, loc="Paris",
                              plateform=k, url="wwww.i.fr", user_id=1, search_id=1))

    for i, j, k in zip(["D", "E", "F"], [3, 4, 5], ["apec", 'regionjob', 'monster']):
      o_li.append(Opportunity(company=i, job="fake_dev{j}", text=Lorem.three, loc="Paris",
                              plateform=k, url="wwww.i.fr", user_id=1, search_id=2))

    for i, j, k in zip(["G", "H", "I"], [6, 7, 8], ["apec", 'regionjob', 'monster']):
      o_li.append(Opportunity(company=i, job="fake_dev{j}", text=Lorem.three, loc="Paris",
                              plateform=k, url="wwww.i.fr", user_id=1, search_id=3))

    db.session.add_all(o_li)
    db.session.commit()

    if verbose:
      info(Opportunity.query.all())

  def _make_fake_posts(db=db, verbose=False):
    for post_text in BlogText.posts:
      post = Post()
      for k, v in post_text.items():
        setattr(post, k, v)
      db.session.add(post)
    db.session.commit()

    if verbose:
      info(Post.query.all())

  def _make_alex(db=db, verbose=False):

    password = bcrypt.generate_password_hash("Azerty1&!").decode('utf-8')
    alex = User(username="AlexEdhuntTest", email=Alex.EMAIL, password=password)
    db.session.add(alex)
    db.session.commit()

    alex = User.query.filter_by(email=Alex.EMAIL).first()
    if not alex:
      raise AttributeError("Alex n'a pas été créé")
    if verbose:
      info(alex)

   # CREATE PLATEFORMS
    _list = [i for i in Plateforms.list_all if (i != "apec")]
    for p in _list:
      Plate = getattr(Plateforms.tables, p)
      db.session.add(Plate(user_id=alex.id))
    db.session.commit()

    apec = Plateforms.tables.apec(user_id=alex.id,
                                  email=Alex.APEC_EMAIL,
                                  password=Alex.APEC_PASSWORD,
                                  account="Oui",
                                  connexion="Off",
                                  # connected="Off",
                                  autorisation="Oui",
                                  good_user="Oui",
                                  edhunt_integrity="Oui")
    db.session.add(apec)
    db.session.commit()

    apec = Plateforms.tables.apec.query.filter_by(user_id=alex.id).first()
    if not apec:
      raise AttributeError("Apec Alex n'a pas été créé")
    if verbose:
      info(apec)

    search = Search(name=f"python", mob="Ville", town="Paris",
                    key_words="python", user_id=alex.id)
    db.session.add(search)
    db.session.commit()

    search = Search.query.filter_by(user_id=alex.id).first()
    if not search:
      raise AttributeError("search Alex n'a pas été créé")
    if verbose:
      info(search)

  def reset_db(db=db, verbose=False, force=False):

    if not force:
      ans = input("Are you sure to reset the db ????\n")
      ans = True if ans.lower().strip() == "y" else False
    else:
      ans = True
    if ans:
      _Admin._reboot(db)
      _Admin._make_features(db, verbose)
      _Admin._make_enums_tables(db, verbose)
      _Admin._make_fake_users(db, verbose)
      _Admin._make_fake_searchs(db, verbose)
      _Admin._make_fake_oppotunities(db, verbose)
      _Admin._make_fake_posts(db, verbose)
      _Admin._make_alex(db, verbose)
      print("Done")
    else:
      print("Aborted")

    return None


class _Handler:

  def extract_table(table, index=True, db='edhunt/site.db'):
    conn = sqlite3.connect(db)
    # c = conn.cursor()
    querry = f"SELECT * from {table}"
    df = pd.read_sql(querry, conn)
    if index:
      df = df.set_index("id", drop=True)
    return df

  def list_all_tables(db='edhunt/site.db'):
    conn = sqlite3.connect(db)
    # c = conn.cursor()
    querry = "SELECT name FROM sqlite_master WHERE type='table';"
    df = pd.read_sql(querry, conn)
    return df


class Db:
  admin = _Admin
  handler = _Handler
