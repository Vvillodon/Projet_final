import BlueOrigin

donnees_filtrees = BlueOrigin.FiltrageDonnees()
data = donnees_filtrees.process_data()

BlueOrigin.Affichage(data).plot_trajectory()

print(BlueOrigin.GoNoGo(data).go_nogo())
