---
show_toc: true
---

# Contrôler son code

{{% box type="info" title="Lecture par l'ordinateur" %}}

En Python, les instructions sont lues et traduites ligne par ligne, mais il existe des situations où on a envie de lancer un bout de programme seulement dans un contexte précis ou de manière répétée. Il faut donc l'isoler du reste du code. Cette section y est dédiée.

{{% /box %}}

## Identation
Python utilise l'indentation pour isoler certains bouts de codes.
Mais l'indentation, qu'est-ce que c'est ?

Il s'agit en fait de l'espace en début de ligne. Le nombre d'espace n'est pas important tant que c'est la même dans tout le bloc qu'on souhaite isolé, ici nous utiliserons 4 espaces.

On peut voir l'indentation comme quelque chose qui divise le 'bloc' de code en différent sous-blocs.

<!-- Peut-etre privilegier un schema avec une decoupe du code a la place ?-->
```python {nocopy=true}
"Cette ligne n'est pas indentee" # 0 espaces = pas d'indentation

    "Celle la si" # 1 niveau d'indentation = 4 espaces

        "Celle la encore plus" # 2 niveau d'indentation = 8 espaces
```

Mais Python ne nous laisse pas indenter comme bon nous semble, le code au-dessus provoquera une erreur. Puisque l'indentation sert à isoler le code, il faut une raison d'isoler ! Une manière de le faire est avec l'utilisation du mot-clé `if`.
<!-- remplace cette phrase :"La première manière de le faire est avec le mot-clé `if`" par celle au dessus. à confirmer-->
<!-- Derniere phrase peut porter a confusion, fait penser que le mot clé if est utile spécialement pour l'indentation-->

## Conditions
Imaginons qu'on a un programme que l'on souhaite vérifier si une variable que l'on a créée est plus grande que 0. En informatique on utilise ce qu'on appelle des booléens.

Les booléens sont utilisés pour représenter des valeurs de vérités.
Le **booléen** peut prendre deux valeurs différentes : **`True` ou `False`**, soit `vrai` ou `faux`.
Donc pour contrôler son code, on utilise des conditions qui sont ensuite interprétées comme des booléens.

Pour créer une condition il suffit juste d'écrire le **mot-clé `if`** ("si" en français), suivi de la condition qu'on veut tester avec un `:` à la fin de la ligne.

```codepython
n = 2
if n > 0:
    print("Je suis un nombre positif !")
```

On peut donc enfin voir à quoi ressemble l'indentation expliquée juste avant.
Inutile de trop se prendre la tète avec l'indentation.
La plupart du temps, l'éditeur de code que vous utiliserez indentera automatiquement de la bonne manière après un `if` ou les autres 'mots-clés' qui nécessitent un niveau d'indentation.

On utilise du coup des opérations booléennes pour tester des conditions
- Pour vérifier "a est inférieur à b" on écrit `a < b`
- Pour vérifier "a est supérieur à b" on écrit `a > b`
- Pour vérifier "a est inférieur ou égal à b" on écrit `a <= b`
- Pour vérifier "a est supérieur ou égal à b" on écrit `a >= b`
- Pour vérifier "a est égal à b" on écrit `a == b`
- Pour vérifier "a est différent de b" on écrit `a != b`.

Dans le code suivant, on affiche quelque chose si et seulement si n est plus grand que 0.
```codepython
n = -1
if n > 0:
    print("Je suis un nombre positif !")
```
Dans la situation au-dessus, le `print` ne se fera jamais car n est inférieur à 0, donc la condition est fausse et vous ne verrez rien sur la console. 

Et que faire si l'on veut réaliser une opération lorsque la condition n'est pas remplie ? Dans ce cas, on utilisera le **mot-clé `else`**, qui signifie "sinon" en français.
```codepython
n = -1
if n > 0:
    print("Je suis un nombre positif !")
else: # Pas besoin de condition ici
    print("Je suis un nombre negatif !")
```
Mais que se passe-t-il si on voulait tester plusieurs conditions ?

