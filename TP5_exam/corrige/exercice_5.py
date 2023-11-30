"""
    Nom :
    Prénom :
    M2 Physique 2023
    Exercice 4
"""
import pandas as pd


def load_file(filename):
    temperatures = []
    # Votre réponse à la question 1 ici
    temperatures = pd.read_csv(filename, sep=";")
    return temperatures


def window_mean(T, start, end):
    m = 0
    # Votre réponse à la question 2 ici

    for i in range(start, end+1):
        m += T["temperature_max"].iloc[i]

    return m / (end+1 - start)

def moving_average(T, width):
    moving = 0
    slide = 1
    # Votre réponse à la question 3 ici
    len_T = len(T)
    nb_mean = 0

    for i in range(0, len_T, slide):

        if len_T - i < width:
            break
        else:
            mean = window_mean(T, i, i+width-1)
            nb_mean += 1

            moving += mean


    return moving / nb_mean


if __name__ == '__main__':
    filename = "../stubs/temperatures_moule.csv"
    T = load_file(filename)
    width = 5

    m = window_mean(T, 1, 10)

    moving = moving_average(T, width=width)
    print(moving)


"""
Illustration de la moyenne glissante avec un pas de recouvrement de 1et rejet des fenêtres incomplètes.

Soient les valeurs [1, 5, 9, 6, 7, 5], une largeur de 3 et un recouvrement de 1.
La moyenne classique est : (1 + 5 + 9 + 6 + 7 + 5) / 6 = 5.5
La moyenne glissante de taille 3 et de recouvrement 1 est calculée ainsi :
(1 + 5 + 9) / 3 = 15/3 = 5
(5 + 9 + 6) / 3 = 20/3 = 6.66
(9 + 6 + 7) / 3 = 22/3 = 7.33
(6 + 7 + 5) / 3 = 18/3 = 6
Comme il reste moins de trois éléments à partir de 7, on rejette le reste des données.

La moyenne glissante est de  : (5 + 6.66 + 7.33 + 6) / 4 = 6.57
"""