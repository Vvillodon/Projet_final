import tkinter as tk
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import BlueOrigin


class Interface:
    """
    Interface utilisateur pour le programme de lancement de fusée.
    """

    def __init__(self, data):
        """
        Initialise l'interface utilisateur et crée les éléments graphiques.
        """
        self.data = data
        self.window = tk.Tk()
        self.window.title("Programme de lancement de fusée")

        # Crée la figure pour l'affichage 3D
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')

        # Crée les champs de saisie
        wind_speed_label = tk.Label(self.window, text="Vitesse du vent au sol (m/s):")
        wind_speed_label.pack()
        self.wind_speed_entry = tk.Entry(self.window)
        self.wind_speed_entry.pack()

        payload_label = tk.Label(self.window, text="Charge utile (kg):")
        payload_label.pack()
        self.payload_entry = tk.Entry(self.window)
        self.payload_entry.pack()
        
        Rayon_gonogo_label = tk.Label(self.window, text="Rayon Go/NoGo:")
        Rayon_gonogo_label.pack()
        self.Rayon_gonogo_entry = tk.Entry(self.window)
        self.Rayon_gonogo_entry.pack()

        # Crée le bouton de lancement
        launch_button = tk.Button(self.window, text="Lancer la fusée", command=self.launch_rocket)
        launch_button.pack()

        # Crée le widget Label pour afficher le résultat
        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()

        # # Crée le bouton pour afficher la trajectoire
        # trajectory_button = tk.Button(self.window, text="Afficher la trajectoire", command=self.plot_trajectory_interface)
        # trajectory_button.pack()

        # Affiche la fenêtre 3D
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

    def launch_rocket(self):
        """
        Fonction appelée lors du clic sur le bouton de lancement.
        Récupère les valeurs saisies et effectue une action en conséquence.
        """
        wind_speed = float(self.wind_speed_entry.get())
        payload_mass = float(self.payload_entry.get())

        # Affiche le résultat dans la fenêtre
        if BlueOrigin.GoNoGo(self.data).go_nogo():
            self.result_label.config(text="Décollage autorisé !")
        else:
            self.result_label.config(text="Décollage non autorisé !")

        BlueOrigin.Affichage(self.data).plot_trajectory_interface(self.ax, self.canvas)

    def run(self):
        """
        Lance la boucle principale de l'interface utilisateur.
        """
        self.window.mainloop()
