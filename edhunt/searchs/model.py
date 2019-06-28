from edhunt import db, UserMixin
from datetime import datetime
from edhunt.searchs.utils import SearchsEnums
from edhunt.opportunities.model import Opportunity


class Search(db.Model, UserMixin):
    """table Search"""

    # positional cols
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    mob = db.Column(db.Enum(*SearchsEnums.mob), unique=False, nullable=False)
    country = db.Column(db.String(200), unique=False, nullable=True)
    region = db.Column(db.String(200), unique=False, nullable=True)
    departement = db.Column(db.String(200), unique=False, nullable=True)
    town = db.Column(db.String(200), unique=False, nullable=True)
    key_words = db.Column(db.Text(300), unique=False, nullable=False,
                          default=".")
    created = db.Column(db.String(20), unique=False, nullable=False,
                        default=datetime.utcnow)
    last_update = db.Column(db.String(20), unique=False, nullable=True)

    # work status
    contract = db.Column(db.String(200), unique=False, nullable=True)
    employer = db.Column(db.String(200), unique=False, nullable=True)
    status = db.Column(db.String(200), unique=False, nullable=True)
    rem = db.Column(db.String(200), unique=False, nullable=True)
    currency = db.Column(db.Enum(*SearchsEnums.currency), unique=False,
                         nullable=True)
    management = db.Column(db.Enum(*SearchsEnums.booleen), unique=False,
                           nullable=True)

    # Job
    company = db.Column(db.String(200), unique=False, nullable=True)
    not_company = db.Column(db.String(200), unique=False, nullable=True)
    company_size = db.Column(db.String(200), unique=False, nullable=True)
    job = db.Column(db.String(200), unique=False, nullable=True)
    sector = db.Column(db.String(200), unique=False, nullable=True)
    function = db.Column(db.Enum(*SearchsEnums.function), unique=False,
                         nullable=True)
    position = db.Column(db.String(200), unique=False, nullable=True)
    not_key_words = db.Column(db.Text(300), unique=False, nullable=True)

    # optional cols : language
    english_mandatory = db.Column(db.String(200),
                                  unique=False, nullable=True)
    other_languages = db.Column(db.String(200), unique=False, nullable=True)

    # relationship
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=False,
                        nullable=False)
    opportunities = db.relationship('Opportunity', backref='search', lazy=True)

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

    @property
    def search_fields(self):
        keys = ["contract", "employer", "status", "rem", "management", "company",
                "not_company", "company_size", "job", "sector", "function", "position",
                "not_key_words", "english_mandatory", "other_languages"]
        vals = [getattr(self, k) for k in keys]
        labels = ["Contrat", "Employeur", "Status", "Rémuneration", "Mangement", "Entr. souhaitée(s)", "Entr. évitée(s)", "Taille", "Poste", "Secteur", "Fonction", "Position hiéarchique", "Mots clés évités", "Anglais souhaité", "Autres Langue"]
        return zip(labels, vals)

    @property
    def search_fields2(self):
        keys = ['name', "key_words", "contract",
                "employer", "status", "rem", "management", "company",
                "not_company", "company_size", "job", "sector", "function", "position",
                "not_key_words", "english_mandatory", "other_languages"]
        vals = [getattr(self, k) for k in keys]
        labels = ['Nom', "Mots Clés", "Contrat", "Employeur", "Status", "Rémuneration", "Mangement", "Entr. souhaitée(s)", "Entr. évitée(s)", "Taille", "Poste", "Secteur", "Fonction", "Position hiéarchique", "Mots clés évités", "Anglais souhaité", "Autres Langue"]

        l1 = [(k, (v if v else "-")) for k, v in zip(labels, vals)]
        l2 = list()
        for i, data in enumerate(l1):
            if not i % 2:
                try:
                    l2.append((l1[i][0], l1[i][1], l1[i + 1][0], l1[i + 1][1]))
                except Exception as e:
                    l2.append((l1[i][0], l1[i][1], "", ""))
        return l2

    @property
    def search_fields_text(self):
        txt = ""
        for k, v in self.search_fields:
            txt += f"{k} : {v if v else '-'};  "
        return txt

    @property
    def opportunities_count(self):
        opps = Opportunity.query.filter_by(search_id=self.id).all()
        return len(opps)

    @property
    def candidatures_count(self):
        opps = Opportunity.query.filter_by(search_id=self.id).all()
        opps = [i for i in opps if i.send]
        return len(opps)

    @property
    def global_score(self):
        vals = [getattr(self, k) for k in self.columns_list() if getattr(self, k)]
        n = round(len(vals) * 100 / len(self.columns_list()))
        return n

    @property
    def essentiel_keys(self):
        keys = ["name", "key_words", 'mob', 'created', 'last_update']
        return keys

    @property
    def essentiel_score(self):
        vals = [getattr(self, k) for k in self.essentiel_keys if getattr(self, k)]
        n = round(len(vals) * 100 / len(self.essentiel_keys))
        return n

    @property
    def essentiel_fields(self):
        vals = [getattr(self, k) for k in self.essentiel_keys]
        vals = [(i if i else '-') for i in vals]
        labels = ['Nom', 'Mots Clés', 'Mobilité', 'Créée', 'Dernière MAJ']
        return zip(labels, vals)

    @property
    def job_keys(self):
        keys = ["company", "not_company", 'company_size', 'job', 'sector', 'function', 'position', 'not_key_words']
        return keys

    @property
    def job_score(self):
        vals = [getattr(self, k) for k in self.job_keys if getattr(self, k)]
        n = round(len(vals) * 100 / len(self.job_keys))
        return n

    @property
    def job_fields(self):
        vals = [getattr(self, k) for k in self.job_keys]
        vals = [(i if i else '-') for i in vals]
        labels = ['Entreprise(s) souhaitée(s)', 'Entreprise(s) évitée(s)', 'Taille', 'Poste', 'Secteur', "Fonction", 'Position', 'Mots clés évités']
        return zip(labels, vals)

    @property
    def status_keys(self):
        keys = ["contract", "employer", 'status', 'rem', 'currency', 'management']
        return keys

    @property
    def status_score(self):
        vals = [getattr(self, k) for k in self.status_keys if getattr(self, k)]
        n = round(len(vals) * 100 / len(self.status_keys))
        return n

    @property
    def status_fields(self):
        vals = [getattr(self, k) for k in self.status_keys]
        vals = [(i if i else '-') for i in vals]
        labels = ['Contrat(s)', "Type d'employeur(s)", 'Status', 'Rémuneration', 'Monnaie', "Management"]
        return zip(labels, vals)

    @property
    def language_keys(self):
        keys = ["english_mandatory", 'other_languages']
        return keys

    @property
    def language_score(self):
        vals = [getattr(self, k) for k in self.language_keys if getattr(self, k)]
        n = round(len(vals) * 100 / len(self.language_keys))
        return n

    @property
    def language_fields(self):
        vals = [getattr(self, k) for k in self.language_keys]
        vals = [(i if i else '-') for i in vals]
        labels = ["Niveau d'Anglais", "Autres langues"]
        return zip(labels, vals)
