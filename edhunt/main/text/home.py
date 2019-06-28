import os
from flask import render_template, url_for, flash, redirect
from edhunt import warning


PATH = "edhunt/static/"

WORDS = """la
(solution plateforme, web application)
(ultime parfaite idéale ideale complète complete intégrée)
pour les
(candidats recruteurs recrutement recrutements chasseur de tete chasseurs de tete employeurs demandeur d'emploi étudiants etudiant)
pour trouver un
(emploi job travail poste cadre non cadre, cdi cdd salaire promotion carrière carriere)
grace à
(edhunt, intelligence artificielle, algorithmes, solution, plateforme assistant
jarvis IA, AI, machine learning, deep learning, neural networks, code, plateforme)
"""
WORDS = ""


class _Page:
    title = "edhunt"
    subtitle = "L'assistant 100% dédié à votre recherche d'emploi"
    head = ["edhunt centralise, simplifie et automatise votre recherche d’emploi",
            "donnez-lui votre profil, votre CV et votre recherche, il gère le reste pour vous"]


class _TextBox1:
    items = ["Quelque soit le site d’emploi, edhunt épluche les offres, les sélectionne et vous les présente de façon claire et centralisée",
             """Avec edhunt vous candidatez
en un seul clic à n'importe quelle
offre d'emploi partout
sur le web""",
             "Au besoin, mais surtout avec votre autorisation, edhunt met votre CV en ligne, le diffuse et candidate automatiquement à votre place",
             """En recherche active, à l'écoute du marché ou simplement en veille, edhunt simplifie votre accès au marché de l'emploi"""]


class _Status:

    default = """... faciliter considérablement
votre recherche ou
votre veille d'emploi,
centraliser toutes vos démarches,
tout en automatisant les tâches pénibles,
longues ou répétitves
-
edhunt vous permet de le faire,
rapidement,
simplement et
depuis une seule plateforme."""

    recherche = """... vous assurer une visibilité maximale,
multiplier les candidatures sans vous
perdre sur les multiples plateformes et
pouvoir suivre vos différentes pistes.
Tout cela, si possible,
sans polluer votre boîte mail.
-
edhunt vous permet de le faire,
rapidement,
simplement et
depuis une seule plateforme."""

    ecoute = """... sentir le marché discrètement,
pouvoir candidater si nécessaire sur les
quelques offres vraiment intéressantes pour vous.
Le tout sans mettre votre CV en ligne
ni vous faire harceler pour
des postes non pertinents.
-
edhunt vous permet de le faire,
rapidement,
simplement et
depuis une seule plateforme."""


class _Aide:
    items = ["""Nombreux sont ceux qui aident les
recruteurs et les entreprises
à trouver des candidats""",
             """edhunt fait exactement l'inverse,
il aide les candidats dans
leur recherche de poste""",
             """A l'écoute ou en recherche active,
il leur rend la tâche
plus facile et plus rapide"""]


class _TextBox2:

    items = ["""edhunt vous permet
de piloter
toutes vos candidatures depuis
une seule plateforme""",
             """edhunt vous permet <br>
de visualiser et <br>
de chercher simplement des offres <br>
d'emploi sur l'ensemble du web""",
             """edhunt vous permet <br>
d'envoyer l'ensemble de  <br>
vos candidatures <br>
en un seul clic""",
             """dhunt identifie <br>
pour vous les  décisionnaires <br>
RH ou opérationnels pour une <br>
prise de contact rapide""",
             """edhunt évalue <br>
pour vous vos chances de <br>
succès sur les différents postes <br>
qui vous intéressent<br>""",
             """edhunt créé pour vous <br>
tous les comptes nécessaires <br>
à la diffusion de votre profil<br>
ou à l'envoi d'une candidature"""]


class _Avatar:
    loc = 'images/main/avatar.png'


class HomeText:
    page = _Page
    text_box_1 = _TextBox1
    status = _Status
    aide = _Aide
    text_box_2 = _TextBox2
    avatar = _Avatar


# def render_text(where, path=PATH):
#     return [str(where + i) for i in sorted(os.listdir(path + where))][0]


# def render_slides(where, path=PATH):
#     return [(i - 1, str(where + f)) for i, f in enumerate(
#         sorted(os.listdir(path + where)))][1:]

# class _Suis:
    """JE SUIS"""

    # text = render_text("images/main/carousel/suis/", PATH)
    # slides = render_slides("images/main/carousel/suis/", PATH)


# class _Peux:
#     """JE PEUX"""
#     text = render_text("images/main/carousel/peux/", PATH)
#     slides = render_slides("images/main/carousel/peux/", PATH)


# class _Soyez:
#     """QUE VOUS SOYEZ"""
#     text = render_text("images/main/carousel/soyez/", PATH)
#     slides = render_slides("images/main/carousel/soyez/", PATH)


# class _Allez:
#     """AVEC MOI VOUS ALLEZ"""
#     text = render_text("images/main/carousel/allez/", PATH)
#     slides = render_slides("images/main/carousel/allez/", PATH)


# class _AllezPlus:
#     """AVEC MOI VOUS ALLEZ PLUS"""
#     text = render_text("images/main/carousel/allezplus/", PATH)
#     slides = render_slides("images/main/carousel/allezplus/", PATH)


# class _Cest:
#     """CEST"""
#     text = render_text("images/main/carousel/cest/", PATH)
#     slides = render_slides("images/main/carousel/cest/", PATH)


# class _Saviez:
#     """LE SAVIEZ VOUS"""
#     text = render_text("images/main/carousel/saviez/", PATH)
#     slides = render_slides("images/main/carousel/saviez/", PATH)

# class _End:
#     loc = 'images/main/end3.png'
