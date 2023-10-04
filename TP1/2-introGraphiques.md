@author scholet @date 4 oct 2023

# Graphiques en Python

Le package matplotlib peut être utilisé pour afficher des graphiques (_chart_, en anglais) en Python. Avant toute chose, il faut importer le package. Il est d'usage de le renommer en `plt`.

```python
from matplotlib import pyplot as plt
```

Les données qui vont servir de support à un graphique peuvent idéalement être présentes dans une liste python, un tableau `numpy` ou bien une structure `pandas`. Par conséquent, il y a toujours une étape de chargement des données avant l'étape d'affichage d'un graphique - ce qui semble logique.

## Principes de base

La documentation de `matplotlib` est précise à ce sujet. On peut afficher deux types de graphiques : 
* ceux basés sur des points de données. Vous fournissez les données de type (x, y), f(x) = y, ou x(_1, ..., x_n), et elles sont affichées en tant que telles.
* ceux basés sur des statistiques. Vous fournissez des données de type x(_1, ..., x_n), et on affiche leur distribution (ou calculs relatifs)

### Plot et Scatter

1. Créez un tableau `numpy` contenant des valeurs aléatoires dans 100 lignes et 2 colonnes.

2. En Python, si X est un tableau 2D, alors `X[:, 0]` désigne toutes les lignes de la colonne 0.
   * Comment isoler toutes les lignes de la colonne 1 ?
   * Comment isoler toutes les colonnes de la ligne 8 ?
   * Comment isoler les lignes 10 à 27 des deux colonnes ?

Affichez un `scatter` de `X`, et pour chaque cas, afficher un `scatter` des données isolées.

3. Affichez un `plot` du tableau `X`. Pourquoi a-t-il l'air étrange ?

4. Remplacez la première colonne de `X` par les valeurs de `np.linspace(0, 10, 100)` et la seconde colonne par les valeurs de `4 + 2 * np.sin(2 * x)`.

5. Refaites un `plot` et un `scatter` de `X`. Que constatez-vous ?

## Hist et Boxplot

Hist et Boxplot permettent d'afficher respectivement la distribution et le diagramme à moustaches d'une variable.

1. En vous inspirant du code sous `TP0/loadCsvExamples.py`, chargez dans un tableau numpy le fichier de températures `TP0/ressources/loadCsvExamples.py`. Les colonnes d'indices 1 et 2 contiennent les températures maximales et minimales observées.

2. Affichez un histogramme des températures minimales, et un histogramme des températures maximales.

3. Affichez une boite à moustaches des températures minimales, et un histogramme des températures maximales. Pour cette question, inspirez-vous du snippet suivant.


```python
   ...
   fig, ax1 = plt.subplots(nrows=1, ncols=1)
   ax1.set_ylabel("Température (C°)")
   ax1.set_title("Distribution des températures minimales et maximales\n observées au Moule entre févier et mai 2023")
   boxplot = ax1.boxplot( ??? )
   plt.show()
    ...
```



