import math
import csv
import numpy as np
import matplotlib.pyplot as plt

class ProfilVent():
    def __init__(self, altitude, vitesse_sol, rugosite):
        self.altitude = altitude
        self.vitesse_sol = vitesse_sol
        self.rugosite = rugosite
    
    def calcul_vent(self):
        """"""
        z0 = self.rugosite
        
        V1 = self.vitesse_sol
        h_zero = self.altitude[0]

        # Création du profil de vent retournant une liste de vitesse de vent par altitudes renseignées
        profil_vent = V1 * (np.log(altitude/z0)) / (np.log(h_zero/z0))

        # Création du profil de la masse volumique retournant une liste de masse volumique par altitudes renseignées
        masse_volumique = []
        for h in self.altitude:
            if h > 85000:
                masse_volumique.append(0.0)  # Masse volumique de la thermosphère en kg/m^3
            elif h > 50000:
                h = h - 50000
                masse_volumique.append(0.0423 * 2.71828 ** (-0.0001 * h))  # Masse volumique de la mésosphère en kg/m^3
            elif h > 12000:
                h = altitude - 12000
                masse_volumique.append(0.025 * 2.71828 ** (-0.00015 * h))  # Masse volumique de la stratosphère en kg/m^3
            else:
                h = altitude
                masse_volumique.append(1.225 * 2.71828 ** (-0.000125 * h))  # Masse volumique de la troposphère en kg/m^3

        return profil_vent, masse_volumique[0]
        
    
# altitude=(np.linspace(100,10000,1000))
# profil_vent, masse_volumique=ProfilVent(altitude).calcul_vent( 10, 0.1)
# print(masse_volumique[0]-masse_volumique[1])



# altitude=(np.linspace(100,100000,1000))
#
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
# print(altitude)
# # print(masse_volumique)
# plt.plot(masse_volumique, altitude)
# plt.xlabel("Masse volumique (kg/m^3)")
# plt.ylabel("Altitude (m)")
# plt.title("Profil de masse volumique")
# plt.grid(True)
# plt.show()
#
# print(ProfilVent(altitude, vitesse_sol, rugosite).calcul_vent())
#
