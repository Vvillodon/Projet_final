Base de données
================

Afin de réaliser une étude réaliste, nous avons récupéré les données brutes enregistrées par les capteurs de la fusée
Blue Origin. Ces valeurs sont rentrées principalement dans le fichier .csv défini ci-dessous :

- truth.csv : contient les données de positions et de vélocité du véhicule. Les positions sont exprimées en [m] dans le
référentiel terrestre centré sur la Terre et les vitesses en [m/s] .

Un trie des données devra être effectué par notre algorithme Python.
Les données récupérées proviennent des banques de données libres de la NASA (https://techport.nasa.gov/view/116144 ).
Nous utiliserons une base de données de profils de vent pour différentes altitudes, afin de perturber la trajectoire du
lanceur. Cette base de données est créée par nos soins dans le package conditions_entrees détaillé plus tard.

<https://techport.nasa.gov/view/116144?fbclid=IwAR1C1g9ue-6Q-pUHyxb45yE6VOPpWl2Yi1jHuWZxrmFZ4wKXlNqutcjHKQ0>

.. image:: _static/mission.png

.. image:: _static/site_lancement.png