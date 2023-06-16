import numpy as np


class PlanVol:

    def __init__(self, data: list):
        self.data = data
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

        return altitude_normee, vitesse_normee

    def creer_plan_vol(self):

        tp_ignition = 0
        tp_liftoff = 0
        tp_MECO = 0
        tp_apogee = 0
        tp_deploy_brakes = 0
        tp_restart_ignition = 0
        tp_touchdown = 0

        altitude_liftoff = self.data[1][9]
        i = 2

        altitude_normee, vitesse_normee = self.calcul_valeurs_normees()

        while i <= len(self.time) - 1:

            altitude = self.z_cartesian[i]
            altitude_before = self.z_cartesian[i-1]

            deltaV = vitesse_normee[i] - vitesse_normee[i - 1]
            deltaV_before = vitesse_normee[i - 1] - vitesse_normee[i - 2]

            if tp_liftoff == 0 and altitude - altitude_liftoff >= 1:
                tp_liftoff = self.time[i]

            elif tp_liftoff != 0 and tp_MECO == 0 and -9.81 < deltaV < -9.5:
                tp_MECO = self.time[i]

            elif tp_MECO != 0 and tp_apogee == 0 and altitude - altitude_before <= 0:
                tp_apogee = self.time[i]

            elif tp_apogee != 0 and tp_deploy_brakes == 0 and deltaV - deltaV_before <= 0 and -20 < deltaV < 0 and altitude < 10000:
                tp_deploy_brakes = self.time[i]

            elif tp_deploy_brakes != 0 and tp_restart_ignition == 0 and deltaV - deltaV_before > 0 and deltaV > 0:
                tp_restart_ignition = self.time[i]

            elif tp_restart_ignition != 0 and tp_touchdown == 0 and altitude - altitude_liftoff <= -12:
                tp_touchdown = self.time[i]

            i += 1

        plan_vol_final = {'ignition': tp_ignition, 'liftof': tp_liftoff, 'MECO': tp_MECO, 'apogee': tp_apogee,
                          'deploy_brake': tp_deploy_brakes, 'restart ignition': tp_restart_ignition,
                          'touch down': tp_touchdown}
        print(plan_vol_final)

        return plan_vol_final
