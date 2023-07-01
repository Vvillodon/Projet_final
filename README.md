# Projet_final

Réalisé par Bazetoux Noé, Farina Alice, Sourd de Villodon Victor.

Le projet final « Blue Origin » s’inscrit dans le cours MGA802 (Etude de cas en aéronautique) de l’ETS. Le but principal de ce projet est de manipuler des bases de données et de les traiter afin de réaliser des modifications de données en utilisant principalement la Programmation Orientée Objet.

## Description du projet

Le projet est divisé en plusieurs parties :

Filtrage des données de la fusée à partir du module BlueOrigin.
Création de l'interface utilisateur avec tkinter.
Calcul des paramètres physiques de la fusée en fonction des valeurs saisies par l'utilisateur.
Affichage de la trajectoire 3D de la fusée avec les effets du vent.
Vérification du statut Go/NoGo pour le lancement de la fusée.
Création et affichage du plan de vol de la fusée.

Le projet est organisé comme suit :

- main.py : Fichier principal contenant le code de l'interface utilisateur et la logique de lancement de la fusée. Il utilise les modules tkinter et matplotlib pour créer l'interface utilisateur et afficher les graphiques de la trajectoire de la fusée.
- BlueOrigin.py : Module contenant les différentes classes et fonctions nécessaires pour le calcul et l'affichage de la trajectoire de la fusée.
- Data : Dossier contenant les données de trajectoire au format CSV.

## Configuration des Chemins de Fichiers

Les chemins de fichiers utilisés par le projet sont configurés comme suit dans le fichier globs.py:

- CURRENT_USER : Nom de l'utilisateur actuel.
- CURRENT_PATH : Chemin absolu du répertoire courant.
- OUTPUT_FOLDER_PATH_DEFAULT : Chemin du dossier de sortie par défaut pour les fichiers générés.
- CVS_FILENAME_DEFAULT : Nom du fichier CSV contenant les données de trajectoire.
- CVS_FILTERED_FILENAME_DEFAULT : Nom du fichier CSV filtré contenant les données de trajectoire filtrées.
- FINAL_CVS_FILTERED_FILENAME_DEFAULT : Nom du fichier CSV final contenant les données de trajectoire filtrées.
- CSV_PROFIL_VENT : Nom du fichier CSV contenant le profil de vent.
- CSV_PATH_DEFAULT : Chemin complet du fichier CSV contenant les données de trajectoire.
- CSV_FILTERED_PATH_DEFAULT : Chemin complet du fichier CSV filtré contenant les données de trajectoire filtrées.
- FINAL_CSV_FILTERED_PATH_DEFAULT : Chemin complet du fichier CSV final contenant les données de trajectoire filtrées.
- CSV_PATH_PROFIL_VENT : Chemin complet du fichier CSV contenant le profil de vent.

## Configuration et Utilisation

Pour utiliser le projet final « Blue Origin », suivez les étapes ci-dessous :

1. Assurez-vous d'avoir les prérequis logiciels nécessaires installés sur votre système.
2. Assurez-vous d'avoir installé les dépendances requises
3. Exécutez le main.py pour lancer l'interface utilisateur
4. Dans l'interface utilisateur, saisissez les valeurs de la vitesse du vent au sol, de la charge utile et du rayon Go/NoGo.
5. Cliquez sur le bouton "Lancer la fusée" pour effectuer la simulation.

La trajectoire 3D de la fusée avec les effets du vent sera affichée, ainsi que le statut du décollage (autorisé ou non) et le plan de vol de la fusée. On peut réitérer l'étape 4 autant de fois qu'on veut.

## Dépendances

Le projet dépend des modules suivants :

- tkinter : Module de la bibliothèque standard Python utilisé pour créer l'interface utilisateur.
- matplotlib : Bibliothèque de visualisation de données utilisée pour afficher les graphiques de la trajectoire de la fusée.
- Assurez-vous d'installer ces dépendances avant d'exécuter le projet.
- csv : Module de la bibliothèque standard Python utilisé pour lire les données de trajectoire à partir d'un fichier CSV.
- math : Module de la bibliothèque standard Python utilisé pour effectuer des calculs mathématiques.
- numpy : Bibliothèque pour le calcul numérique en Python.

# Pretraitement

Le package `pretraitement` contient des classes utilisées pour effectuer le prétraitement des données provenant du site https://techport.nasa.gov/view/116144.

## Classe `ConversionTemps`

La classe `ConversionTemps` est responsable de la conversion des valeurs de temps et du filtrage des données.

### Méthodes

