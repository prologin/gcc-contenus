---
title: MicroMorse
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
tâche, déjà suffisament complexe comme ça... Vous pouvez aussi le retrouver dans
le fichier `given_code.py`.

```py
from microbit import *
import radio

class Noeud:
    def __init__(self, key, left, right):
        """
        Cree le noeud
        """
        self.key = key # La valeur du noeud
        self.left = left # Le noeud gauche
        self.right = right # Le noeud droit

# Arbre permettant de traduire du morse
NEUF = Noeud('9', None, None)
ZERO = Noeud('0', None, None)
HUIT = Noeud('8', None, None)
SEPT = Noeud('7', None, None)
SIX = Noeud('6', None, None)
DEUX = Noeud('2', None, None)
UN = Noeud('1', None, None)
TROIS = Noeud('3', None, None)
QUATRE = Noeud('4', None, None)
CINQ = Noeud('5', None, None)
C = Noeud('C', None, None)
Q = Noeud('Q', None, None)
Z = Noeud('Z', SEPT, None)
X = Noeud('X', None, None)
B = Noeud('B', SIX, None)
Y = Noeud('Y', None, None)
F = Noeud('F', None, None)
V = Noeud('V', None, TROIS)
H = Noeud('H', CINQ, QUATRE)
J = Noeud('J', None, UN)
P = Noeud('P', None, None)
L = Noeud('L', None, None)
O = Noeud('O', Noeud(None, HUIT, None), Noeud(None, NEUF, ZERO))
G = Noeud('G', Z, Q)
D = Noeud('D', B, X)
K = Noeud('K', C, Y)
U = Noeud('U', F, Noeud(None, None, DEUX))
S = Noeud('S', H, V)
W = Noeud('W', P, J)
R = Noeud('R', L, None)
M = Noeud('M', G, O)
N = Noeud('N', D, K)
I = Noeud('I', S, U)
A = Noeud('A', R, W)
E = Noeud('E', I, A)
T = Noeud('T', N, M)

MORSE = Noeud(None, E, T)



# Ecris tes fonctions ici !


radio.on() # Allumer la radio
radio.config(channel=42) # Configure le canal utilise (doit etre compris entre 0 et 83)

while True:
    message_recu = radio.receive() # Essaye de recevoir un message
    if message_recu != None:
        display.scroll(received_message) # Affiche le message recu s'il existe

    # Continue le code ici !
```


### Des conventions (titre a revoir ?)
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


#### Exercice 1 : Traduire une chaine de caractères
**But :** Écrire une fonction `translate_letter(S, arbre)` qui prend en paramètre
    une chaine de caractères ainsi que l'arbre représentant le code morse, 
    et renvoie la lettre qui correspond à la chaine donnée. 
    Pensez à utiliser le fichier qui vous est donné ;) 

**Exemple :** `translate_into_letter("0010", MORSE)` va nous renvoyer `'F'`. 

**Aide :** Vous pouvez découper cette fonction en deux étapes : 
        - D'abord, quel est ou quels sont le ou les cas d'arrêts ?
        - Ensuite, si le cas d'arrêt n'est pas atteint, que faire ?

**Rappels :** Vous pouvez tester vos fonctions directement dans Mu en appuyant 
sur le bouton 'Lancer'

# Récupérer l'entrée utilisateur
## Lorsque tout se passe bien...
Maintenant que nous savons traduire une chaine de caractères en lettres, nous
allons devoir trouver un moyen de transformer des appuis sur des boutons en
chaine de caractères. Pour ce faire, je te rappelle que nous avons mis en place
quelques conventions que l'utilisateur doit respecter afin de pouvoir utiliser
notre outil de communication moderne. Voici un bref rappel :
> Le bouton A correspond à un point, il est traduit par un `'0'` dans les
> chaines de caractères
> Le bouton B correspond à un trait, il est traduit par un `'1'` dans les
> chaines de caractères
> Pour valider un mot, l'utilisateur doit toucher le logo tactile
> Pour valider un message entier et l'envoyer, l'utilisateur doit secouer le
> microbit

