---
title: Matrices
date: 2019
---

## Introduction aux matrices



## Testez votre code!

Testez votre code le plus régulièrement possible. C'est important pour savoir où
se trouve le bug, car bug il y aura !

Avec ce sujet vous seront fournis plusieurs fichiers tests vous permettant de
vérifier que votre code fonctionne.

Pour être certain que votre travail est correct, et que vous puissiez le tester,
il vous faudra respecter quelques règles :

- Nommer votre fichier *matrices.py*, toutes vos fonctions devront se trouver
  dans ce fichier
- Respecter les noms de fonctions précisés dans les énoncés suivants
- Exécuter le fichier test avec `./tests-matrices.py` dans le terminal


## Pratiquons !


### Exercice 1 : initialiser une matrice

**But** : écrire la fonction `initMat(lignes, cols, val)` qui cree une matrice de
dimensions 'lignes' par 'cols' et met chaque case de cette matrice a la valeur
'val'.

**Exemple** :

```python
initMat(3, 2, 42)
```

creera la matrice

```
42 42
42 42
42 42
```


### Exercice 2 : afficher une matrice

**But** : écrire la fonction `printMat(m)` qui affichera la matrice prise en
parametre en separant chaque terme affiche par un espace, et un retour a la
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


### Exercice 3 : laissons une trace

**But** : écrire la fonction `trace(m)` qui prend une matrice carree en
parametre, calcule la somme des elements sur sa diagonale et la renvoit.

**Exemple** :

```python
m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

printf(trace(m))
```

affichera `15`.


### Exercice 4 : ajoutons deux matrices !

**But** : écrire la fonction `addMat(a, b)` qui ajoute les valeurs des deux
matrices a et b **si et seulement si** elles sont de memes dimensions.
Dans le cas inverse, votre fonction doit renvoyer la valeur `None`.

*__Tips__ : pour ajouter deux matrices de memes tailles, on ajoute simplement les
valeurs des cases qui se situent au meme endroit, et ca pour chaque case.
La matrice resultante de l'addition aura donc les memes dimensions que les deux
matrices prises en parametres.*

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

resultat = ajouter(a, b)

afficher(resultat)
```

affichera

```python
2 4 6
8 10 12
14 16 18
```


### Exercice 5 : symetrie sur la diagonale

**But** : ecrire la fonction `symmetricDiag(m)` qui renvoie `True` si la matrice
est symetrique par rapport a l'axe de sa diagonale, `False` sinon.

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

**But**: ecrire la fonction `minimax(m)` qui determine la valeur minimale parmi
les maximums de chaque ligne de la matrice passee en parametre.

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

*__Tips__ : il faut diviser le probleme, et ecrire plusieurs fonctions
differentes pour trouver une solution efficace a cet exercice. Par exemple, on
peut ecrire une fonction qui permet de determiner le maximum d'une seule ligne,
une fonction qui stocke ces maximums dans une liste, et une fonction qui permet
de trouver le minimum parmi tous ces maximum.*


### Exercice 7 : les crateres de la Lune

On represente une partie de la Lune vue de haut dans une matrice.
Les cercles dans la matrice representent les crateres formes a la surface de la
Lune. Ces cercles sont dessines avec des '#'.
Tout le reste de la surface de la Lune est represente par des '.'.

**But** : ecrire la fonction `craters(m)` qui compte le nombre de crateres
dessines dans la matrice passee en argument.

Vous trouverez dans le dossier `maps` des exemples de terrains pour tester
votre code. Sur le fichier `0.map`, votre fonction devrait renvoyer `0`, sur le
fichier `1.map`, elle devrait renvoyer `1`, et sur le fichier `3.map`, elle
devrait renvoyer `3`.

Il vous faudra completer le fichier `craters.py`, dans lequel vous trouverez
certaines fonctions deja ecrites, vous permettant d'ouvrir un fichier et de
creer une matrice en le lisant ligne par ligne. Il est certainement interessant
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

Sur cette partie de la Lune, il y a 3 crateres. Votre fonction `craters` devrait
alors renvoyer la valeur `3`.
