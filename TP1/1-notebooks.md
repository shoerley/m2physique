@author scholet @date 4 oct 2023

# Notebooks

Les notebooks sont (encore) une manière de programmer en Python. Ils sont pratiques pour faire du pas à pas, plutôt que d'écrire beaucoup de code pour ensuite le tester. Ils sont également pratiques pour rédiger des rapports intégrant des expérimentations (calculs, graphiques, etc.) : de la sorte, il n'est plus nécessaire de copier-coller des captures d'écrans dans des fichiers words.

Voir un exemple ici : https://jupyter.org/try-jupyter/lab/?path=notebooks%2FIntro.ipynb

Les notebooks sont composés de cellules, qu'il est possible d'exécuter séparément. Une cellule peut contenir du texte, des images, mais aussi et surtout du code source.

# Exercice

Localisez le notebook sous TP1/ressources/notebook-toy sur le Github consacré au TP.

1. Depuis https://jupyter.org/try-jupyter, implémentez le notebook et essayez-le. Pour ce faire, créez les cellules dans Jupyter et exécutez-les.

2. Que contiennent `x` et `y`, compte tenu de la documentation sur `np.linspace()` ?

3. Essayez d'autres types de représentations : scatter, hist, et stem ; en particulier

4. Pour chaque type de représentation, faites varier les options d'affichage :
   * type de marqueur
   * couleur des lignes
   * titre des axes et du graphique

Dans tous les cas, consultez la documentation de matplotlib !

# Code du notebook

```python
   import numpy as np
   from matplotlib import pyplot as plt
   
   x = np.linspace(0, 10, 100)
   y = 4 + 2 * np.sin(2 * x)
   
   plt.plot(x, y)
   plt.show
```

