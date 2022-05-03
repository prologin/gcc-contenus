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

1. `from microbit import *` permet d'indiquer à l'ordinateur la signification
   des commandes propres aux micro:bit. Sans cela, le programme ne sait pas ce
   que doivent faire les commandes permettant d'utiliser le micro:bit.
2. Nous avons ensuite une ligne vide. Cela n'a aucune influence sur le
   comportement de votre code, il ne faut donc pas hésiter à s'en servir pour
   espacer son programme. Cela rend le code plus lisible pour toi comme pour les
   personnes qui voudront lire ton code.
3. `display.set_pixel(0, 2, 9)` est une fonction propre au micro:bit, elle
   permet d'allumer le pixel situé sur la colonne n°0 et la ligne n°2. Le dernier
   paramètre (9) indique la luminosité de la diode. 
4. `sleep(500)` est aussi une fonction propre au micro:bit. Elle met l'exécution 
   du programme en pause pendant 500 millisecondes. Essaye de supprimer cette 
   ligne, le programme s'exécute tellement vite que tu n'as pas le temps de voir
   qu'une diode s'allume avant l'autre !
5. La suite du programme se répète : on allume les diodes des colonnes numéro 1,
   2, 3 puis 4.

Comme tu peux le voir avec la ligne numéro `3`, le décompte des lignes et des
colonnes se fait à partir de 0. 

# Les fonctions de contrôle du micro:bit

Comme tu l'as vu plus tôt, il existe des fonctions qui permettent de contrôler
le microbit. En ce qui concerne la fonction `display.set_pixel(colonne, ligne,
intensite)`, voici un petit schéma qui permet de mieux comprendre les
corrdonnées de chaque led (la coordonnée **X** correspond au numéro de 
**colonne** et la coordonnée **Y** correspond au numéro de **ligne**) :

![Coordonnées des leds](resources/microbit_coordinates.png)

## Comment afficher quelque chose ?
Voici les principales fonctions principales permettant d'afficher quelque chose
sur les LED :

- `display.set_pixel(C, L, I)` : permet d'allumer la LED située au croisement de
la colonne `C` et de la ligne `L` avec une intensité de `I` (l'intensité variant
        de 0 pour une LED éteinte à 9 pour une LED allumée à pleine puissance).

- `display.scroll(message)` : permet d'afficher une chaine de caractères
- `display.show(Image)` : permet d'afficher une image pré-enregistrée. Le
fonctionnement des images est expliquée juste après.


### Les images
Les images que l'ont peut afficher sur la matrice LED sont des sortes de smiley
assez minimalistes. Il en existe de nombreuses qui sont déjà dessinée. On y
accède en tapant `Image.MONIMAGE` où `MONIMAGE` est le nom de l'image. 
Voici à quoi ressemblent les images `HEART` et `SMILE` :

![`Image.HEART` et `Image.SMILE`](resources/microbit_images.jpg)


## Ça va trop vite !
Une autre fonction bien pratique est la fonction `seep(millisecondes)` qui
permet, comme évoqué plus haut, de mettre en pause ton programme pour, par
exemple, te laisser le temps de voir ce qu'il se passe. 


Nous avons déjà vu beaucoup de choses nouvelles. Si jamais tu as une question ou
si tu n'as pas compris quelque chose, n'hésite surtout pas à demander de l'aide
à un organisateur. 
N'hésite pas non plus à relire les parties que tu n'as pas compris. 
Si jamais tu as besoin, une liste _presque_ exhaustive des fonctions de contrôle
du microbit est disponible à la toute fin de ce TP. 

# Mini-exercice
**But :** Essayez d'afficher une barre de chargement, puis d'afficher le message
`"Salut !"` suivi de l'image de votre choix

