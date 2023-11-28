"""
    Nom :
    Prénom :
    M2 Physique 2023
    Exercice 4
"""


def load_file():
    temperatures = []
    # Votre réponse à la question 1 ici
    return temperatures


def window_mean():
    m = 0
    # Votre réponse à la question 2 ici
    return m

def moving_average():
    moving = 0
    slide = 1
    # Votre réponse à la question 3 ici
    return moving


if __name__ == '__main__':
    filename = "temperatures_moule.csv"
    T = load_file(filename)
    width = 5

    moving = moving_average(T, width=width)


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