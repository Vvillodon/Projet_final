""" DESCRIPTION FICHIER """

from math import sqrt
import numpy as np


class PhysiqueVol:
    g = 9.81
    isp = 315
    masse_vide_fusee = 20569  # kg
    masse_pleine_fusee = 75000  # kg
    diametre_fusee = 7  # m
    hauteur_fusee = 15  # m

    def __init__(self,
                 masse_payload: int,
                 data: list,
                 effet_vent : list = None):
        self.masse_payload = masse_payload
        self.data = data
        self.effet_vent = effet_vent

        self.time = [colonne[0] for colonne in self.data]
        self.vx_ecef = [colonne[4] for colonne in self.data]
        self.vy_ecef = [colonne[5] for colonne in self.data]
        self.vz_ecef = [colonne[6] for colonne in self.data]

        self.x_cartesian = [colonne[7] for colonne in self.data]
        self.y_cartesian = [colonne[8] for colonne in self.data]
        self.z_cartesian = [colonne[9] for colonne in self.data]


    def calcul_valeurs_normees(self):
        """
        Calcule la norme des vitesses vx, vy, vz et la norme des altitudes en coordonées cartésiennes x_cart, y_cart,
        z_cart pour chaque instant t.
        L'origine du repère cartésiens se trouve au pas de tir du lancement de la fusée.

        :return: liste_valeurs_normees : liste de listes contenant chaque temps d'échantillonage et altitude et vitesse
        normées respectives [[to, ho, vo], [t1, h1, v1],...]
        """
        altitude_normee = []
        vitesse_normee = []

        for i in range(len(self.x_cartesian)):
            altitude_normee.append(
                np.sqrt(self.x_cartesian[i] ** 2 + self.y_cartesian[i] ** 2 + self.z_cartesian[i] ** 2))
            vitesse_normee.append(np.sqrt(self.vx_ecef[i] ** 2 + self.vy_ecef[i] ** 2 + self.vz_ecef[i] ** 2))

        return [altitude_normee, vitesse_normee]

    def creer_plan_vol(self):

        tp_ignition = 0
        tp_liftoff = 0
        tp_MECO = 0
        tp_apogee = 0
        tp_deploy_brakes = 0
        tp_restart_ignition = 0
        tp_touchdown = 0
        h_ignition = 0
        h_liftoff = 0
        h_MECO = 0
        h_apogee = 0
        h_deploy_brakes = 0
        h_restart_ignition = 0
        h_touchdown = 0

        altitude_liftoff = self.z_cartesian[0]
        index = 2 # Initialisation de l'index pour parcourir les listes des coordonnées

        altitude_normee, vitesse_normee = self.calcul_valeurs_normees()

        while index <= len(self.time) - 1:

            altitude = self.z_cartesian[index]
            altitude_before = self.z_cartesian[index - 1]

            deltaV = vitesse_normee[index] - vitesse_normee[index - 1]
            deltaV_before = vitesse_normee[index - 1] - vitesse_normee[index - 2]

            if tp_liftoff == 0 and altitude - altitude_liftoff >= 0:
                tp_liftoff = self.time[index]
                h_liftoff = altitude

            elif tp_liftoff != 0 and tp_MECO == 0 and -9.81 < deltaV < -9.5:
                tp_MECO = self.time[index]
                h_MECO = altitude
            elif tp_MECO != 0 and tp_apogee == 0 and altitude - altitude_before <= 0:
                tp_apogee = self.time[index]
                h_apogee = altitude
            elif tp_apogee != 0 and tp_deploy_brakes == 0 and deltaV - deltaV_before <= 0 and -20 < deltaV < 0 and altitude < 10000:
                tp_deploy_brakes = self.time[index]
                h_deploy_brakes = altitude
            elif tp_deploy_brakes != 0 and tp_restart_ignition == 0 and deltaV - deltaV_before > 0 and deltaV > 0:
                tp_restart_ignition = self.time[index]
                h_restart_ignition = altitude
            elif tp_restart_ignition != 0 and tp_touchdown == 0 and altitude - altitude_liftoff <= -12:
                tp_touchdown = self.time[index]
                h_touchdown = altitude
            index += 1

        plan_vol_final = {
            'Phase': ['Ignition', 'Liftoff', 'MECO', 'Apogee', 'Deploy brakes', 'Restart ignition', 'Touchdown'],
            'Temps écoulé (s)': [tp_ignition, tp_liftoff, tp_MECO, tp_apogee, tp_deploy_brakes, tp_restart_ignition,
                                 tp_touchdown],
            'Altitude (m)': [altitude_liftoff, h_liftoff, h_MECO, h_apogee, h_deploy_brakes, h_restart_ignition,
                             h_touchdown]
            }

        return plan_vol_final

    def deltaV_burnout(self):
        """

        :return:
        """
        t_MECO = self.creer_plan_vol().get('Temps écoulé (s)')[2]
        indice_MECO = self.time.index(t_MECO)
        deltaV_ecef_meco = self.calcul_valeurs_normees()[0]

        return (deltaV_ecef_meco, t_MECO)

    def calcul_debit_massique():
        deltaV_ecef_meco = self.deltaV_burnout()[0]
        debit_massique = self.masse_pleine_fusee * (1 - np.exp(-(deltaV_ecef_meco / (g * isp)))) / t_MECO
        return debit_massique

    def calcul_poussee(self):
        debit_massique = self.calcul_debit_massique()
        pousee = isp * g * debit_massique

        return poussee

