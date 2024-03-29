import os
import getpass

CURRENT_USER = getpass.getuser()
CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
OUTPUT_FOLDER_PATH_DEFAULT = os.path.join(CURRENT_PATH, 'Data')

CVS_FILENAME_DEFAULT = 'truth.csv'
CVS_FILTERED_FILENAME_DEFAULT = 'truth_filtered.csv'
FINAL_CVS_FILTERED_FILENAME_DEFAULT = 'final_truth_filtered.csv'

CSV_PROFIL_VENT = 'profil_vent.csv'

CSV_PATH_DEFAULT = os.path.join(OUTPUT_FOLDER_PATH_DEFAULT, CVS_FILENAME_DEFAULT)
CSV_FILTERED_PATH_DEFAULT = os.path.join(OUTPUT_FOLDER_PATH_DEFAULT, CVS_FILTERED_FILENAME_DEFAULT)
FINAL_CSV_FILTERED_PATH_DEFAULT = os.path.join(OUTPUT_FOLDER_PATH_DEFAULT, FINAL_CVS_FILTERED_FILENAME_DEFAULT)

CSV_PATH_PROFIL_VENT = os.path.join(OUTPUT_FOLDER_PATH_DEFAULT, CSV_PROFIL_VENT)