Maintenant que les choses sont claires, passons à la pratique !

#### Exercice 2 : l'utilisateur parle à notre programme...
**But :** Coder une fonction `create_message()` qui ne prend aucun paramètre et
renvoie le message (sous forme d'alphabet latin) que l'utilisateur veut envoyer.

**Exemple :** _L'utilisateur appuie sur A, puis sur le logo, puis appui sur B,_
_puis à nouveau sur le logo avant de secouer le microbit_
La fonction `create_message()` renvoie donc `"E T"`



## ... mais que l'utilisateur est humain !
Dans la plupart des programmes que nous allons créer, nous allons le faire pour
qu'ils soient utilisés par un humain. Malheureusement, il n'est pas rare que
l'utilisateur ne respecte pas parfaitement le fonctionnement de notre programme.
Nous devons donc faire attention à ce qu'une erreur ne vienne pas provoquer une
erreur dans notre code. 
Il faut donc toujours vérifier les informations que l'utilisateur nous transmet,
   c'est un bon réflexe à avoir afin de limiter les bugs. 

### Pourquoi MicroMorse est concerné ?
Bien que nous n'ayions que deux boutons, l'utilisateur doit respecter un
alphabet bien spécifique. 
Ici, la seule erreur que l'utilisateur peut comettre, c'est de valider une
lettre qui n'existe pas dans l'alphabet morse.
Modifions notre fonction précédente (`translate_into_letter`) afin de gérer les
cas où l'entrée utilisateur (c'est à dire la chaine de caractères donnée en
        paramètre).

#### Exercice 3 : Vérifier la chaine de caractères
**But :** Modifier la fonction `translate_into_letter` pour que cela ne crée pas
d'erreur si l'utilisateur entre une mauvaise séquence, renvoyer une chaine vide
(`''`) si c'est le cas.

**Exemple :** `translate_into_letter("0101", MORSE)` va nous renvoyer une chaine
vide (`''`) sans produire d'erreur

**Aide :** En cas de mauvaise entrée, au niveau de quelles lignes de code peut-on trouver
une erreur ?



# Accordons nos fonctions ensemble !
Voici le moment tant attendu, maintenant que toutes les étapes de notre projet
fonctionnent, il est l'heure de les faire fonctionner ensemble. 

## Comment mon code doit se comporter ?
Vous l'avez peut-être vue, dans le code que nous vous avons donné, par défaut,
notre programme est en mode _réception_, c'est-à-dire qu'il est prêt à recevoir
le message d'un autre microbit. 
Pour le passer en mode _émission_, il doit suffire d'appuyer sur n'importe quel
bouton. C'est un choix très arbitraire de notre part, mais vous pourriez tout
aussi bien faire en sorte d'entrer dans ce mode lorsque le microbit est secoué,
ou bien de manière plus originale lorsqu'il est en chute libre ! (C'est une
blague, ne tente pas de lacher le microbit du 4e étage, tu aurais du mal à
envoyer un message par la suite).

#### Exercice 4 : Et que le MicroMorse fut
**But :** Ajouter une condition pour entrer en mode _émission_ dans la boucle
principale.



# C'est déjà la fin ?
C'est en effet la fin de ce TP. Nous espérons que cela t'as plu, et
encore une fois si tu as des questions, n'hésite surtout pas à les poser à des
organisateurs. 
Tu peux désormais passer au TPs suivants, ou bien essayer d'améliorer ce
mini-projet :)

## Des améliorations ?
Comme tu t'en doutes peut-être, ce TP est un mini-projet améliorable à l'infini
ou presque. Si tu veux continuer à améliorer ton programme, tu es libre de faire
ce que tu veux avec. 

Si jamais tu as besoin d'idées, en voici quelques unes :
- Possibilité de choisir son canal radio afin de pouvoir discuter _presque_
secrètement
- Pouvoir corriger une faute de frappe en appyuant simultanémant sur `A` et `B`
- Visualisation du code morse déjà entré (En affichant la lettre qui a été
        trouvée avant une confirmation par l'utilisateur par exemple)
- Confirmation du message avant son envoie

