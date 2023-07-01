import csv  # Importe le module CSV pour lire et écrire des fichiers CSV.
from globs import (CSV_PATH_DEFAULT, CSV_FILTERED_PATH_DEFAULT)  # Importe les chemins de fichiers par défaut.


class ConversionTemps:
    def __init__(self):
        self.filename = CSV_PATH_DEFAULT  # Chemin du fichier CSV d'entrée par défaut.
        self.data = self.read_csv_file()  # Lit le fichier CSV et stocke les données dans self.data.
        self.output_filename = CSV_FILTERED_PATH_DEFAULT  # Chemin du fichier CSV de sortie par défaut.

    def read_csv_file(self):
        """
        Lit un fichier CSV et retourne les données sous forme de liste de dictionnaires.

        :return: Les données du fichier CSV sous forme de liste de dictionnaires.
        """
        data = []
        with open(self.filename, "r") as csvfile:
            reader = csv.DictReader(csvfile)  # Crée un lecteur de fichier CSV basé sur des dictionnaires.
            for row in reader:
                data.append(row)  # Ajoute chaque ligne du fichier CSV à la liste des données.
        return data

    def write_csv_file(self, filename, data, fieldnames):
        """
        Écrit les données dans un fichier CSV.

        :param filename: Le nom du fichier CSV de sortie.
        :param data: Les données à écrire dans le fichier CSV.
        :param fieldnames: Les noms de colonnes du fichier CSV.
        """
        with open(filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  # Crée un écrivain de fichier CSV basé sur des
            # dictionnaires.
            writer.writeheader()  # Écrit les noms de colonnes dans le fichier CSV.
            writer.writerows(data)  # Écrit les données dans le fichier CSV.

    def convert_nanoseconds_to_seconds(self):
        """
        Convertit les valeurs de temps de nanosecondes en secondes dans les données.
        Supprime les données avant le temps 1602596210210000000.

        :return: Les données avec les valeurs de temps converties en secondes et filtrées.
        """
        converted_data = []
        reference_time = 1602596210.21  # Nouveau temps de référence en secondes
        for row in self.data:
            time = float(row["TIME_NANOSECONDS_TAI "])
            if time >= 1.60259621021e+18:
                row["TIME_NANOSECONDS_TAI "] = (time / 1000000000) - reference_time
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

    def process_data(self, sampling_rate=1):
        """
        Effectue le traitement des données, y compris la conversion et le filtrage.
        Écrit les données traitées dans un nouveau fichier CSV.

        :param sampling_rate: Le taux d'échantillonnage en secondes pour le filtrage des données. Par défaut, la valeur est 1.
        """
        self.convert_nanoseconds_to_seconds()  # Convertit les valeurs de temps en secondes.
        self.filter_data_by_sampling_rate(sampling_rate)  # Filtre les données en fonction du taux d'échantillonnage.

        fieldnames = self.data[0].keys()  # Récupère les noms de colonnes à partir du premier élément des données.
        self.write_csv_file(self.output_filename, self.data, fieldnames)  # Écrit les données traitées dans un
        # fichier CSV.
