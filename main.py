import BlueOrigin

donnees_filtrees = BlueOrigin.FiltrageDonnees()
data = donnees_filtrees.process_data()

# BlueOrigin.Affichage(data).plot_trajectory()
BlueOrigin.PlanVol(data).creer_plan_vol()

print(BlueOrigin.GoNoGo(data).go_nogo())
