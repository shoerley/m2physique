@author scholet @date november 2023


# Informations générales
__Examen du 28 novembre 2023__

L'examen dure 2h, conformément à ce qui est prévu dans la maquette de la formation. Le délai court à compter du top donné en séance.

L'examen comporte deux parties :
- une partie contenant des questions de cours, pour lesquelles les réponses attendues doivent être rédigées à la main en français.
- une partie contenant des questions de programmation, pour lesquelles les réponses attendues doivent être écrites en Python.

Pendant toute la durée de l'examen :
- Vous ne devez pas communiquer avec les autres étudiants.
- Votre téléphone portable doit être en mode silencieux, rangé dans un sac, hors de votre portée et de votre vue. Vous ne devez pas y accéder.
- Vous ne devez pas porter d'écouteurs.
- L'utilisation de tout appareil est interdite, à l'exception de l'ordinateur que vous utilisez pour composer.

Vous allez remettre deux types éléments :
- une feuille, sur laquelle vous aurez répondu (de manière manuscrite) aux exercices de la première partie.
- des programmes Python, pour les exercices de la seconde partie.

Les programmes Python doivent être envoyés à (faites un copier-coller) : `scholet.pro+m2physique@proton.me`.

Pendant toute la durée de l'examen :
- L'utilisation du cours, de vos notes personnelles et des TP que vous avez réalisés est autorisée.
- L'utilisation de la documentation trouvée sur Internet est autorisée pendant l'examen.
- L'utilisation de ChatGPT n'est pas autorisée. Aucune forme d'IA n'est autorisée.


# Questions de cours (10 points)

## Exercice 1 (6 points)

Les questions 1 à 6 valent 1 point.

1. Un camarade vous avoue ne pas faire la différence entre une valeur et une variable. Expliquez-lui.
2. Quels sont les types de données de base existant en Python ? Pour chacun d'entre-eux, donnez un exemple de valeur. Citez-en au moins quatre.
3. Qu'est-ce qu'une fonction ?
4. A quoi sert un bloc "try/catch" ?
5. Un camarade (le même !) vous avoue ne pas bien comprendre la différence entre une classe et une instance. Expliquez-lui.
6. Citez quelques différences notables entre Numpy et Pandas, en précisant par exemple des cas d'utilisation où l'un est préférable à l'autre, et vice-versa.

## Exercice 2 (4 points)

Les questions 1 et 2 valent 1 point. La question 3 vaut 3 points.

Soit le snippet suivant :
```python 
x = 10
def magic_function(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * magic_function(n-1)
```

1. Sans lancer le programme, donnez le résultat de la fonction pour les valeurs 2 et 4. Vous détaillerez et justifierez votre raisonnement.
2. La fonction `magic_function(n)` est en réalité une fonction mathématique bien connue. Laquelle est-ce ? 
3. Donnez une version de cette fonction fonctionnant avec une boucle `for`.

 
# Questions de programmation (10 points + 7 bonus)

**NOTE**: vous devez faire l'exercice 3, impérativement, plus l'un des deux exercices 4 ou 5, au choix.

Si vous faites les deux exercices 4 et 5, vous n'obtiendrez les points des deux exercices que si vous obtenez au moins 6 points (sur 7) à l'un d'entre-eux. Dans ce cas, vous aurez des points bonus, dans la limite d'une note sur 20. Il vous est recommandé d'en choisir un seul et de vous concentrer dessus.


## Exercice 3 (3 points)

La question 1 vaut 1 point. La question 2 vaut 2 points.

Pour cet exercice, vous devez compléter le fichier `./stubs/exercice_3.py` et l'envoyer par mail à l'adresse précisée dans la partie "Informations générales" du sujet d'examen.

On cherche à calculer une valeur en sortie, étant données deux valeurs en entrée, `a` et `b`. Le processus de calcul est défini comme suit :
> Si `a` est nul, on renvoie `b`. Si `b` est nul, on renvoie `a`. Sinon, tant que `a` est différent de `b`, si `a` est supérieur à `b`, on remplace la valeur de `a` par la valeur de `a-b`. Sinon, on remplace la valeur de `b` par `b-a`. Enfin, on renvoie `a`

