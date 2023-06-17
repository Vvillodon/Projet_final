import matplotlib.pyplot as plt
import numpy as np


class Affichage:
    def __init__(self, data, velocity=None, thrust=None, effet_vent=None):
        """
        Initialise un objet Affichage avec les données fournies.

        :param data: Les données de trajectoire.
        :param velocity: Liste des valeurs de vitesse.
        :param thrust: Liste des valeurs de poussée.
        """
        self.effet_vent = effet_vent
        self.canvas = None
        self.ax = None
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

    # plus utilisé
    # def plot_trajectory(self):
    #     """
    #     Affiche la trajectoire 3D de la fusée.
    #     """
    #     fig = plt.figure()
    #     ax = fig.add_subplot(111, projection='3d')
    #     ax.plot(self.x_cartesian, self.y_cartesian, self.z_cartesian)
    #     ax.set_xlabel('X')
    #     ax.set_ylabel('Y')
    #     ax.set_zlabel('Z')
    #     plt.show()

    def plot_trajectory_interface(self, ax, canvas):
        """
        Affiche la trajectoire 3D de la fusée.
        """
        ax.plot(self.x_cartesian, np.add(self.y_cartesian, self.effet_vent), self.z_cartesian)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        canvas.draw()

    def affichage_plan_de_vol(self, plan_vol_final):
        """
        Affiche le plan de vol de la fusée.
        """
        max_width_event = max(len(event) for event in plan_vol_final['Event'])
        max_width_time = max(len(str(time)) for time in plan_vol_final['Elapsed Time(s)'])
        max_width_altitude = max(len(str(altitude)) for altitude in plan_vol_final['Altitude (m)'])

        # Affichage des en-têtes centrés
        print(
            f"{'Event':^{max_width_event}} {'Elapsed Time(s)':^{max_width_time}} {'Altitude (m)':^{max_width_altitude}}")
        print('-' * (max_width_event + max_width_time + max_width_altitude + 2))

        # Affichage des données centrées
        for event, time, altitude in zip(plan_vol_final['Event'], plan_vol_final['Elapsed Time(s)'],
                                         plan_vol_final['Altitude (m)']):
            print(f"{event:^{max_width_event}} {str(time):^{max_width_time}} {str(altitude):^{max_width_altitude}}")

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
