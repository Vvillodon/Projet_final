import math
import csv


class Profil_vent():
    def __init__(self):
        pass
    
    def calcul_vent(self,altitude_minimal ,altitude_maximal,vitesse_sol, rugosite):
        """
        

        Parameters
        ----------
        altitude_minimal : TYPE
            DESCRIPTION.
        altitude_maximal : TYPE
            DESCRIPTION.
        vitesse_sol : TYPE
            DESCRIPTION.
        rugosite : TYPE
            DESCRIPTION.

        Returns
        -------
        result : TYPE
            DESCRIPTION.

        """
        z0 = rugosite
        h1 = altitude_minimal
        h2 = altitude_maximal
        V1 = vitesse_sol

        result = {}

        for altitude in range(h1, h2 + 1):
            vitesse_vent = V1 * (math.log(altitude/z0)) / (math.log(h1/z0))
            result[altitude] = vitesse_vent
            
        return result
        
    


print(Profil_vent().calcul_vent(100, 2000, 10, 0.1))