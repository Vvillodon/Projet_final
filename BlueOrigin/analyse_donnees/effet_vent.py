
import numpy as np


class EffetVent():
    g = 9.81
    masse_vide_fusee = 20569 # kg
    masse_pleine_fusee = 75000 # kg
    diametre_fusee = 7 # m
    hauteur_fusee = 15 # m
    surface_projetee = hauteur_fusee * diametre_fusee
    coefficient_trainee = 1.17
    
    def __init__(self, profil_vent,masse_volumique):
        self.profil_vent = profil_vent
        self.masse_volumique = masse_volumique

        
    def force_vent(self):
        """
        Calcul la force du vent appliquée sur la surface projetée de la fusée en fonction des vitesses du vent à chaque
        altitude données par profil_vent
        :return:
        """
        force_vent = 0.5 * coefficient_trainee * surface_projetee * self.masse_volumique * self.profil_vent ** 2
        return force_vent
    
    def decalage(self):
        decalage = self.force_vent * masse_pleine_fusee/g
        decalage_cumule = [decalage[0]]  # Initialiser le tableau résultant avec le premier élément de l'entrée

        for i in range(0, len(decalage)):
            somme = decalage_cumule[i-1] + decalage_cumule[i]  # Calculer la somme de l'élément précédent et de l'élément actuel
            decalage_cumule.append(somme)
        return decalage_cumule





altitude=(np.ones(1000))
masse_volumique=(np.ones(1000))
profil_vent=(np.ones(1000))

# force_vent = Effet_vent(profil_vent, masse_volumique).force_vent()

# print (Effet_vent(profil_vent, masse_volumique).decalage(force_vent))
