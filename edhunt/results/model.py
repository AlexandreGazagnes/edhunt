from edhunt import db, UserMixin
from edhunt.searchs.utils import SearchEnums


class Result(db.Model, UserMixin):
    """table Search"""

    # positional cols
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.String(20), unique=False, nullable=False,
                        default=datetime.utcnow)
    # name = db.Column(db.String(50), unique=False, nullable=False)
    # mob = db.Column(db.Enum(*SearchEnums.mob), unique=False, nullable=False)
    # country = db.Column(db.String(200), unique=False, nullable=True)
    # region = db.Column(db.String(200), unique=False, nullable=True)
    # departement = db.Column(db.String(200), unique=False, nullable=True)
    # town = db.Column(db.String(200), unique=False, nullable=True)
    # key_words = db.Column(db.Text(300), unique=False, nullable=False,
    #                       default=".")

    # # work status
    # contract = db.Column(db.String(200), unique=False, nullable=True)
    # employer = db.Column(db.String(200), unique=False, nullable=True)
    # status = db.Column(db.String(200), unique=False, nullable=True)
    # rem = db.Column(db.String(200), unique=False, nullable=True)
    # currency = db.Column(db.Enum(*SearchEnums.currency), unique=False,
    #                      nullable=True)
    # management = db.Column(db.Enum(*SearchEnums.booleen), unique=False,
    #                        nullable=True)

    # # Job
    company = db.Column(db.String(200), unique=False, nullable=True)
    job = db.Column(db.String(200), unique=False, nullable=True)
    # not_company = db.Column(db.String(200), unique=False, nullable=True)
    # company_size = db.Column(db.String(200), unique=False, nullable=True)
    # sector = db.Column(db.String(200), unique=False, nullable=True)
    # function = db.Column(db.Enum(*SearchEnums.function), unique=False,
    #                      nullable=True)
    # position = db.Column(db.String(200), unique=False, nullable=True)
    # not_key_words = db.Column(db.Text(300), unique=False, nullable=True)

    # # optional cols : language
    # english_mandatory = db.Column(db.String(200),
    #                               unique=False, nullable=True)
    # other_languages = db.Column(db.String(200), unique=False, nullable=True)

    # relationship
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=False,
                        nullable=False)

    def columns_list(self=None):
        if self:
            return [column.key for column in self.__table__.columns]
        else:
            return [column.key for column in Search.__table__.columns]

    def __repr__(self):
        keys = ['id', 'name', 'town', 'country', "key_words", "user_id"]
        txt = "\n".join([str(key.ljust(20, " ") + ": " +
                             str(self.__dict__[key])) for key in keys])
        return "\n" + txt
