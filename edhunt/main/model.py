import secrets
from datetime import datetime
from edhunt import db
from edhunt.users.utils import UsersEnums, Joboard
from edhunt.main.utils import QuestionnaireEnums


class Features(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    searchs_max = db.Column(db.String(10), unique=False, nullable=False)
    candidatures_max = db.Column(db.String(10), unique=False, nullable=False)
    plateforms_max = db.Column(db.String(10), unique=False, nullable=False)
    candidature_auto = db.Column(db.Boolean(), unique=False, nullable=False)
    opportunity_score = db.Column(db.Boolean(), unique=False, nullable=False)
    decideur_identification = db.Column(db.Boolean(), unique=False, nullable=False)
    edhunt_email = db.Column(db.Boolean(), unique=False, nullable=False)
    create_plateform_account = db.Column(db.Boolean(), unique=False, nullable=False)
    handle_external_app = db.Column(db.Boolean(), unique=False, nullable=False)
    decideur_contact = db.Column(db.Boolean(), unique=False, nullable=False)
    decideur_contact_auto = db.Column(db.Boolean(), unique=False, nullable=False)
    coach = db.Column(db.Boolean(), unique=False, nullable=False)

    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True,
    #                     nullable=False)

    def __repr__(self):
        keys = ['name', 'searchs_max', 'candidatures_max', "candidature_auto",
                "opportunity_score", "opportunity_score", "decideur_identification", "edhunt_email", "create_plateform_account", "handle_external_app", "decideur_contact", "decideur_contact_auto", "coach"]
        txt = "\n".join([str(key.ljust(20, " ") + ": " +
                             str(self.__dict__[key])) for key in keys])
        return "\n" + txt + "\n"


class Questionnaire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(34), unique=True, nullable=False)

    # FORM_1
    search = db.Column(db.Enum(*UsersEnums.search), unique=False, nullable=True)
    employed = db.Column(db.Enum(*UsersEnums.trooleen), unique=False, nullable=True)

    offer_timing = db.Column(db.Enum(*QuestionnaireEnums.timing), unique=False, nullable=True)
    candidature_timing = db.Column(db.Enum(*QuestionnaireEnums.timing), unique=False, nullable=True)
    call_timing = db.Column(db.Enum(*QuestionnaireEnums.timing), unique=False, nullable=True)
    interview_timing = db.Column(db.Enum(*QuestionnaireEnums.timing), unique=False, nullable=True)

    # FORM_2
    feat_1 = db.Column(db.Enum(*UsersEnums.trooleen), unique=False, nullable=True)
    feat_2 = db.Column(db.Enum(*UsersEnums.trooleen), unique=False, nullable=True)
    feat_3 = db.Column(db.Enum(*UsersEnums.trooleen), unique=False, nullable=True)
    feat_4 = db.Column(db.Enum(*UsersEnums.trooleen), unique=False, nullable=True)
    feat_5 = db.Column(db.Enum(*UsersEnums.trooleen), unique=False, nullable=True)
    feat_6 = db.Column(db.Enum(*UsersEnums.trooleen), unique=False, nullable=True)
    feat_7 = db.Column(db.Enum(*UsersEnums.trooleen), unique=False, nullable=True)
    feat_8 = db.Column(db.Enum(*UsersEnums.trooleen), unique=False, nullable=True)
    feat_9 = db.Column(db.Enum(*UsersEnums.trooleen), unique=False, nullable=True)
    feat_10 = db.Column(db.Enum(*UsersEnums.trooleen), unique=False, nullable=True)
    feat_11 = db.Column(db.Enum(*UsersEnums.trooleen), unique=False, nullable=True)
    feat_12 = db.Column(db.Enum(*UsersEnums.trooleen), unique=False, nullable=True)
    feat_13 = db.Column(db.Enum(*UsersEnums.trooleen), unique=False, nullable=True)
    feat_14 = db.Column(db.Enum(*UsersEnums.trooleen), unique=False, nullable=True)

    # FORM_3
    contract = db.Column(db.Enum(*UsersEnums.contract), unique=False,
                         nullable=True)
    status = db.Column(db.Enum(*UsersEnums.status), unique=False, nullable=True)
    sector = db.Column(db.Enum(*UsersEnums.sector), unique=False, nullable=True)
    function = db.Column(db.Enum(*UsersEnums.function), unique=False, nullable=True)
    position = db.Column(db.Enum(*UsersEnums.position), unique=False, nullable=True)
    management = db.Column(db.Enum(*UsersEnums.management), unique=False,
                           nullable=True)
    rem = db.Column(db.Enum(*UsersEnums.small_rem), unique=False, nullable=True)
    xp_at_work = db.Column(db.String(2), unique=False, nullable=True)
    diploma_level = db.Column(db.Enum(*UsersEnums.diploma_level), unique=False,
                              nullable=True)
    # diploma_type = db.Column(db.Enum(*UsersEnums.diploma_type), unique=False,
    #                          nullable=True)
    diploma_year = db.Column(db.String(4), unique=False, nullable=True)
    zip_code = db.Column(db.String(5), unique=False, nullable=True)

    # FORM_4
    fond_already = db.Column(db.String(4), unique=False, nullable=True)
    fond_concurency = db.Column(db.String(300), unique=False, nullable=True)
    # forme_choc_level = db.Column(db.Enum(*QuestionnaireEnums.satisfaction),
    #                              unique=False, nullable=True)
    # forme_cool_level = db.Column(db.Enum(*QuestionnaireEnums.satisfaction),
    #                              unique=False, nullable=True)
    fond_compr_level = db.Column(db.Enum(*QuestionnaireEnums.satisfaction),
                                 unique=False, nullable=True)
    fond_painful_level = db.Column(db.Enum(*QuestionnaireEnums.satisfaction),
                                   unique=False, nullable=True)
    fond_interest_level = db.Column(db.Enum(*QuestionnaireEnums.satisfaction),
                                    unique=False, nullable=True)
    device_type = db.Column(db.String(50), unique=False, nullable=True)
    # device_name = db.Column(db.String(50), unique=False, nullable=True)
    remarque = db.Column(db.Text(1000), unique=False, nullable=True)

    # CONNECTION
    email = db.Column(db.String(40), unique=False, nullable=True)
    phone = db.Column(db.String(40), unique=False, nullable=True)
    hour = db.Column(db.String(40), unique=False, nullable=True)

    created = db.Column(db.String(20), unique=False, nullable=False,
                        default=datetime.utcnow)

    # DEPRECIATED
    # forme_generic = db.Column(db.Text(1000), unique=False, nullable=True)
    # forme_good = db.Column(db.Text(1000), unique=False, nullable=True)
    # forme_bad = db.Column(db.Text(1000), unique=False, nullable=True)
    # fond_generic = db.Column(db.Text(1000), unique=False, nullable=True)
    # fond_questions = db.Column(db.Text(1000), unique=False, nullable=True)
    # user = db.Column(db.String(50), unique=False, nullable=True)
    # device = db.Column(db.String(50), unique=False, nullable=True)
    # # offers_week = db.Column(db.String(50), unique=False, nullable=True)
    # offers_month = db.Column(db.String(50), unique=False, nullable=True)
    # offers_semester = db.Column(db.String(50), unique=False, nullable=True)
    # call_week = db.Column(db.String(50), unique=False, nullable=True)
    # call_month = db.Column(db.String(50), unique=False, nullable=True)
    # call_semester = db.Column(db.String(50), unique=False, nullable=True)
    # interview_week = db.Column(db.String(50), unique=False, nullable=True)
    # interview_month = db.Column(db.String(50), unique=False, nullable=True)
    # interview_semester = db.Column(db.String(50), unique=False, nullable=True)
    # candidaté derniereme
    # xp_at_job = db.Column(db.String(2), unique=False, nullable=True)
    # xp_at_company = db.Column(db.String(2), unique=False, nullable=True)
    # linkedin
    # dummy
    # earth = db.Column(db.Enum(*QuestionnaireEnums.satisfaction),
    #                   unique=False, nullable=True)
    # moon = db.Column(db.Enum(*QuestionnaireEnums.satisfaction),
    #                  unique=False, nullable=True)
    # marre = db.Column(db.Enum(*QuestionnaireEnums.satisfaction),
    #                   unique=False, nullable=True)

    def __repr__(self):
        keys = ['forme_generic', 'forme_good', 'forme_bad', 'fond_generic',
                "fond_questions", "fond_already", "forme_choc_level",
                "forme_cool_level", "fond_compr_level", "fond_interest_level", "user",
                "device"]
        txt = "\n".join([str(key.ljust(20, " ") + ": " +
                             str(self.__dict__[key])) for key in keys])
        return "\n" + txt + "\n"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=False, nullable=True)
    tags = db.Column(db.String(50), unique=False, nullable=True)
    author = db.Column(db.String(50), unique=False, nullable=True)
    text = db.Column(db.Text(1000), unique=False, nullable=True)
    created = db.Column(db.String(18), unique=False, nullable=True,
                        default=str(datetime.utcnow())[:16])
    source = db.Column(db.String(50), unique=False, nullable=True)
    link = db.Column(db.String(50), unique=False, nullable=True)

    @property
    def header(self):
        return str(self.text)[:140]

    def __repr__(self):
        keys = ['title', 'author', 'text', 'source', 'created']
        txt = "\n".join([str(key.ljust(20, " ") + ": " +
                             str(self.__dict__[key])) for key in keys])
        return "\n" + txt + "\n"


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=False, nullable=True)
    # topic = None
    text = db.Column(db.Text(1000), unique=False, nullable=True)
    name = db.Column(db.String(50), unique=False, nullable=True)
    email = db.Column(db.String(50), unique=False, nullable=True)
    phone = db.Column(db.String(20), unique=False, nullable=True)
    # user = db.Column(db.String(50), unique=False, nullable=True)
    created = db.Column(db.String(20), unique=False, nullable=False,
                        default=datetime.utcnow)

    def __repr__(self):
        keys = ['title', 'text', 'name', 'email', 'phone']
        txt = "\n".join([str(key.ljust(20, " ") + ": " +
                             str(self.__dict__[key])) for key in keys])
        return "\n" + txt + "\n"


class MainTables:
    contact = Contact
    post = Post
    questionnaire = Questionnaire
    features = Features


class Country(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.country

    @staticmethod
    def list_all():
        return [i.country for i in Country.query.all()]


class Town(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    town = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.town

    @staticmethod
    def list_all():
        return [i.town for i in Town.query.all()]


class School(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    school = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.school

    @staticmethod
    def list_all():
        return [i.school for i in School.query.all()]


class Company(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.company

    @staticmethod
    def list_all():
        return [i.company for i in Company.query.all()]


class Job(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    job = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.job

    @staticmethod
    def list_all():
        return [i.job for i in Job.query.all()]


class ZipCode(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    zip_code = db.Column(db.SmallInteger(), unique=True, nullable=False)

    def __repr__(self):
        return self.zip_code

    @staticmethod
    def list_all():
        return [i.zip_code for i in ZipCode.query.all()]


class Region(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.region

    @staticmethod
    def list_all():
        return [i.region for i in Region.query.all()]


class Departement(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    departement = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.departement

    @staticmethod
    def list_all():
        return [i.departement for i in Departement.query.all()]
