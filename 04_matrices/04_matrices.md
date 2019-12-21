---
title: Matrices
date: 2019
---

## Introduction aux matrices

Une matrice est un tableau a deux dimensions, une sorte de grille, dans laquelle
chaque case est accessible grâce à ses coordonnées.

Toutes les lignes de la matrice doivent avoir la même longueur.

En python, les matrices sont représentées par une liste de listes.
Une grosse liste qui est elle-même la matrice et qui contient chaque ligne de la
matrice.
De cette facon, comme pour les listes, les indices dans les matrices commencent
à 0.

```
1  2  3
4  5  6
7  8  9
```

Dans cette matrice, la valeur 5 se trouve aux coordonnées (1, 1).
La valeur 1 se trouve alors aux coordonnées (0, 0).
La valeur 9 se trouve aux coordonnées (2, 2)

Une matrice est dite carrée si son nombre de colonnes est égal à son nombre de
lignes. Une matrice de 3 lignes par 3 colonnes est carrée, une matrice de 4
lignes par 5 colonnes ne l'est pas.


Alors en python, ca donne quoi ?

Pour créer la matrice, on crée simplement une liste:

```python
M = []
```

puis pour y ajouter une ligne, on va `append` (ajouter dans la liste) à cette
liste... une autre liste vide !

```python
M = []
M.append([])
```

Notre matrice contient maintenant une ligne.

Pour ajouter des valeurs à cette ligne, on peut faire

```python
M[0].append(1) #on ajoute 1 a la ligne 0 de la matrice
M[0].append(2)
M[0].append(3)
```

A présent, notre matrice contient une seule ligne, qui contient les valeurs 1, 2
et 3.

Pour avoir une seconde ligne qui contient les valeurs 4, 5 et 6, on peut soit
faire comme au-dessus

```python
M.append([]) #pour ajouter une deuxieme ligne vide apres la premiere ligne
M[1].append(4) #on ajoute 4 a la ligne 1 de la matrice
M[1].append(5)
M[1].append(6)
```

soit plus efficacement,

```python
M.append([4, 5, 6])
```

Maintenant, notre matrice M ressemble à

```
1  2  3
4  5  6
```

Pour accéder à la valeur 6, on appelera `M[1][2]` car 6 se trouve aux
coordonnées (1, 2).

Vous avez maintenant tous les outils pour vous lancer dans les exercices !
Bon courage et n'hésitez pas à poser des questions !

## Testez votre code!

Avec ce sujet est fourni un fichier vous permettant de vérifier que votre code
fonctionne comme il devrait.

Pour que la vérification se passe bien, il faudra
- Respecter les noms de fonctions précisés dans les énoncés suivants
- Lancer les tests avec `./tests-matrices.py <votre-fichier>` dans le terminal


## Pratiquons !


### Exercice 0 : rechercher dans une matrice

**But** : écrire la fonction `searchMat(M, val)` qui renvoie l'indice de la
ligne à laquelle se trouve la valeur `val` recherchée, ou -1 si la valeur n'est
pas présente dans la matrice.

**Exemple** :

```python
m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

print(searchMat(M, 8)
```

affichera `2`.


### Exercice 1 : initialiser une matrice

**But** : écrire la fonction `initMat(lignes, cols, val)` qui crée une matrice
de dimensions 'lignes' par 'cols' et met chaque case de cette matrice à la
valeur 'val'.

**Exemple** :

```python
initMat(3, 2, 42)
```

créera la matrice

```
42 42
42 42
42 42
```


### Exercice 2 : afficher une matrice

**But** : écrire la fonction `printMat(m)` qui affichera la matrice prise en
paramètre en séparant chaque terme affiché par un espace, et un retour à la
ligne en fin de ligne de matrice.

**Exemple** :

```python
m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

printMat(m)
```

affichera

```python
1 2 3
4 5 6
7 8 9
```


### Exercice 3 : laisser une trace

**But** : écrire la fonction `trace(m)` qui prend une matrice en paramètre,
calcule la somme des éléments sur sa diagonale (du coin en haut à gauche, au
coin en bas à droite) et la renvoie.

