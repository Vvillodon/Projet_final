import BlueOrigin

donnees_filtrees = BlueOrigin.FiltrageDonnees()
data = donnees_filtrees.process_data()

gui = BlueOrigin.Interface(data)
gui.run()
# BlueOrigin.Affichage(data).plot_trajectory()
# plandevol = BlueOrigin.PlanVol(data).creer_plan_vol()
# BlueOrigin.Affichage(data).affichage_plan_de_vol(plandevol)
# print(BlueOrigin.GoNoGo(data).go_nogo())
