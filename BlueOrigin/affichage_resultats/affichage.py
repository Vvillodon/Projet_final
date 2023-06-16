import matplotlib.pyplot as plt


class Affichage:
    def __init__(self, data, velocity=None, thrust=None):
        """
        Initialise un objet Affichage avec les données fournies.

        :param data: Les données de trajectoire.
        :param velocity: Liste des valeurs de vitesse.
        :param thrust: Liste des valeurs de poussée.
        """
        if thrust is None:
            thrust = []
        if velocity is None:
            velocity = []
        self.data = data
        self.time = [colonne[0] for colonne in self.data]  # Liste des valeurs de temps
        self.x_cartesian = [colonne[7] for colonne in self.data]  # Liste des valeurs de coordonnée X
        self.y_cartesian = [colonne[8] for colonne in self.data]  # Liste des valeurs de coordonnée Y
        self.z_cartesian = [colonne[9] for colonne in self.data]  # Liste des valeurs de coordonnée Z
        self.velocity = velocity  # Liste des valeurs de vitesse
        self.thrust = thrust  # Liste des valeurs de poussée

    def plot_trajectory(self):
        """
        Affiche la trajectoire 3D de la fusée.
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(self.x_cartesian, self.y_cartesian, self.z_cartesian)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()

    def affichage_plan_de_vol(self):
        """
        Affiche le plan de vol de la fusée.
        """
        pass

    def affichage_physique(self):
        """
        Affiche les graphiques de vitesse, altitude et poussée en fonction du temps.
        """
        # Graphique de la vitesse en fonction du temps
        plt.figure()
        plt.plot(self.time, self.velocity)
        plt.xlabel('Temps')
        plt.ylabel('Vitesse')
        plt.title('Vitesse en fonction du temps')
        plt.grid(True)
        plt.show()

        # Graphique de l'altitude en fonction du temps
        plt.figure()
        plt.plot(self.time, self.z_cartesian)
        plt.xlabel('Temps')
        plt.ylabel('Altitude')
        plt.title('Altitude en fonction du temps')
        plt.grid(True)
        plt.show()

        # Graphique de la poussée en fonction du temps
        plt.figure()
        plt.plot(self.time, self.thrust)
        plt.xlabel('Temps')
        plt.ylabel('Poussée')
        plt.title('Poussée en fonction du temps')
        plt.grid(True)
        plt.show()
