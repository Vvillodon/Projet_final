""" DESCRIPTION FICHIER """

from math import sqrt
from .plan_vol import PlanVol
import numpy as np


class PhysiqueVol(PlanVol):

    def __init__(self, masse_payload: int, data: list):
        PlanVol.__init__(self.data)  # [[t, pos_x, pos_y, pos_z, vx, vy, vz, x_cart, y_cart, z_cart], [ti+1, ...],...]
        self.masse_payload = masse_payload
        self.plan_vol = self.creer_plan_vol()

        self.g = 9.81
        self.isp = 315
        self.masse_vide_fusee = 20569  # kg
        self.masse_pleine_fusee = 75000  # kg
        self.diametre_fusee = 7  # m
        self.hauteur_fusee = 15  # m
        # self.plan_vol_final=PlanVol.creer_plan_vol()
        self.plan_vol_final = {
            'Event': ['Ignition', 'Liftoff', 'MECO', 'Apogee', 'Deploy brakes', 'Restart ignition', 'Touchdown'],
            'Elapsed Time(s)': [0, 8.000040292739868, 145.00068020820618, 248.00118017196655, 407.0019702911377,
                                427.00207018852234, 448.002170085907],
            'Altitude (m)': [1118.743806391023, 1119.3699683938175, 57774.66587874014, 106740.76328460686,
                             5968.729973513633, 1907.2613385310397, 1106.0021588746458]}
        self.data = data

    def deltaV_burnout(self):
        t_MECO = self.plan_vol_final.get('Elapsed Time(s)')[2]
        indice_MECO = self.time.index(t_MECO)
        deltaV_ecef_meco = np.sqrt(
            self.x_cartesian[indice_MECO] ** 2 + self.y_cartesian[indice_MECO] ** 2 + self.z_cartesian[
                indice_MECO] ** 2)

        return deltaV_ecef_meco, t_MECO

    def calcul_debit_massique(self, deltaV_ecef_meco, t_MECO):
        debit_massique = self.masse_pleine_fusee * (1 - np.exp(-(deltaV_ecef_meco / (self.g * self.isp)))) / t_MECO
        return debit_massique

    def calcul_poussee(self, debit_massique):
        thrust = self.isp * self.g * debit_massique
        return thrust
