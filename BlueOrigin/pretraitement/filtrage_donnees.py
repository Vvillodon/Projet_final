import csv
import math
from globs import (CSV_FILTERED_PATH_DEFAULT, FINAL_CSV_FILTERED_PATH_DEFAULT)


class FiltrageDonnees:
    def __init__(self):
        self.filename = CSV_FILTERED_PATH_DEFAULT
        self.output_filename = FINAL_CSV_FILTERED_PATH_DEFAULT
        self.data = self.read_csv_file()

    def read_csv_file(self):
        """
        Lit un fichier CSV et retourne les données sous forme de liste de dictionnaires.

        :return: Une liste de dictionnaires contenant les données du fichier CSV.
        :rtype: list[dict]
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
        :type filename: str
        :param data: Les données à écrire dans le fichier CSV.
        :type data: list[dict]
        :param fieldnames: Les noms de colonnes du fichier CSV.
        :type fieldnames: list[str]
        """
        with open(filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    def convert_ecef_to_cartesian(self):
        """
        Convertit les positions du repère ECEF vers le repère LLA (Latitude, Longitude, Altitude).

        """
        a = 6372368.0  # Demi-grand axe de la Terre (m)
        for row in self.data:
            pos_x = float(row["pos_X"])
            pos_y = float(row["pos_Y"])
            pos_z = float(row["pos_Z"])

            # Calcul des coordonnées cartésiennes
            r = math.sqrt(pos_x ** 2 + pos_y ** 2 + pos_z ** 2)
            theta = math.acos(pos_z / r)
            phi = float(math.atan2(pos_y, pos_x))

            # Conversion en coordonnées cartésiennes sur Terre
            z_cartesian = r - a
            x_cartesian = theta * a - 6533890.282256417
            y_cartesian = phi * a - -11650966.007387657

            row["x_cartesian"] = x_cartesian
            row["y_cartesian"] = y_cartesian
            row["z_cartesian"] = z_cartesian

    def filter_and_rename_columns(self):
        """
        Filtre les colonnes et les renomme dans les données.

        :return: Les données avec les colonnes filtrées et renommées.
        :rtype: list[dict]
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

    def process_data(self):
        """
        Effectue le traitement des données, y compris le filtrage, la conversion ECEF vers LLA
        et le renommage des colonnes. Écrit les données traitées dans un nouveau fichier CSV.

        :return: Les données traitées.
        :rtype: list[list[float]]
        """
        self.filter_and_rename_columns()
        self.convert_ecef_to_cartesian()

        fieldnames = self.data[0].keys()
        self.write_csv_file(self.output_filename, self.data, fieldnames)

        data_new = [[float(value) for value in row.values()] for row in self.data]
        return data_new
