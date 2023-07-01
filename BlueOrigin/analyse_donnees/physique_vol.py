""" DESCRIPTION FICHIER """

from math import sqrt
import numpy as np

#nulllllllllllllllllllllllllll
class PhysiqueVol:
    g = 9.81  # Accélération gravitationnelle (m/s^2)
    isp = 315  # Impulsion spécifique du moteur (s)
    masse_vide_fusee = 20569  # Masse à vide de la fusée (kg)
    masse_pleine_fusee = 75000  # Masse totale de la fusée avec le carburant (kg)
    masse_capsule_vide=1500
    diametre_fusee = 7  # Diamètre de la fusée (m)
    hauteur_fusee = 15  # Hauteur de la fusée (m)

    def __init__(self,
                 masse_payload: int = None,
                 data: list = None,
                 effet_vent: list = None):

        self.masse_payload = masse_payload
        self.data = data
        self.effet_vent = effet_vent

        self.time = [colonne[0] for colonne in self.data]  # Liste des temps d'échantillonnage
        self.vx_ecef = [colonne[4] for colonne in self.data]  # Liste des vitesses selon l'axe x en coordonnées ECEF
        self.vy_ecef = [colonne[5] for colonne in self.data]  # Liste des vitesses selon l'axe y en coordonnées ECEF
        self.vz_ecef = [colonne[6] for colonne in self.data]  # Liste des vitesses selon l'axe z en coordonnées ECEF

        self.x_cartesian = [colonne[7] for colonne in self.data]  # Liste des coordonnées x en coordonnées cartésiennes
        self.y_cartesian = [colonne[8] for colonne in self.data]  # Liste des coordonnées y en coordonnées cartésiennes
        self.z_cartesian = [colonne[9] for colonne in self.data]  # Liste des coordonnées z en coordonnées cartésiennes

    def calcul_valeurs_normees(self):
        """
        Calcule la norme des vitesses vx, vy, vz et la norme des altitudes en coordonnées cartésiennes x_cart, y_cart,
        z_cart pour chaque instant t.
        L'origine du repère cartésien se trouve au pas de tir du lancement de la fusée.

        :return: liste_valeurs_normees : liste de listes contenant chaque temps d'échantillonnage et altitude et vitesse
        normées respectives [[to, ho, vo], [t1, h1, v1],...]
        """
        altitude_normee = []  # Liste pour stocker les altitudes normées
        vitesse_normee = []  # Liste pour stocker les vitesses normées

        for i in range(len(self.x_cartesian)):
            # Calcul de la norme de l'altitude en coordonnées cartésiennes
            altitude_normee.append(
                np.sqrt(self.x_cartesian[i] ** 2 + self.y_cartesian[i] ** 2 + self.z_cartesian[i] ** 2))

            # Calcul de la norme de la vitesse en coordonnées ECEF
            vitesse_normee.append(np.sqrt(self.vx_ecef[i] ** 2 + self.vy_ecef[i] ** 2 + self.vz_ecef[i] ** 2))

        return [altitude_normee, vitesse_normee]  # Retourne les listes d'altitudes et de vitesses normées

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

        altitude_liftoff = self.z_cartesian[0]  # Altitude au liftoff
        index = 2  # Initialisation de l'index pour parcourir les listes des coordonnées

        altitude_normee, vitesse_normee = self.calcul_valeurs_normees()  # Calcul des valeurs normées

        while index <= len(self.time) - 1:
            altitude = self.z_cartesian[index]  # Altitude à l'instant t
            altitude_before = self.z_cartesian[index - 1]  # Altitude à l'instant t-1

            deltaV = vitesse_normee[index] - vitesse_normee[index - 1]  # Variation de vitesse à l'instant t
            deltaV_before = vitesse_normee[index - 1] - vitesse_normee[
                index - 2]  # Variation de vitesse à l'instant t-1

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

        return plan_vol_final  # Retourne le plan de vol final

    def deltaV_burnout(self):
        """
        Calcule la variation de vitesse (deltaV) et le temps de Main Engine Cut-Off (t_MECO) à partir du plan de vol.

        :return: deltaV_ecef_meco : variation de vitesse à MECO en coordonnées ECEF (Earth-Centered, Earth-Fixed)
                 t_MECO : temps de Main Engine Cut-Off
        """
        t_MECO = self.creer_plan_vol().get('Temps écoulé (s)')[2]  # Obtient le temps de MECO à partir du plan de vol
        indice_MECO = self.time.index(t_MECO)  # Obtient l'indice correspondant à MECO dans la liste des temps
        deltaV_ecef_meco = self.calcul_valeurs_normees()[1][indice_MECO]  # Obtient la variation de vitesse à MECO

        return deltaV_ecef_meco, t_MECO

    def calcul_debit_massique(self):
        """
        Calcule le débit massique de carburant.

        :return: debit_massique : débit massique de carburant
        """
        deltaV_ecef_meco, t_MECO = self.deltaV_burnout()  # Obtient la variation de vitesse à MECO et le temps de MECO
        debit_massique = self.masse_pleine_fusee * (
                    1 - np.exp(-(deltaV_ecef_meco / (PhysiqueVol.g * PhysiqueVol.isp)))) / t_MECO
        # Calcule le débit massique en utilisant la masse de la fusée, la variation de vitesse et le temps de MECO

        return debit_massique

    def calcul_poussee(self):
        """
        Calcule la poussée de la fusée.

        :return: poussee : poussée de la fusée
        """
        debit_massique = self.calcul_debit_massique()  # Obtient le débit massique de carburant
        poussee = PhysiqueVol.isp * PhysiqueVol.g * debit_massique  # Calcule la poussée en utilisant l'ISP et l'accélération de la gravité

        return poussee

    def calcul_masse(self):
        """
        Calcule la masse totale de la fusée à chaque instant.

        :return: liste_masse : liste des masses totales de la fusée à chaque instant
        """
        liste_masse = []
        debit_fuel = self.calcul_debit_massique()  # Obtient le débit massique de carburant
        deltaV, t_MECO = self.deltaV_burnout()  # Obtient la variation de vitesse à MECO et le temps de MECO
        for t in self.time:
            if t <= t_MECO:
                masse_totale = PhysiqueVol.masse_pleine_fusee + self.masse_payload - t * debit_fuel
                # Calcule la masse totale de la fusée à chaque instant avant MECO
                liste_masse.append(masse_totale)
            else:
                liste_masse.append(PhysiqueVol.masse_pleine_fusee + self.masse_payload - t_MECO * debit_fuel)
                # Calcule la masse totale de la fusée à chaque instant après MECO
        
        t_apogee = self.creer_plan_vol().get('Temps écoulé (s)')[3]  # Obtient le temps de MECO à partir du plan de vol
        indice_apogee = self.time.index(t_apogee)
        
        for i in range (indice_apogee,len(liste_masse)):
            liste_masse[i]=liste_masse[i]-(self.masse_payload + PhysiqueVol.masse_capsule_vide)
        return liste_masse

        return liste_masse

    def calcul_distance(self):
        return sqrt((self.x_cartesian[0]-self.x_cartesian[-1])**2+(self.y_cartesian[0]-self.y_cartesian[-1])**2)
