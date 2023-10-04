@author scholet @date 03 oct 2023

# TP 1 : Données météo

Dans ce TP, vous analyserez des données météorologiques tel que le ferait 
un data analyst versé dans la physique (ou un physicien versé dans la data analysis ...).

Voici votre feuille de route.

## Recherche, connaissance et récupération des données

On s'intéresse aux données météo concernant la Guadeloupe entre 2010 et 2023.
1. Chercher et télécharger de telles données. Chercher notamment du côté de https://public.opendatasoft.com/.

Attention : seules les données concernant la Guadeloupe sur la période d'intérêt doivent être téléchargées.

Lorsque l'on télécharge des données, elles sont souvent au format CSV. Dans ce format, assimilable à un
tableau (ou bien à une matrice), chaque ligne est une observation (= un relevé), et chaque colonne est un paramètre, (= une variable). 

L'intersection d'une ligne et d'une colonne est donc la mesure d'un paramètre donné, lors d'une observation.

Les fichiers CSV contiennent ainsi plusieurs lignes et plusieurs colonnes. Par convention, la première ligne du tableau précise le nom des variables. Cependant, ces noms ne sont pas toujours parlants.

2. Sur la page de téléchargement des données, cherchez la signification de chacune des colonnes.

Le type, l'unité ou encore des exemples de valeurs peuvent aider à mieux concevoir l'analyse des données.

3. Vérifier que la licence d'utilisation des données vous donne le droit de les analyser pour des besoins académiques

La licence d'utilisation confère à l'utilisateur des droits et des devoirs vis à vis des données. Si cette étape est souvent rapidement passée dans la sphère personnelle ou académique (on se contente de cliquer sur "suivant" jusqu'à obtenir ce qu'on veut ...), dans le monde professionnel, utiliser des données pour un usage proscrit peut vous coûter cher (amandes, poursuites, etc.).


## Analyse : première partie

Ouvrir le fichier et prendre connaissance de son contenu. Notamment, s'intéresser :

* Aux formats de dates
* Aux séparateurs décimaux (point ou virgule)
* Aux unités 
* Aux types de représentation des variables (date, texte ou numérique) 
* Aux types statistique des variables (quantitatif, qualitatif ; ordinal, nominal)
* Aux valeurs manquantes

3. Rédigez un bref paragraphe pour faire part de vos impressions à ce sujet. Donnez votre avis quant à l'utilisabilité des données

Selon la taille ou le format des données, il n'est pas toujours possible de l'ouvrir dans Excel ou bien dans un fichier texte. Parfois, il faut "coder" pour avoir ces informations. 

4. Codez, en Python, une fonction permettant de charger le fichier.


5. Codez, en Python, une fonction permettant :
d'afficher les différentes stations météo d'où proviennent les relevés

## Analyse : deuxième partie

Python n'est pas une fin en soi, c'est un outil. Et c'est important que vous le gardiez à l'esprit, en particulier dans votre cas : vous êtes des physiciens, pas des développeurs. Dès lors, en situation réelles, on ne vous posera pas ce genre de question :

* Chargez le fichier csv
* Affichez la colonne 12 en fonction de la colonne 18
* Pour chaque 


1. Apportez des preuves 

Plus la visibilité horizontale est élevée, plus il fait chaud
Plus il fait chaud, plus il fait humide
Plus il fait humide, plus il pleut
Plus il pleut, plus la pression atmosphérique est basse



Sur les 10 dernières années, quelle est la tendance de la température ?
Sur les 10 dernières années, quelle est la tendance des précipitations ?


En Guadeloupe, la saison cyclonique s'étend de juin à novembre.
Quelle saison cyclonique fut la plus froide, la plus chaude ?
Quelle saison cyclonique fut la plus pluvieuse, la moins pluvieuse ?

Recherchez la saison cyclonique pour laquelle la pression atmosphérique était la plus faible, et la saison pour laquelle la pression atmosphérique était la plus élevée. Comparez ces saisons en termes de vitesse du vent, de température, de précipitations et d'humidité.



## Familia
Vous cherchez à analyser des données météorologiques, telles que l'humidité, la température, la direction et la force du
vent, etc. 