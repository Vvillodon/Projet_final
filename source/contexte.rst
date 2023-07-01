Contexte
=============

.. toctree::
   :maxdepth: 2

   blue_origin
   base_donnees
   objectifs


**Lumache** (/lu'make/) is a Python library for cooks and food lovers that
creates recipes mixing random ingredients.  It pulls data from the `Open Food
Facts database <https://world.openfoodfacts.org/>`_ and offers a *simple* and
*intuitive* API.

En se basant sur les données récupérées d’un vol suborbital de la fusée Blue Origin, notre programme repose sur
l’analyse et la modification des valeurs enregistrées décrivant la désorbitation, la descente et l'atterrissage du
véhicule. Notre objectif principal est ici, de créer un programme d’aide à la décision sur le décollage ou non de la
fusée (GO/NO GO) en fonction des conditions météorologique (profile de vent) et de la masse de la charge utile
(touristes). En effet, en tant que compagnie de tourisme spatial, la sécurité du vol est primordial.
Ainsi, notre programme simulera chaque vol en prenant compte du vent et validera le lancement si la trajectoire de la
fusée à chaque instant t n’est pas trop déviée. Sinon, elle reverra un message et interdira le décollage. En dehors du
GO/NO GO, le programme renverra également les données calculées et des graphiques de représentations des trajectoires,
et surtout le nouveau plan de vol (altitude et temps de chaque phase clés du vol).

Notre étude de vol se concentre surtout sur les phases influencées par la vitesse des vents, à savoir :
− Démarrage moteur
− Décollage
− Extinction du moteur principal
− Apogée
Les phases postérieures ne seront pas modifiées par les vitesses du vent, car celles-ci seront contrôlées par
asservissement pour assurer le retour au sol. L’objectif du GO/NO GO est de savoir si lors du déploiement des aérofreins (début du contrôle de la redescente), le lanceur est capable de revenir au pas de tir. Les valeurs des phases définies ci-après, seront tout de même affichée et représentées graphiquement pour la trajectoire :
− Déploiement des aérofreins
− Redémarrage moteur
− Atterrissage