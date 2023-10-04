@author scholet @date 4 oct 2023

# Graphiques en Python

Le package matplotlib peut être utilisé pour afficher des graphiques (_chart_, en anglais) en Python. Avant toute chose, il faut importer le package. Il est d'usage de le renommer en `plt`.

```python
import matplotlib as plt
```

Les données qui vont servir de support à un graphique peuvent idéalement être présentes dans une liste python, un tableau `numpy` ou bien une structure `pandas`. Par conséquent, il y a toujours une étape de chargement des données avant l'étape d'affichage d'un graphique - ce qui semble logique.

## Principes de base

La documentation de `matplotlib` est précise à ce sujet. On peut afficher deux type des graphiques : 
* ceux basés sur des points de données. Vous fournissez les données de type (x, y), f(x) = y, ou x(_1, ..., x_n), et elles sont affichées en tant que telles.
* ceux basés sur des statistiques. Vous fournissez des données de type x(_1, ..., x_n), et on affiche leur distribution (ou calculs relatifs)

### Plot et Scatter