1. Écrivez une fonction Python qui implémente le processus ci-dessus.
2. A quelle opération correspond cette fonction (vue au collège) ?

## Exercice 4 (7 points)

Les questions 1 et 4 valent chacune 0.5 point. Les questions 2, 3, et 5 valent chacune 2 points.

Pour cet exercice, vous devez compléter le fichier `./stubs/exercice_4.py` et l'envoyer par mail à l'adresse précisée dans la partie "Informations générales" du sujet d'examen.

Une étudiante du Master Physique raconte un cauchemar qu'elle a eu la veille d'un examen de Python.
> J'étais à l'étage des salles de TP Informatique, mais le couloir semblait si long que je ne pouvais pas en voir la fin. Il faisait nuit et les chauves-souris fuyaient la lumière des néons. Au début du rêve, j'étais devant la salle TP+203, mais elle était vide. Il y avait une sorte bruit récurrent, comme quand on tape sur une touche de clavier avec énervement ; une sorte de "clap" qui semblait venir des ténèbres. Je me suis mise à chercher le reste de la promo. Mais plutôt que de parcourir le couloir, à chaque "clap", mes pieds me portaient aléatoirement soit d'une salle vers l'avant, soit d'une salle vers l'arrière. À un moment, j'ai entendu la voix insupportable du prof qui disait "envoyez-moi ce que vous avez fait avant la fin de la séance". À ce moment-là, je me suis réveillée, en sueur. Je n'ai jamais été aussi heureuse de l'entendre dire ça.

1. Etudiez la fonction `get_direction()`. En particulier, indiquez son nombre de paramètres, ce qu'elle renvoie et ce qu'elle fait.
2. Créez une fonction `walk()` qui prend en paramètres un nombre de pas `nb_steps` et une position de départ `start_position`, et qui renvoie `W`, un tableau Numpy où chaque ligne `[i, current_position]` indique la position `current_position` atteinte au temps `i` (c'est -à-dire au i-ème "clap")..
3. Créez une fonction `experience_1()` qui ne prend aucun paramètre et ne renvoie rien. La fonction simule le déplacement de l'étudiante, à partir de la salle TP+203 (on considère `start_position=203`), en considérant qu'elle aura entendu 300 "claps". La fonction doit afficher la salle où se trouve l'étudiante juste avant de se réveiller de son cauchemar.
4. Lancez la fonction `experience_1()` une dizaine de fois et relevez, pour chaque lancer, la salle d'arrivée. Que constatez-vous concernant l'écart entre la salle de départ, et la salle d'arrivée après 300 déplacements ?
5. Dans le `__main__`, ajoutez le code nécessaire pour afficher un graphique du parcours de l'étudiante pendant son cauchemar. On mettra en abscisse les claps, et en ordonnée le numéro de la salle TP. Votre graphique doit comporter un titre, tout comme les axes. Une légende n'est pas nécessaire.

## Exercice 5 (7 points)

La question 1 vaut 1 point. La question 2 vaut 2 points. La question 3 vaut 4 points.

Pour cet exercice, vous devez compléter le fichier `./stubs/exercice_5.py` et l'envoyer par mail à l'adresse précisée dans la partie "Informations générales" du sujet d'examen.

Pour cet exercice, on considère le fichier `./stubs/temperatures_moule.csv` présent dans le répertoire Git. Une illustration de la moyenne glissante est donnée dans le fichier `exercice_5.py`.

1. Créez une fonction `load_file()` qui prend en paramètre le nom d'un fichier et qui charge, dans une variable `temperatures`, le contenu du fichier. La fonction renvoie la variable `temperatures`. Vous devez utiliser Pandas ou Numpy.
2. Créer une fonction `window_mean()` qui prend en paramètre les données (issues de la fonction `load_file()`), un indice de départ `start` et un indice de fin `end`. La fonction renvoie la moyenne des températures maximales trouvées entre les indices passés en paramètre (indices de début et de fin inclus).
3. Créer une fonction `moving_average()` qui prend en paramètre les données et une largeur de fenêtre `width`. La fonction renvoie la moyenne glissante (avec un pas de recouvrement `slide` de 1) des températures minimales pour la taille de fenêtre passée en paramètre. Les fenêtres incomplètes seront rejetées du calcul.








