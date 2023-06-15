import math
import csv
import numpy as np


class ProfilVent():
    def __init__(self, altitude):
        self.altitude = altitude
    
    def calcul_vent(self ,vitesse_sol, rugosite):
        """
        

        Parameters
        ----------
        altitude : array.
        vitesse_sol :  int
        rugosite : float

        Returns
        -------
        profil_vent : TYPE
            DESCRIPTION.

        """
        z0 = rugosite
        
        V1 = vitesse_sol
        h_zero = self.altitude[0]

        result = {}
        profil_vent=V1 * (np.log(altitude/z0)) / (np.log(h_zero/z0))

            
        return profil_vent
        
    
altitude=(np.linspace(100,10000,1000))

#print(ProfilVent(altitude).calcul_vent( 10, 0.1))

pv = ProfilVent(altitude)