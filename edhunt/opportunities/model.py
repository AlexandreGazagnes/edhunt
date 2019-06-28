from datetime import datetime
from edhunt import db, UserMixin


class Opportunity(db.Model, UserMixin):
    """table Search"""

    # positional cols
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), unique=False, nullable=False)
    job = db.Column(db.String(100), unique=False, nullable=False)
    plateform = db.Column(db.String(20), unique=False, nullable=False)
    url = db.Column(db.Text(1000), unique=False, nullable=False)
    loc = db.Column(db.String(20), unique=False, nullable=False,)
    applied = db.Column(db.Boolean(), unique=False, nullable=False,
                        default=False)  # IT IS THE ORDER
    send = db.Column(db.Boolean(), unique=False, nullable=False,
                     default=False)  # IF REALLY SENT
    text = db.Column(db.Text(1000), unique=False, nullable=False,
                     default=".")
    created = db.Column(db.String(20), unique=False, nullable=False,
                        default=datetime.utcnow)

    # optionals cols
    rem = db.Column(db.String(40), unique=False, nullable=True)
    status = db.Column(db.String(20), unique=False, nullable=True)
    contract = db.Column(db.String(20), unique=False, nullable=True)

    # score
    score = db.Column(db.String(2), unique=False, nullable=True)

    # relationship
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=False,
                        nullable=False)
    search_id = db.Column(db.Integer, db.ForeignKey('search.id'), unique=False,
                          nullable=False)

    def columns_list(self=None):
        if self:
            return [column.key for column in self.__table__.columns]
        else:
            return [column.key for column in Opportunity.__table__.columns]

    def __repr__(self):
        keys = ['id', 'company', 'job', 'plateform', "applied", "loc", "user_id", "search_id"]
        txt = "\n".join([str(key.ljust(20, " ") + ": " +
                             str(self.__dict__[key])) for key in keys])
        return "\n" + txt


# class Opportunity(db.Model, UserMixin):
#     """table Job"""

#     # positional cols

#     # optional cols : job desc
#     url_mirror = db.Column(db.String(100), unique=False, nullable=True)
#     company_mirror = db.Column(db.String(20), unique=False, nullable=True)
#     company_desc = db.Column(db.Text(300), unique=False, nullable=True)
#     job_desc = db.Column(db.Text(300), unique=False, nullable=True)
#     profile_desc = db.Column(db.Text(300), unique=False, nullable=True)
#     diploma_level = db.Column(db.String(20), unique=False, nullable=True)
#     diploma_type = db.Column(db.String(20), unique=False, nullable=True)
#     xp = db.Column(db.SmallInteger(), unique=False, nullable=True)

#     # optional cols : contacts
#     contact_1_name = db.Column(db.String(20), unique=False, nullable=True)
#     contact_1_position = db.Column(db.String(20), unique=False, nullable=True)
#     contact_1_email = db.Column(db.String(20), unique=False, nullable=True)
#     contact_1_phone = db.Column(db.String(20), unique=False, nullable=True)
#     contact_2_name = db.Column(db.String(20), unique=False, nullable=True)
#     contact_2_position = db.Column(db.String(20), unique=False, nullable=True)
#     contact_2_email = db.Column(db.String(20), unique=False, nullable=True)
#     contact_2_phone = db.Column(db.String(20), unique=False, nullable=True)

#     # optional cols : loc
#     town = db.Column(db.String(20), unique=False, nullable=True)
#     loc = db.Column(db.String(20), unique=False, nullable=True)
#     country = db.Column(db.String(20), unique=False, nullable=True)
#     mob = db.Column(db.String(20), unique=False, nullable=True)

#     # optional cols : level
#     management = db.Column(db.String(20), unique=False, nullable=True)

#     # optional cols : type
#     sector = db.Column(db.String(20), unique=False, nullable=True)
#     company_size = db.Column(db.String(20), unique=False, nullable=True)
#     position = db.Column(db.String(20), unique=False, nullable=True)
#     function = db.Column(db.String(20), unique=False, nullable=True)

#     # optional cols : others
#     keys_words = db.Column(db.Text(300), unique=False, nullable=True)
#     english = db.Column(db.String(20), unique=False, nullable=True)

#     def columns_list(self=None):
#         if self:
#             return [column.key for column in self.__table__.columns]
#         else:
#             return [column.key for column in Job.__table__.columns]
