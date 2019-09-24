---
title: Découverte de Python via microbit
date: 2019
---

 - **TODO**: une petite introduction à ce qu'est `micro:bit` ...
 - **TODO**: petit tuto de setup du `micro:bit` ...


Notre premier programme
=======================

Un programme en python est constitué d'une série d'instruction à exécuter par
un ordinateur (dans notre cas, le `micro:bit`). Chaque instruction doit être
écrite sur une nouvelle ligne, et le programme sera lu par l'ordinateur de haut
en bas. Commençons par analyser un premier exemple de programme:

```python
from microbit import *

display.set_pixel(0, 2, 9)
sleep(500)
display.set_pixel(1, 2, 9)
sleep(500)
display.set_pixel(2, 2, 9)
sleep(500)
display.set_pixel(3, 2, 9)
sleep(500)
display.set_pixel(4, 2, 9)
```

Si tu testes ce programme, il affiche une barre de chargement sur la ligne de
diode centrale de ton `micro:bit`.

Ligne à ligne voilà ce que signifie ce programme:

 1. `from microbit import *` permet d'indiquer que dans la suite du programme,
    on va avoir besoin de toutes les fonctionnalités relative à l'utilisation
    du `micro:bit`. Ici, toutes les instructions qui suivent ne seraient pas
    valide sans cette ligne.
 2. Une ligne vide n'a aucun effet, il ne faut pas hésiter à s'en servir pour
    espacer son programme (on peut ainsi séparer des morceaux de codes, à la
    manière dont on sépare des paragraphes dans du texte).
 3. `display.set_pixel(0, 2, 9)` allume le pixel situé sur la colonne n°0 et la
    ligne n°2. Le dernier paramètre (9) indique la luminosité de la diode entre
    0 (diode éteinte) et 9 (pleine puissance).
 4. `sleep(500)` met l'exécution du programme en pause pendant 500
    millisecondes. Essayes de supprimer cette ligne, le programme s'execute
    tellement vite que tu n'as pas le temps de voir qu'une diode s'allume avant
    l'autre!
 5. La suite du programme se répète : on allume les diodes des colonnes numéro
    1, 2, 3 puis 4.

**TODO**: quelques remarques sur la rigueur de la syntaxe

Les variables
=============

Pour l'instant on a seulement vu comment créer un programme qui exécute une
liste d'instructions assez bêtement, qui donneront toujours exactement le même
résultat. On va voir que les ordinateurs (et donc le `micro:bit` aussi) ont une
mémoire que l'on peut manipuler dans un programme pour que celui-ci agisse
différemment en fonction de ce qu'il a retenu dans sa mémoire.

Une *variable* est un morceau de la mémoire dans lequel on va pouvoir
enregistrer des valeurs. Quand on créé une variable, on commence par lui
choisir un nom qui va ensuite pouvoir être utilisé pour lire ou modifier la
valeur qui est enregistrée dans la variable.

Utilisation des variables
-------------------------

Pour **créer une variable** il suffit d'écrire `nom_de_la_variable =
valeur_initiale`, par exemple: `nombre_de_patates = 42`.

Ensuite on peut **réutiliser la valeur** stockée dans la variable en
l'identifiant par son nom, par exemple on peut créer une nouvelle variable
`prix` qui dépend de la variable qui a été créé précédemment : `prix =
nombre_de_patates * 50`.

Pour **modifier une variable** on utilise aussi le symbole d'égalité, par
exemple on peut augmenter de 1 la valeur stockée dans une variable :
`nombre_de_patates = nombre_de_patates + 1`.

Voici un exemple de programme complet que tu peux tester sur ton `micro:bit`
suivi d'un petit schéma qui représente ce qui est enregistré dans les variables
après chaque ligne du programme:

```python
from microbit import *

x = 3
y = 5
y = 2 * y
x = x + y

