import os
from flask import render_template, url_for, flash, redirect
from edhunt import warning


PATH = "edhunt/static/"
PREZ_DIR = "images/slides/prez/"


class _Log:
    title = "Corporate"
    head = ["Rertouvez ici toutes les informations sur le projet edhunt",
            "-",
            "Désolé, mais au regard de la sensibilité de ces informations, cet accès est privé "]


class _Data:
    title = "Corporate"
    head = ["Rertouvez ici toutes les informations sur le projet edhunt",
            "-",
            "Bravo tu as saisi le bon mot de passe"]

    one1 = "edhunt est la 1ere solution globale au service des candidats  qu’ils soient à l’écoute, en veille ou en recherche d’opportunitées professionnelles."

    one2 = "edunt permet de gérer, de piloter et d'automatiser, depuis une plateforme unique, simple et intuitive, l'ensemble de ses process de recrutement "

    two1 = "Concu par, avec et pour les candidats, edunt leur de propose"
    two2 = ["de mettre leur CV en ligne",
            "de chercher, lire et trier et classer les offres d'emploi",
            "d'envoyer les candidatures en un clic quelque soit la plateforme",
            "de suivre et de mettre à jour ses différents process"]

    two3 = "automatiquement, depuis une seule plateforme et facilement"

    three = ["Le projet est né d’un constat très simple", "Il est aujourdhui trop long, trop difficile et trop pénible de gerér une recherche d’emploi, qu’on soit en recherche active à l’écoute ou en veille. ",
             "L’atomicité du marché et la mutpilicité des plateformes est la première cause directe de cette situation",
             "La seconde est à chercher du coté de l’automatisation des process coté recruteur, entraiant une explosion de la demande, alors que rien - ou si peu - n'a été fait du coté candidat. ",
             "Il faut enfin aider les candidats, en (re)mettant de la simplicité, de la centralisation et de l’automatisation dans la gestion du process de recrutement."]

    four1 = "Quelques chiffres"

    four2 = [
        ("12", "le nombres de plateformes / jobboards généralistes en France (hors réseaux sociaux)"),
        ("30+", " le nombres de plateformes / jobboards total, si on compte les spécialiste et les acteurs de 2nd rang"),
        ("15%", "le nombre d’offres publiées demandant de créer un compte sur une platefome tièrce (site corporate nécessitant la création d’un compte spécifique)"),
        ("75%", "le taux d’abandon de la candidature si l’offre est sur une platefome tièrce"),
        ("+10%", "l’augmentation de recrutements cadres prévus entre 2018 – 2019, +20% au global (cadre et non cadre)"),
        ("3.8%", "Le taux de chômage des cadres, soit 25 % en dessous du chomage dit ‘structurel’"),
        ("0", "le nombre de requettes pertinentes si avec mots clés 'au service des candidats'")]

    slides = [str(PREZ_DIR + i) for i in sorted(os.listdir(PATH + PREZ_DIR))]


class CorporateText:

    log = _Log
    data = _Data
