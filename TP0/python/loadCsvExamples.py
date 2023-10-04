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
	data = pd.read_csv(filename, delimiter=separator)

	"""
	Pandas est un peu rebutant, mais vient avec des facilités de sélection de lignes. Par exemple,
	on peut sans effort, moyennant de manipuler la syntaxe du panda :
		- isoler les lignes où la colonne "X" vaut "y", et où la colonne "Z" ne vaut "T", etc.
		- regrouper des lignes sur un certain critère de colonne
		- calculer des moyennes, des délais, etc.
		- et avec geopandas, tirer profit des projections sur des cartes géographiques.
	Sur la base des exemples ci-dessous, tentez d'isoler des lignes sur d'autres critères et de faire des calculs
	"""

	# S'assurer que la colonne "date" contient bien une date reconnaissable par pandas
	data["date_releve"] = pd.to_datetime(data['date_releve'], format="%d/%m/%Y")

	# La température qu'il a fait le 3 mars 2023
	mask_date = data["date_releve"] == "03/03/2023"
	temp_3mars2023 = data[mask_date]

	# Affichage.
	print("Le 3 mars 2023 il a fait maximum {} degrés".format(temp_3mars2023["temperature_max"].values[0]))

	"""
	Essayez :
		- avec et sans le "values[0]", mettez autre chose à la place du 0 ... A quoi sert-il ?
		- affichez d'autres colonnes
		- ajoutez un masque, mettez un intervalle de date au lieu d'une seule
		- affichez la moyenne au lieu du min ou du max
	"""

	return data

def load_file_with_numpy(filename, separator):
	"""
	Numpy charge des données de manière plus brute, dans un array numpy. C'est pratique si on
	n'a pas besoin de la "lourdeur" de pandas.
	:param filename: chemin vers le fichier à ouvrir
	:param separator: caractère utilisé dans le fichier pour séparer les champs d'une ligne
	:return: np.array contenant les données
	"""
	data = np.genfromtxt(filename, delimiter=separator)

	return data

def load_file_with_python(filename, separator):
	"""
	On peut aussi charger un CSV avec une fonction native de Python.
	:param filename: chemin vers le fichier à ouvrir
	:param separator: caractère utilisé dans le fichier pour séparer les champs d'une ligne
	:return: Tableau contenant les données
	"""

	data = []
	with open(filename, newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter=separator)
		for line in reader:
			data.append(line)

	return data

if __name__ == '__main__':
	filename = "../ressources/temperatures_moule.csv"
	separator = ";"

	# exemple d'affichage du contenu du fichier
	load_file_with_numpy(filename, separator)


	"""
	Pour aller plus loin, pour chaque méthode de chargement de fichier:
		- affichez le nom des colonnes
		- affichez le nombre de lignes
		- affichez le contenu du fichier
		- isolez une colonne ou bien un ensemble de colonnes
		- isolez une ligne ou bien un ensemble de lignes
		- faites un calcul sur une colonne, une ligne ou bien un ensemble
		
	Par "isoler", on entend "mettre dans une variable". Vous pouvez ensuite afficher la variable pour vérifier 
	que ça s'est bien passé.
	"""




