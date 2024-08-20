---
title: Matrices
weight: 15
date: 2021
author: Tanguy Segarra
code_stub_url: ./resources/given_resources/matrices.zip
tags:
    - python
showcase: ./resources/showcase.webp
score: 50
description: "Découvre l'univers enchanteur des matrices en Python, transformant les chiffres en toiles numériques où la créativité s'épanouit. 🌟💻"
---

# Introduction aux matrices

Une matrice est un tableau à deux dimensions, une sorte de grille, dans laquelle
chaque case est accessible grâce à ses coordonnées.

Toutes les lignes de la matrice doivent avoir la même longueur.

En Python, les matrices sont représentées par une liste de listes : soit une
grande liste qui est elle-même la matrice et qui contient chaque ligne de la
matrice.
De cette façon, comme pour les listes, les indices dans les matrices commencent
à 0.

$$
\begin{bmatrix}
    1 & 2 & 3 \\\\
    4 & 5 & 6 \\\\
    7 & 8 & 9
\end{bmatrix}
$$

Dans cette matrice, la valeur 5 se trouve aux coordonnées (1, 1).
La valeur 1 se trouve alors aux coordonnées (0, 0).
La valeur 9 se trouve aux coordonnées (2, 2)


{{<figure src="resources/images/1.svg">}}


## Alors en Python, ca donne quoi ?

**Initialiser une matrice**

On peut initialiser une matrice de taille 3 lignes par 2 colonnes remplie de 0
avec

```python
matrice = [[0,0],
           [0,0],
           [0,0]]
```

On peut créer une matrice en manipulant la methode de liste `.append()` et
embriquant deux boucles comme cela :

```python
matrice = []
nb_lignes = 3
nb_colonnes = 2
for lig in range(nb_lignes):
    ligne = []
    for col in range(nb_colonnes):
        ligne.append(0)
    matrice.append(ligne)
```

ou alors de façon plus rapide et "pythonesque" :

```python
M = [[0 for i in range(2)] for j in range(3)]
```

**Parcourir une matrice**

Pour parcourir une matrice, le plus simple est d'utiliser deux boucles
`for` imbriquées. La première doit aller de 0 jusqu'au nombre de lignes, et
celle à l'intérieur doit aller de 0 jusqu'à la largeur d'une ligne de la
matrice.

On peut calculer la hauteur de la matrice (nombre de lignes) dans la matrice M,
en utilisant `len(M)`, qui correspond à la longueur de la liste principale qui
constitue la matrice.

De la même façon, on peut calculer la largeur de la matrice en faisant
`len(M[0])` qui correspond à la longueur de la première ligne de la matrice.
Le fait que ce soit la première ligne n'a pas tant d'importance, mais on est
certain que cette ligne existe à priori.

**Manipuler une matrice**

Soit la matrice M

$$
\begin{bmatrix}
    1 & 2 & 3 \\\\
    4 & 5 & 6 \\\\
    7 & 8 & 9
\end{bmatrix}
$$

Pour accéder à la valeur 6, on appelera `M[1][2]` car 6 se trouve aux
coordonnées (1, 2).


{{<figure src="resources/images/2.svg">}}

On peut aussi changer la valeur d'une case directement.
Par exemple, la valeur dans le coin supérieur gauche peut être mise à 42 avec

```python
M[0][0] = 42
```

On peut aussi accéder à toute la première ligne de la matrice avec `M[0]`.

Vous avez maintenant tous les outils pour vous lancer dans les exercices !
Bon courage et n'hésitez pas à poser des questions !

# Testez votre code!

Avec ce sujet est fourni un fichier vous permettant de vérifier que votre code
fonctionne comme il le devrait.

Pour que la vérification se passe bien, il faudra
- Respecter les noms de fonctions précisés dans les énoncés suivants
- Lancer les tests avec `./tests-matrices.py <votre-fichier>` dans le terminal


# Pratiquons !

Pour certains de ces exercices, on représente le terrain de chasse d'un loup
dans une matrice P.  Le caractère 'M' représente alors un mouton, et le
caractere 'L' représente le loup.  Un '.' représente simplement une case du
terrain qui est vide, de l'herbe !  Le loup ne peut manger que les moutons qui
se situent autour de lui directement.

## Exercice 1 : présence dans une matrice

On représente une prairie dans une matrice.
Le caractère 'M' représente un mouton. On souhaite savoir s'il y a au moins un
mouton dans la prairie P, soit au moins une fois le caractère 'M' dans la
matrice.

**But** : écrire la fonction `is_in_matrix(P, val)` qui renvoie `True` si la
valeur 'val' est présente dans la matrice, `False` sinon.

**Exemple** :

```python
prairie = [

        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', 'M', '.']

    ]

print(is_in_matrix(prairie, 'M'))
```

{{<figure src="resources/images/3.svg">}}

affichera `True`

et

```python
prairie_vide = [

        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']

    ]

print(is_in_matrix(prairie_vide, 'M'))
```

affichera `False`.


## Exercice 2 : coordonnées dans une matrice

On représente encore une prairie P dans une matrice, et on cherche toujours le
mouton 'M' sauf que cette fois on veut connaitre sa position exacte !


**But** : écrire la fonction `search_matrix(P, val)` qui renvoie une liste
contenant deux éléments, l'indice de la ligne et l'indice de la colonne sur
lesquelles se trouve la valeur recherchée 'val'.

On admet que l'élément recherché **est présent une seule fois** dans la
matrice.

**Exemple** :

```python
prairie = [

        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', 'M', '.']

    ]

print(search_matrix(prairie, 'M')
```

