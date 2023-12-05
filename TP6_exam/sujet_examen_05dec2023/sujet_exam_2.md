@author scholet @date december 2023


# Informations générales
__Examen du 28 novembre 2023__

L'examen dure 2h, conformément à ce qui est prévu dans la maquette de la formation. Le délai court à compter du top donné en séance.

L'examen comporte deux types de questions :
- des questions où une réponse écrite est attendue. Pour ces questions, vous devez rédiger la réponse en français, en formulant des phrases (sujet + verbe + complément). 
- des questions où une réponse sous la forme d'un code source est attendue. Pour ces questions, vous devez produire le code source dans un fichier Python.

Pendant toute la durée de l'examen :
- Vous ne devez pas communiquer avec les autres étudiants, ni avec qui que ce soit, par aucun moyen ; en dehors du surveillant.
- Votre téléphone portable doit être en mode silencieux, rangé dans un sac, hors de votre portée et de votre vue. Vous ne devez pas y accéder.
- Vous ne devez pas porter d'écouteurs.
- L'utilisation de tout appareil est interdite, à l'exception de l'ordinateur que vous utilisez pour composer.

Vous allez remettre deux types éléments :
- une feuille, sur laquelle vous aurez répondu (de manière manuscrite) aux exercices de la première partie (questions de cours).
- des programmes Python, pour les exercices de la seconde partie (questions de programmation).

Certaines questions de la deuxième partie nécessitent une réponse rédigée. Dans ce cas, vous rédigerez votre réponse directement dans le fichier à remettre.

Les programmes Python doivent être envoyés à (faites un copier-coller) : `scholet.pro+m2physique@proton.me`.

Pendant toute la durée de l'examen :
- L'utilisation du cours, de vos notes personnelles et des TP que vous avez réalisés est autorisée.
- L'utilisation de la documentation trouvée sur Internet est autorisée pendant l'examen.
- L'utilisation de ChatGPT n'est pas autorisée. Aucune forme d'IA n'est autorisée.


# Questions de cours (10 points)

## Exercice 1 (6 points)

Les questions 1 à 6 valent chacune 1 point.

1. Choisir la ou les bonnes réponses :
   - [ ] Une fonction est un bloc de code qui prend des variables en entrée et qui retourne un résultat, calculé dans le corps de la fonction 
   - [ ] Une fonction est un bloc de code réemployable, et qui remplit un objectif précis.
   - [ ] Une fonction peut renvoyer plusieurs résultats. Dans ce cas, elle retourne un tableau.
   - [ ] Une fonction est une variable qui ne stocke pas une valeur, mais un code source.
   - [ ] Dans une fonction, un affichage n'est pas considéré comme un retour.
2. Un camarade vous avoue ne pas faire la différence entre `print` et `input`, en Python. Expliquez-lui.
3. Citer quelques différences notables entre les tableaux Python "purs" et les tableaux Numpy. Donnez par exemple des cas où l'un est préférable à l'autre, et vice-versa.
4. Un camarade (le même) vous avoue ne pas saisir l'analogie entre une classe et une variable. Expliquez-lui.
5. Si on commence une boucle `for` à 1 et qu'on précise, dans le `range`, qu'elle doit arriver à 15 par pas de 2, combien d'itérations la boucle réalisera-t-elle ?
6. Quelle est la différence entre _gérer une erreur_ et _éviter une erreur_, en Python ?



## Exercice 2 (4 points)

Les questions 1 et 2 valent 1 point. La question 3 vaut 2 points.

Soit le snippet suivant :

```python
def magic_function(n):
    if n < 2:
        return 1
    else:
       return magic_function(n-1) + magic_function(n-2) 
```

1. Sans lancer le programme, donnez le résultat de la fonction pour les valeurs `n=2` et `n=4`. Vous détaillerez et justifierez votre raisonnement.
2. La fonction `magic_function(n)` calcule en réalité un résultat bien connu. De quoi s'agit-il ? 
3. Donnez une version de cette fonction fonctionnant avec une boucle `for`.


# Questions de programmation (10 points + 7 bonus)

**NOTE**: vous devez faire l'exercice 3, impérativement, plus l'un des deux exercices 4 ou 5, au choix.

Si vous faites les deux exercices 4 et 5, vous n'obtiendrez les points des deux exercices que si vous obtenez au moins 6 points (sur 7) à l'un d'entre-eux. Dans ce cas, vous aurez des points bonus, dans la limite d'une note sur 20. Il vous est recommandé d'en choisir un seul et de vous concentrer dessus.


## Exercice 3 (3 points)

La question 1 vaut 2 points. La question 2 vaut 1 point.

Un étudiant ayant passé le contrôle continu explique aux étudiantes qui s'apprêtent à passer le contrôle continu de substitution le principe du bonus lié aux exercices 4 et 5 : 
> Yo, pour le devoir, c'est simple : fais l'exo 3 obligé et choisis entre le 4 et le 5, peu importe. Si tu fais qu'un des deux, c'est cool, les points de celui-là comptent. Mais si t'as la motivation, fais les deux 4 et 5. Attention, si tu fais les deux, ils comptent que si l'un d'eux a au moins 6 points sur 7. Sinon, seul le mieux noté est pris en compte. Et oublie pas, la note max c'est 20. Bonne chance ! 

