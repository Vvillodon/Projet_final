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
        coeff_vent = 0.5 * EffetVent.coefficient_trainee * EffetVent.surface_projetee
        coeff_vent = np.array(coeff_vent)
        masse_volumique = np.array(self.masse_volumique)
        profil_vent = np.array(self.profil_vent)
        force_vent = coeff_vent * masse_volumique * np.square(profil_vent)
        return force_vent

    def decalage(self):
        """
        Calcule le décalage dû à l'effet du vent sur la fusée.

        :return: Liste des décalages cumulés.
        """
        force_vent = self.force_vent()
        self.masse = np.array(self.masse)
        decalage = np.divide(0.5 * force_vent, self.masse)
        indice_td = 419  # Indice de référence pour le décalage (par exemple, le temps de décollage)

        # Réinitialisation du décalage après l'indice de référence
        for i in range(indice_td, len(decalage)):
            decalage[i] = 0

        decalage_cumule = [decalage[0]]  # Initialiser le tableau résultant avec le premier élément de l'entrée

        # Calcul du décalage cumulé
        for i in range(1, len(decalage)):
            somme = decalage_cumule[i - 1] + decalage[
                i]  # Calculer la somme de l'élément précédent et de l'élément actuel
            decalage_cumule.append(somme)

        return decalage_cumule
