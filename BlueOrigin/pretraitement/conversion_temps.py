"""
Description : Ce fichier contient la classe "ConversionTemps" qui permet de convertir les valeurs de temps de nanosecondes en secondes dans un fichier CSV et de filtrer les données en fonction d'un taux d'échantillonnage.

La classe "ConversionTemps" prend en compte un fichier CSV d'entrée et un fichier CSV de sortie par défaut. Elle utilise les modules "csv" et "globs" pour la lecture et l'écriture des fichiers CSV, ainsi que pour l'accès aux chemins de fichiers par défaut.

Les principales méthodes de la classe sont "read_csv_file", "write_csv_file", "convert_nanoseconds_to_seconds", "filter_data_by_sampling_rate" et "process_data".

La méthode "read_csv_file" lit un fichier CSV et retourne les données sous forme de liste de dictionnaires.

La méthode "write_csv_file" écrit les données dans un fichier CSV.

La méthode "convert_nanoseconds_to_seconds" convertit les valeurs de temps de nanosecondes en secondes dans les données et supprime les données avant un temps spécifié.

La méthode "filter_data_by_sampling_rate" filtre les données en fonction d'un taux d'échantillonnage spécifié.

La méthode "process_data" effectue le traitement complet des données, y compris la conversion et le filtrage, et écrit les données traitées dans un nouveau fichier CSV.

Remarques :
- Ce fichier nécessite le module "csv" pour la manipulation des fichiers CSV.
- Les chemins de fichiers d'entrée et de sortie par défaut sont définis dans les variables "CSV_PATH_DEFAULT" et "CSV_FILTERED_PATH_DEFAULT" du module "globs".
"""

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
