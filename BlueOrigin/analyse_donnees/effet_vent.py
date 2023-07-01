"""
Description : Ce fichier contient la classe "EffetVent" qui permet de calculer les effets du vent sur une fusée.

La classe "EffetVent" utilise les paramètres spécifiés tels que le profil du vent, la masse volumique et la masse à chaque altitude pour effectuer les calculs. Les principales méthodes de la classe sont "force_vent" et "decalage".

La méthode "force_vent" calcule la force du vent appliquée sur la surface projetée de la fusée en fonction des vitesses du vent à chaque altitude donnée par le profil du vent. Elle retourne une liste des forces du vent.

La méthode "decalage" calcule le décalage dû à l'effet du vent sur la fusée. Elle utilise la force du vent calculée précédemment et la masse de la fusée à chaque altitude. Elle retourne une liste des décalages cumulés.

Remarques :
- Ce fichier nécessite le module "numpy" pour effectuer les calculs mathématiques.
"""

import numpy as np


class EffetVent:
    g = 9.81
    masse_vide_fusee = 20569  # kg
    masse_pleine_fusee = 75000  # kg
    diametre_fusee = 7  # m
    hauteur_fusee = 15  # m
    surface_projetee = hauteur_fusee * diametre_fusee
    coefficient_trainee = 1.17

    def __init__(self, profil_vent, masse_volumique, masse):
        """
        Initialise un objet EffetVent avec les paramètres spécifiés.
        :param profil_vent: Liste des vitesses du vent à chaque altitude.
        :param masse_volumique: Liste des masses volumiques à chaque altitude.
        :param masse: Liste des masses à chaque altitude.
        """
        self.profil_vent = profil_vent
        self.masse_volumique = masse_volumique
        self.masse = masse

    def force_vent(self):
        """
        Calcule la force du vent appliquée sur la surface projetée de la fusée en fonction des vitesses du vent à chaque
        altitude données par le profil_vent.
        :return: Liste des forces du vent.
        """
        coeff_vent = 0.5 * EffetVent.coefficient_trainee * EffetVent.surface_projetee  # Coefficient de la force du vent
        coeff_vent = np.array(coeff_vent)  # Conversion en un tableau numpy
        masse_volumique = np.array(self.masse_volumique)  # Conversion en un tableau numpy
        profil_vent = np.array(self.profil_vent)  # Conversion en un tableau numpy
        force_vent = coeff_vent * masse_volumique * np.square(profil_vent)  # Calcul de la force du vent
        return force_vent

    def decalage(self):
        """
        Calcule le décalage dû à l'effet du vent sur la fusée.
        :return: Liste des décalages cumulés.
        """
        force_vent = self.force_vent()  # Calcul de la force du vent
        self.masse = np.array(self.masse)  # Conversion en un tableau numpy
        decalage = np.divide(0.5 * force_vent, self.masse)  # Calcul du décalage
        indice_td = 419  # Indice de référence pour le décalage (par exemple, le temps de décollage)

        # Réinitialisation du décalage après l'indice de référence
        for i in range(indice_td, len(decalage)):
            decalage[i] = 0

        decalage_cumule = [decalage[0]]  # Initialiser le tableau résultant avec le premier élément de l'entrée

        # Calcul du décalage cumulé
        for i in range(1, len(decalage)):
            somme = decalage_cumule[i - 1] + decalage[
                i]  # Calcul de la somme de l'élément précédent et de l'élément actuel
            decalage_cumule.append(somme)

        return decalage_cumule

