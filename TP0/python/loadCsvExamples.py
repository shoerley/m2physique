import numpy as np
import pandas as pd
import csv
def load_file_with_pandas(filename, separator):
	"""
	Pandas charge les fichiers csv sous un format particulier, qui lui est propre.
	On peut y faire des recherches (presque) comme si on était dans une base de données,
	faire des calculs, extraire des colonnes, etc.
	:param filename: chemin vers le fichier à ouvrir
	:param separator: caractère utilisé dans le fichier pour séparer les champs d'une ligne
	:return: DataFrame contenant les données
	"""

	return pd.read_csv(filename, delimiter=separator)

def load_file_with_numpy(filename, separator):
	"""
	Numpy charge des données de manière plus brute, dans un array numpy. C'est pratique si on
	n'a pas besoin de la "lourdeur" de pandas.
	:param filename: chemin vers le fichier à ouvrir
	:param separator: caractère utilisé dans le fichier pour séparer les champs d'une ligne
	:return: np.array contenant les données
	"""
	return np.genfromtxt(filename, delimiter=separator)

def load_file_with_python(filename, separator):
	"""
	On peut aussi charger un CSV avec une fonction native de Python.
	:param filename: chemin vers le fichier à ouvrir
	:param separator: caractère utilisé dans le fichier pour séparer les champs d'une ligne
	:return: Tableau contenant les données
	"""

	with open(filename, newline='') as csvfile:
		data = csv.reader(csvfile, delimiter=separator)



if __name__ == '__main__':
	filename = "../ressources/temperatures_moule.csv"
	fileLoadedPandas = load_file_with_pandas(filename, ";")

	print(load_file_with_pandas(filename, ";"))
	print(load_file_with_numpy(filename, ";"))
	print(load_file_with_python(filename, ";"))




