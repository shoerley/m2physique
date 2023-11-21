@author scholet @date november 2023

# Répertoire d'ouragans

On cherche à créer un outil permettant d'enregistrer des ouragans dans un fichier texte, et de modifier cette liste, à la manière d'un répertoire. Dans ce TP on introduira la notion de classe en Python, et de manière plus générale, celle de programmation orientée objet.

## 1. Attributs d'un ouragan

Déterminez quels attributs (i.e. propriétés) doivent avoir un ouragan. Implémentez la classe Ouragan et initialisez ses attributs. Chaque attribut doit avoir un `setter` et un `getter`.

## 2. Affichage d'un ouragan

Créez une fonction, dans la classe Ouragan, capable d'afficher un ouragan. Vous devrez choisir quels attributs afficher.

## 3. CRUD

En informatique, l'acronyme CRUD fait référence à Create, Read, Update, Delete. Il s'agit d'opérations de base pour la manipulation de données. 

Dans cette question, vous vous servirez d'un fichier comme base de données. Tout ajout d'un ouragan, modification ou suppression doit être répercutée dans la base de données. Pour ce faire, vous devez imaginer un `pipeline d'opérations` pour chaque action CRUD. Par exemple, pour la création, affecter une variable ne suffit pas : il faut ensuite la persister dans le fichier, et recharger le fichier. Un pipeline fait simplement référence à une suite d'instructions, par exemple : instancier une classe, interroger l'utilisateur, affecter les variables, stocker dans un fichier, lire depuis un fichier.

1. Implémentez le pipeline nécessaire pour créer un ouragan.
2. Implémentez le pipeline nécessaire pour stocker et lire des ouragans dans un fichier texte. L'utilisation de Pandas est recommandée, mais vous pouvez utiliser du python pur.
3. Implémentez le pipeline nécessaire pour mettre à jour un ouragan
4. Implémentez le pipeline nécessaire pour supprimer un ouragan.

