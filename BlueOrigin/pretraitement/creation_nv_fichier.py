import csv
from pyproj import CRS, Transformer

class DataProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.read_csv_file()

    def read_csv_file(self):
        """
        Lit un fichier CSV et retourne les données sous forme de liste de dictionnaires.

        :return: Les données du fichier CSV sous forme de liste de dictionnaires.
        """
        data = []
        with open(self.filename, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
        return data

    def write_csv_file(self, filename, data, fieldnames):
        """
        Écrit les données dans un fichier CSV.

        :param filename: Le nom du fichier CSV de sortie.
        :param data: Les données à écrire dans le fichier CSV.
        :param fieldnames: Les noms de colonnes du fichier CSV.
        """
        with open(filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    def convert_ecef_to_lla(self):
        """
        Convertit les positions du repère ECEF vers le repère LLA (Latitude, Longitude, Altitude).

        """
        transformer = Transformer.from_crs(CRS.from_epsg(4978), CRS.from_epsg(4326))
        for row in self.data:
            pos_X = float(row["pos_X"])
            pos_Y = float(row["pos_Y"])
            pos_Z = float(row["pos_Z"])
            lon, lat, alt = transformer.transform(pos_X, pos_Y, pos_Z)
            row["Latitude"] = lat
            row["Longitude"] = lon
            row["Altitude"] = alt

    def filter_and_rename_columns(self):
        """
        Filtre les colonnes et les renomme dans les données.

        :return: Les données avec les colonnes filtrées et renommées.
        """
        filtered_data = []
        for row in self.data:
            filtered_row = {
                "TIME[S]": row["TIME_NANOSECONDS_TAI "],
                "pos_X": row["truth_pos_CON_ECEF_ECEF_M[1] "],
                "pos_Y": row["truth_pos_CON_ECEF_ECEF_M[2] "],
                "pos_Z": row["truth_pos_CON_ECEF_ECEF_M[3] "],
                "vel_X": row["truth_vel_CON_ECEF_ECEF_MpS[1] "],
                "vel_Y": row["truth_vel_CON_ECEF_ECEF_MpS[2] "],
                "vel_Z": row["truth_vel_CON_ECEF_ECEF_MpS[3] "]
            }
            filtered_data.append(filtered_row)
        self.data = filtered_data

    def process_data(self, output_filename):
        """
        Effectue le traitement des données, y compris le filtrage, la conversion ECEF vers LLA et le renommage des colonnes.
        Écrit les données traitées dans un nouveau fichier CSV.

        :param output_filename: Le nom du fichier CSV de sortie.
        """
        self.filter_and_rename_columns()
        self.convert_ecef_to_lla()

        fieldnames = self.data[0].keys()
        self.write_csv_file(output_filename, self.data, fieldnames)


# Utilisation de la classe DataProcessor
filename = "C:\\Users\\noeba\\PycharmProjects\\MGA802_Project\\Projet_final\\Data\\truth_filtered.csv"
output_filename = "C:\\Users\\noeba\\PycharmProjects\\MGA802_Project\\Projet_final\\Data\\new_truth_filtered.csv"

processor = DataProcessor(filename)
processor.process_data(output_filename)