affichera `[2, 1]` car 'M' se situe sur la ligne 2 et la colonne 1.


## Exercice 3 : toutes les coordonnées !

Cette fois-ci, la matrice qui représente la prairie P peut contenir plusieurs
moutons 'M'.
On veut alors savoir toutes les positions des moutons.


**But** : écrire la fonction `search_all(P, val)` qui renvoie une liste
contenant tous les duos de coordonnées sur lesquelles on peut trouver la valeur
recherchée 'val'.

**Exemple** :

```python
prairie = [

        ['.', '.', 'M'],
        ['.', '.', '.'],
        ['.', 'M', '.']

    ]

print(search_all(prairie, 'M'))
```

affichera `[[0, 2], [2, 1]]` car il y a un 'M' sur la ligne 0 et la colonne 2,
et un autre sur la ligne 2 et la colonne 1.


## Exercice 4 : compter les moutons...

On veut savoir combien de moutons se trouvent dans la prairie.

**But** : écrire la fonction `count(P, val)` qui renvoie le nombre de fois où
est présente la valeur `val` dans la matrice P.

**Exemple** :

```python
prairie = [

        ['.', '.', 'M'],
        ['.', '.', '.'],
        ['.', 'M', '.']

    ]

print(count(prairie, 'M'))
```


affichera `2`.


## Exercice 5 : initialiser une matrice

**But** : écrire la fonction `init_matrix(lines, cols, val)` qui crée une
matrice de dimensions 'lines' par 'cols', parcourt la matrice et met chaque
case de cette matrice à la valeur 'val'.

**Exemple** :

```python
init_matrix(3, 2, 42)
```

créera la matrice

```text
42 42
42 42
42 42
```


## Exercice 6 : afficher une matrice

**But** : écrire la fonction `print_matrix(M)` qui affichera la matrice prise en
paramètre en séparant chaque terme affiché par un espace, et un retour à la
ligne en fin de ligne de matrice.

**Exemple** :

```python
M = [
        [1, 2, 3],
        [4, 5, 6]
    ]

print_matrix(M)
```

affichera

```python
1 2 3
4 5 6
```


## Exercice 7 : somme des éléments de la matrice

**But** : écrire la fonction `sum_matrix(M)` qui prend une matrice en paramètre,
et renvoie la somme de tous ses éléments.

**Exemple** :

```python
M = [
        [1, 2],
        [4, 5],
        [2, 8]
    ]

print(sum_matrix(M))
```

affichera `22`.


## Exercice 8 : ajouter deux matrices

**But** : écrire la fonction `add_matrix(a, b)` qui ajoute les valeurs des deux
matrices a et b dans une nouvelle matrice **si et seulement si** elles sont de
mêmes dimensions.  Si les dimensions sont invalides, votre fonction doit
renvoyer la valeur `None`, au lieu de renvoyer la matrice nouvellement créée.

*__Tips__ : `None` est la valeur qui représente littéralement RIEN. On s'en sert
souvent pour dire qu'il est impossible de faire ce qui est demandé donc on ne
renvoie rien. Cela sert surtout pour vérifier la valeur de retour de l'appel à
une fonction. Si la valeur est `None`, on sait que ca a échoué.*

*__Tips__ : pour ajouter deux matrices de mêmes tailles, on ajoute simplement
les valeurs des cases qui se situent au même endroit, et cela pour chaque case.
La matrice résultante de l'addition aura donc les mêmes dimensions que les deux
matrices prises en paramètres.*

**Exemple** :

```python
a = [
        [1, 2],
        [4, 5],
        [7, 8]
    ]

b = [
        [1, 2],
        [4, 5],
        [7, 8]
    ]

resultat = add_matrix(a, b)

print_matrix(resultat)
```

affichera

```python
2 4
8 10
14 16
```


## Exercice 9 : symétrie sur la diagonale

**But** : écrire la fonction `sym_diago(m)` qui renvoie `True` si la matrice
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


## Exercice 10 : minimax

**But**: écrire la fonction `minimax(m)` qui calcule les maximums de chaque
ligne de la matrice passée en paramètre puis renvoie la valeur minimum entre
ces maximums.


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
et une fonction qui permet de trouver le minimum parmi tous ces maximums.*


## Exercice 11 : une faim de loup


**But** : écrire la fonction `eat(P)` qui prend une matrice représentant le
terrain en paramètre et renvoie le nombre de moutons que va pouvoir manger le
loup. Le loup ne peut manger que les moutons sur les cases adjacentes : les 8
cases qui se trouvent autour de la case cible.

**Exemple** :

```text
..................
..M...............
.............M....
......M...........
....ML............
.....M............
..M........M......
..................
```

Votre fonction `eat` doit renvoyer `3` sur cette matrice, car il y a trois
moutons sur les cases adjacentes au loup.

Si la matrice ne contient pas de loup, ou pas de moutons, ou aucun des deux,
alors votre fonction doit renvoyer `0`.


## Exercice 12 : les cratères de la Lune

On représente une partie de la Lune vue de haut dans une matrice.
Les cercles dans la matrice représentent les cratères formés à la surface de la
Lune. Ces cercles sont dessinés avec des '#'.
Tout le reste de la surface de la Lune est représenté par des '.'.


**But** : écrire la fonction `craters(m)` qui compte le nombre de cratères
dessinés dans la matrice passée en argument.

**Exemple** :

```text
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

On admet que deux cratères ne peuvent pas se toucher.

*_Tips_ : réfléchissez à une solution par vous-même, et après cela n'hésitez pas
à demander à un.e organisat.eur.rice de vous donner un petit coup de pouce !*
