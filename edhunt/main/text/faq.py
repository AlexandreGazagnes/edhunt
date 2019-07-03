class _Page:

    title = "FAQ"
    head = ["FAQ ou ' Foire Aux Questions ' : retrouvez ici les réponses à (presque) toutes vos questions",
            "Si ça n'est pas le cas, direction la page - Contact - "]


class _Oui:
    name = "Oui, mais . . ."
    text = [(1, ("si je ne n'ai pas de compte sur les plateformes d'emploi", "edhunt vous en créé un")),
            (2, ("si je n'ai pas de CV", "edhunt vous en créé un")),
            (3, ("si mon CV n'est pas en ligne", "edhunt le met en ligne pour vous")),

            (4, ("si je veux juste un outil pour suivre mes process de recrutement", "edhunt possède un outil spécialement dédié au suivi de vos process")),
            (5, ("si je n'ai pas confiance en edhunt", "edhunt vous montre juste les offres, c'est vous qui lui dîtes s'il faut candidater ou pas")),
            (6, ("si je n'ai pas le temps de lire les offres", "edhunt candidate pour vous")),

            (7, ("si je n'ai pas envie de répondre à n'importe quelle offre", "choisissez le score minimal à partir duquel il candidate à une offre")),
            (8, ("si je veux avoir un conseiller, un ' vrai '", " les conseillers sont là, mais ne passe pas les entretiens pour vous")),
            (9, ("edhunt me garantit de trouver l'emploi de mes rêves?", "Non, mais il vous aide grandement à ne pas le rater!")),

            (10, ("pas besoin de edhunt pour trouver un job", "c'est vrai, mais avec edhunt c'est plus simple, plus rapide et moins pénible!")),
            (11, ("et mes mots de passe, vous en faîtes quoi", "edhunt ne les stocke pas 'en clair' par soucis de confidentialité")),
            (12, ("si c'est gratuit c'est forcément une arnaque", "parlez en avec nos embassadeurs, il ne sont pas du tout de cet avis")),

            (13, ("ça veut dire quoi le nom 'edhunt'", "un chasseur de têtes en anglais c'est 'head hunter', francisé ça fait 'edhunt' ")),
            (14, ("et pour la lettre de motivation", "deux options soit vous la faîtes, soit edhunt la fait pour vous")),
            (15, ("si c'est gratuit c'est forcément une arnaque", "parlez en avec nos embassadeurs, il ne sont pas du tout de cet avis")), ]


