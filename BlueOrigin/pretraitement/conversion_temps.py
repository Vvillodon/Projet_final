"""DESCRIPTION FICHIER"""


import csv


def read_csv_file(filename):
    """
    Lit un fichier CSV et retourne les données sous forme de liste de dictionnaires.

    :param filename: Le nom du fichier CSV à lire.
    :return: Les données du fichier CSV sous forme de liste de dictionnaires.
    """
    data = []
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data


def write_csv_file(filename, data, fieldnames):
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


def convert_nanoseconds_to_seconds(data):
    """
    Convertit les valeurs de temps de nanosecondes en secondes dans les données.

    :param data: Les données à convertir.
    :return: Les données avec les valeurs de temps converties en secondes.
    """
    converted_data = []
    reference_time = float(data[0]["TIME_NANOSECONDS_TAI "]) / 1000000000  # Nouveau temps de référence
    for row in data:
        row["TIME_NANOSECONDS_TAI "] = (float(row["TIME_NANOSECONDS_TAI "]) / 1000000000) - reference_time
        converted_data.append(row)
    return converted_data


def filter_data_by_sampling_rate(data, sampling_rate):
    """
    Filtre les données en fonction du taux d'échantillonnage.

    :param data: Les données à filtrer.
    :param sampling_rate: Le taux d'échantillonnage en secondes.
    :return: Les données filtrées.
    """
    filtered_data = []
    last_sampled_time = 0
    for row in data:
        time = row["TIME_NANOSECONDS_TAI "]
        if time >= last_sampled_time + sampling_rate:
            filtered_data.append(row)
            last_sampled_time = time
    return filtered_data


# Lecture du fichier CSV
filename = "C:\\Users\\alice\\Documents\\MGA802 - Python\\Projet_Final\\Projet_final\\Data\\truth.csv"  # Remplacez "nom_du_fichier.csv" par le nom réel de votre fichier
data = read_csv_file(filename)

# Conversion du temps de nanosecondes en secondes et ajustement du nouveau temps de référence
new_data = convert_nanoseconds_to_seconds(data)


# Filtrage des données avec un taux d'échantillonnage de 1 seconde
sampling_rate = 1
filtered_data = filter_data_by_sampling_rate(new_data, sampling_rate)

# Écriture des données filtrées dans un nouveau fichier CSV
output_filename = "C:\\Users\\alice\\Documents\\MGA802 - Python\\Projet_Final\\Projet_final\\Data\\truth.csv"
fieldnames = new_data[0].keys()
write_csv_file(output_filename, filtered_data, fieldnames)