display.scroll(x)  # affiche 13 sur l'écran à diodes
```

![](figures/variables.pdf)


### Types de variables

Les valeurs stockées dans des variables peuvent être diverses, comme des
nombres, du texte ou un ensemble de valeurs, on verra peut-être même plus tard
qu'en décrivant au programme ce que c'est, les variables peuvent stocker des
pokémons.

##### Nombres

C'est le type de variable le plus courant, on a déjà vu qu'on peut créer des
valeurs numériques avec leur écriture naturelle, et qu'on peut utiliser les
opérations classiques: `+`, `-`, `*` (multiplication), `/` (division) et `**`(
(puissance).

```python
x = 3 * 4        # x vaut 12
y = x // 2       # y vaut 6 (`//` est une division pour laquelle on attend
                 #           un résultat sans virgule)
z = 3 ** 2       # z vaut 9
x = (x - y) + z  # x vaut maintenant 15

```

##### Chaines de caractère

On peut créer du texte en mettant son contenu entre guillemets (par exemple:
`mon_texte = "Bonjour tous le monde !"`). On peut aussi concaténer des morceaux
de textes entre eux avec l'opérateur `+` (par exemple: `mon_texte = mon_texte +
"!!"`).

À noter qu'il est souvent très pratique de convertir un nombre en texte pour
ensuite l'incorporer dans une phrase, on peut faire ça avec la fonction
`str(nombre)`.

```python
from microbit import *

nombre_de_patates = 42
texte = "Il y a " + str(nombre_de_patates) + " patates !"
display.scroll(texte)  # Affiche `Il y a 42 patates !` sur l'écran
```

##### Booléens

Enfin, les booléens servent à exprimer le vrai ou le faux. Ils n'y a que deux
valeurs possibles pour ce type de variables: `True` (vrai) et `False` (faux).

Des valeurs booléennes sont renvoyées par les opérations de comparaisons: `==`
(égalité), `!=` (différence), `<`, `>` (les inégalités strictes), `<=` et `>=`
(les inégalités larges). Par exemple `1 < 2` vaut `True` mais `3 != 3` faut
`False`.

Enfin, il est possible de manipuler les valeurs booléennes avec les opérateurs
`not`, `and` et `or`:

 - `not a` vaut `True` si et seulement si `a` vaut `False`;
 - `a and b` vaut `True` si et seulement si `a` **et** `b` valent `True`;
 - `a or b` vaut `True` si et seulement si `a` **ou** `b` valent `True`.


Exemples
--------

On peut récupérer le nombre d'appuis qui ont été fait sur un bouton du
`micro:bit` en utilisant les fonctions `button_a.get_presses()` et
`button_b.get_presses()` pour le second bouton.

Voici un exemple de petit jeu qui déclenche un compte à rebours avant de donner
5 secondes pour appuyer autant de fois que possible sur le bouton de gauche.

```python
from microbit import *

# Compte à rebours
display.set_pixel(0, 2, 9)
sleep(500)
display.set_pixel(1, 2, 9)
sleep(500)
display.set_pixel(2, 2, 9)
sleep(500)
display.set_pixel(3, 2, 9)
sleep(500)
display.set_pixel(4, 2, 9)

# Phase de jeu
button_a.get_presses()     # réinitialise le compteur d'appuis
sleep(5000)                # donne 5 secondes pour jouer
a = button_a.get_presses() # récupère le nombre d'appuis

# Affichage du score
display.scroll("Score: " + str(a))
```

### Exercice: calculatrice

En t'inspirant de l'exemple précédent, écris un programme qui donne le résultat
de la multiplication de deux nombres. Pour récupérer la valeur des deux nombres
tu peux donner quelques secondes à l'utilisateur pour appuyer le bon nombre de
fois sur chaque bouton. Par exemple, si pendant ce temps, tu appuies 3 fois sur
le bouton de gauche et 7 fois sur celui de droite, le programme affichera "3 *
7 = 21" sur l'écran.


Les boucles et conditions
=========================

**TODO**: intro


La boucle `for`
---------------

La boucle *for* sert à répéter plusieurs fois le même morceau d'un programme.
Elle s'utilise comme suit:

```python
from microbit import *

for colonne in range(5):
    # Ce qui suit va être répété 10 fois, une variable `colonne` est créée,
    # qui va prendre les valeurs 0, 1, 2, ..., puis 9.
    display.set_pixel(colonne, 2, 9)
    sleep(500)