class _Manifeste:

    items = [
        {"question": "C'est presque le plein emploi, alors pourquoi aider les candidats et pas les recruteurs?",
         "réponse": """Le niveau des recrutements attendu pour 2019 atteind un niveau record, il y a donc beaucoup de postes à pourvoir. Pourtant, beaucoup d’entreprises ne trouvent pas les candidats ou n’arrivent pas à recruter… Cette situation est pour le moins paradoxale. On pourrait penser qu’il s’agit d’un problème de compétences, mais cela n’est pas une explication suffisante.

    En effet, dans un marché aussi tendu, les entreprises privilégient les « savoirs être » sur les « savoirs faire ». Elles recherchent des profils adaptables, motivés et qui ont envie d’évoluer, plutôt que des candidats qui répondent à une grille de compétences prédéfinie. La question des « compétences disponibles » sur le marché de l’emploi n’explique donc pas tout.

    Si on ajoute le fait que 2/3 des personnes en poste sont « à l’écoute » ou « en veille » on accentue le paradoxe de cette situation : on a d’un coté beaucoup de postes à pouvoir et de l’autre beaucoup de candidats « potentiels »… Certes, être à l’écoute ca ne veut pas dire « être vraiment prêt à changer de poste » et certes, de nombreuses questions entrent en jeu : rémunération, localisation, périmètre des postes proposés (...). Ce n’est pas parce qu’il y a beaucoup de postes à pourvoir que ces postes vont intéresser les candidats potentiels.

    Une fois dit cela et après avoir émis les réserves nécessaires, reste une question fondamentale : comment dans un marché aussi vaste que celui de l’emploi en France, l’offre d’emploi rencontre aussi peu la demande d’emploi ?

    Pour edhunt, il y a 2 raisons qui peuvent expliquer en partie cette situation, et sur lesquelles il faut apporter des réponses :


    1 – La multiplicité des plateformes d’emploi ne sert ni l’intérêt des candidats, ni celui des recruteurs. En effet, plus de 30 plateformes différentes permettent d’accéder au marché de l’emploi, soit en mettant son CV en ligne, soit en répondant à des offres. Autant d’identifiants, de mots de passe, d’interfaces de connexions différentes. Pour le candidat, à l’écoute ou en veille, ca n’est ni simple, ni agréable, ni rapide.

    2 – A part pôle emploi, dont on connaît bien les limites, personne n’est « du coté des candidats ». Or, et c’est bien là le problème : on manque cruellement de candidats ! Peut-être qu’il faudrait – simplement – aider les candidats, un peu... On trouve de nombreux cabinets de recrutement, de nombreuses SSII… Mais il suffirait d’une plateforme pour vraiment aider les candidats dans leur recherche pour détendre le marché de l’emploi en France, apportant au passage un sucroit de croissance et de dynamisme économique. Songez donc que si on arrivait à aider suffisamment de candidats pour répondre à 2% des postes à pourvoir, on pourrait faire en sorte que tous les habitants d'une ville comme d'Annecy change de poste en 2019 !"""},


        {"question": "Moi, je reçois souvent des appels de chasseurs de têtes, c'est que ca marche non? ",
         "réponse": """Soyons très clair, le recrutement est un business, et c'est d'ailleurs un business très (très) rentable. Le consultant d'un cabinet de recrutement peut facturer entre 10 et 30% du montant de la rémunération brute annuelle d'un candidat. Pour un bon consultant en recrutement, seul, cela peut peser entre 500 000 et 1 million d'euros de factures par an. Le numéro 1 mondial de l'intérim pèse plusieurs dizaines de milliards d'euros de chiffres d'affaires et les plus grosses SSII plusieurs centaines de milliards d’euros. Cela n'est aucunement un mal, mais ce qui est vu par le candidat comme une décision très personnelle, ayant des répercussions directes et très importantes sur son style ou son niveau de vie, sa carrière, son épanouissement, disons le clairement, c'est avant tout un business.

    "Et alors ?" vous direz vous. Et bien, croyez vous que l'agent immobilier qui cherche à vendre ou à louer un bien soit - vraiment - de votre côté? Croyez vous que le vendeur automobile recherche  - vraiment - la voiture qui vous convient ? Sont-ils incentivés sur votre niveau de satisfaction à 1, 3 ou 10 ans ou bien sur le chiffre d'affaires qu'ils réalisent? Le consultant RH, le cabinet de recrutement, pôle emploi ou votre futur manager, ils défendent toujours - aussi - votre intérêt, mais pas que, et entre le leur et le votre, lequel passe en premier?

    Le marché de l’emploi étant en forte demande, vous serez amené à être orienté vers là où les besoins sont, et non là ou vous voudriez aller. Evidement, on vous dira «  chercher le meilleur pour vous », « être vraiment à l’écoute », mais celui qui paie, c’est souvent celui qui décide, et si la personne qui est chargée de vous trouver un poste est payé par son client, c'est à dire l’entreprise, soyons assurés qu’un des deux intérêts en présence passera en premier.


    "C’est le jeu ma pauvre Lucette ?" Oui et Non. Oui, car c’est une réalité actuelle, et une réalité qui fonctionne globalement bien. Non, car elle montre clairement ses limites au regard de la situation de l’emploi en France et  car rien n’oblige candidats et recruteurs à s’enfermer dans un modèle unique, voué à maximiser les intérets des uns au détriment de celui des autres.
    Il est toujours flatteur de se faire « chasser » comme on dit, mais se faire chasser, c’est aussi être à la merci de l'intéret d’un tiers. Or fait étonnant donné le nombre d’annonces actuellement disponibles, ne serait-il pas judicieux d’aider les candidats à choisir parmi les offres disponibles, plutôt que de se laisser porter par les besoins les plus urgents ?

    Être chassé n'est donc plus l'alpha et l'oméga d'une carrière professionnelle, et plutôt que d'être chassé, on pourrait inciter les candidats à "choisir" leur futur emploi parmi une offre florissante qui, d'ailleurs, ne fera que croître dans les mois à venir."""},

        {"question": "Alors, pourquoi c'est si 'pénible' de trouver un job en France?",
         "réponse": """Il existe deux approches différentes mais complémentaires, l’une explique l’autre et réciproquement. La première est à chercher d’un coté politique ou macro-économique, l’autre d’un coté plus pragmatique et plus concret. Pour bien comprendre, il faut aborder la premiere, mais surtout expliquer la seconde.

    Le marché de l’emploi en France est un marché assez rigide et assez inertiel. Le droit français protège le salarié de facon beaucoup plus forte que dans les pays anglo-saxons. Peut-être trop pour certains, peut-être pas assez pour d’autres : là n’est pas la question. La question est que la sécurité et la rigidité du droit du travail a pour conséquence directe un comportement tres attentiste pour les candidats et les entreprises. Les premiers regardent à 2, 3 ou 4 fois avant de vraiment changer de poste et les seconds regardent à 2, 3 ou 4 fois avant de créer un poste. Encore une fois, en dehors de tout jugement de valeur, il convient de constater qu’on ne créé pas un poste ou on ne change pas de poste en France comme en Angleterre, en Irlande, en Suede ou au Danemark. Cette inertie et cette rigidité explique de façon directe ou indirecte la lenteur des process de recrutement, la bonne santé des intermédiaires, le nombre de postes non pourvus, le taux de chômages des jeunes diplomés, la multiplicité des entretiens de recrutements etc. Et de ce point de vue, pour les candidats, et même si on observe une légère accéleration et une légère simplification des process de recurtement, peu de groses évolutions à venir dans les prochains mois.

    Mais le droit, l’économie et le ce bon vieux « marché », cela n’explique pas tout. En effet, d’un coté très pratique, une veille, une écoute ou une recherche d’emploi, ca n’est pas si simple. À l’heure ou même l’administration simplifie, centralise et automatise les démarches, combien de sites d’emploi vous proposent de mettre votre CV en ligne, ou de candidater ? Combien de comptes sur les sites de l'entreprise X ou Y devrez vous créer pour envoyer une candidature ? Combien de mots de passe d’interfaces différents, combien de doublons ou de lignes sur votre tableau excel?

    Comment donc expliquer une telle situation ? Par une raison bien simple et déjà évoquée : il s'agit avant tout d'un business. Et d'ailleurs, d'un business encore plus profitable aux plateformes d'emploi qu’aux cabinets de recrutement ou au autres intermédiaires. De fait, leur utilité est réelle, et l'arrivée et la généralisation du web dans la décennies 2000-2010 en est l'un des facteurs de réussite clé. Mais point de rupture ou d'évolution - réellement - significative concernant l'accès à l'emploi depuis ces 10 dernières années. Aucune ? Sauf à regarder du côté des GAFA et des mastodontes américains qui trusteront demain le marché de l'accès à l'emploi, au détriment des acteurs actuellement en place, et surtout, des candidats.

    À l’écoute, en veille ou en recherche, même combat : il faut faire simple, rapide, efficace et automatiser – en partie ou totalement si besoin – ce qui peut l’être. Car c’est bien la le credo d’edhunt : simplifier le parcours du candidat pour lui redonner les clés de sa recherche ou de sa veille. Une phrase de type « remettre le candidat au centre du process de recrutement » conviendrait parfaitement si elle n’avait pas perdu tout son sens. Du reste, « apporter une solution concrète et efficace à un problème avéré et partagé par beaucoup » est moins catchy, mais tout aussi pleine de sens.

    Attention, edhunt, ne sera jamais en capacité de passer un entretien à votre place, ou de créer un poste spécialement fait pour vous. edhunt aura toujours une limite, mais pour tout ce qui est centralisable, automatisable, simplifiable et faciliatble, il sera là aux avant-postes, au côté et surtout du côté des candidats. """},

        {"question": "Donc tout le monde aurait tort et seul edhunt aurait raison?",
         "réponse": """Comme l’a dit un jour une grande philosophe : « Quand on est tout seul à avoir raison, c’est qu’on a tort ». En effet, il ne faudrait pas voir un modèle global défaillant, et une solution unique à la rescousse de tous les candidats contre le ‘méchant système de l’emploi’.

    Non, car encore une fois, ce modèle fonctionne globalement bien, en tout cas pour ceux qui en profitent réellement. Non, car si une solution comme edhunt a mis si longtemps à se mettre en place, c’est aussi est surtout que construire un modèle en contradiction totale avec les pratiques en vigueur, et souhaitant se mettre au services de ceux qui n’ont pas, ou si peu le pouvoir, c’est tout sauf simple. Non enfin, car malgré l’apport réel de valeur pour les candidats concernés, il n’est pas dit que ce modèle soit pérenne à long ou très long terme.

    Du reste, il faut naviguer entre modestie et ambition. La modestie, c'est celle de rendre un service simple, clair et précis aux candidats, de le faire avec le plus de transparence et d’intégrité, et connaître à chaque instant les limites d’une solution. L’ambition, c'est celle de poposer son service au plus grand nombre, de s’amélioerer encore et toujours, de ne pas fixer de limites à l’étude des possibles, et de rester fidèle à son credo quelque soit l’état de l’art.

    Quand on va là où personne n’est allé, il ne faut s’attendre à rencontrer des personnes connues : en clair, l’avenir est toujours beaucoup incertain pour certains que pour d’autres.

    Il faut toutefois, encore et toujours, se raccrocher à un principe : rendre service aux candidats, rester de leur côté, apporter le service le plus complet et le plus intuitif possible, et le faire pour le plus grand nombre possible, dans les limites des contraintes techniques."""},

        # {"question": "edhunt peut-ils - vraiment - m'aider?",
        #  "réponse": lorem},

        # {"question": "OK, pourquoi pas. Je veux bien qu'on m'aide mais je n'ai certainement pas envie de payer pour ce type service!",
        #  "réponse": lorem},

        # {"question": "D'ailleurs, si c'est gratuit c'est pas une arnaque?",
        #  "réponse": lorem},

        # {"question": "Donner mes mots de passe à edhunt, ce n'est pas dangereux?",
        #  "réponse": lorem},

        # {"question": "Et mes données personnelles?",
        #  "réponse": lorem},

        # {"question": "D'ou est venue l'idée et le concept de edhunt? ",
        #  "réponse": lorem},

        # {"question": "Pouvez-vous me garantir que edhunt ne va pas candidater sur une offre non pertinente?",
        #  "réponse": lorem},
    ]


class FaqText:
    page = _Page
    oui = _Oui
    manifeste = _Manifeste
