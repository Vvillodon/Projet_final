import numpy as np
from .physique_vol import PhysiqueVol


class PlanVol(PhysiqueVol):
    def __init__(self, masse_payload: int, data: list):
        """
        Initialise un objet PlanVol avec les données fournies.

        :param masse_payload: La masse du payload de la fusée.
        :param data: Les données de la trajectoire de la fusée.
        """
        super().__init__(masse_payload, data)

        self.time = [colonne[0] for colonne in self.data]
        self.vx_ecef = [colonne[4] for colonne in self.data]
        self.vy_ecef = [colonne[5] for colonne in self.data]
        self.vz_ecef = [colonne[6] for colonne in self.data]

        self.x_cartesian = [colonne[7] for colonne in self.data]
        self.y_cartesian = [colonne[8] for colonne in self.data]
        self.z_cartesian = [colonne[9] for colonne in self.data]

    def creer_plan_vol(self):
        """
        Crée le plan de vol de la fusée en identifiant les différentes phases du vol.

        :return: Un dictionnaire contenant les phases, le temps écoulé et l'altitude correspondante.
        """
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
        index = 2  # Initialisation de l'index pour parcourir les listes des coordonnées

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
        Calcule le deltaV au moment du burnout (MECO).

        :return: La valeur du deltaV au burnout et le temps écoulé jusqu'au burnout.
        """
        t_MECO = self.creer_plan_vol().get('Temps écoulé (s)')[2]
        indice_MECO = self.time.index(t_MECO)
        deltaV_ecef_meco = self.calcul_valeurs_normees()[0]
        # np.sqrt(self.vx_ecef[indice_MECO] ** 2 + self.vy_ecef[indice_MECO] ** 2 + self.vz_ecef[indice_MECO] ** 2)

        return deltaV_ecef_meco, t_MECO
