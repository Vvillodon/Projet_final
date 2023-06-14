""" DESCRIPTION FICHIER """

from plan_vol import PlanVol

class PhysiqueVol(PlanVol):
    g=9.81
    isp=260
    masse_vide_fusee = 20569 # kg
    masse_pleine_fusee = 75000 # kg
    diametre_fusee = 7 # m
    hauteur_fusee = 15 # m

    def __init__(self,
                 masse_payload : int,
                 data : list):
        self.masse_payload = masse_payload
        self.date = data  # [[ti, Xi, Yi, Zi, Vxi, Vyi, Vzi], [i+1], ...]

    def deltaV_burnout(self):
        self.deltaV_burnout = self.

    def calcul_debit_massique(self):

        pass

    def calcul_vitesse(self):
        pass

    def calcul_poussee(self):
        pass

    def calcul_altitude(self):
        pass

    def calcul_centre_gravite(self):
        pass