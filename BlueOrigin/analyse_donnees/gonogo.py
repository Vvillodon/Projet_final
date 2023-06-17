import math


class GoNoGo:
    def __init__(self, data):
        """
        Initialise un objet GoNoGo avec les données fournies.

        :param data: Les données de la trajectoire de la fusée.
        """
        self.data = data
        self.time = [colonne[0] for colonne in self.data]
        self.altitude = [colonne[9] for colonne in self.data]
        self.x_cartesian = [colonne[7] for colonne in self.data]
        self.y_cartesian = [colonne[8] for colonne in self.data]
        self.time_limit = 400  # Limite de temps pour le GO/NO GO
        self.altitude_limit = 6184  # Altitude limite pour le GO/NO GO
        self.circle_radius = 100  # Rayon du cercle limite pour le GO/NO GO
        self.x_centre = -3206  # Coordonnée x du centre du cercle limite
        self.y_centre = -627  # Coordonnée y du centre du cercle limite

    def go_nogo(self):
        """
        Vérifie si le GO/NO GO est atteint lors du déploiement des aérofreins.

        :return: "GO" si le GO est atteint, "NO GO" sinon.
        """
        for i in range(len(self.time)):
            if self.altitude_limit - 1000 < self.altitude[i] < self.altitude_limit + 1000 and self.time[
                i] > self.time_limit:
                distance_to_centre = math.sqrt(
                    (self.x_cartesian[i] - self.x_centre) ** 2 + (self.y_cartesian[i] - self.y_centre) ** 2)
                if distance_to_centre > self.circle_radius:
                    return False
                else:
                    return True