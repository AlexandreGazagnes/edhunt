
class _Page:
    title = "L'offre"
    head = ["edhunt propose 4 offres qui répondent chacune à des services différents, des plus légers aux plus complets",
            "A vous d'arbitrer votre niveau d'accompagnement en fonction de votre de niveau de recherche",
            ]


class _Page2:
    title = "L'offre"
    head = ["edhunt propose une offre de services et d'outils très différents, allant des plus légers au plus complets",
            "A vous d'arbitrer votre niveau d'accompagnement en fonction de votre de niveau de recherche",
            ]


class _FreeHunt:
    name = "freeHunt"
    price_main = "gratuit sans engagement et sans empreinte CB"
    price_title = "gratuit\nsans engagement\n sans empreinte CB"
    features = [
        "Accès à l’ensemble des offres d’emploi disponibles sur les plateformes connectées ",
        "Envoi de vos candidatures en un clic, quelque soit la plateforme connectée",
        "Accès à la l'outil myBord pour piloter vos différents process de recrutement * ",
        "Accès gratuit d'un mois à l'offre smartHunt, sans engagement ni empreinte CB",
        "",
        "Plateformes disponibles: 7",
        "Nombre de recherches: 3",
        "Nombre de candidatures par mois: 90"
    ]


class _SmartHunt:
    name = "smartHunt"
    price_main = "3.95€ par mois, sans engagement, premier mois offert"
    price_title = "3.95€ par mois\nsans engagement\npremier mois offert"
    features = [
        "Ensemble des offres de freeHunt",
        "+",
        "Accès à la l'outil myScore qui trie et évalue automatiquement les offres d’emploi pour vous en fonction de vos critères et de vos chances de succès *",
        "Candidatures automatiques selon la pertinence de l'offre*",
        "Mise en ligne de votre CV ou de votre profil sur les différentes plateformes connectées **",
        "Identification automatique des décisionnaires RH/opérationnels **",
        "",
        "Plateformes disponibles : 11",
        "Nombre de recherches : 100",
        "Nombre de candidatures par mois : 1200"]


class _BigHunt:
    name = "bigHunt"
    price_main = "11.95€ par mois, sans engagement, premier mois offert"
    price_title = "11.95€ par mois\nsans engagement\npremier mois offert"
    features = [
        "Ensemble des offres de smartHunt",
        "+",
        "Adresse mail personnelle prenom.nom@edhunt.fr **",
        "Accès via edhunt à tout site/interface externe nécessitant des actions d’enregistrement spécifique **",
        "Mise en ligne et diffusion de votre CV ou de votre profil sur toutes les plateformes d'emploi **",
        "Gestion des retours aux offres d’emplois, mise à jour et intégration automatique du statut de la candidature **",
        "Prise de contact automatique ou manuelle avec des décisionnaires RH/opérationnels **",
        "",
        "Plateformes disponibles : illimitées",
        "Nombre de recherches : illimitées",
        "Nombre de candidatures par mois : illimitées",
    ]


class _ProHunt:
    name = "proHunt"
    price_main = "129.95€ par mois, sans engagement"
    price_title = "129.95€ par mois\nsans engagement"
    features = [
        "Ensemble des offres de bigHunt",
        "+",
        "Accompagnement d’un consultant edhunt pour la définition du  projet professionnel et dans la selection des offres sur lesquelles candidater ",
        "Accompagnement d’un consultant edhunt pour la rédaction ou l'amélioration du CV, et la rédaction automatique ou manuelle des lettres de motivations ",
        "Accompagnement d’un consultant edhunt dans les différentes phases opérationnelles des process de recrutement : brief avant les entretiens, débrief après les entretiens, choix parmi les différentes pistes...",
        " Votre consultant edhunt cherche pour vous des postes sur mesure en appellant ou en rencontrant en direct les décisionnaires RH/opérationnels pour défendre votre candidature (myHunt)",
        "Accompagnement d’un consultant edhunt lors de négociation salariale, la signature du contrat de travail et la période d'essai"
        "",
        "Plateformes disponibles : illimitées",
        "Nombre de recherches : illimitées",
        "Nombre de candidatures par mois : illimitées",
    ]


class _Stars:
    items = [("*", "disponible Septembre 2019"),
             ("**", "disponible Novembre 2019"), ]


class _Feats:
    items = [
        "Accès à l’ensemble des offres d’emploi disponibles sur les plateformes connectées ",
        "Envoi de vos candidatures en un clic, quelque soit la plateforme connectée",
        "Accès à l'outil myBord pour piloter vos différents process de recrutement ",
        "Accès à l'outil myScore qui trie et évalue automatiquement les offres d’emploi pour vous *",
        "Candidatures automatiques selon la pertinence de l'offre *",
        "Identification automatique des décisionnaires RH/opérationnels **",
        # "Mise en ligne de votre CV ou de votre profil sur les différentes plateformes connectées **",
        "Adresse mail personnelle prenom.nom@edhunt.fr **",
        "Accès via edhunt à tout site/interface externe nécessitant des actions d’enregistrement spécifique **",
        # "Mise en ligne et diffusion de votre CV ou de votre profil sur toutes les plateformes d'emploi **",
        "Gestion des retours aux offres d’emplois, mise à jour et intégration automatique du statut de la candidature **",
        "Prise de contact automatique ou manuelle avec des décisionnaires RH/opérationnels **",
        "Accompagnement d’un consultant edhunt pour la définition du projet professionnel et dans la sélection des offres sur lesquelles candidater ",
        "Accompagnement d’un consultant edhunt pour la rédaction ou l'amélioration du CV et la rédaction automatique ou manuelle des lettres de motivations ",
        "Accompagnement d’un consultant edhunt dans les différentes phases opérationnelles des process de recrutement : brief avant les entretiens, débrief après les entretiens, choix parmi les différentes pistes...",
        "Votre consultant edhunt cherche pour vous des postes sur mesure en appellant ou en rencontrant en direct les décisionnaires RH/opérationnels pour défendre votre candidature",
        "Accompagnement d’un consultant edhunt lors de négociation salariale, la signature du contrat de travail et la période d'essai"]


class _Tools:
    items = [
        ("myBord", "C'est l'outil de gestion et de suivi de vos candidatures, de vos pistes et de vos process de recrutement."),
        ("myScore", "C'est l'outil de scoring des différentes offres d'emploi. Il prend en compte vos attentes, vos critères de recherche, mais aussi les chances que vous avez de postuler sur un poste donné."),
        ("myHunt", "C'est plus une méthodologoie qu'un outil : myHunt va chercher vous le poste de vos rèves, et si ce poste n'existe pas, myHunt va essayer de le créer sur le marché de l'emploi.")]


class OffreText:
    page = _Page
    free = _FreeHunt
    smart = _SmartHunt
    big = _BigHunt
    pro = _ProHunt
    feats = _Feats
    star = _Stars


class Offre2Text:
    page = _Page2
    feats = _Feats
    stars = _Stars
    tools = _Tools
