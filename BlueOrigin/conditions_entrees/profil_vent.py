import math
import csv
import numpy as np

class Profil_vent():
    def __init__(self):
        pass
    
    def calcul_vent(self,altitude ,vitesse_sol, rugosite):
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
        
        V1 = vitesse_sol
        h_zero=altitude[0]

        result = {}
        profil_vent=V1 * (np.log(altitude/z0)) / (np.log(h_zero/z0))

            
        return profil_vent
        
    
altitude=(np.linspace(100,10000,1000))

print(Profil_vent().calcul_vent(altitude, 10, 0.1))