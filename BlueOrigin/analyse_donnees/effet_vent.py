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
        self.profil_vent = profil_vent
        self.masse_volumique = masse_volumique
        self.masse = masse

    def force_vent(self):
        """
        Calcul la force du vent appliquée sur la surface projetée de la fusée en fonction des vitesses du vent à chaque
        altitude données par profil_vent
        :return:
        """
        coeff_vent = 0.5 * EffetVent.coefficient_trainee * EffetVent.surface_projetee
        coeff_vent = np.array(coeff_vent)
        masse_volumique = np.array(self.masse_volumique)
        profil_vent = np.array(self.profil_vent)
        force_vent =coeff_vent * masse_volumique * np.square(profil_vent)
        return force_vent

    def decalage(self):
        force_vent = self.force_vent()
        decalage = np.divide(0.5 *force_vent,self.masse)
        # time_td = self.creer_plan_vol().get('Temps écoulé (s)')[6]
        # indice_td = self.time.index(time_td)
        indice_td = 430
        for i in range(indice_td, len(decalage)):
            decalage[i] = 0
        decalage_cumule = [decalage[0]]  # Initialiser le tableau résultant avec le premier élément de l'entrée

        for i in range(1, len(decalage)):
            somme = decalage_cumule[i - 1] + decalage[
                i]  # Calculer la somme de l'élément précédent et de l'élément actuel
            decalage_cumule.append(somme)
        return decalage_cumule

# altitude = (np.ones(1000))
# masse_volumique = (np.ones(1000))
# profil_vent = (np.ones(1000))
#
# force_vent = EffetVent(profil_vent, masse_volumique).force_vent()
#
# print (EffetVent(profil_vent, masse_volumique).decalage())
