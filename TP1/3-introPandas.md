@author scholet @date 4 oct 2023

# Pandas

Pandas est un outil intéressant et incontournable en Python. Il n'adresse pas les mêmes problématiques que Numpy, et vient par conséquent en complément. 

Votre objectif pour cet atelier sera de prendre en main pandas, au travers des exemples donnés, et de l'utiliser pour analyser un jeu de données réel. N'oubliez pas que la documentation de pandas et les nombreux exemples d'utilisation présents sur la toile vous sont disponibles.

## 1. Prise en main de Pandas

Etudiez le snippet suivant : 

```python
import pandas as pd

def load_file_with_pandas(filename, separator):
	"""
	Pandas charge les fichiers csv vers un format particulier, qui lui est propre : le DataFrame.
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
```

## 2. Analyse de données météorologiques

On s'intéresse aux données météo concernant la Guadeloupe entre 2010 et 2023.

### 2.1. Recherche et téléchargement

Chercher notamment du côté de https://public.opendatasoft.com/.

**Attention :** seules les données concernant la Guadeloupe sur la période d'intérêt doivent être téléchargées. 

Lorsque l'on télécharge des données, elles sont souvent au format CSV. Dans ce format, assimilable à un tableau (ou bien à une matrice), chaque ligne est une observation (= un relevé), et chaque colonne est un paramètre, (= une variable). L'intersection d'une ligne et d'une colonne est donc la mesure d'un paramètre donné, lors d'une observation.

Les fichiers CSV contiennent ainsi plusieurs lignes et plusieurs colonnes. Par convention, la première ligne du tableau précise le nom des variables. Cependant, ces noms ne sont pas toujours parlants.


#### 2.1.a. Signification des colonnes

Sur la page de téléchargement des données, cherchez la signification de chacune des colonnes.

Le type, l'unité ou encore des exemples de valeurs peuvent aider à mieux concevoir l'analyse des données.

#### 2.1.b. Licence d'utilisation

Vérifier que la licence d'utilisation des données vous donne le droit de les analyser pour des besoins académiques

La licence d'utilisation confère à l'utilisateur des droits et des devoirs vis à vis des données. Si cette étape est souvent rapidement passée dans la sphère personnelle ou académique (on se contente de cliquer sur "suivant" jusqu'à obtenir ce qu'on veut ...), dans le monde professionnel, utiliser des données pour un usage proscrit peut vous coûter cher (amandes, poursuites, etc.).

### 2.2 Analyse : première partie

Ouvrez le fichier (avec un tableur, Excel ou Calc, par exemple) et prendre connaissance de son contenu. Notamment, relevez :

* Aux formats de dates
* Aux séparateurs décimaux (point ou virgule)
* Aux unités 
* Aux types de représentation des variables (date, texte ou numérique) 
* Aux types statistique des variables (quantitatif, qualitatif ; ordinal, nominal)
* Aux valeurs manquantes

* Rédigez un bref paragraphe pour faire part de vos impressions à ce sujet. Donnez votre avis quant à l'utilisabilité des données.

**Note :** Selon la taille ou le format des données, il n'est pas toujours possible de l'ouvrir dans Excel ou bien dans un fichier texte. Parfois, il faut "coder" pour avoir ces informations. 

1. Codez, en Python, une fonction permettant de charger le fichier avec pandas. La fonction doit revoyer un DataFrame.

2. Compte tenu des différentes colonnes, affichez des graphiques permettant d'afficher une colonne en fonction d'une autre, par exemple :
   * la température en fonction de la date
   * l'humidité en fonction de la pression atmosphérique
   * la température de la saison cyclonique 2018


### 2.2 Analyse : deuxième partie

Vous croisez un expert tous domaines (comme il en existe beaucoup) avec lequel vous engagez une conversation passionnante. Toutes ses phrases commencent par "_de toutes les manières_" ou bien par "_j'ai constaté que_", suivi d'une assertion concernant le climat. On a repris ci-dessous certaines d'entre elles.

Muni de votre compréhension de ce qu'expriment les données, et de votre récente montée en compétences en Python, essayez de prouver ou de réfuter certaines d'entre-elles, au choix. Vous pourrez notamment utiliser des graphiques ou des recherches dans les données.

1. Plus la visibilité horizontale est élevée, plus il fait chaud 
2. Plus il fait froid, plus il fait humide
3. Plus il fait humide, plus il pleut
4. Plus il pleut, plus la pression atmosphérique est haute (c'est pour cela que ses oreilles sifflent juste avant les averses)
5. Sur les 10 dernières années, la température n'a pas augmenté (si on en a l'impression, c'est parce qu'il y a plus de routes et de bâtiments, qui réfléchissent la chaleur)
6. Sur les 10 dernières années, la tendance des précipitations est à la baisse.

En Guadeloupe, la saison cyclonique s'étend de juin à novembre.

7. La saison cyclonique la plus froide fut celle de 2016.
8. La saison cyclonique la plus chaude fut celle de 2018. 
9. La saison cyclonique la plus pluvieuse fut celle de 2018. 
10. La saison cyclonique la moins pluvieuse fut celle de 2013. 

### Analyse : Miss & Mister Météo

Recherchez la saison cyclonique pour laquelle la pression atmosphérique était la plus faible, et la saison pour laquelle la pression atmosphérique était la plus élevée. Comparez ces saisons en termes de vitesse du vent, de température, de précipitations et d'humidité. 
1. Comment semblent varier ces paramètres en fonction de la pression atmosphérique ? 
2. Ces résultats sont-ils en accord avec vos connaissances ?
