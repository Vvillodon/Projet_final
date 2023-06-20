import matplotlib.pyplot as plt
import numpy as np

class Affichage:
    def __init__(self, data, rayon_gonogo, velocity=None, thrust=None, effet_vent=None):
        """
        Initialise un objet Affichage avec les données fournies.

        :param data: Les données de trajectoire.
        :param velocity: Liste des valeurs de vitesse.
        :param thrust: Liste des valeurs de poussée.
        """
        self.plan_vol_final = None
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
        self.rayon_gonogo = rayon_gonogo

    def plot_trajectory_interface(self, ax, canvas, rayon_gonogo):
        """
        Affiche la trajectoire 3D de la fusée avec un cercle de gonogo.
        """
        max_range = 1000 + max(max(self.x_cartesian), max(self.y_cartesian), abs(min(self.x_cartesian)),
                               abs(min(self.y_cartesian)))
        # Trouver la valeur maximale entre x et y
        ax.set_xlim([-max_range, 1000])  # Définir les limites de l'axe x avec la valeur maximale
        ax.set_ylim([-2000, 2000])  # Définir les limites de l'axe y avec la valeur maximale

        ax.plot(self.x_cartesian, np.add(self.y_cartesian, self.effet_vent), self.z_cartesian)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('Trajectoire 3D de la fusée')

        # Ajouter un cercle de gonogo
        theta = np.linspace(0, 2 * np.pi, 100)
        x_circle = -3206 + rayon_gonogo * np.cos(theta)
        y_circle = -627 + rayon_gonogo * np.sin(theta)
        z_circle = np.full_like(theta, 6000)  # Altitude du cercle

        ax.plot(x_circle, y_circle, z_circle, 'r--', label='Gonogo Circle')
        # ax.legend()

        canvas.draw()

    def affichage_plan_de_vol(self, plan_vol_final):
        """
        Affiche le plan de vol de la fusée.
        """
        max_width_event = max(len(event) for event in plan_vol_final['Phase'])
        max_width_time = max(len(str(time)) for time in plan_vol_final['Temps écoulé (s)'])
        max_width_altitude = max(len(str(altitude)) for altitude in plan_vol_final['Altitude (m)'])

        # Affichage des en-têtes centrés
        print(
            f"{'Phase':^{max_width_event}} {'Temps écoulé (s)':^{max_width_time}} {'Altitude (m)':^{max_width_altitude}}")
        print('-' * (max_width_event + max_width_time + max_width_altitude + 2))

        # Affichage des données centrées
        for event, time, altitude in zip(plan_vol_final['Phase'], plan_vol_final['Temps écoulé (s)'],
                                         plan_vol_final['Altitude (m)']):
            print(f"{event:^{max_width_event}} {int(time):^{max_width_time}} {int(altitude):^{max_width_altitude}}")

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
