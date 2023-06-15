import BlueOrigin

filename = "C:\\Users\\noeba\\PycharmProjects\\MGA802_Project\\Projet_final\\Data\\truth_filtered.csv"
output_filename = "C:\\Users\\noeba\\PycharmProjects\\MGA802_Project\\Projet_final\\Data\\new_truth_filtered.csv"

processor = BlueOrigin.DataProcessor(filename)
data = processor.process_data(output_filename)

BlueOrigin.Affichage(data).plot_trajectory()
