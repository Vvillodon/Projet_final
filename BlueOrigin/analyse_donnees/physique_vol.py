""" DESCRIPTION FICHIER """

class PhysiqueVol():
    g=9.81
    isp=0
    masse_vide_fusee=0

    def __init__(self, masse_payload):
        self.masse_payload = masse_payload

    def calcul_vitesse(self):
        pass

    def calcul_masse(self):
        pass

    def calcul_poussee(self):
        pass

    def calcul_altitude(self):
        pass

    def calcul_centre_gravite(self):
        pass

class Trajectoire(PhysiqueVol):

    def __init__(self, masse_payload):
        super().__init__(masse_payload)

    def points_trajectoire(self):
        """traitement des points de trajectoire récupérés dans la base de données"""




class PlanVol():
    def __init__(self):
        pass

class ConeLimie():
    def __init__(self):
        pass

class GoNoGo():
    def __init__(self):
        pass