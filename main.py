import BlueOrigin

processor = BlueOrigin.DataProcessor()
data = processor.process_data()

BlueOrigin.Affichage(data).plot_trajectory()

print(BlueOrigin.GoNoGo(data).go_nogo())
