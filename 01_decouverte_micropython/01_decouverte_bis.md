---
title: Découverte de Python
date: 2022
---

# Introduction à la programmation

Tous les ordinateurs ne sont rien d'autres que des composants électroniques qui
exécutent des instructions. Lorsque tu ouvres un navigateur internet, ton
ordinateur exécute les instructions du logiciel utilisé, qu'on appelle aussi
**programme**. Le but de cet atelier est de te faire découvrir comment nous
pouvons créer nos propres programmes, et pour cela il nous faut un moyen
d'écrire ces instructions : un **langage de programmation**.

Il existe énormément de langage de programmation, tout comme il existe des
milliers de langue dans le monde ! Certains sont plus connus que d'autres et
nous allons te faire découvrir Python, un langage facile à prendre en main mais
très puissant.

## Qu'est-ce qu'un `micro:bit` ?

Pour cet atelier, nous allons utiliser un `micro:bit`, c'est un microcontrôleur
de la taille d'une carte bancaire. Nous pouvons écrire des programmes et les
lancer dessus, ainsi qu'interagir avec ses composants : l'écran de LED, les
boutons, l'accéléromètre (pour détecter des mouvements), etc.

Tu peux garder les microcontrôleurs avec toi, et continuer à écrire tes propres
programmes en Python dessus après l'atelier !

## Notre environnement de travail

Pour écrire nos programmes, nous utiliserons `Mu`, que vous avez pu découvrir dans le TP0.

Si tu n'as pas réussi à bien installer `Mu`, demande aux organisateurs de t'aider.

# Notre premier programme

Un programme en Python est constitué d'une série d'instruction à exécuter par un
ordinateur (dans notre cas, le `micro:bit`). Chaque instruction doit être écrite
sur une nouvelle ligne, et le programme sera lu par l'ordinateur de haut en bas.

Commençons par analyser un premier exemple de programme :

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

Ligne à ligne voilà ce que signifie ce programme :

1. `from microbit import *` permet d'indiquer que dans la suite du programme, on
   va avoir besoin de toutes les fonctionnalités relative à l'utilisation du
   `micro:bit`. Ici, toutes les instructions qui suivent ne seraient pas valides
   sans cette ligne.
2. Une ligne vide n'a aucun effet, il ne faut pas hésiter à s'en servir pour
   espacer son programme (on peut ainsi séparer des morceaux de codes, à la
   manière dont on sépare des paragraphes dans du texte).
3. `display.set_pixel(0, 2, 9)` allume le pixel situé sur la colonne n°0 et la
   ligne n°2. Le dernier paramètre (9) indique la luminosité de la diode entre 0
   (diode éteinte) et 9 (pleine puissance).
4. `sleep(500)` met l'exécution du programme en pause pendant 500 millisecondes.
   Essaye de supprimer cette ligne, le programme s'exécute tellement vite que tu
   n'as pas le temps de voir qu'une diode s'allume avant l'autre !
5. La suite du programme se répète : on allume les diodes des colonnes numéro 1,
   2, 3 puis 4.



