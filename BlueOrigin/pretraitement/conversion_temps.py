import csv
from Projet_final.globs import CSV_FILTERED_PATH_DEFAULT, FINAL_CSV_FILTERED_PATH_DEFAULT

class ConversionTemps:
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

    def convert_nanoseconds_to_seconds(self):
        """
        Convertit les valeurs de temps de nanosecondes en secondes dans les données.
        Supprime les données avant le temps 1602596210210000000.

        :return: Les données avec les valeurs de temps converties en secondes et filtrées.
        """
        converted_data = []
        reference_time = 1.60259621021e+18 / 1000000000  # Nouveau temps de référence
        for row in self.data:
            time = float(row["TIME_NANOSECONDS_TAI "])
            if time >= 1.60259621021e+18:
                row["TIME_NANOSECONDS_TAI "] = (float(row["TIME_NANOSECONDS_TAI "]) / 1000000000) - reference_time
                converted_data.append(row)
        self.data = converted_data

    def filter_data_by_sampling_rate(self, sampling_rate):
        """
        Filtre les données en fonction du taux d'échantillonnage.

        :param sampling_rate: Le taux d'échantillonnage en secondes.
        :return: Les données filtrées.
        """
        filtered_data = []
        last_sampled_time = -1  # Permet d'avoir la première valeur à 0 seconde
        for row in self.data:
            time = row["TIME_NANOSECONDS_TAI "]
            if time >= last_sampled_time + sampling_rate:
                filtered_data.append(row)
                last_sampled_time = time
        self.data = filtered_data

    def process_data(self, output_filename, sampling_rate=1):
        """
        Effectue le traitement des données, y compris la conversion et le filtrage.
        Écrit les données traitées dans un nouveau fichier CSV.

        :param output_filename: Le nom du fichier CSV de sortie.
        :param sampling_rate: Le taux d'échantillonnage en secondes.
        """
        self.convert_nanoseconds_to_seconds()
        self.filter_data_by_sampling_rate(sampling_rate)

        fieldnames = self.data[0].keys()
        self.write_csv_file(output_filename, self.data, fieldnames)


# Utilisation de la classe DataProcessor

filename = CSV_FILTERED_PATH_DEFAULT
output_filename = FINAL_CSV_FILTERED_PATH_DEFAULT

conversion = ConversionTemps(filename)
conversion.process_data(output_filename)
