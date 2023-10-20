import numpy as np
from matplotlib import pyplot as plt

"""
	scholet @softbridge in october 2023
	
	Proposition de correction du TP1 - M2 Physique, Introduction à Python - Promo 2023
	
	Les codes ci-dessous sont donnés à titre illustratif de ce qu'on peut parvenir à réaliser de manière abordable.
	Il ne fallait toutefois pas en faire autant pour espérer avoir une bonne note. 
	
	Voir les commentaires dans le code.
"""


# ----------------- TP1 . PRINCIPES DE BASE -----------------------

def plot_and_scatter():
	# 1. Créez un tableau numpy contenant des valeurs aléatoires dans 100 lignes et 2 colonnes.
	random_array = np.random.rand(100, 2)

	# 2. Isoler des lignes et des colonnes en particulier
	col_1 = random_array[:, 1]
	line_8 = random_array[8, :]
	lines_10_to_27 = random_array[10:27, :]

	make_scatter(col_1)
	make_scatter(line_8)
	make_scatter(lines_10_to_27)

	# 3. Affichez un plot du tableau X. Pourquoi a-t-il l'air étrange ?
	plt.title("Le plot est bizarre parce qu'ont tente d'afficher \nune courbe de points non liés entre eux.\nIl n'y a pas de relation entre le point p et le point p+1")
	plt.plot(random_array[:, 0], random_array[:, 1])
	plt.show()

	# 4. Remplacez la première colonne de X par les valeurs de np.linspace(0, 10, 100) et la seconde colonne par les valeurs de 4 + 2 * np.sin(2 * x).
	random_array[:, 0] = np.linspace(0, 10, 100)
	random_array[:, 1] = 4 + 2 * np.sin(2 * random_array[:, 0])

	# 5. Refaites un plot et un scatter de X. Que constatez-vous ?
	plt.title("Maintenant qu'il y a une relation entre les points, la courbe ressemle à quelque chose.")
	plt.plot(random_array[:, 0], random_array[:, 1])
	plt.show()

	make_scatter(random_array)

	print("Conclusion : les plot sont adaptés aux données pour lequelles il y a une relation entre les points, par exemple une relation chronologique, ou encore fonctionnelle")

def hist_and_boxplot():
	# 1.
	filename = "../../TP0/ressources/temperatures_moule.csv"
	separator = ";"
	data = np.genfromtxt(filename, delimiter=separator)

	# On se débarasse de la ligne 0 car elle contient des entêtes, qui vont perturber les graphiques (chercher sur un moteur de recherche : NaN).
	# Vous pouvez tenter de la laisser pour voir la différence.
	# En chargeant avec Pandas, on n'a pas ce problème.
	data = data[1:, :]

	# On garde les noms de colonne sous la main, afin d'y accéder par nom plutôt que par numéro de colonne
	# Le code "columns.index("temperature_min")" donne l'indice de temperature_min dans la liste columns, c'est à dire son numéro de colonne
	# Si l'ordre des colonnes venant à changer, il suffirait de refléter le changement dans la liste columns.
	columns = ["ville", "temperature_max", "temperature_min", "date_releve"]

	# Encore une fois, cette manière de gérer les noms de colonnes et NaN n'est pas professionnelle, mais utile à connaître

	# 2. Affichez un histogramme des températures minimales, et un histogramme des températures maximales.

	# Figure avec une ligne et deux colonnes, de taille 10x4
	fig, ax = plt.subplots(1, 2, figsize=(10, 4))
	fig.suptitle("Distribution des températures minimales et maximales au Moule")

	# Première sous-figure
	# Remarquer comment on peut jouer avec les paramètres factultatifs de hist (linewidth, edgecolor, color)
	# Certaines couleurs n'ont pas de nom, elles ont un code. Pour le trouver, taper "colorpicker" dans un moteur de recherche et prendre le code "HEX"
	ax[0].hist(x=data[1:, columns.index("temperature_min")], linewidth=0.5, edgecolor="white", color="#83b5ea")
	ax[0].set_xlabel("Température minimale (C°)")
	ax[0].set_ylabel("Distribution")

	# Deuxième sous-figure
	ax[1].hist(data[1:, columns.index("temperature_max")], linewidth=0.5, edgecolor="white", color="#4998ed")
	ax[1].set_xlabel("Température maximale (C°)")

	plt.show()

	# 3.
	fig, ax1 = plt.subplots(nrows=1, ncols=1)
	ax1.set_ylabel("Température (C°)")
	ax1.set_title("Distribution des températures minimales et maximales\n observées au Moule entre févier et mai 2023")
	ax1.boxplot([data[1:, 2], data[1:, 1]],  labels=['Températures minimales', 'Températures maximales'])

	plt.show()

def make_scatter(data):

	nb_dim = data.ndim
	nb_lines = data.shape[0]
	nb_col = 0
	if nb_dim > 1:
		nb_col = data.shape[1]

	if nb_dim == 1 and len(data) == 2:
		# Une ligne comportant deux éléments : on peut afficher un scatter (un seul point)
		plt.title(f"Scatter d'un tableau de {len(data)} éléments")
		plt.scatter(data[0], data[1])
		plt.show()
	elif nb_dim == 2 and nb_col == 2:
		# Plusieurs lignes et plusieurs colonnes : on peut afficher un scatter (plusieurs points)
		plt.title(f"Scatter d'un tableau de {nb_lines} lignes et {nb_col} colonnes")
		plt.scatter(data[:, 0], data[:, 1])
		plt.show()
	else:
		print(f"Impossible d'afficher un scatter pour un tableau de {nb_lines} lignes et {nb_col} colonnes")



if __name__ == '__main__':

	# Dé commenter pour lancer l'exo 1
	plot_and_scatter()

	# Dé commenter pour lancer l'exo 2
	hist_and_boxplot()