Si la matrice n'est pas carrée, votre fonction doit renvoyer `None`.

**Exemple** :

```python
m = [
        [1, 2, 3],
        [4, 5, 6],
        [2, 8, 9]
    ]

printf(trace(m))
```

affichera `15`.


### Exercice 4 : ajouter deux matrices

**But** : écrire la fonction `addMat(a, b)` qui ajoute les valeurs des deux
matrices a et b **si et seulement si** elles sont de mêmes dimensions.
Dans le cas inverse, votre fonction doit renvoyer la valeur `None`.

*__Tips__ : pour ajouter deux matrices de mêmes tailles, on ajoute simplement
les valeurs des cases qui se situent au même endroit, et cela pour chaque case.
La matrice résultante de l'addition aura donc les mêmes dimensions que les deux
matrices prises en paramètres.*

**Exemple** :

```python
a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

b = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

resultat = addMat(a, b)

printMat(resultat)
```

affichera

```python
2 4 6
8 10 12
14 16 18
```


### Exercice 5 : symétrie sur la diagonale

**But** : écrire la fonction `symmetricDiag(m)` qui renvoie `True` si la matrice
est symétrique par rapport à l'axe de sa diagonale (du coin en haut à gauche, à
son coin en bas à droite), `False` sinon.

**Exemple** :

```python
m = [
        [1, 2, 5],
        [2, 1, 8],
        [5, 8, 1]
    ]

print(sym_diago(m))
```

affichera `True` et

```python
a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

print(sym_diago(a))
```

affichera `False`.


### Exercice 6 : minimax

**But**: écrire la fonction `minimax(m)` qui détermine la valeur minimale parmi
les maximums de chaque ligne de la matrice passée en paramètre.

**Exemple** :

```python
m = [
        [11, 42, 39],
        [12, 15, 86],
        [98, 56, 27]
    ]

print(minimax(m))
```

affichera `42`.

*__Tips__ : il faut diviser le problème et écrire plusieurs fonctions
différentes pour trouver une solution efficace à cet exercice. Par exemple, on
peut écrire une fonction qui permet de déterminer le maximum d'une seule ligne,
une fonction qui stocke ces maximums dans une liste, et une fonction qui permet
de trouver le minimum parmi tous ces maximum.*


### Exercice 7 : les cratères de la Lune

On représente une partie de la Lune vue de haut dans une matrice.
Les cercles dans la matrice représentent les cratères formés à la surface de la
Lune. Ces cercles sont dessinés avec des '#'.
Tout le reste de la surface de la Lune est représenté par des '.'.


**But** : écrire la fonction `craters(m)` qui compte le nombre de cratères
dessinés dans la matrice passée en argument.

Vous trouverez dans le dossier `maps` des exemples de terrains pour tester
votre code. Par exemple, sur le fichier `0.map`, votre fonction devrait renvoyer
`0`, et sur le fichier `3.map`, elle devrait renvoyer `3`.

Il vous faudra compléter le fichier `craters.py`, dans lequel vous trouverez
certaines fonctions déjà écrites, vous permettant d'ouvrir un fichier et de
créer une matrice en le lisant ligne par ligne. Il est certainement intéressant
pour vous de lire ces fonctions afin d'en apprendre un peu plus sur la
manipulation de fichier en python.

**Exemple** :

```
.........................................
.........................................
....#####................................
...#.....#...............................
...#......#..............................
....#.....#..............................
.....##.##........#####..................
.......#.........#.....#.................
..................#.....#................
...................#....#................
....................#####................
...........###...........................
..........#...#..........................
..........#...#..........................
...........###...........................
.........................................
.........................................
```

Sur cette partie de la Lune, il y a 3 cratères. Votre fonction `craters` devrait
alors renvoyer la valeur `3`.

A noter : par soucis de simplicité, aucun bout de cratère ne peut se trouver
sur les bords de la matrice. Autrement dit, pas de '#' sur la première ligne,
première colonne, dernière ligne et dernière colonne de la matrice.

*_Tips_ : réfléchissez à une solution par vous-même, et apres cela n'hésitez pas
à demander à un.e organisat.eur.rice de vous donner un petit coup de pouce !*
