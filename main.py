#!/usr/bin/env python3
# coding: utf-8

from edhunt import *


from edhunt.plateforms.webdriver.apec import Apec


# reset
DbAdmin.reset_db()


# handle user
u = Users.table.query.filter_by(email="a_syoez@yahoo.fr").first()
if not u:
    raise AttributeError("No u")
info(u)

# handle search
s = Search.query.filter_by(user_id=u.id).first()
if not s:
    raise AttributeError("No s")
info(s)

# handle apec
a = Plateforms.tables.apec.query.filter_by(user_id=u.id).first()
if not a:
    raise AttributeError("No a")
info(a)

# handle opportunity
o = Opportunity.query.filter_by(user_id=u.id).first()
if o:
    raise AttributeError("THERE IS AN o")
info(o)


# handle search
driver = Apec()
driver.login(a.email, a.password, a.status)
done, res, msg, col = driver.perform_search_light(s.key_words, s.town)

pages = 3
opportunities_list = list()
if done:
    for i in range(pages):
        res = driver.scrap_search_light()
        opportunities_list.extend(res)
        info(len(opportunities_list))
        driver.next_search_page()


for _opp in opportunities_list:
    opp = Opportunity(user_id=u.id, search_id=s.id, **_opp)
    db.session.add(opp)
    db.session.commit()


# handle opportunity
o = Opportunity.query.filter_by(user_id=u.id).all()
for i in o:
    print(i)
