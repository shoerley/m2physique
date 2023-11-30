import random
import matplotlib.pyplot as plt
import numpy as np

random.seed(None)
def get_direction():
    choices = [0, 1]
    return random.choice(choices)
def walk(nb_steps=10, start_position=0):

    W = []
    current_position = start_position
    p = 0
    for i in range(nb_steps):
        direction = get_direction()
        if direction == 0:
            current_position += 1
            p += 1
        else:
            current_position -= 1

        W.append([i, current_position])
    return np.array(W)

def experience_1():
    W = walk(nb_steps=300, start_position=203)
    print(f"A son réveil, l'étudiant se trouve en salle TP+{W[-1, 1]}")

if __name__ == '__main__':

    experience_1()
    W = walk(nb_steps=300, start_position=203)

    plt.plot(W[:, 0], W[:, 1])
    plt.title("Evolution de la position de l'étudiante pendant son cauchemar")
    plt.xlabel("Clap")
    plt.ylabel("Salle TP")
    plt.show()

"""
Question 1 : la fonction get_direction() renvoie une valeur parmi 0 ou 1, aléatoirement, suivant une loi uniforme. 

Les séquences renvoyées (en cas d'appels successifs) sont potentiellement différents d'une exécution à l'autre du programme, dans la mesure où la graine du hasard est initialisée à None (comme précisé dans la documentation de Random). Cette précision n'était pas attendue.

Question 4 : malgré 300 déplacements, la salle d'arrivée n'est jamais très loin de la salle de départ. C'est censé si on considère que la probabilité d'avancer et de reculer est la même. 
"""