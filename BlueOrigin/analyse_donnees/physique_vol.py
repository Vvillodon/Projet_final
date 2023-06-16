""" DESCRIPTION FICHIER """

from math import sqrt
from .plan_vol import PlanVol


class PhysiqueVol(PlanVol):
    

    def __init__(self, masse_payload : int):
        PlanVol.__init__(self.data)  # [[t, pos_x, pos_y, pos_z, vx, vy, vz, x_cart, y_cart, z_cart], [ti+1, ...],...]
        self.masse_payload = masse_payload
        self.plan_vol = self.creer_plan_vol()

        self.g = 9.81
        self.isp = 315
        self.masse_vide_fusee = 20569 # kg
        self.masse_pleine_fusee = 75000 # kg
        self.diametre_fusee = 7 # m
        self.hauteur_fusee = 15 # m
        self.plan_vol_final
    def deltaV_burnout(self):
        

        # data_meco = self.plan_vol['MECO'][]
        pass


    def calcul_debit_massique(self):
        pass

    def calcul_poussee(self):
        pass

    

   
    
