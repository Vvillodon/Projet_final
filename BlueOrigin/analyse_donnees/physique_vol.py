""" DESCRIPTION FICHIER """

from math import sqrt
from plan_vol import PlanVol

class PhysiqueVol(PlanVol):
    g=9.81
    isp=260
    masse_vide_fusee = 20569 # kg
    masse_pleine_fusee = 75000 # kg
    diametre_fusee = 7 # m
    hauteur_fusee = 15 # m

    def __init__(self,
                 masse_payload : int):
        super().__init__(data)
        self.masse_payload = masse_payload
        self.plan_vol = self.creer_plan_vol()

    def calcul_vitesse_normee(self):

        vitesse


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