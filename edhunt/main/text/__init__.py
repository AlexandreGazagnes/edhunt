
from edhunt.main.text.home import HomeText
from edhunt.main.text.offre import OffreText, Offre2Text
from edhunt.main.text.apropos import AproposText
from edhunt.main.text.faq import FaqText
from edhunt.main.text.contact import ContactText
from edhunt.main.text.blog import BlogText
from edhunt.main.text.questionnaire import QuestionnaireText
from edhunt.main.text.corporate import CorporateText
from edhunt.main.text.connexion import ConnexionText
from edhunt.main.text.post import PostText


class MainText:
    home = HomeText
    offre = OffreText
    offre2 = Offre2Text
    apropos = AproposText
    faq = FaqText
    blog = BlogText
    questionnaire = QuestionnaireText
    corporate = CorporateText
    connexion = ConnexionText
    contact = ContactText
    post = PostText


# class classproperty(object):
#     def __init__(self, f):
#         self.f = f

#     def __get__(self, obj, owner):
#         return self.f(owner)
