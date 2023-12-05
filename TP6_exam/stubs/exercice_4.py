from random import random, randint
import numpy as np

"""
    Exercice 4
    CC Substitution 5 décembre 2023
    Introduction à Python 
    M2 Physique, Université des Antilles
    Nom et Prénom : 
"""


def mystery_func(n):
    digits = [int(digit) for digit in str(n)]

    ascending_order = int(''.join(map(str, sorted(digits))))
    descending_order = int(''.join(map(str, sorted(digits, reverse=True))))

    return descending_order, ascending_order

def repeat_process(n, nb_times):
    T = []
    # Votre réponse à la question 2 :

    return np.array(T)


def converges():
    # N'oubliez pas l'entrée de la fonction
    is_convergent = False
    towards_value = None

    # Une manière simple (et naive) de vérifier si les valeurs de la liste convergent est de vérifier si plusieurs valeurs à la fin de la liste sont identiques à la dernière valeur de la liste.
    # On pose ensuite un seuil, par exemple 5, et on dit que la liste converge si les 5 dernières valeurs de la liste sont identiques à la dernière valeur de la liste.
    # Attention, pour que cela ait du sens, il faut que la liste soit assez grande par rapport au seuil.

    last_value = values[-1]
    nb_identical = 0
    threshold = 5

    # Votre réponse à la question 3


    # N'oubliez pas le retour de la fonction


def test_values(nb_tests):
    random_integers = []

    # Génération d'un nombre aléatoire à 4 chiffres
    for i in range(nb_tests):
        random_integers.append(randint(1000, 10000))

    for r in random_integers:
        # Votre réponse à la question 4


if __name__ == '__main__':
    n = 4844
    nb_times = 10
    #T = repeat_process(n, nb_times)
    #print(T)

    # c, val = converges(T[:, 1])
    # print(c, val)

    #nb_tests = 50
    # test_values(nb_tests)

"""
    Votre réponse à la question 1 :

"""