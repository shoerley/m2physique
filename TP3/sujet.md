@author scholet @date novembre 2023

# TP3

On souhaite étudier certains phénomènes dont l'occurrence dépend de probabilités connues. L'objectif de ces exercices est de comprendre comment mettre en place un environnement de simulation pour un problème donné. 

## Exercice 1

Un joueur se présente au casino avec une fortune évaluée à `fortune_initiale`€. Il joue à pile ou face à l'aide d'une pièce non truquée.

1. Comment simuler le lancer d'une pièce ?
2. Comment simuler `nb_lancers` lancers de pièces ?

A chaque lancer de pièce, il mise `mise_unitaire`€. Le joueur cesse de parier dans l'un des deux cas suivants : 
- il n'a plus un rond, ou
- il a gagné au moins 50% de sa fortune (c'est à dire que sa fortune finale `fortune_finale` vaut `(1 + 0.5) * fortune_initiale`)

3. Quelles sont les chances pour que le joueur perde toute sa fortune ?
4. Quelles sont les chances pour que le joueur gagne au moins 50% de sa fortune ?

## Exercice 2

Une approche simple (ou simpliste) pour établir des prévisions météorologiques est l'approche markovienne d'ordre 1. Elle consiste à attribuer une probabilité à la condition météo du temps T+1 en fonction de celle du temps T.

Un exemple d'un tel modèle est :
- S'il fait soleil aujourd'hui, il y a 40% de chances pour qu'il en soit de même demain. Mais le ciel peut s'avérer nuageux dans 40% des cas, voire pluvieux dans les 20% restants
- Si le ciel est nuageux aujourd'hui, il y a 30% de chances pour qu'il soit ensoleilé demain. Mais il y a 30% de chances pour qu'il soit aussi nuageux demain, et 40% de chances pour qu'il pleuve
- Enfin, s'il pleut aujourd'hui, il n'y a que 10% de chances pour qu'il fasse soleil demain. Mais il y a 60% de chances pour que le ciel soit nuageux, et 30% de chances pour qu'il pleuve encore demain.

1. Vérifier que la somme des probabilités des issues pour chaque situation de départ vaut 1.

Ces énoncés peuvent être illustrés simplement à l'aide de graphes dits de markov. Dans un tel graphe, les noeuds sont des états (soleil, pluvieux, nuageux) et les arcs portent les probabilités de passage d'un état à un autre

2. Représenter (sur papier) le graphe de markov associé au modèle énoncé plus haut


On souhaite connaitre les chances pour qu'il pleuve après-demain, sachant qu'il fait beau aujourd'hui. La suite de l'exercice consiste à répondre à cette interrogation.

3. Stocker dans une matrice Numpy (3x3) les probabilités de passage. 

La fonction `np.random.choice()` permet de tirer au sort un ou plusieurs éléments, étant donnée la probabilité de tirage de chacun.

4. Utiliser la fonction `np.random.choice()` pour déterminer le temps qu'il fera demain en fonction du temps qu'il fait aujourd'hui

5. Pour savoir quel temps il fera après-demain, il faut faire deux appels à la fonction `np.random.choice()`. Comment les enchainer ?

6. Finalisez votre code, afin de répondre à la question énoncée plus haut.
