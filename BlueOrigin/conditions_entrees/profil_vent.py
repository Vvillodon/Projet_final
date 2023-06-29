import math
import csv
import numpy as np
import matplotlib.pyplot as plt


class ProfilVent:
    def __init__(self, altitude, vitesse_sol, rugosite=4):
        """
        Initialise un objet ProfilVent avec les données fournies.

        :param altitude: Liste des altitudes.
        :param vitesse_sol: Vitesse du vent au niveau du sol.
        :param rugosite: Valeur de la rugosité (par défaut : 4).
        """
        self.altitude = altitude
        self.vitesse_sol = vitesse_sol
        self.rugosite = rugosite

    def calcul_vent(self):
        """
        Calcule le profil du vent en fonction de l'altitude.

        :return: Tuple contenant le profil du vent et le profil de masse volumique.
        """
        z0 = self.rugosite

        V1 = self.vitesse_sol
        h_zero = self.altitude[0]

        # Création du profil de vent retournant une liste de vitesse de vent par altitudes renseignées
        profil_vent = V1 * (np.log(np.divide(self.altitude, z0))) / (np.log(h_zero / z0))

        # Création du profil de la masse volumique retournant une liste de masse volumique par altitudes renseignées
        masse_volumique = []
        for h in self.altitude:
            if h > 85000:
                masse_volumique.append(0.0)  # Masse volumique de la thermosphère en kg/m^3
            elif h > 50000:
                h = h - 50000
                masse_volumique.append(0.0423 * 2.71828 ** (-0.0001 * h))  # Masse volumique de la mésosphère en kg/m^3
            elif h > 12000:
                h = h - 12000
                masse_volumique.append(0.025 * 2.71828 ** (-0.00015 * h))  # Masse volumique de la stratosphère en kg/m^3
            else:
                masse_volumique.append(1.225 * 2.71828 ** (-0.000125 * h))  # Masse volumique de la troposphère en kg/m^3

        plt.figure(figsize=(8, 6))
        plt.plot(profil_vent, self.altitude)
        plt.xlabel("Vitesse du vent (m/s)")
        plt.ylabel("Altitude (m)")
        plt.title("Profil de vent")
        plt.grid(True)
        plt.show()
        return profil_vent, masse_volumique


# Exemple d'utilisation de la classe ProfilVent
# altitude = np.linspace(100, 10000, 1000)
# profil_vent, masse_volumique = ProfilVent(altitude, 5).calcul_vent()
# print(profil_vent)

# altitude = np.linspace(100, 100000, 1000)
# vitesse_sol = 10  # Vitesse du vent au niveau du sol
# rugosite = 0.1  # Rugosité
#
# profil_vent, masse_volumique = ProfilVent(altitude, vitesse_sol, rugosite).calcul_vent()
#
# # Tracer le profil de vent
# plt.figure(figsize=(8, 6))
# plt.plot(profil_vent, altitude)
# plt.xlabel("Vitesse du vent (m/s)")
# plt.ylabel("Altitude (m)")
# plt.title("Profil de vent")
# plt.grid(True)
# plt.show()
#
# # Tracer la masse volumique
# plt.figure(figsize=(8, 6))
# plt.plot(masse_volumique, altitude)
# plt.xlabel("Masse volumique (kg/m^3)")
# plt.ylabel("Altitude (m)")
# plt.title("Profil de masse volumique")
# plt.grid(True)
# plt.show()