1. Créer une fonction `compute_mark()` qui prend en paramètre deux nombres de points `points_exo_4` et `points_exo_5`, et qui renvoie le nombre de points qui sera pris en compte pour la note au contrôle continu. Lorsqu'un seul exercice est réalisé, la valeur de `points_exo` à passer en paramètre pour l'autre exercice vaut `None`.
2. Dans le `__main__`, ajouter le code nécessaire pour afficher la note de contrôle continu liée aux points suivants : exercice 1 : 6 points, exercice 2 : 3 points, exercice 3 : 2 points, exercice 4 : 6 points, exercice 5 : 4.5 points. 

## Exercice 4 (7 points)

La question 1 vaut 1 point. Les questions 2, 3 et 4 valent chacune 2 points.

On cherche à calculer une valeur suivant le procédé suivant :
> On commence par choisir un nombre `n` à quatre chiffres, par exemple 8745. A partir de `n`, on produit deux nombres `n1` et `n2`, tel que `n1 > n2`. Le calcul de `n1` et `n2` est réalisé par fonction `mystery_func` qui se trouve dans le fichier `./stubs/exercice_4.py`. Ensuite, on soustrait le plus grand de ces nombres au plus petit. On répète alors l'opération un grand nombre de fois, en prenant, à chaque répétition, `n = n1 - n2`.

**Note** : Pour être sûr d'avoir bien compris le procédé, et après avoir lu l'exercice dans son intégralité et répondu à la question 1, vous pouvez simuler manuellement le processus pour quelques répétitions et noter chaque `n`. Cette étape pourra être vérifiée par le surveillant, qui vous indiquera si votre compréhension est correcte ou non, à l'exception de toute autre indication.

1. Tester la fonction `mystery_func` fournie dans le fichier `./stubs/exercice_4.py`, avec plusieurs valeurs pour `n`. Compte tenu des résultats obtenus, dire en une phrase ce que fait la fonction `mystery_func`. Noter qu'il n'est pas demandé d'étudier le code source de la fonction, mais seulement son résultat
2. Créer une fonction `repeat_process()` qui prend en paramètre un nombre `n` et un nombre de répétitions `nb_times`, et qui fournit en sortie un tableau Numpy `T`. Dans `T`, chaque ligne `[i, n]` indique la valeur `n` calculée à la répétition numéro `i` du procédé. La première ligne du tableau doit contenir la valeur de `n` passée en paramètre (avec `i=0`).
3. Créer une fonction `converges()` qui prend en paramètre une liste `values` et qui fournit en sortie deux valeurs : un booléen `is_convergent` et une valeur `towards_value`. La fonction détermine si les valeurs de la deuxième colonne de `T` convergent vers une valeur. Si c'est le cas, alors `is_convergent` vaut `True` et `towards_value` vaut la valeur vers laquelle la liste `values` converge. Sinon, `is_convergent` vaut `False` et `towards_value` vaut `None`. Une aide est fournie dans le fichier `./stubs/exercice_4.py`.
4. Créer une fonction `test_values()` qui prend en paramètre un nombre `nb_tests` et qui ne renvoie rien. La fonction teste le procédé `nb_tests` fois, avec à chaque fois un nombre de 4 chiffres généré aléatoirement. A chaque test, elle affiche s'il y a eu convergence, et si c'est le cas, elle affiche aussi la valeur de convergence. Sinon, elle affiche qu'il n'y a pas eu convergence.


## Exercice 5 (7 points)

La question 1 vaut 0.5 point. La question 2 vaut 1 point. Les questions 3 et 4 valent chacune 2 points. La question 5 vaut 1.5 points.

Un client de EDF vous fait parvenir son relevé de consommation électrique dans le fichier `./stubs/electricity_consumption_data.csv`.

**Note** : tous les graphiques demandés devront être présentables (titre, titre des axes, etc.).

1. Etudiez le fichier. En particulier, précisez les variables qu'il contient ainsi que le nombre d'observations.
2. Créer une fonction `load_file()` qui prend en paramètre le chemin vers un fichier csv `filename` et qui renvoie les données `data` qu'il contient. Il est recommandé d'utiliser Pandas. Vous devrez utiliser cette fonction pour charger les données du fichier `./stubs/electricity_consumption_data.csv`.
3. Créer une fonction `graphique_1()` qui prend en paramètre les données (issues de la fonction `load_file()`) et qui ne renvoie rien. La fonction affiche un graphique de la consommation journalière du client, heure par heure, tous équipements confondus. 
4. Créer une fonction `graphique_2()`qui prend en paramètre les données (issues de la fonction `load_file()`) et qui ne renvoie rien. La fonction affiche un graphique comprenant :
   - La consommation électrique journalière, heure par heure, tous équipements confondus (comme à la question 3.)
   - La consommation électrique journalière, heure par heure, du climatiseur (en bleu), de l'éclairage (en vert) et de la cuisine (en orange). Votre graphique devra présenter une légende.
5. Créer une fonction `consumer()` qui prend en paramètre les données (issues de la fonction `load_file()`) et le nom d'un équipement `equipment_name`, et qui renvoie une valeur numérique `consumption`. La fonction calcule et renvoie la consommation électrique de l'équipement dont le nom est passé en paramètre.
6. [Bonus - Pour 1 point] Dans le `__main__`, ajoutez le code nécessaire afin d'afficher le nom de l'équipement le plus gourmand en électricité.