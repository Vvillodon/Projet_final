"""
Description : Ce fichier contient la classe "Affichage" qui permet d'afficher les données de trajectoire et les graphiques associés.

La classe "Affichage" prend en compte les données de trajectoire ainsi que des paramètres optionnels tels que la vitesse et la poussée. Les principales méthodes de la classe sont "plot_trajectory_interface" et "affichage_physique".

La méthode "plot_trajectory_interface" affiche la trajectoire 3D de la fusée avec un cercle de gonogo. Elle utilise un objet Axes3D et un objet Canvas pour l'affichage, ainsi que le rayon du cercle Go/NoGo.

La méthode "affichage_physique" affiche les graphiques de vitesse, altitude et poussée en fonction du temps.

Remarques :
- Ce fichier nécessite le module "matplotlib.pyplot" pour l'affichage des graphiques.
- Les graphiques sont affichés séparément à l'aide de la méthode "show" de pyplot.
"""

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
        :param ax: Objet Axes3D pour afficher la trajectoire.
        :param canvas: Objet Canvas pour mettre à jour l'affichage.
        :param rayon_gonogo: Rayon du cercle Go/NoGo.
        """
        # Calcul de la valeur maximale entre les coordonnées x et y de la trajectoire
        max_range = 1000 + max(max(self.x_cartesian), max(self.y_cartesian), abs(min(self.x_cartesian)),
                               abs(min(self.y_cartesian)))
        ax.set_xlim([-max_range, 1000])  # Définition des limites de l'axe x
        ax.set_ylim([-2000, 2000])  # Définition des limites de l'axe y

        # Traçage de la trajectoire 3D de la fusée en utilisant les coordonnées x, y et z
        ax.plot(self.x_cartesian, np.add(self.y_cartesian, self.effet_vent), self.z_cartesian)
        ax.set_xlabel('X')  # Label de l'axe x
        ax.set_ylabel('Y')  # Label de l'axe y
        ax.set_zlabel('Z')  # Label de l'axe z
        ax.set_title('Trajectoire 3D de la fusée')  # Titre du graphique

        # Calcul des coordonnées du cercle de gonogo
        theta = np.linspace(0, 2 * np.pi, 100)  # Points angulaires pour le cercle
        x_circle = -3206 + rayon_gonogo * np.cos(theta)  # Coordonnées x du cercle
        y_circle = -627 + rayon_gonogo * np.sin(theta)  # Coordonnées y du cercle
        z_circle = np.full_like(theta, 6000)  # Coordonnées z du cercle (constantes)

        ax.plot(x_circle, y_circle, z_circle, 'r--', label='Gonogo Circle')  # Traçage du cercle de gonogo

        canvas.draw()  # Mise à jour de l'affichage

    def affichage_plan_de_vol(self, plan_vol_final):
        """
        Affiche le plan de vol de la fusée.
        :param plan_vol_final: Dictionnaire contenant les données du plan de vol.
        """
        # Calcul des largeurs maximales des colonnes pour l'affichage aligné
        max_width_event = max(
            len(event) for event in plan_vol_final['Phase'])  # Longueur maximale de la colonne 'Phase'
        max_width_time = max(len(str(time)) for time in
                             plan_vol_final['Temps écoulé (s)'])  # Longueur maximale de la colonne 'Temps écoulé (s)'
        max_width_altitude = max(len(str(altitude)) for altitude in
                                 plan_vol_final['Altitude (m)'])  # Longueur maximale de la colonne 'Altitude (m)'

        # Affichage des en-têtes centrés
        print(
            f"{'Phase':^{max_width_event}} {'Temps écoulé (s)':^{max_width_time}} {'Altitude (m)':^{max_width_altitude}}")
        print('-' * (max_width_event + max_width_time + max_width_altitude + 2))  # Ligne de séparation

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