- `read_csv_file()`: Lit un fichier CSV et retourne les données sous forme de liste de dictionnaires.
- `write_csv_file(filename, data, fieldnames)`: Écrit les données dans un fichier CSV.
- `convert_nanoseconds_to_seconds()`: Convertit les valeurs de temps de nanosecondes en secondes dans les données et supprime les données antérieures à un certain temps de référence.
- `filter_data_by_sampling_rate(sampling_rate)`: Filtre les données en fonction d'un taux d'échantillonnage.
- `process_data(sampling_rate=1)`: Effectue le traitement des données, y compris la conversion et le filtrage, puis écrit les données traitées dans un nouveau fichier CSV.

## Classe `FiltrageDonnees`

La classe `FiltrageDonnees` est utilisée pour filtrer et convertir les données géographiques.

### Méthodes

- `read_csv_file()`: Lit un fichier CSV et retourne les données sous forme de liste de dictionnaires.
- `write_csv_file(filename, data, fieldnames)`: Écrit les données dans un fichier CSV.
- `convert_ecef_to_cartesian()`: Convertit les positions du repère ECEF (Earth-Centered, Earth-Fixed) en coordonnées cartésiennes sur Terre.
- `filter_and_rename_columns()`: Filtre les colonnes des données et les renomme.
- `process_data()`: Effectue le traitement des données, y compris le filtrage, la conversion ECEF vers LLA (Latitude, Longitude, Altitude) et le renommage des colonnes. Les données traitées sont ensuite écrites dans un nouveau fichier CSV.

# analyse_donnees

Le package `analyse_donnees` contient des classes pour l'analyse des données de vol d'une fusée.

## Classe `EffetVent`

La classe `EffetVent` permet de calculer l'effet du vent sur une fusée en fonction des données de profil de vent, de masse volumique et de masse à chaque altitude.

### Méthodes

- `force_vent()` : Calcule la force du vent appliquée sur la surface projetée de la fusée en fonction des vitesses du vent à chaque altitude données par le profil_vent.
- `decalage()` : Calcule le décalage dû à l'effet du vent sur la fusée.

#### Attributs

- profil_vent : Liste des vitesses du vent à chaque altitude.
- masse_volumique : Liste des masses volumiques à chaque altitude.
- masse : Liste des masses à chaque altitude.

## Classe `GoNoGo`

La classe `GoNoGo` permet de vérifier si une fusée peut atterrir au bon endroit lors du déploiement des aérofreins en fonction des données de trajectoire fournies.

### Méthodes

- `go_nogo()` : Vérifie si la fusée peut atterrir au bon endroit lors du déploiement des aérofreins. Renvoie True si le GO est atteint, False sinon.

#### Attributs

- data : Les données de la trajectoire de la fusée.
- time : Liste des valeurs de temps.
- altitude : Liste des valeurs de coordonnée Z.
- x_cartesian : Liste des valeurs de coordonnée X.
- y_cartesian : Liste des valeurs de coordonnée Y.
- time_limit : Limite de temps pour le GO/NO GO.
- altitude_limit : Altitude limite pour le GO/NO GO.
- circle_radius : Rayon du cercle limite pour le GO/NO GO.
- x_centre : Coordonnée X du centre du cercle limite.
- y_centre : Coordonnée Y du centre du cercle limite.

## Classe `Physique_vol`

Cette classe fournit des méthodes pour calculer différentes grandeurs physiques telles que la variation de vitesse, le débit massique de carburant, la poussée, la masse totale de la fusée, etc.

### Méthodes

- `calcul_valeurs_normees()` : Calcule la norme des vitesses vx, vy, vz et la norme des altitudes en coordonnées cartésiennes x_cart, y_cart, z_cart pour chaque instant t.
- `creer_plan_vol()` : Création du plan de vol de la fusée et déterminations des différentes phases du vol.
- `deltaV_burnout()` : Calcule la variation de vitesse (deltaV) et le temps de Main Engine Cut-Off (t_MECO) à partir du plan de vol.
- `calcul_debit_massique()` : Calcule le débit massique de carburant.
- `calcul_poussee()` : Calcule la poussée de la fusée.
- `calcul_masse()` : Calcule la masse totale de la fusée à chaque instant.
- `calcul_distance()` : Calcule la distance parcourue par la fusée.

#### Attributs

