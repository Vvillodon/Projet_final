import tkinter as tk
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import BlueOrigin


# effet_vent = BlueOrigin.EffetVent()

# donnees_filtrees = BlueOrigin.FiltrageDonnees()
# data = donnees_filtrees.process_data()
# 
# gui = BlueOrigin.Interface(data)
# gui.run()
# BlueOrigin.Affichage(data).plot_trajectory()
# plandevol = BlueOrigin.PlanVol(data).creer_plan_vol()
# BlueOrigin.Affichage(data).affichage_plan_de_vol(plandevol)
# print(BlueOrigin.GoNoGo(data).go_nogo())


def launch_rocket():
    """
    Fonction appelée lors du clic sur le bouton de lancement.
    Récupère les valeurs saisies et effectue une action en conséquence.
    """
    wind_speed = float(wind_speed_entry.get())
    payload_mass = int(payload_entry.get())

    # Faire quelque chose avec les valeurs saisies
    # par exemple, appeler une fonction de votre programme principal
    # qui utilise les valeurs pour prendre une décision de lancement

    # Affiche le résultat dans la fenêtre
    if BlueOrigin.GoNoGo(data).go_nogo():
        result_label.config(text="Décollage autorisé !")
    else:
        result_label.config(text="Décollage non autorisé !")
    altitude = BlueOrigin.PhysiqueVol(payload_mass, data).z_cartesian
    profil_vent, masse_volumique = BlueOrigin.ProfilVent(altitude, wind_speed).calcul_vent()
    vitesse_vent = BlueOrigin.EffetVent(profil_vent, masse_volumique).decalage()
    BlueOrigin.Affichage(data, effet_vent=vitesse_vent).plot_trajectory_interface(ax, canvas)


def run():
    """
    Lance la boucle principale de l'interface utilisateur.
    """
    window.mainloop()


donnees_filtrees = BlueOrigin.FiltrageDonnees()
data = donnees_filtrees.process_data()

window = tk.Tk()
window.title("Programme de lancement de fusée")

# Crée la figure pour l'affichage 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Crée les champs de saisie
wind_speed_label = tk.Label(window, text="Vitesse du vent au sol (m/s):")
wind_speed_label.pack()
wind_speed_entry = tk.Entry(window)
wind_speed_entry.pack()

payload_label = tk.Label(window, text="Charge utile (kg):")
payload_label.pack()
payload_entry = tk.Entry(window)
payload_entry.pack()

# Crée le bouton de lancement
launch_button = tk.Button(window, text="Lancer la fusée", command=launch_rocket)
launch_button.pack()

# Crée le widget Label pour afficher le résultat
result_label = tk.Label(window, text="")
result_label.pack()

# # Crée le bouton pour afficher la trajectoire
# trajectory_button = tk.Button(window, text="Afficher la trajectoire", command=plot_trajectory_interface)
# trajectory_button.pack()

# Affiche la fenêtre 3D
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack()

run()
