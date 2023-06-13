import math
import csv


class Profil_vent():
    def __init__(self):
        pass
    
    def calcul_vent(self,altitude_minimal ,altitude_maximal,vitesse_sol, rugosite):
        z0 = rugosite
        h1 = altitude_minimal
        h2 = altitude_maximal
        V1 = vitesse_sol

        with open('vitesse_vent.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Altitude (m)', 'Vitesse Vent (m/s)'])

            for altitude in range(h1, h2 + 1):
                vitesse_vent = V1 * (math.log(altitude/z0)) / (math.log(h1/z0))
                writer.writerow([altitude, vitesse_vent])

        print("Le fichier CSV 'vitesse_vent.csv' a été généré avec succès.")
        
    


Profil_vent().calcul_vent(100, 2000, 10, 0.1)