Imaginons que nous avons une variable `n` entre `0` et `5` et que nous voulions savoir lequel c'est ? Nous pouvons utiliser le **mot-clé `elif`** dans ce cas.
```codepython
n = 3
if n == 0:
    print("0")
elif n == 1: # Avec des elif, on peut tester une nouvelle condition
    print("1")
elif n == 2:
    print("2")
elif n == 3:
    print("3")
elif n == 4:
    print("4")
elif n == 5:
    print("5")
else:
    print("Aucun")
```
Bon, on ne va pas se le cacher le code au-dessus n'est pas très joli, et si on voulait aller jusqu'à 10 il faudrait encore rajouter des lignes à la main.
De plus, on ne fait que de répéter la meme action en changeant juste le nombre.

Fort heureusement, il existe un moyen de répéter des actions de manière contrôlée.

## Boucles

{{% box type="info" title="for ou while ?" %}}

Il existe deux types de boucles en Python. Les boucles `while` et les boucles `for`.

{{% /box %}}

### While
Cette boucle se traduit par `tant que` en français.
On peut voir cette boucle comme la répétition d'un `if` **tant que** la condition est vraie.

Donc si on en revenait à l'exemple d'avant avec une boucle `while` à la place :

```codepython
n = 3
i = 0 # On crée une variable qui servira de compteur

while i <= 5: # tant que notre compteur est entre 0 et 5

    if i == n: # Si n est égal à la valeur actuelle du compteur
        print(i) # Afficher la valeur actuelle

    i = i + 1 # il est important de changer la valeur de i 
              # sinon la condition serait toujours vraie
              # et on bouclerait à l'infini
```

Ca devient déjà beaucoup plus propre d'un coup, et en plus pas besoin de rajouter des lignes si on veut chercher plus loin ! Il suffit juste de changer la condition.

### For
Il existe une autre manière de créer une boucle.
La boucle `while` est pratique pour répéter une action tant que la condition vérifiée par la boucle est vraie mais si on n'a pas de condition à vérifier on préfère utiliser la boucle `for`.

La boucle `for` est pratique pour répéter une action un nombre fixe de fois, ou pour parcourir des ensembles (des listes par exemple, on verra ce que c'est plus tard). Si on échangeait la boucle de l'exemple précédent, on aurait :

```codepython
n = 3 
for i in range(5): # Pas besoin de faire i + 1 cette ligne le fait deja
    if n == i:
        print(i)
```
On peut apercevoir ici une nouvelle fonction mise à disposition par Python, la fonction `range`.
Cette fonction permet à partir d'un nombre de créer une suite de nombres (une espèce d'ensemble).
À noter que cette fonction, comme `print`, peut prendre plusieurs arguments (3 maximum) qui correspondent au début de la suite, la fin de la suite et enfin la distance entre les nombres (qu'on appelle la raison de la suite).

```python {nocopy=true}
range(5)       # 0 1 2 3 4
range(1, 5)    # 1 2 3 4
range(0, 6, 2) # 0 2 4 
```

{{% box type="exercise" title="Un peu de pratique" %}}

Maintenant que les bases sont posées, il est temps de mettre en pratique ces nouvelles connaissances.

Tu as une tirelire vide contenant 0 pièce. Écris un programme en Python qui, à chaque tour de boucle :
- demande à l'utilisateur combien de pièces il souhaite ajouter dans la tirelire 
- affiche le nombre total de pièces tant qu'il est inférieur à 25

Pour ce faire, tu pourras utiliser toutes les fonctions vues précédemment.

Pour obtenir le nombre de pièces entré par l'utilisateur, tu peux utiliser la fonction `input()` comme l'exemple suivant :

```python
# Demande à l'utilisateur un nombre et l'assigne à "valeur"
valeur = int(input())
print(valeur)
```

{{% /box %}}

Jusque-là on parle de fonctions que Python nous propose mais il est possible de créer nos propres fonctions ! Plus d'explications dans la section suivante.
