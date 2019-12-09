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

Pour être certains que tout cela se passe dans les règles de l'art, il vous
faudra respecter quelques règles :

- Nommer votre fichier *tp_listes.py*, toutes vos fonctions devront se trouver
  dans ce fichier
- Respecter les noms de fonctions précisés dans les énoncés suivants
- Exécuter le fichier test avec `./tests.py` dans le terminal


## Pratiquons !


### Exercice 1 : initialiser une matrice

**But :** écrire la fonction `init(lignes, cols, val)` qui cree une matrice de
dimensions 'lignes' par 'cols' et met chaque case de cette matrice a la valeur
'val'.

### Exercice 2 : afficher une matrice

**But :** écrire la fonction `afficher(m)` qui affichera la matrice prise en
parametre en separant chaque terme affiche par un espace, et un retour a la
ligne en fin de ligne de matrice.

**Exemple:**

```python
m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
afficher(m)
```

affichera

```python
1 2 3
4 5 6
7 8 9
```

### Exercice 3 : laissons une trace

**But :** écrire la fonction `trace(m, n)` qui prend une matrice carree en
parametre, calcule la somme des elements sur sa diagonale et la renvoit.

**Exemple :**

Soit la matrice m

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

**But :** écrire la fonction `ajouter(a, b)` qui ajoute les valeurs des deux
matrices a et b **si et seulement si** elles sont de memes dimensions.
Dans le cas inverse, votre fonction doit renvoyer la valeur 'None'.

*_Tips_: pour ajouter deux matrices de memes tailles, on ajoute simplement les
valeurs des cases qui se situent au meme endroit, et ca pour chaque case.
La matrice resultante de l'addition aura donc les memes dimensions que les deux
matrices prises en parametres.*

**Exemple :**

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

**But**: ecrire la fonction `sym_diago(m)` qui renvoie True si la matrice est
symetrique par rapport a l'axe de sa diagonale, False sinon.

**Exemple :**

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


### Exercice 7: les crateres de Mars

On represente une partie de la planete Mars vue de haut dans une matrice.
Les anneaux au sol formes par des crateres sont representes par des '#'.
Tout le reste de la surface de Mars est representee par des '.'.

Par exemple:
[insert image here]

Sur ce terrain de Mars, il y a 3 crateres.
