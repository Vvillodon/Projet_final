""" DESCRIPTION FICHIER """

from math import sqrt
from plan_vol import PlanVol
from Projet_final.BlueOrigin.conditions_entrees.profil_vent import
class PhysiqueVol(PlanVol):
    g=9.81
    isp=260
    masse_vide_fusee = 20569 # kg
    masse_pleine_fusee = 75000 # kg
    diametre_fusee = 7 # m
    hauteur_fusee = 15 # m

    def __init__(self,
                 masse_payload : int):
        PlanVol.__init__(data)  # [[t, pos_x, pos_y, pos_z, vx, vy, vz, x_cart, y_cart, z_cart], [ti+1, ...],...]
        self.masse_payload = masse_payload
        self.plan_vol = self.creer_plan_vol()

    def calcul_vitesse_normee(self):

        liste_vitesses_normees = []
        for ligne in self.data:
            for elt in self.data[ligne]:
                vx = self.data[ligne][4]
                vy = self.data[ligne][4]
                vitesses_normees = sqrt(self.data)


    def deltaV_burnout(self):
        data_meco = self.plan_vol['MECO'][]


    def calcul_debit_massique(self):

        pass



    def calcul_poussee(self):
        pass

    def calcul_altitude(self):
        pass

    def calcul_centre_gravite(self):
        pass