- `g` : Accélération gravitationnelle (m/s^2)
- `isp` : Impulsion spécifique du moteur (s)
- `masse_vide_fusee` : Masse à vide de la fusée (kg)
- `masse_pleine_fusee` : Masse totale de la fusée avec le carburant (kg)
- `diametre_fusee` : Diamètre de la fusée (m)
- `hauteur_fusee` : Hauteur de la fusée (m)
- `masse_payload` : Masse de la charge utile de la fusée
- `data` : Données de trajectoire de la fusée
- `effet_vent` : Effet du vent sur la fusée
- `time` : Liste des temps d'échantillonnage
- `vx_ecef` : Liste des vitesses selon l'axe x en coordonnées ECEF
- `vy_ecef` : Liste des vitesses selon l'axe y en coordonnées ECEF
- `vz_ecef` : Liste des vitesses selon l'axe z en coordonnées ECEF
- `x_cartesian` : Liste des coordonnées x en coordonnées cartésiennes
- `y_cartesian` : Liste des coordonnées y en coordonnées cartésiennes
- `z_cartesian` : Liste des coordonnées z en coordonnées cartésiennes

# conditions_entrees

Le package `conditions_entrees` contient des classes pour calculer le profil du vent en fonction de l'altitude.

## Classe `ProfilVent`

### Méthodes

- `__init__(self, altitude, vitesse_sol, rugosite=4)` : Initialise un objet `ProfilVent` avec les données altitude, vitesse_sol et rugosite.
- `calcul_vent(self)` : Calcule le profil du vent en fonction de l'altitude. Retourne un tuple contenant le profil du vent et le profil de masse volumique.

#### Attributs

- `altitude` : Liste des altitudes (m).
- `vitesse_sol` : Vitesse du vent au niveau du sol (m/s).
- `rugosite` : Valeur de la rugosité (par défaut : 4).

# affichage_resultats

Le package `affichage_resultats` contient la classe `Affichage` qui permet d'afficher des graphiques et des trajectoires de fusée.

## Classe `Affichage`

Le fichier `Affichage.py` contient la définition de la classe `Affichage`. Cette classe permet d'afficher la trajectoire 3D d'une fusée, ainsi que des graphiques de vitesse, altitude et poussée en fonction du temps.

### Méthodes

- `__init__(self, data, rayon_gonogo, velocity=None, thrust=None, effet_vent=None)` : Initialise un objet `Affichage` avec les données data, rayon_gonogo, velocity, thrustet effet_vent.
- `plot_trajectory_interface(self, ax, canvas, rayon_gonogo)` :,Affiche la trajectoire 3D de la fusée avec un cercle de gonogo.
          - `ax` : Objet Axes3D de `matplotlib` pour le tracé en 3D.
          - `canvas` : Objet `FigureCanvasTkAgg` de `matplotlib` pour l'affichage dans une interface graphique.
          - `rayon_gonogo` : Rayon du cercle de gonogo.
- `affichage_plan_de_vol(self, plan_vol_final)` : Affiche le plan de vol de la fusée.
- `plan_vol_final` : Dictionnaire contenant les phases, temps écoulés et altitudes du plan de vol.
- `affichage_physique(self)` : Affiche les graphiques de vitesse, altitude et poussée en fonction du temps.

#### Attributs

- `data` : Les données de trajectoire.
- `rayon_gonogo` : Rayon du cercle de gonogo.
- `velocity` : Liste des valeurs de vitesse (facultatif).
- `thrust` : Liste des valeurs de poussée (facultatif).
- `effet_vent` : Effet du vent sur la trajectoire (facultatif).

# Exemple d'utilisation

## Installation des dépendances

Avant de pouvoir exécuter le programme, vous devez installer les dépendances requises. Assurez-vous d'avoir Python installé sur votre système. Ensuite, exécutez la commande suivante pour installer les dépendances :

pip install tkinter matplotlib numpy csv math

## Exécution du programme

1. Exécutez le fichier `main.py` pour lancer le programme.
2. Une interface utilisateur s'ouvrira. Vous pouvez saisir les paramètres de la fusée tels que la vitesse du vent, la charge utile et le rayon Go/NoGo.
3. Cliquez sur le bouton "Lancer la fusée" pour afficher la trajectoire de la fusée et obtenir le statut de Go/NoGo.
4. Le programme affichera également le plan de vol de la fusée et la distance entre le pas de tir et la zone d'atterrissage.
   
   ![image](https://github.com/Vvillodon/Projet_final/assets/133155488/16125825-85c7-4996-a23c-9707dd62fb3b)

6. Vous pouvez fermer l'application en cliquant sur la croix en haut à droite de la fenêtre.

C'est tout! Vous pouvez maintenant utiliser ce programme de lancement de fusée pour simuler et visualiser différentes trajectoires en fonction des paramètres que vous avez saisis.
