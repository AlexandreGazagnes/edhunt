
class _Page:
    title = "A propos"
    head = ["edhunt est la seule plateforme 100% dédiée au service des candidats en recherche active, à l'écoute ou en veille",
            "les recruteurs ont leurs robots à eux, les candidats ont edhunt, une plateforme pensée par, avec et pour eux"]


class _DejaDit:
    name = "Vous êtes vous déjà dit :"
    text = [(1, "Je changerais bien de job mais je n’ai pas le temps de chercher"),
            (2, "Je quitterais bien Paris, mais il n’y a pas de travail en province"),
            (3, "J’ai vu des offres mais rien de bien intéressant pour moi"),
            (4, "A ce qu'il paraît c’est le plein emploi, mais pas pour moi"),
            (5, "A part LinkedIn, il n’y a pas de bons outils  pour trouver un job"),
            (6, "Ca n'existe pas de chasseurs d’emploi pour les candidats")]
    answer = "c'était Vrai . . .\njusqu'à la naissance d'edhunt"


class _About:
    name = "alors edhunt, c'est quoi?"

    questions = ["Que fait-il?", "C'est-à-dire?", 'Comment ça marche?']

    default = ["Il gère pour vous",
               "automatiquement",
               "la recherche, la lecture",
               "et le tri des offres d'emploi",
               "en fonction de votre profil",
               "et surtout de votre recherche.",
               "-",
               "Au besoin, il gère aussi",
               "la mise en ligne et la diffusion",
               "de votre CV ou de votre profil et",
               "l'envoi de vos candidatures.", ]

    fait = ["Il gère pour vous",
            "automatiquement",
            "la recherche, la lecture",
            "et le tri des offres d'emploi",
            "en fonction de votre profil",
            "et surtout de votre recherche.",
            "-",
            "Au besoin, il gère aussi",
            "la mise en ligne et la diffusion",
            "de votre CV ou de votre profil et",
            "l'envoi de vos candidatures.", ]

    cad = ["Lire une offre, décider si elle ",
           "est pertinente ou non . . .",
           "la mettre dans un bel outil de",
           "gestion des candidatures,",
           "envoyer le CV . . . ",
           "en gros il fait le boulot à votre place !",
           "-",
           "Ca n'a pas l'air de grand chose",
           "mais c'est facilement 1, 2 voire 3h",
           "de gagnées dans la journée",
           "sans compter le risque de rater une offre"]

    marche = [
        "Vous allez d'abord donner à edhunt quelques",
        "informations vous concernant :",
        "votre profil, vos attentes,",
        "votre niveau de recherche ou d'écoute,",
        "le type de postes que vous souhaitez et ",
        "les plateformes d'emploi qui vous intéressent",
        "-",
        "Ensuite, c'est très simple : chaque jour",
        " edhunt se connecte sur vos plateformes d'emploi",
        "et fait en quelques secondes ce que  vous auriez ",
        "fait en quelques minutes ou en quelques heures.",
    ]

    answer = "comme un chasseur de têtes\nmais à l'envers"


class _JeFais:
    name = "OK mais edhunt il fait quoi?"
    text = ["Il gère pour vous",
            "automatiquement",
            "la recherche, la lecture",
            "et le tri des offres d'emploi",
            "en fonction de votre profil",
            "et surtout de votre recherche.",
            "-",
            "Au besoin, il gère aussi",
            "la mise en ligne et la diffusion",
            "de votre CV ou de votre profil et",
            "l'envoi de vos candidatures.", ]

    answer = "comme un chasseur de têtes\nmais à l'envers\nle Jarvis de l'emploi"


class _CestADire:
    name = "Oui, mais concrètement ca veut dire quoi?"
    text = ["Vous allez d'abord donner à edhunt quelques",
            "informations vous concernant :",
            "votre profil, vos attentes,",
            "votre niveau de recherche ou d'écoute,",
            "le type de postes que vous souhaitez et ",
            "les plateformes d'emploi qui vous intéressent",
            "-",
            "Ensuite, c'est très simple :",
            "chaque jour edhunt se connecte",
            "sur vos plateformes d'emploi",
            "et fait en quelques secondes ce que",
            "vous auriez fait en quelques minutes ou",
            "en quelques heures.",
            "-",
            "Lire une offre, décider si elle ",
            "est pertinente ou non . . .",
            "la mettre dans un bel outil de",
            "gestion des candidatures,",
            "envoyer le CV . . . ",
            "en gros il fait le boulot à votre place !"
            ]
    answer = "Simple et efficace,\n clair et facile, \n mais surtout automatique"


class _EtAlors:
    name = "Et alors?"
    text = ["Ca n'a pas l'air grand chose",
            "mais c'est facilement 1, 2 voire 3h",
            "de gagnées dans la journée",
            "sans compter le risque de rater une offre"]


class _PourResumer:
    name = "Pour résumer : "
    text = ["Si vous êtes en recherche active",
            "on va bien s'entendre",
            "si vous êtes déjà en poste,",
            "en veille ou à l'écoute,",
            "vous allez m'adorer!",
            "On parie?"]


class _CommentCaMarche:
    name = "Mais comment ca marche?"
    text = ["techniquement cela ne marche pas",
            "ca fonctionne",
            "mais pour répondre à la question",
            "jutilise des technologies très avancées",
            "addition",
            "soustraction",
            "multiplication",
            "et parfois même des divisions",
            "pour apprendre a vous connaitre",
            "et à vous comprendre",
            "et croyez moi...",
            "j'apprends très vite!"
            ]


class _Fin:
    name = "C'est donc la fin . . ."
    text = [("si je ne n'ai pas de compte sur les plateformes d'emploi", "edhunt vous en créé un"),
            ("si je n'ai pas de CV", "edhunt vous en créé un"),
            ("si mon CV n'est pas en ligne", "edhunt le met en ligne pour vous"),
            ("si je veux juste un outil pour suivre mes process de recrutement", "edHunt possède un outil spécialement dédié au suivi de vos process"),
            ("si je n'ai pas confiance en edhunt", "edhunt vous montre juste les offres, c'est vous qui lui dites s'il faut candidater ou pas"),
            ("si je n'ai pas le temps de lire les offres", "edhunt candidate pour vous"),
            ("si je n'ai pas envie de répondre à n'importe quelle offre", "edhunt vous laisse sélectionner le score minimal à partir duquel il candidate à une offre"),
            ("si je n'ai pas envie de répondre à n'importe quelle offre", "edhunt vous laisse sélectionner le score minimal à partir duquel il candidate à une offre"),
            ("si je n'ai pas envie de répondre à n'importe quelle offre", "edhunt vous laisse sélectionner le score minimal à partir duquel il candidate à une offre"),
            ("si je n'ai pas envie de répondre à n'importe quelle offre", "edhunt vous laisse sélectionner le score minimal à partir duquel il candidate à une offre"),
            ("si je veux avoir un conseiller, un ' vrai '", "edhunt peux vous accompagner de A-Z, mais ne passe pas les entretiens pour vous"),
            ("si c'était aussi simple ca existerai déjà", "justement, edhunt existe!")
            ]
    answer = "Oui c'est vrai, mais c'est pas plus mal !"


class AproposText:
    page = _Page
    dejadit = _DejaDit
    about = _About
    je = _JeFais
    cest = _CestADire
    et = _EtAlors
    pour = _PourResumer
    comment = _CommentCaMarche
    fin = _Fin
