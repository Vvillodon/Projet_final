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


def filter_and_rename_columns(data):
    """
    Filtre les colonnes et les renomme dans les données.

    :param data: Les données à filtrer et renommer.
    :return: Les données avec les colonnes filtrées et renommées.
    """
    filtered_data = []
    for row in data:
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
    return filtered_data


# Lecture du fichier CSV "truth_filtered.csv"
filename = "C:\\Users\\noeba\\PycharmProjects\\MGA802_Project\\Projet_final\\Data\\truth_filtered.csv"
data = read_csv_file(filename)

# Filtrage des colonnes et renommage
filtered_data = filter_and_rename_columns(data)

# Écriture des données filtrées dans un nouveau fichier CSV
output_filename = "C:\\Users\\noeba\\PycharmProjects\\MGA802_Project\\Projet_final\\Data\\new_truth_filtered.csv"
fieldnames = filtered_data[0].keys()
write_csv_file(output_filename, filtered_data, fieldnames)