# Ce qui suit ne va être exécuté qu'une fois
display.scroll("fini !")
```

Remarques comme les lignes 4 à 7 sont décalées vers la droite, cette
transformation permet d'identifier le morceau du programme qui est concerné par
la boucle. À chaque fois que tu écris un `for`, la ligne suivante doit être
décalée vers la droite, et le morceau de code qui sera répété par cette boucle
s'arrêtera juste avant la première ligne qui ne sera plus décalée vers la
droite.

![](figures/for.pdf)

#### Exercice

Modifies ta barre de chargement pour qu'au lieu d'allumer les diodes d'un coup
(avec une intensité de 9), elles s'allument en douceur (en faisant
progressivement varier l'intensité de 0 à 9).


La boucle `while`
-----------------

La boucle *while* sert à répéter un morceau de programme tant qu'une
affirmation est vraie. Elle s'utilise comme suit:

```python
from microbit import *

while button_a.get_presses() == 0:
    # Ce qui suit va être exécuté tant que le bouton de gauche n'a pas été
    # pressée.
    display.set_pixel(2, 2, 9)  # Allume la diode
    sleep(500)
    display.set_pixel(2, 2, 0)  # Éteint la diode avant de recommencer
    sleep(500)

display.scroll("fini !")
```

#### Exercice

Modifie ton jeu pour que la partie recommence tant que le joueur n'a pas
atteint un score de 20, une fois qu'il a atteint ce score tu peux afficher une
image de victoire avec l'instruction `display.show(Image.HAPPY)`.

#### Exercice

*(je ne sait pas si c'est une bonne idée)*: Modifie ton jeu pour qu'il
affiche une barre de progression, la barre doit être pleine quand il a appuyé
20 fois sur le bouton. À la fin, le jeu affiche le temps qu'il a fallu pour
atteindre les 20 appuis.

Voici un exemple de comment mesurer un temps, en secondes en utilisant le
module `time` de Python:

```python
import time
from microbit import *

# enregistre l'instant de début d'execution du programme
debut = time.time()

# simule un programme qui prend 2.5 secondes à s'executer
sleep(2500)

# calcul du temps écoulé (en secondes)
duree = time.time() - debut

# affiche le temps écoulé (2 chiffres après la virgule)
display.scroll('%.2f' % duree)
```

**TODO**: expliquer comment compter le temps

Les conditions: `if` ... `elif` ... `else`
------------------------------------------

L'instruction `if` permet de décider de n'exécuter un morceau de code que
lorsqu'une condition est vraie. Pour se faire la syntaxe est d'écrire `if
condition:` suivi d'un bloc de code indenté. Le bloc de code en question ne
sera alors exécuté que si `condition` s'évalue à `True`. Pour simplifier, un
`if` peut être suivi d'un ou plusieurs `else:` qui exécute un bloc de code
uniquement si la condition du `if` était fausse.

Voici un exemple simple pour illustrer:

```python
import random
from microbit import *

x = random.randint(0, 100)  # assigne un nombre aléatoire à x

if x < 50:
    display.scroll('x est inférieur à 50')
else:
    display.scroll('x est supérieur à 50')
```

Ou un exemple légèrement plus poussé qui permet de lier les boutons du
`micro:bit` à des diodes:

```python
from microbit import *

while True:
    # Ce qui suit est executé indéfiniment

    if button_a.is_pressed():
        # Allume la diode de gauche si le bouton de gauche est enfoncé
        display.set_pixel(1, 2, 9)
    else:
        # Éteint la diode de gauche sinon
        display.set_pixel(1, 2, 0)

    if button_b.is_pressed():
        # Allume la diode de droite si le bouton de droite est enfoncé
        display.set_pixel(3, 2, 9)
    else:
        # Éteint la diode de droite sinon
        display.set_pixel(3, 2, 0)
```

Les fonctions
=============


Projets
=======

**TODO**: Je crois qu'il y en a pas mal qui ne demandent pas à savoir utiliser
de liste dans les idées du TP microbit, on peut les réutiliser, elles ont déjà
pas mal de trucs à digérer c'est le moment de les lancer dans un truc perso je
pense.


Références `micro:bit`
======================

**TODO**
