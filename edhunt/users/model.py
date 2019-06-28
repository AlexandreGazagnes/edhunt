from datetime import datetime
from flask_login import UserMixin
from edhunt import db, warning, info
from edhunt.users.utils import UsersEnums, Joboard
from edhunt.plateforms import Plateforms
from edhunt.opportunities.model import Opportunity


class User(db.Model, UserMixin):
    # account
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=False, nullable=False)
    password = db.Column(db.String(40), unique=False, nullable=False)
    created = db.Column(db.String(40), unique=False, nullable=False, default=datetime.utcnow)

    # expectations
    employed = db.Column(db.Enum(*UsersEnums.trooleen), unique=False, nullable=True)
    sub_employed = db.Column(db.Enum(*UsersEnums.sub_employed),
                             unique=False, nullable=True)
    search = db.Column(db.Enum(*UsersEnums.search), unique=False, nullable=True)
    order = db.Column(db.Enum(*UsersEnums.order), unique=False, nullable=True)
    automation = db.Column(db.Enum(*UsersEnums.automation), unique=False, nullable=True)

    # resumes
    resume1_doc = db.Column(db.String(40), nullable=True, unique=True)
    resume1_name = db.Column(db.String(40), nullable=False, unique=False,
                             default="no resume")
    resume2_doc = db.Column(db.String(40), nullable=True, unique=True)
    resume2_name = db.Column(db.String(40), nullable=False, unique=False,
                             default="no resume")
    resume3_doc = db.Column(db.String(40), nullable=True, unique=True)
    resume3_name = db.Column(db.String(40), nullable=False, unique=False,
                             default="no resume")

    # identity
    firstname = db.Column(db.String(40), unique=False, nullable=True)
    lastname = db.Column(db.String(40), unique=False, nullable=True)
    sex = db.Column(db.Enum(*UsersEnums.sex), unique=False, nullable=True)
    birthdate = db.Column(db.String(12), unique=False, nullable=True)
    nationality = db.Column(db.String(50), unique=False, nullable=True)
    birth_country = db.Column(db.String(50), unique=False, nullable=True)
    birth_zip_code = db.Column(db.String(5), unique=False, nullable=True)
    birth_town = db.Column(db.String(50), unique=False, nullable=True)

    # localisation
    town = db.Column(db.String(50), unique=False, nullable=True)
    zip_code = db.Column(db.String(5), unique=False, nullable=True)
    country = db.Column(db.String(50), unique=False, nullable=True)
    driver_licence = db.Column(db.Enum(*UsersEnums.trooleen), unique=False,
                               nullable=True)
    vehicule = db.Column(db.Enum(*UsersEnums.trooleen), unique=False, nullable=True)

    # diploma
    diploma_name = db.Column(db.String(50), unique=False, nullable=True)
    diploma_school = db.Column(db.String(50), unique=False, nullable=True)
    diploma_town = db.Column(db.String(50), unique=False, nullable=True)
    diploma_level = db.Column(db.Enum(*UsersEnums.diploma_level), unique=False,
                              nullable=True)
    diploma_type = db.Column(db.Enum(*UsersEnums.diploma_type), unique=False,
                             nullable=True)
    diploma_year = db.Column(db.String(4), unique=False, nullable=True)

    # work experience
    company = db.Column(db.String(50), unique=False, nullable=True)
    xp_at_company = db.Column(db.String(2), unique=False, nullable=True)
    company_size = db.Column(db.Enum(*UsersEnums.company_size), unique=False,
                             nullable=True)
    job = db.Column(db.String(50), unique=False, nullable=True)
    xp_at_job = db.Column(db.String(2), unique=False, nullable=True)
    sector = db.Column(db.Enum(*UsersEnums.sector), unique=False, nullable=True)
    function = db.Column(db.Enum(*UsersEnums.function), unique=False, nullable=True)
    position = db.Column(db.Enum(*UsersEnums.position), unique=False, nullable=True)
    mob = db.Column(db.Enum(*UsersEnums.mob), unique=False, nullable=True)
    key_words = db.Column(db.Text(300), unique=False, nullable=True)

    # work status
    contract = db.Column(db.Enum(*UsersEnums.contract), unique=False,
                         nullable=True)
    employer = db.Column(db.Enum(*UsersEnums.employer), unique=False,
                         nullable=True)
    status = db.Column(db.Enum(*UsersEnums.status), unique=False, nullable=True)
    rem = db.Column(db.Enum(*UsersEnums.small_rem), unique=False, nullable=True)
    currency = db.Column(db.Enum(*UsersEnums.currency), unique=False,
                         nullable=True)
    management = db.Column(db.Enum(*UsersEnums.management), unique=False,
                           nullable=True)
    xp_at_work = db.Column(db.String(2), unique=False, nullable=True)

    # languages
    english = db.Column(db.Enum(*UsersEnums.english), unique=False, nullable=True)
    others = db.Column(db.String(100), unique=False, nullable=True)

    # admin
    last_connexion = db.Column(db.String(20), unique=False, nullable=True)
    connexions_all = db.Column(db.SmallInteger(), unique=False, nullable=True,
                               default=0)
    connexions_this_week = db.Column(db.SmallInteger(), unique=False, nullable=True,
                                     default=0)
    connexions_this_month = db.Column(db.SmallInteger(), unique=False, nullable=True,
                                      default=0)
    features = db.Column(db.String(10), unique=False, nullable=True)
    features_stop_day = db.Column(db.String(10), unique=False, nullable=True)
    auto_test_plateforms = db.Column(db.Boolean(), unique=False, nullable=True)
    auto_update_searchs = db.Column(db.Boolean(), unique=False, nullable=True)

    # plateforms
    # apec = Joboard.status()
    # apec_email = Joboard.email()
    # apec_password = Joboard.password()
    # apec_autorisation = Joboard.autorisation()
    # apec_good_user = Joboard.good_user()
    # apec_edhunt_integrity = Joboard.edhunt_integrity()

    # cadremploi = Joboard.status()
    # cadremploi_email = Joboard.email()
    # cadremploi_password = Joboard.password()
    # cadremploi_autorisation = Joboard.autorisation()
    # cadremploi_good_user = Joboard.good_user()
    # cadremploi_edhunt_integrity = Joboard.edhunt_integrity()

    # indeed = Joboard.status()
    # indeed_email = Joboard.email()
    # indeed_password = Joboard.password()
    # indeed_autorisation = Joboard.autorisation()
    # indeed_good_user = Joboard.good_user()
    # indeed_edhunt_integrity = Joboard.edhunt_integrity()

    # jobintree = Joboard.status()
    # jobintree_email = Joboard.email()
    # jobintree_password = Joboard.password()
    # jobintree_autorisation = Joboard.autorisation()
    # jobintree_good_user = Joboard.good_user()
    # jobintree_edhunt_integrity = Joboard.edhunt_integrity()

    # keljob = Joboard.status()
    # keljob_email = Joboard.email()
    # keljob_password = Joboard.password()
    # keljob_autorisation = Joboard.autorisation()
    # keljob_good_user = Joboard.good_user()
    # keljob_edhunt_integrity = Joboard.edhunt_integrity()

    # leboncoin = Joboard.status()
    # leboncoin_email = Joboard.email()
    # leboncoin_password = Joboard.password()
    # leboncoin_autorisation = Joboard.autorisation()
    # leboncoin_good_user = Joboard.good_user()
    # leboncoin_edhunt_integrity = Joboard.edhunt_integrity()

    # lesjeudis = Joboard.status()
    # lesjeudis_email = Joboard.email()
    # lesjeudis_password = Joboard.password()
    # lesjeudis_autorisation = Joboard.autorisation()
    # lesjeudis_good_user = Joboard.good_user()
    # lesjeudis_edhunt_integrity = Joboard.edhunt_integrity()

    # linkedin = Joboard.status()
    # linkedin_email = Joboard.email()
    # linkedin_password = Joboard.password()
    # linkedin_autorisation = Joboard.autorisation()
    # linkedin_good_user = Joboard.good_user()
    # linkedin_edhunt_integrity = Joboard.edhunt_integrity()

    # meteojob = Joboard.status()
    # meteojob_email = Joboard.email()
    # meteojob_password = Joboard.password()
    # meteojob_autorisation = Joboard.autorisation()
    # meteojob_good_user = Joboard.good_user()
    # meteojob_edhunt_integrity = Joboard.edhunt_integrity()

    # monster = Joboard.status()
    # monster_email = Joboard.email()
    # monster_password = Joboard.password()
    # monster_autorisation = Joboard.autorisation()
    # monster_good_user = Joboard.good_user()
    # monster_edhunt_integrity = Joboard.edhunt_integrity()

    # polemploi = Joboard.status()
    # polemploi_email = Joboard.email()
    # polemploi_password = Joboard.password()
    # polemploi_autorisation = Joboard.autorisation()
    # polemploi_good_user = Joboard.good_user()
    # polemploi_edhunt_integrity = Joboard.edhunt_integrity()

    # regionjob = Joboard.status()
    # regionjob_email = Joboard.email()
    # regionjob_password = Joboard.password()
    # regionjob_autorisation = Joboard.autorisation()
    # regionjob_good_user = Joboard.good_user()
    # regionjob_edhunt_integrity = Joboard.edhunt_integrity()

    # relationship
    searchs = db.relationship('Search', backref='user', lazy=True)
    opportunities = db.relationship('Opportunity', backref='user', lazy=True)

    # features = db.relationship('Features', backref='user')
    apec = db.relationship('Apec', backref='user')
    cadremploi = db.relationship('Cadremploi', backref='user')
    indeed = db.relationship('Indeed', backref='user')
    jobintree = db.relationship('Jobintree', backref='user')
    keljob = db.relationship('Keljob', backref='user')
    # leboncoin = db.relationship('Leboncoin', backref='user')
    lesjeudis = db.relationship('Lesjeudis', backref='user')
    meteojob = db.relationship('Meteojob', backref='user')
    monster = db.relationship('Monster', backref='user')
    regionjob = db.relationship('Regionjob', backref='user')

    def __repr__(self):
        keys = ['id', 'username', 'email', 'password']
        txt = "\n".join([str(key.ljust(20, " ") + ": " +
                             str(self.__dict__[key])) for key in keys])
        return "\n" + txt

    def columns_list(self=None):
        """return all field of User Table"""

        if self:
            return [column.key for column in self.__table__.columns]
        else:
            return [column.key for column in User.__table__.columns]

    def _compute_score(self, keys):
        filed = [getattr(self, k) for k in keys]
        filed = [k for k in filed if (k and (k != '-'))]
        l_filed, l_keys = len(filed), len(keys)
        return f"{l_filed * 100 / l_keys:.0f}"

    def _give_vals(self, keys):
        return [getattr(self, k) for k in keys]

    @property
    def profile_score(self):
        """return a % of field info for a User"""

        keys = ['username', 'email', 'password', 'created', 'employed', 'sub_employed', 'search', 'order', 'automation',
                'resume1_doc', 'resume2_doc', 'resume3_doc',
                'firstname', 'lastname', 'sex', 'birthdate', 'nationality',
                'birth_country', 'birth_zip_code', 'birth_town',
                'town', 'zip_code', 'country', 'driver_licence', 'vehicule',
                'diploma_name', 'diploma_school', 'diploma_town',
                'diploma_level', 'diploma_type', 'diploma_year',
                'company', 'xp_at_company', 'company_size', 'job', 'xp_at_job',
                'sector', 'function', 'position', 'mob', 'key_words',
                'contract', 'employer', 'status', 'rem', 'currency',
                'management', 'xp_at_work',
                'english', 'others']

        return self._compute_score(keys)

    # def plateform_list(self):
    #     return ["apec", "cadremploi", 'indeed', 'jobintree', 'keljob',
    #             'leboncoin', 'lesjeudis', 'meteojob', 'monster',
    #             'polemploi', 'regionjob']

    # def joboard_score(self):
    #     #     """return a % of field info for a joboards"""

    #     #     keys = ["apec", "cadremploi", 'indeed', 'jobintree', 'keljob',
    #     #             'leboncoin', 'lesjeudis', 'meteojob', 'monster',
    #     #             'polemploi', 'regionjob']
    #     #     filed = [self.__dict__[i] for i in keys if self.__dict__[i] == "On"]
    #     #     l_filed, l_keys = len(filed), len(keys)
    #     #     return f"{l_filed}/{l_keys}"

    #     return "122"

    # Resume
    @property
    def resume_keys(self):
        return ['resume1_name', 'resume2_name', 'resume3_name']

    @property
    def resume_fields(self):
        labels = ["CV n°1", "CV n°2", "CV n°3"]
        return zip(labels, self._give_vals(self.resume_keys))

    @property
    def resume_score(self):
        keys = ['resume1_doc', 'resume2_doc', 'resume3_doc', ]
        return self._compute_score(keys)

    # expectation
    @property
    def expectation_keys(self):
        return ['employed', 'sub_employed', 'search', 'order', 'automation']

    @property
    def expectation_fields(self):
        labels = ['En poste', 'Disponible', 'Situation', 'Attentes', 'Candidatures']
        return zip(labels, self._give_vals(self.expectation_keys))

    @property
    def expectation_score(self):
        return self._compute_score(self.expectation_keys)

    # identification
    @property
    def identification_keys(self):
        return ['firstname', 'lastname', 'sex', 'birthdate', 'nationality',
                'birth_country', 'birth_zip_code', 'birth_town']

    @property
    def identification_fields(self):
        labels = ['Prénom', 'Nom', 'Sexe', 'Date de naissance', 'Nationalité',
                  "Pays de naissance", 'Code Postal', "Ville de naissance"]
        return zip(labels, self._give_vals(self.identification_keys))

    @property
    def identification_score(self):
        return self._compute_score(self.identification_keys)

    # localisation
    @property
    def localisation_keys(self):
        return ['town', 'zip_code', 'country', 'driver_licence', 'vehicule']

    @property
    def localisation_fields(self):
        labels = ['Ville', 'Code postal', 'Pays', 'Permis', 'Véhicule', ]
        return zip(labels, self._give_vals(self.localisation_keys))

    @property
    def localisation_score(self):
        return self._compute_score(self.localisation_keys)

    # diploma
    @property
    def diploma_keys(self):
        return ['diploma_name', 'diploma_school', 'diploma_town',
                'diploma_level', 'diploma_type', 'diploma_year']

    @property
    def diploma_fields(self):
        labels = ['Nom', 'Ecole', 'Ville', 'Niveau', 'Type', 'Année']
        return zip(labels, self._give_vals(self.diploma_keys))

    @property
    def diploma_score(self):
        return self._compute_score(self.diploma_keys)

    # work_experience
    @property
    def work_experience_keys(self):
        return ['company', 'xp_at_company', 'company_size', 'job', 'xp_at_job',
                'sector', 'function', 'position', 'mob', 'key_words']

    @property
    def work_experience_fields(self):
        labels = ["Entreprise", 'Experience en entr.', "Taille d'entr.", "Poste",
                  "Experience à ce poste", 'Secteur', 'Fonction',
                  'Position hiérarchique', 'Mobilité', 'Mots clés']
        return zip(labels, self._give_vals(self.work_experience_keys))

    @property
    def work_experience_score(self):
        return self._compute_score(self.work_experience_keys)

    # work_status
    @property
    def work_status_keys(self):
        return ['contract', 'employer', 'status', 'rem', 'currency',
                'management', 'xp_at_work']

    @property
    def work_status_fields(self):
        labels = ["Contrat", "Type d'entr.", "Statut", "Salaire",
                  "Monnaie", 'Management', 'Experience prof.']
        return zip(labels, self._give_vals(self.work_experience_keys))

    @property
    def work_status_score(self):
        return self._compute_score(self.work_status_keys)

    # language
    @property
    def language_keys(self):
        return ['english', 'others']

    @property
    def language_fields(self):
        labels = ["Anglais", "Autres"]
        return zip(labels, self._give_vals(self.language_keys))

    @property
    def language_score(self):
        return self._compute_score(self.language_keys)

    @property
    def plateform_score(self):
        plateforms = [getattr(Plateforms.tables, p).query.filter_by(user_id=self.id).first() for p in Plateforms.list_all]
        plateforms = [i for i in plateforms if i]
        connexions = [i for i in plateforms if i.connexion == "On"]
        score = round(100 * len(connexions) / len(Plateforms.list_all))
        return score

    def avialable_plateforms(self):
        plateforms = [getattr(Plateforms.tables, p).query.filter_by(user_id=self.id).first() for p in Plateforms.list_all]
        plateforms = [i for i in plateforms if i]
        connexions = [i for i in plateforms if i.connexion == "On"]

        return [i.__name__ for i in connexions]

    @property
    def opportunities_count(self):
        li = Opportunity.query.filter_by(user_id=self.id).all()
        return len(li)

    @property
    def candidatures_count(self):
        li = Opportunity.query.filter_by(user_id=self.id).all()
        li = [i for i in li if i.send]
        return len(li)

    @property
    def opportunities_max(self):
        return 100

    @property
    def candidatures_max(self):
        return 100

    @property
    def pistes_max(self):
        return 100

    @property
    def searchs_max(self):
        return 3
