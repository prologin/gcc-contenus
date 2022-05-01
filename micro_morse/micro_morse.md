---
title: Télémorse
date: 2022
---

# Introduction
Les Micro:bit sont de tout petits ordinateurs embarqués, conçus pour s’entraîner à program-
mer. Ils ont beaucoup de composants en plus de leur processeur : un carré de 5x5 diodes élec-
troluminescentes, un capteur de mouvement, une boussole 3D, des boutons programmables,
une antenne Bluetooth et un port USB.
En utilisant MicroPython, une version simplifiée de Python, on peut programmer le Micro:bit
pour utiliser tous ces composants comme on le souhaite. 
Pour ce TP, nous allons vous accompagner dans la création d'un nouveau moyen de
communiquer avec vos amis : le code morse ! 
Vous avez déjà dû en entendre parler, mais ici vous allez pouvoir l'utiliser !

## Le code morse, qu'est-ce que c'est ?
Voilà la définition de Wikipédia :
> Le code Morse international, ou l’alphabet Morse international, est un code permettant de transmettre un texte à l’aide de séries d’impulsions courtes et longues, qu’elles soient produites par des signes, une lumière, un son ou un geste. 
> Wikipedia

On est d'accord, ce n'est pas très clair... Pour faire simple, c'est un nouvel
alphabet constitué uniquement de points (`·`) et de traits (`-`), et chaque
lettre correspond à une suite de points et de traits dont l'ordre permet de
donner un sens à chaque séquence. 
Voici un tableau représentant les traductions de toutes les lettres et tous les
chiffres :
![Code Morse International](resources/International_Morse_Code.png){width=9cm height=11.6cm}

# Les arbres
## La theorie

## Application à notre problème
Vous avez pu lire une partie très théorique sur une représentation complexe des
données. Il est très important que vous ayez compris la partie précédente afin
de profiter pleinement de la suite du TP. Si jamais vous avez une question ou
qu'il y a quelque chose que vous n'avez pas compris, n'hésitez pas à demander à
un organisateur de vous réexpliquer. 

### Notre arbre
Voici donc l'arbre que nous allons utiliser afin de décoder le message morse :
[arbre morse]

Comme vous pouvez le voir, il suffit de parcourir l'arbre (comme expliqué plus
        haut) afin de trouver la représentation correspondante. 

Voici le code de base de ce TP, il vous est donné afin de vous faciliter la
tâche, déjà suffisament complexe comme ça...

```py
from microbit import *

class BinTree:
    def __init__(self, key, left, right):
        """
        Init Tree
        """
        self.key = key # La valeur du noeud
        self.left = left # Le noeud gauche
        self.right = right # Le noeud droit
```


# Des conventions (titre a revoir ?)
Pour mener notre projet à bien, nous allons devoir poser quelques conventions 
qui vont nous faciliter la tâche pour la suite du projet.
Tout d'abord, un point (`·`) correspond à un appui sur le bouton `A` et un trait 
correspond à un appui sur le bouton `B`. Nous allons représenter les appuis sur
les boutons par une chaine de caractères dans laquelle les points sont
representés par des 0 et les traits par des 1. Le principal avantage d'utiliser
une chaine de caractères est que celle-ci va conserver l'ordre d'appui sur les
touches, ce qui nous est très utile pour ne pas créer de confusions. 
Ces derniers paragraphes ont été assez dense et ne sont pas des plus faciles à
comprendre. Si vous avez un doute sur quelque chose ou que vous avez une
question, n'hésitez surtout pas à faire appel à un organisateur. 

Si tout est bon pour vous, nous allons pouvoir commencer ! 


#### Exercice
**But :** Écrire une fonction `translate_letter(s)` qui prend une chaine de
    caractères en paramètre, et renvoie la lettre qui correspond à la chaine
    donnée. Pensez à utiliser le fichier qui vous est donné. 

**Exemple :** `translate_into_letter("0010")` va nous renvoyer `'F'`. 





# Améliorations possibles
- Faire un système de sélection du `channel`
- Pouvoir corriger une faute de frappe en appyuant simultanémant sur `A` et `B`
- Visualisation du code morse déjà entré
- Confirmation avant l'envoie

