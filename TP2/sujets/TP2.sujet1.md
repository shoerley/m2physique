@author scholet @date 10 oct 2023

# 1. Cas pratique : choisir son abonnement à EDF

Pour ce cas pratique, vous prenez la casquette d'un expert en consommation d'énergie. Un client (particulier) fait appel à vous pour choisir l'abonnement EDF qui lui fera économiser le maximum d'argent. 

Pour information, EDF Guadeloupe propose aux particuliers deux options dans son tarif dit "tarif bleu résidentiel" : l'option "base" et l'option "heures-pleines heures-creuses", dite HP/HC. La facture d'un consommateur se décline en trois grands postes : sa consommation électrique, son abonnement, et les taxes et autres imputations (éclairage public, etc.). Dans ce cas pratique, on s'intéresse uniquement aux deux postes que sont la consommation électrique et l'abonnement.

1. Documentez-vous sur les tarifs, et reprenez dans un tableau (sur papier, pas dans un tableau python), pour chaque option, le prix de l'électricité et le prix de l'abonnement. Pour ce faire, recherchez directement sur le site d'EDF Guadeloupe les tarifs. On s'intéressera aux tarifs liés à une fourniture monophasée calibrée à 6kVA.

Le raisonnement de votre client est le suivant : 
> "_A mon avis, on propose pas aux gens de payer moins cher pour le même service. En HP/HC, c'est plus économique (en €) de faire ses machines la nuit, mais d'un autre côté l'abonnement est plus cher que l'abonnement de l'option base. Donc si c'est pour payer la consommation moins cher et payer l'abonnement plus cher, je préfère autant faire mes machines quand ça me chante et souscrire à l'option base._"

2. Codez, en Python, le nécessaire pour calculer le montant d'une facture étant donnés la consommation électrique en HP, la consommation électrique en HC et l'option souscrite (base ou HP/HC). Inspirez-vous du fichier `TP2/python/aideTP2.py` si vous êtes perdu. Dans tous les cas :
   - la ou les fonctions doivent renvoyer un montant, en euros
   - la ou les fonctions doivent prendre en paramètre une ou plusieurs consommations électriques
   - vous devez utiliser des variables globales

3. Faites plusieurs essais pour garantir que votre code produit les bons résultats. En particulier, donnez des exemples de sortie de votre programme pour les consommations annuelles suivantes :
    - HP: 400kWh, HC: 200kWh, abonnement : base
    - HP: 400kWh, HC: 200kWh, abonnement : HP/HC
    - HP: 400kWh, HC: 1000kWh, abonnement : base
    - HP: 1000kWh, HC: 400kWh, abonnement : HP/HC

On cherche à déterminer, pour une consommation électrique annuelle donnée, pour quelle répartition en heures-pleines heures-creuses est-ce qu'une facture en HP/HC est moins chère qu'une facture en option base. 

4. Quel est le montant d'une facture pour une consommation de 1000kWh avec l'option base ? Utilisez les codes produits à la question 2. 

5. Essayez plusieurs répartitions heures-pleines heures-creuses de 1000kWh (par exemple 50/50, 70/30, 30/70, etc.) et déterminez l'option pour laquelle la facture sera moins chère. Dans chaque cas, mettez en avant l'écart entre le montant de la facture pour une l'option base et le montant de la facture pour l'option HP/HC.

Les essais que vous avez réalisés donnent une première intuition sur la manière dont votre client peut tirer profit d'un abonnement choisi de manière éclairée. Il existe une technique de _tuning_ appelée le **gridsearch**, et qui consiste à tester plusieurs combinaisons de paramètres et à comparer les résultats ensuite.

6. Codez une fonction qui prend en paramètre une consommation électrique, et qui renvoie un tableau de trois colonnes, où chaque ligne précise un nombre d'heures pleines, un nombre d'heures creuses et un montant, correspondant à prix de la consommation électrique de la répartition à l'option HP/HC. Vous devez tester toutes les répartitions possibles par pas de 1.
> Par exemple, si la consommation électrique passée en paramètre est 1000, vous devez renvoyer un tableau de 1000 lignes. La première ligne aura le contenu `[0, 1000, p1]`, la seconde `[1, 999, p2]` ; l'avant dernière `[999, 1, p999]` et la dernière `[1000, 0, p1000]`, avec `pi` le prix de la consommation électrique correspondant à la répartition en heure pleine et en heures creuse donnée par les premier et deuxième éléments de la ligne.

7. Déterminez quels affichages (graphiques) des données contenues dans le résultat renvoyé par le code produit à la question 6. permettent de déterminer la répartition à partir de laquelle il est préférable d'opter pour l'option HP/HC, ainsi que les répartitions pour lesquelles ce n'est pas à l'avantage du consommateur. Codez, en python, une fonction qui prend en paramètre un tableau (produit par la réponse à la question 6.) et qui produit un tel affichage. Soignez le graphique (titre, axes, couleurs, etc.).

8. Votre client vous indique qu'il consomme annuellement autour de 4200kWh. Sur la base de cette information, produisez un petit paragraphe, graphique et données à l'appui pour le conseiller au mieux quant à son choix d'abonnement auprès d'EDF. 

# Disclaimer

L'auteur de ces exercices n'a aucun lien avec EDF/EDF Guadeloupe et n'a pas été autorisé ou encouragé à produire ce sujet par eux. Le sujet a un unique objectif pédagogique pour l'enseignement de Python. Toute ressemblance avec des situations réelles serait purement fortuite.