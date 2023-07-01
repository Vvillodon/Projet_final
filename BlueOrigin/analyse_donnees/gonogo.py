"""
Description : Ce fichier contient la classe "GoNoGo" qui permet de vérifier si une fusée peut atterrir au bon endroit lors du déploiement des aérofreins.

La classe "GoNoGo" prend en compte les données de trajectoire de la fusée, les coordonnées cartésiennes (X, Y, Z), et les paramètres de limite (temps, altitude, rayon). Elle effectue une vérification en deux étapes : la vérification de l'altitude de la fusée et du temps écoulé, puis le calcul de la distance entre la position de la fusée et le centre de la zone d'atterrissage.

Si la fusée satisfait les conditions d'altitude et de temps, la classe vérifie si la distance calculée est inférieure ou égale au rayon du cercle limite. Si c'est le cas, la fusée peut atterrir au bon endroit et la méthode "go_nogo" renvoie True. Sinon, la méthode renvoie False.

Remarques :
- Ce fichier nécessite le module "math" pour les calculs mathématiques.
"""


import math


class GoNoGo:
    def __init__(self, data, x_cartesian, y_cartesian, z_cartesian, rayon_gonogo):
        """
        Initialise un objet GoNoGo avec les données fournies.
        :param data: Les données de la trajectoire de la fusée.
        :param x_cartesian: Liste des valeurs de coordonnée X.
        :param y_cartesian: Liste des valeurs de coordonnée Y.
        :param z_cartesian: Liste des valeurs de coordonnée Z.
        :param rayon_gonogo: Rayon du cercle limite pour le GO/NO GO.
        """
        self.data = data
        self.time = [colonne[0] for colonne in self.data]
        self.altitude = z_cartesian
        self.x_cartesian = x_cartesian
        self.y_cartesian = y_cartesian
        self.time_limit = 400  # Limite de temps pour le GO/NO GO
        self.altitude_limit = 6184  # Altitude limite pour le GO/NO GO
        self.circle_radius = rayon_gonogo  # Rayon du cercle limite pour le GO/NO GO
        self.x_centre = -3206  # Coordonnée x du centre du cercle limite
        self.y_centre = -627  # Coordonnée y du centre du cercle limite

    def go_nogo(self):
        """
        Vérifie si la fusée peut atterrir au bon endroit lors du déploiement des aérofreins.
        :return: True si le GO est atteint, False sinon.
        """
        for i in range(len(self.time)):
            # Vérification de deux conditions : altitude de la fusée et temps écoulé
            if self.altitude_limit - 1000 < self.altitude[i] < self.altitude_limit + 1000 and self.time[
                i] > self.time_limit:
                # Calcul de la distance entre la position de la fusée et le centre de la zone d'atterrissage
                distance_to_centre = math.sqrt(
                    (self.x_cartesian[i] - self.x_centre) ** 2 + (self.y_cartesian[i] - self.y_centre) ** 2)
                if distance_to_centre > self.circle_radius:
                    # La distance est supérieure au rayon, la fusée ne peut pas atterrir au bon endroit
                    return False
                else:
                    # La distance est inférieure ou égale au rayon, la fusée peut atterrir au bon endroit
                    return True
