import tkinter as tk
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import BlueOrigin


def launch_rocket():
    """
    Fonction appelée lors du clic sur le bouton de lancement.
    Récupère les valeurs saisies et effectue une action en conséquence.
    """
    wind_speed = float(wind_speed_entry.get())  # Récupère la vitesse du vent saisie par l'utilisateur
    payload_mass = int(payload_entry.get())  # Récupère la masse de la charge utile saisie par l'utilisateur
    rayon = float(rayon_gonogo_entry.get())  # Récupère le rayon Go/NoGo saisi par l'utilisateur

    # Calcul de la masse de la fusée en fonction de la charge utile
    masse = BlueOrigin.PhysiqueVol(payload_mass, data).calcul_masse()

    # Calcul de l'altitude de la fusée en fonction de la charge utile
    altitude = BlueOrigin.PhysiqueVol(payload_mass, data).z_cartesian

    # Calcul du profil de vent et de la masse volumique en fonction de l'altitude et de la vitesse du vent
    profil_vent, masse_volumique = BlueOrigin.ProfilVent(altitude, wind_speed).calcul_vent()

    # Calcul de l'effet du vent sur la trajectoire de la fusée
    vitesse_vent = BlueOrigin.EffetVent(profil_vent, masse_volumique, masse).decalage()

    # Traçage de la trajectoire de la fusée avec les effets du vent
    BlueOrigin.Affichage(data, rayon, effet_vent=vitesse_vent).plot_trajectory_interface(ax, canvas, rayon)

    # Calcul des coordonnées x de la trajectoire de la fusée avec les effets du vent
    x = BlueOrigin.Affichage(data, rayon, effet_vent=vitesse_vent).x_cartesian

    # Calcul des coordonnées y de la trajectoire de la fusée avec les effets du vent
    y = np.add(BlueOrigin.Affichage(data, rayon_gonogo=rayon, effet_vent=vitesse_vent).y_cartesian, vitesse_vent)

    # Vérification du statut de Go/NoGo pour le lancement de la fusée
    if BlueOrigin.GoNoGo(data, x, y, altitude, rayon).go_nogo():
        result_label.config(text="Décollage autorisé !")
    else:
        result_label.config(text="Décollage non autorisé !")

    # Création du plan de vol de la fusée
    plandevol = BlueOrigin.PhysiqueVol(data=data).creer_plan_vol()
    distance_atterrissage=BlueOrigin.PhysiqueVol(data=data).calcul_distance()
    distance_label.config(text=("Distance entre le pas de tir et la zone d'atterrissage : "+str(int(distance_atterrissage)) + " m"))
    # Affichage du plan de vol dans l'interface utilisateur
    BlueOrigin.Affichage(data, rayon, effet_vent=vitesse_vent).affichage_plan_de_vol(plandevol)


def run():
    """
    Lance la boucle principale de l'interface utilisateur.
    """
    window.mainloop()


# Filtrage des données de la fusée
donnees_filtrees = BlueOrigin.FiltrageDonnees()
data = donnees_filtrees.process_data()

# Création de la fenêtre principale de l'interface utilisateur
window = tk.Tk()
window.title("Programme de lancement de fusée")

# Crée la figure pour l'affichage 3D de la trajectoire de la fusée
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Crée les champs de saisie pour la vitesse du vent, la charge utile et le rayon Go/NoGo
wind_speed_label = tk.Label(window, text="Vitesse du vent au sol (m/s):")
wind_speed_label.pack()
wind_speed_entry = tk.Entry(window)
wind_speed_entry.pack()

payload_label = tk.Label(window, text="Charge utile (kg):")
payload_label.pack()
payload_entry = tk.Entry(window)
payload_entry.pack()

rayon_gonogo_label = tk.Label(window, text="Rayon Go/NoGo (m):")
rayon_gonogo_label.pack()
rayon_gonogo_entry = tk.Entry(window)
rayon_gonogo_entry.pack()

# Crée le bouton de lancement de la fusée
launch_button = tk.Button(window, text="Lancer la fusée", command=launch_rocket)
launch_button.pack()

# Crée le widget Label pour afficher le résultat du lancement
result_label = tk.Label(window, text="")
result_label.pack()

# Crée le widget Label pour afficher la distance entre le pas de tir et la zone d'atterrissage
distance_label = tk.Label(window, text="")
distance_label.pack()

# Affiche la fenêtre 3D de la trajectoire de la fusée
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack()

# Lance la boucle principale de l'interface utilisateur
run()
