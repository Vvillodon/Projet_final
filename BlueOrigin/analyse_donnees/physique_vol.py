""" DESCRIPTION FICHIER """

from math import sqrt
from .plan_vol import PlanVol


class PhysiqueVol(PlanVol):
    g = 9.81
    isp = 260
    masse_vide_fusee = 20569 # kg
    masse_pleine_fusee = 75000 # kg
    diametre_fusee = 7 # m
    hauteur_fusee = 15 # m

    def __init__(self,
                 masse_payload : int):
        PlanVol.__init__(data)  # [[t, pos_x, pos_y, pos_z, vx, vy, vz, x_cart, y_cart, z_cart], [ti+1, ...],...]
        self.masse_payload = masse_payload
        self.plan_vol = self.creer_plan_vol()

    def calcul_valeurs_normees(self):
        """
        Calcule la norme des vitesses vx, vy, vz et la norme des altitudes en coordonées cartésiennes x_cart, y_cart,
         z_cart pour chaque instant t.
        L'origine du repère cartésiens se trouve au pas de tir du lancement de la fusée.

        :return: liste_valeurs_normees : liste de listes contenant chaque temps d'échantillonage et altitude et vitesse
        normées respectives [[to, ho, vo], [t1, h1, v1],...]
        """

        liste_valeurs_normees = []
        for ligne in self.data:
            for elt in self.data[ligne]:
                x_cart = self.data[ligne][4]
                y_cart = self.data[ligne][6]
                z_cart = self.data[ligne][5]

                vx = self.data[ligne][4]
                vy = self.data[ligne][6]
                vz = self.data[ligne][5]

                altitude_normee = sqrt(x_cart**2+y_cart**2+z_cart**2)
                vitesse_normee = sqrt(vx**2+vy**2+vz**2)

                liste_valeurs_normees.append([self.data[ligne][0],altitude_normee, vitesse_normee])

        return liste_valeurs_normees

    def deltaV_burnout(self):

        # data_meco = self.plan_vol['MECO'][]
        pass


    def calcul_debit_massique(self):
        pass

    def calcul_poussee(self):
        pass

    def calcul_altitude(self):
        pass

    def calcul_centre_gravite(self):
        pass