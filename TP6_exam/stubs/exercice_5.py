import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
    Exercice 5
    CC Substitution 5 décembre 2023
    Introduction à Python
    M2 Physique, Université des Antilles
    Nom et Prénom :
"""


def load_file(filename):
    consumption_data = []

    # Votre réponse à la question 1 ici

    consumption_data["Date"] = pd.to_datetime(consumption_data["Date"], format="%Y-%m-%d %H:%M:%S")
    return consumption_data


def graphique_1(consumption_data):
    heures = consumption_data["Date"]
    conso_horaire = []


    # Votre réponse à la question 2 ici
    # Indication : utilisez les masques Pandas (panda mask)



def graphique_2(consumption_data):
    # Votre réponse à la question 4 dans cette fonction

    heures = consumption_data["Date"]
    conso_horaire = []
    conso_cuisine = []
    conso_eclairage = []
    conso_clim = []


    # Récupération / calcul des consommations horaires
    # ...

    # Conversions vers Numpy
    conso_clim = np.array(conso_clim)
    conso_horaire = np.array(conso_horaire)
    conso_eclairage = np.array(conso_eclairage)
    conso_cuisine = np.array(conso_cuisine)

    # Tracé des lignes
    # ...

    plt.show()


def consumer(consumption_data, equipment_name):
    # Votre réponse à la question 5 dans cette fonction

if __name__ == '__main__':
    filename = "../stubs/electricity_consumption_data.csv"
    consumption_data = load_file(filename)

    # graphique_1(consumption_data)
    # graphique_2(consumption_data)
    # consumer(consumption_data, "ac")

    # Votre réponse à la question 6

"""
    Votre réponse à la question 1 :
    
"""

