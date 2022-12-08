---
title: "Découverte de Micropython"
date: 2022
weight: 5
subtitle: "Au cours de ce TP, tu vas découvrir comment utiliser le micro:bit et comment coder en micropython."
---

# Introduction

Bonjour à toi jeune programmeuse,  
Je me présente, je suis Joseph Marchand, et c'est moi qui vais t'accompagner au
travers des différents TPs afin de t'apprendre à créer tes propres programmes
informatiques. Avant de commencer, laisse moi aussi te présenter mes fidèles
acolytes : les organisateurs. Ce sont eux qui vont t'accompagner en ce début de
matinée. Ils me remplacent car je suis très occupé en ce moment, mais si tu as
une quelconque question à n'importe quel moment, n'hésite surtout pas à leur
demander de l'aide, ils sont là pour ça.
Je m'arrête là pour les présentations, et je vais commencer dans ce TP par te
montrer les bases pour créer un programme. 

Mais d'abord, un ordinateur, c'est quoi ? 
Un ordinateur n'est rien d'autre qu'un ensemble de composants électroniques qui
exécutent des instructions. Lorsque tu ouvres un navigateur internet, ton
ordinateur exécute les instructions du logiciel utilisé, qu'on appelle aussi
**programme**. Le but de cet atelier est de te faire découvrir comment nous
pouvons créer nos propres programmes, et pour cela il nous faut un moyen
d'écrire ces instructions : un **langage de programmation**.

Il existe énormément de langages de programmation, tout comme il existe des
milliers de langues dans le monde ! Certains sont plus connus que d'autres et
nous allons, avec les organisateurs, te faire découvrir Python, un langage 
facile à prendre en main tout en étant puissant.

## Qu'est-ce qu'un `micro:bit` ?

Pour cet atelier, nous allons utiliser un `micro:bit`. C'est un microcontrôleur
de la taille d'une carte à jouer. Nous pouvons écrire des programmes et les
lancer dessus, ainsi qu'intéragir avec ses composants : l'écran de LED, les
boutons, l'accéléromètre (pour détecter des mouvements), etc.

## Notre environnement de travail

Pour écrire nos programmes, nous utiliserons `Mu`, que tu as pu découvrir dans le TP0.
Si tu n'as pas déjà lu le TP0, tu peux aller le lire avant de continuer
celui-ci. 


[SECTION-BREAK]


# Ton premier programme
## Analysons un programme

Un programme en Python est constitué d'une série d'instructions qui sont exécutées par un
ordinateur (dans notre cas, le `micro:bit`). Chaque instruction doit être écrite
sur une nouvelle ligne, et le programme sera lu par l'ordinateur de haut en bas.
Commençons par analyser un premier exemple de programme très basique :

```python
# Debut du programme

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

# Fin du programme
```

Si tu flash ce programme sur ton `micro:bit`, il affiche une barre de chargement
sur la ligne de diodes centrales de ton `micro:bit`.

Exécutons 'à la main' ce petit programme pour comprendre ce qu'il fait : 

1. `from microbit import *` permet de lier la bibliothèque de fonctions
   `micro:bit` à ton programme, pour que l'ordinateur puisse comprendre ce que
   font les fonctions que tu vas utiliser.  Sans cela, le programme ne sait pas ce
   que doivent faire les commandes qui permettent d'utiliser le `micro:bit`. Cette
   ligne est très importante car sans elle, ton programme ne pourra pas
   fonctionner. 
2. Nous avons ensuite une ligne vide. Cela n'a aucune influence sur le
   comportement de ton code, il ne faut donc pas hésiter à t'en servir pour
   espacer ton programme. Cela rend ton code plus lisible pour toi comme pour les
   personnes qui voudront le lire.
3. `display.set_pixel(0, 2, 9)` est une fonction propre au `micro:bit`, elle
   permet d'allumer le pixel situé sur la colonne n°0 et la ligne n°2. Son
   comportement est expliqué plus en détail juste après. 
4. `sleep(500)` est aussi une fonction propre au `micro:bit`. Elle met l'exécution 
   du programme en pause pendant 500 millisecondes. Essaye de supprimer cette 
   ligne, le programme s'exécute tellement vite que tu n'as pas le temps de voir
   qu'une diode s'allume avant l'autre !
5. La suite du programme se répète : on allume les diodes des colonnes numéro 1,
   2, 3 puis 4.



## Et les `#` c'est quoi ?

Les lignes qui commencent par un `#` sont des commentaires. Un commentaire, c'est
une suite de mots qui n'est pas lue par l'ordinateur. Ils sont 
écrits par les développeurs et pour les développeurs afin de mieux comprendre ce
que fait un programme. 

Pour ce qui concerne les commentaires commençant par un `#`, cela signifie que
tout ce qui se trouve après le `#` sur la ligne ne sera pas lu par l'ordinateur. 
Ce sont des commentaires _courts_. 
Il existe aussi des commentaires _longs_ que tu pourras rencontrer au cours des
TPs. C'est la même chose que les commentaires courts, mais sur plusieurs lignes.
En Python, ils commencent et finissent en écrivant `"""` avant et après ton
commentaire. 

Voici un exemple pour que ce soit plus clair :
```python
# Ceci est un commentaire sur une seule ligne

"""
Ceci est un 
commentaire
sur plusieurs
lignes
"""

ceci_n_est_pas_un_commentaire # Mais ça oui
```

Les commentaires courts sont d'ailleurs facilement repérable par leur couleur
grise.  



[SECTION-BREAK]




# Les fonctions de contrôle du `micro:bit`

Comme tu l'as vu plus tôt, il existe des fonctions qui permettent de contrôler
le `micro:bit`. Nous allons ici te présenter les principales.


## Allumer des LEDs

Il existe de nombreuses façons d'afficher quelque chose sur l'écran du `micro:bit`.
La première, et la plus basique, consiste à choisir les LEDs que l'on veut allumer
et à les allumer une par une. 
Pour cela, tu l'as vu juste avant, on utilise la
fonction `display.set_pixel(colonne, ligne, intensite)`, où : 
- `colonne` représente le numéro de la colonne de la LED à allumer
- `ligne` représente le numéro de la ligne de la LED à allumer
- `intensite` représente l'intensité avec laquelle la LED va s'allumer (de 0
pour une LED éteinte à 9 pour une LED allumée à pleine puissance). 

En ce qui concerne cette fonction, voici un petit schéma qui permet de mieux 
comprendre les coordonnées de chaque LED (la coordonnée **X** correspond au
numéro de **colonne** et la coordonnée **Y** correspond au numéro de **ligne**) :

{{<figure src="resources/images/microbit_coordinates_bis.png" width=400 caption="Coordonnées des LEDs">}}


### Mini-exercice
**But :** Affiche un coeur sur l'écran.

_Ça devrait ressembler à quelque chose comme ça :_
{{<figure src="resources/images/empty_heart.png" width=400 caption="">}}


## Les images

Comme tu as pu le constater, c'est assez long et fastidieux d'afficher quelque
chose de complexe avec la fonction précédente. Pour nous faciliter la vie, il
existe quelques autres fonctions, et une en particulier qui est faite pour
afficher des images et des symboles : `display.show(Image.NOM_IMAGE)`, où
`NOM_IMAGE` est le nom anglais d'une image pré-enregistrée. 
Tu peux trouver la liste des images pré-enregistrées
[ici](https://microbit-micropython.readthedocs.io/fr/latest/tutorials/images.html).

Voici à quoi ressemblent les images `HEART` et `HAPPY` :

{{<figure src="resources/images/microbit_images.jpg" width=600 caption="`Image.HEART` et `Image.HAPPY`">}}

### Mini-exercice
**But :** Affiche un smiley content sur l'écran du `micro:bit`.


## Et le texte ?

C'est super, tu sais maintenant comment allumer les LEDs une par une et afficher
une image. Mais comment faire si jamais tu veux afficher un message sur l'écran ?
Et bien la vie est bien faite, puisqu'il existe une fonction pour faire cela.

Mais juste avant, il faut comprendre comment ton ordinateur fait la différence
entre ton code et du texte que tu voudrais afficher. Ce n'est pas compliqué, il
suffit de mettre ton texte entouré par des guillemets (`"`). Ce texte est
appelé `chaîne de caractères`. Nous reviendrons dessus plus en détails par la suite. 
Voici un exemple de chaîne de caractères : `"Je suis Joseph Marchand !"`.

Maintenant, revenons à nos moutons. La fonction pour afficher du 
texte sur l'écran s'appelle `display.scroll(message)`. `message` est la chaîne de 
caractères que tu veux afficher. 

### Mini-exercice
**But :** Affiche le texte de ton choix sur l'écran du `micro:bit`.


## Ça va trop vite !

Une autre fonction bien pratique est la fonction `sleep(millisecondes)` qui
permet, comme évoqué dans la partie "Ton premier programme", de mettre en pause
ton programme pour, par exemple, te laisser le temps de voir ce qu'il se passe. 



Nous avons vu beaucoup de choses nouvelles jusqu'ici. Si jamais tu as une
question ou si tu n'as pas compris quelque chose, n'hésite surtout pas à demander
de l'aide à un organisateur. 

N'hésite pas non plus à relire les parties que tu n'as pas comprises. 
Si jamais tu as besoin, une liste _presque_ exhaustive des fonctions de contrôle
du `micro:bit` est disponible à la toute fin de ce TP. 

### Exercice 1
**But :** Max, qui est un ami de Joseph, te demande de créer un programme
pour que son `micro:bit` affiche une barre de chargement sur la ligne du milieu, 
puis affiche le message `"Salut Joseph !"` suivi d'un smiley qui sourit. 





[SECTION-BREAK]




# Les variables

Jusque là, on a vu comment afficher des images et du texte sur le 
`micro:bit`, mais ces informations sont statiques : une fois écrites dans le
code, elles ne peuvent plus être modifiées. Heureusement, un 
ordinateur peut enregistrer des informations pour les traiter, les modifier,
voire même en créer de nouvelles !

Pour cela, on utilise des variables : un morceau de la mémoire dans lequel on
va pouvoir enregistrer des valeurs. Quand on crée une variable, on commence par
lui donner un nom qui va être utilisé pour lire ou modifier la valeur qui lui
a été donnée.

## Utilisation des variables

Pour **créer une variable**, il suffit d'écrire `nom_de_la_variable =
valeur_initiale`, par exemple : `nombre_de_patates = 42`.

Ensuite on peut **réutiliser la valeur** stockée dans la variable en
l'identifiant par son nom. Par exemple, on peut créer une nouvelle variable
`prix` qui dépend de la variable qui a été créée précédemment : `prix =
nombre_de_patates + 50`. Dans ce cas, comme `nombre_de_patates` vaut
actuellement _42_, alors `prix = 42 + 50`. Donc à la fin de cette ligne, la
variable `prix` vaut _92_. 

Pour **modifier une variable** on utilise aussi le symbole d'égalité, par
exemple on peut augmenter de 1 la valeur stockée dans une variable :
`nombre_de_patates = nombre_de_patates + 1`.

Voici un exemple de programme complet que tu peux tester sur ton `micro:bit`
suivi d'un petit schéma qui représente ce qui est enregistré dans les variables
après chaque ligne du programme :

```python
from microbit import *

x = 3
y = 5
y = 2 * y
x = x + y

display.scroll(x)
```

{{<figure src="resources/images/variables.png" width=850 >}}

### Mini-Exercice
**But :** Crée une variable avec la valeur 42, puis ajoutes-y 2 et affiche-la 
sur l'écran.

## Types de variables

### Nombres

Comme leur nom l'indique, il s'agit tout simplement de nombres (positifs ou 
négatifs). On peut donc faire des opérations dessus avec les opérateurs 
classiques : `+`, `-`, `*` (multiplication), `/` (division), `//` (division
entière), `%` (modulo). 

Les deux dernières opérations ne te sont peut-être pas familières, et c'est
normal, mais elles ne sont pas compliquées. 

La division entière (`//`) et le modulo (`%`) correspondent respectivement au
quotient et au reste de la division euclidienne. 
Pour faire simple, la division entière renvoie la partie entière de la division
classique (la partie avant la virgule), tandis que le modulo correspond à ce
qu'il reste. 

Voici un petit mémo qui te permettra de comprendre ces opérations. 

```python
a = 2 * 5 + 3  # a vaut 13
b = a / 5      # b vaut 13 / 5  = 2.6
c = a // 5     # c vaut 13 // 5 = 2
d = a % 5      # d vaut 13 % 5  = 3
```

Si tu as des questions, n'hésite pas à demander de l'aide à un organisateur. 

Nous pouvons aussi combiner plusieurs opérations ensemble. Par exemple :

```python
e = (a - b) + c * d # (13 - 2.6) + 2 * 3 = 16.4, donc e = 16.4
```

#### Mini-Exercice
**But :** Joseph a envie de bananes. Le marchand lui propose de les acheter pour
2€ l'unité. Combien 10 bananes vont-elles lui coûter ? Affiche le résultat sur 
le `micro:bit`.

### Chaînes de caractères

On peut créer du texte en mettant son contenu entre guillemets (par exemple :
`mon_texte = "Bonjour tout le monde !"`). On peut aussi attacher des morceaux
de textes entre eux avec l'opérateur `+` (par exemple : `mon_texte = mon_texte +
"!!"`).

À noter qu'il est souvent très pratique de convertir un nombre en texte pour
ensuite l'incorporer dans une phrase, on peut faire ça avec la fonction
`str(nombre)`.

```python
from microbit import *

nombre_de_patates = 42
texte = "Il y a " + str(nombre_de_patates) + " patates !"
display.scroll(texte)  # Affiche "Il y a 42 patates !" sur l'écran
```

#### Mini-Exercice
**But :** Comme dans l'exercice précédent, Joseph a besoin de savoir combien 
vont lui coûter ses bananes. Mais le marchand a augmenté le prix et les bananes 
coûtent désormais 3€ chacune. Après avoir calculé, affiche `"Payer (le prix) 
pour 10 bananes ? Mais c'est beaucoup trop cher !"` en remplaçant `le prix` par 
sa valeur.


### Booléens

Enfin, les booléens servent à exprimer le vrai ou le faux. Il n'y a que deux
valeurs possibles pour ce type de variables : `True` (vrai) et `False` (faux).

Des valeurs booléennes sont renvoyées par les opérations de comparaison :  
- `==` pour l'égalité. `a == b` va renvoyer `True` si a et b sont égaux
- `!=` pour la différence. `a != b` va renvoyer `True` si a et b sont différents
- `<` et `>` pour les inégalités strictes. `a < b` va renvoyer `True` si a est
    strictement plus petit que b, et inversement pour `a > b`
- `<=` et `>=` pour les inégalités larges. `a <= b` va renvoyer `True` si a est
    plus petit ou égal à b, et inversement pour `a >= b`

Par exemple `1 < 2` vaut `True` mais `3 != 3` vaut
`False`.

Enfin, il est possible de manipuler les valeurs booléennes avec les opérateurs
`not`, `and` et `or` :

 - `not a` vaut l'inverse de `a`, donc `True` si a vaut `False`;
 - `a and b` vaut `True` si et seulement si `a` **et** `b` valent `True`;
 - `a or b` vaut `True` si et seulement si `a` **ou** `b` valent `True`.

#### Mini-Exercice
**But :** Après une discussion intense avec le marchand, Joseph n'est plus sûr
de ses calculs. Les bananes coûtant 3€, il pense que pour 7 bananes il en aura
pour 22€. Calcule le vrai prix et affiche si celui de Joseph est le bon.



[SECTION-BREAK]




# Comment utiliser les boutons du `micro:bit` ?

Comme tu peux le voir, il y a deux boutons physiques sur le `micro:bit` : le bouton A et
le bouton B. Mais il y a aussi un bouton tactile au niveau du logo au-dessus de
l'écran qui a été ajouté avec la version 2 du `micro:bit`. 

Voici un petit schéma qui te permet de repérer les différents boutons : 

{{<figure src="resources/images/microbit_buttons.png" width=600 >}}

Pour utiliser les boutons A et B, tu peux respectivement utiliser la fonction
`button_a.get_presses()` et `button_b.get_presses()`. Ces fonctions renvoient le
nombre d'appuis sur le bouton depuis la dernière fois qu'elles ont été appelées.
Par exemple, ce code va prendre le nombre de fois que le bouton A a été appuyé
au cours des 5 dernières secondes :

```python
from microbit import *

sleep(5000)
display.scroll(button_a.get_presses())
```

En ce qui concerne le bouton tactile, tu peux détecter si tu appuies dessus
en utilisant la fonction `pin_logo.is_touched()`, qui renvoie un booléen. 

### Mini-exercice
**But :** Crée un programme qui affiche la somme du nombre d'appuis sur les
boutons A et B au cours des 3 dernières secondes. 

## Un exemple un peu plus complexe

Voici un exemple de petit programme qui déclenche un compte à rebours avant de
donner 5 secondes pour appuyer autant de fois que possible sur le bouton de gauche.

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

### Exercice 2

**But :** Joseph voudrait connaître le résultat de la multiplication de deux
nombres. Pour récupérer la valeur des deux nombres tu peux donner quelques secondes
à l'utilisateur pour appuyer le bon nombre de fois sur chaque bouton. Par exemple,
si pendant ce temps, tu appuies 3 fois sur le bouton de gauche et 7 fois sur celui 
de droite, le programme affichera `3 * 7 = 21` sur l'écran.









# Et si...

## Avant de continuer...

Avant de continuer avec les conditions (je t'explique ça juste
après), je dois t'expliquer une partie importante de la programmation Python :
l'**indentation**. 
L'indentation correspond au nombre d'espaces au début d'une ligne et avant une
instruction. Par exemple, la première ligne ci-dessous a une indentation égale
à **0** (pas d'espace en début de ligne), et la troisième ligne a une indentation
égale à **4** (quatre espaces en début de ligne).

```python
display.scroll("Coucou") # Ligne qui n'est pas indentée
if True:
    display.show(Image.HAPPY) # Ligne qui est indentée
```

L'indentation permet surtout de définir des blocs. Chaque ligne avec la même 
indentation fait donc partie du même bloc.

Avec des blocs indentés de 1, 3 puis 2 espaces, Python a du mal à comprendre ce 
qui se passe. En général, on décale le code de 4 espaces à chaque fois.

```python
display.scroll("Coucou")
if True:
  display.scroll("Ceci")
 display.scroll("est un")
   display.scroll("mauvais")
    display.scroll("exemple")
  display.scroll("d'indentation")
```

Tu peux te demander, comment facilement faire des indentations ? 
Eh bien il te suffit simplement d'appuyer sur la touche `tabulation`. Celle qui
ressemble à ça (c'est la touche juste au dessus de la touche `verrouillage
majuscule`): 

{{<figure src="resources/images/tabulation.png" width=200 >}}

Pour l'instant il te suffit juste de savoir ça, je reviendrai là-dessus juste
après. 


## Revenons à nos conditions

Maintenant que tu sais utiliser des variables et plusieurs fonctions de contrôle
du `micro:bit`, tu vas pouvoir faire réagir ton programme en fonction de toutes
ces données dans cette partie. Eh bien ça tombe bien, car Python sait faire ça grâce
aux instructions `if`, `elif` et `else`. 

L'instruction `if` permet de décider de n'exécuter un morceau de code que
lorsqu'une condition est vraie. Ce sont les mêmes conditions que celles décrites
dans la section "Booléens" de la partie sur les types de variables. 
Pour écrire une condition, la syntaxe est : `if condition:`
suivi d'un bloc de code indenté (il ne faut pas oublier les `:` à la fin de la 
ligne, sinon Python n'arrivera pas à exécuter la condition). Le bloc de code en 
question ne sera alors exécuté que si `condition` s'évalue à `True`. 

Un `if` peut être accompagné d'un `else` qui exécute un bloc de code uniquement 
si la condition du `if` est fausse. Enfin, il y a aussi le `elif` qui est la 
contraction du `else` et du `if`. Le `elif` n'est exécuté que si sa condition 
est vraie et que les conditions précédentes sont fausses.

Voici un exemple simple pour illustrer :

```python
from random import randint
from microbit import *

x = randint(0, 100)  # assigne un nombre aléatoire à x compris entre 0 et 100

if x < 30:
    display.scroll('x est inférieur à 30')
elif x < 50:
    display.scroll('x est supérieur ou égal à 30 et inférieur à 50')
elif x < 80:
    display.scroll('x est supérieur ou égal à 50 et inférieur à 80')
else:
    display.scroll('x est supérieur ou égal à 80')
```

### Mini-exercice
**But :** Essaye de trouver ce que va afficher le programme ci-dessus pour `x =
0`, `x = 42` et `x = 238`. 

*Remarques :*

- Un `if` n'est pas nécessairement accompagné d'un `else` (ou d'un `elif`).
Dans ce cas, si sa condition est fausse, rien n'est exécuté
- On peut ajouter autant de `elif` que l'on veut après un `if`

*Tout est clair ?*

Si jamais tu as une question ou s'il y a quelque chose que tu n'as pas compris,
n'hésite pas à demander aux organisateurs.

### Et les indentations dans tout ça ?

Comme tu as pu le voir dans les codes d'exemples, le _bloc de code_ qui est 
exécuté lorsque la condition du `if` est vérifiée est **indenté**. 
Lorsque l'on sort de la condition, le code perd son indentation. L'indentation 
permet à Python de différencier les `blocs de code` appartenant aux conditions, 
et ainsi de savoir ce qui doit être exécuté ou non.

La partie sur les indentations est une partie très importante car elle ne permet
pas seulement à Python de différencier les blocs de code, mais
aussi de rendre ton code plus clair et plus lisible. 
Si jamais tu as une quelconque question ou s'il y a quelque chose que tu n'as
pas compris, n'hésite pas à faire appel à un organisateur. 





[SECTION-BREAK]






# Ça fait beaucoup de lignes

Tu sais maintenant comment créer des programmes assez complexes. Mais imaginons
que tu veuilles effectuer plusieurs fois la même action. Tu pourrais écrire un
bout de code et le copier/coller le nombre de fois que tu veux le répéter, mais
c'est assez long et peu efficace. Eh bien ça tombe bien, il existe en Python ce
que l'on appelle des `boucles`, c'est-à-dire des petits bouts de codes qui
peuvent se répéter. Il en existe deux : les boucles `for` et les boucles
`while`. Nous allons commencer par la première.

## Pour un certain nombre de fois

Nous allons donc ici traiter la boucle `for`. Ce type de boucle sert à répéter
un certain nombre de fois un bloc de code. Ce nombre de répétitions **doit être
connu** d'une manière ou d'une autre. Le cas où ce nombre n'est pas connu est
traité dans la boucle `while` un peu plus bas. 

Voyons le fonctionnement de ce type de boucles à travers un exemple simple : 

```python
for i in range(5):
    # Ce qui suit va être répété 5 fois, une variable `i` est créée,
    # et va prendre successivement les valeurs 0, 1, 2, 3 puis 4.
    display.scroll("Coucou numéro " + str(i))
    sleep(500)

display.show(Image.HAPPY) # Cette ligne de code n'est pas répétée
```

- _Ligne 1_ : Ici, c'est la déclaration de la boucle. C'est la partie la plus complexe.
              Le mot clé `for` indique que la déclaration commence.
              Ensuite, il y a une variable `i`. Elle peut prendre n'importe quel nom,
              ça n'a pas d'importance. Il y a enfin le `range(5)` qui nous indique que
              la boucle sera répétée `5` fois. Comme indiqué en commentaire, la variable
              `i` prendra successivement les valeurs de 0 à 5 exclu. Le `5` peut être
              remplacé par n'importe quelle valeur numérique entière. 
- _Ligne 4_ : Affiche la phrase `"Coucou numéro "` suivie de la valeur de `i`. La fonction
              `str()` permet de transformer un entier en une chaîne de caractères. 
- _Ligne 5_ : Met en pause le programme pendant _500_ millisecondes
- _Ligne 7_ : Affiche un smiley souriant

Voici un petit schéma pour bien différencier les différents blocs de code : 

{{<figure src="resources/images/for_loop.png" width=400 >}}


Bien sûr, il est possible d'"emboîter" des boucles les unes dans les
autres :

```python
# La prochaine ligne ne sera exécutée qu'une seule fois:
display.scroll("start")

for i in range(5):  # Début du bloc `for` n°1
    # La prochaine ligne sera exécutée 5 fois:
    display.scroll("i=" + str(i))

    for j in range(5):  # Début du bloc `for` n°2
        # La prochaine ligne sera exécutée 5*5 = 25 fois:
        display.scroll("j=" + str(j))
    # Fin du bloc `for` n°2

    # La prochaine ligne sera aussi exécutée 5 fois:
    display.scroll("i=" + str(i))
# Fin du bloc `for` n°1

# La prochaine ligne ne sera aussi exécutée qu'une seule fois:
display.scroll("end")
```

### Mini-exercice
**But :** Comme pour l'exercice 2, Joseph voudrait connaître le résultat de la
multiplication de différents nombres. Sauf que cette fois-ci, il ne veut pas se
limiter à deux nombres. Écris un programme qui multiplie 3 nombres entre eux. Tu
peux récupérer les nombres en comptant le nombre d'appuis sur le bouton A, en
laissant quelques secondes à chaque fois. 

_Aide :_ Pour savoir quand tu passes au nombre suivant, tu peux allumer la LED
de coordonnée `(0, i)` à chaque début de boucle. 



## Tant que 

La boucle **while** est une boucle dont le bloc de code est répété tant qu'une
condition est vérifiée (d'où son nom :D). Illustrons cette boucle à travers un
exemple de code : 

```python
while button_a.get_presses() == 0:
    display.scroll("Appuie sur le bouton A pour sortir")
    sleep(500)

display.scroll("Tu es sorti !")
```

Nous avons sur la première ligne la déclaration de la boucle avec le mot-clé
`while` suivi de la condition d'arrêt. Ici, la boucle s'arrêtera lorsque tu 
appuieras sur le bouton A. 
Pour ce qui concerne les lignes suivantes, tu connais déjà leur comportement. 

### Mini-exercice
**But :** Écris un programme qui compte et affiche le nombre d'appuis sur les
boutons A et B avant que le bouton tactile ne soit touché. 

_Aide :_ Tu peux utiliser `display.show(Image.ALL_CLOCKS)` pour afficher une
horloge d'attente. 


[SECTION-BREAK]

# Projet

Il est maintenant temps de mettre en pratique tout ce que tu as appris au
cours de ce TP avec un petit projet. Rien de compliqué, je te rassure, et puis
si tu as des questions, les organisateurs sont là pour ça !

## But

Joseph est dans la panade... Il aurait besoin de deux dés à 6 faces pour jouer
au Monopoly avec ses amis, mais il les a oubliés, et tout ce qu'il a à sa
disposition est un `micro:bit`... 
Joseph te demande alors de lui faire un programme qui simule un lancé de deux 
dés et affiche le résultat (le résultat est donc entre 2 et 12) lorsque le
bouton A ou le bouton B est appuyé. 
Mais comme Joseph ne veut pas que ses amis pensent qu'il a simplement
oublié les vrais dés, il voudrait donc y ajouter quelques fonctionnalités : 
- Il voudrait que si le lancé est un double, un smiley content s'affiche
juste après le chiffre
- Par contre, il voudrait que si trois doubles sont faits d'affilée, un smiley pas
content s'affiche à la place du smiley content
- Il voudrait enfin que le smiley disparaisse 2 secondes après être apparu

## Tips

N'hésite pas à faire ce projet étape par étape. Tu peux commencer par coder le
lancé des deux dés, et lorsque cela fonctionne, ajouter les différentes demandes
de Joseph les unes après les autres. 

Pense aussi à remettre le nombre de doubles à zéro lorsque le `micro:bit` change
de joueur ! 

Tu peux aussi utiliser la fonction `display.clear()` pour effacer l'écran.

Si tu as une quelconque question, encore une fois, les organisateurs sont là
pour y répondre. 



# Conclusion

Voili voulou, je crois que mon rôle touche à sa fin. Tu as appris beaucoup de
choses durant ce TP d'introduction, alors n'hésite surtout pas si tu as une
question par rapport à quelque chose qui a été abordé (ou qui n'a pas été abordé
d'ailleurs) à demander de l'aide aux organisateurs. Tu peux aussi nous faire
part de tes remarques pour améliorer ce TP et le rendre encore plus clair. 

Mais ce n'est pas parce que ce TP est terminé que tu es lachée dans la nature
pour autant. Il te reste encore plein de trucs à découvrir, que ce soit en
Python ou bien en rapport au `micro:bit`. Tu as de nombreux
autres TPs qui sont disponibles. Ils se présentent plutôt sous la forme de
petits projets centrés sur l'utilisation d'un composant en particulier du
`micro:bit`. Tu peux ainsi apprendre à utiliser pleinement le `micro:bit` pour ensuite
créer tes propres projets ! 

Nous t'invitons donc à choisir les projets qui t'intéressent et 
avancer à ton rythme !








# Continuer la programmation chez soi

Si tu souhaites installer un logiciel de programmation sur ton ordinateur
plutôt que d'utiliser un site web, nous te recommandons vivement [Mu
editor](https://codewith.mu/) ([https://codewith.mu/](https://codewith.mu/)),
disponible sur Mac, Windows et Linux, facile à utiliser et possède un mode
spécial pour les `micro:bit`. 

Ce TP couvre les bases essentielles de la programmation, pour continuer nous te
conseillons les ressources suivantes :

- Girls Can Code! : Nous organisons des stages courts et des stages longs, tous
  les TPs des stages sont disponibles ici :
  [https://tp.girlscancode.fr/](https://tp.girlscancode.fr/).
- Prologin : un concours d'informatique pour les moins de 20 ans que nous
  organisons en plus des stages Girls Can Code!. Candidater ou s'entraîner sur
  les archives peuvent être un bon moyen de continuer à programmer. Si tu es
  sélectionnée, les épreuves régionales seront l'occasion de revoir les
  organisateurs que tu as rencontré ; et la finale est un super événement, mais ce
  n'est pas facile !
- France IOI ([http://www.france-ioi.org/](http://www.france-ioi.org/)) : un
  site d'entraînement à la programmation qui propose des leçons suivies de
  problèmes à résoudre, la difficulté y est très progressive.

Si un domaine de l'informatique t'intéresse en particulier, n'hésite pas à
demander aux organisateurs des références plus spécifiques.

Bonne continuation !


[SECTION-BREAK]



# Les fonctions du `micro:bit`

Cette partie regroupe toutes les fonctions de contrôle du `micro:bit` que nous
avons utilisées au cours de ce TP. Tu en verras aussi des nouvelles que nous
n'avons pas abordées, mais leur utilisation se base sur le même principe que les
autres. 
Si tu souhaites aller encore plus loin, tu peux trouver des informations plus
complète sur la documentation officielle en ligne trouvable ici:
[https://bbcmicrobitmicropython.readthedocs.io/en/latest/](https://bbcmicrobitmicropython.readthedocs.io/en/latest/).

Pour utiliser toutes ces fonctions il est nécessaire de les importer depuis le
module `micro:bit` en ajoutant `from microbit import *` au début de ton
programme.

## L'écran

### `display.clear()` - effacer l'écran

```python
display.clear()  # l'écran est maintenant éteint
```

### `display.set_pixel(x, y, value)` - allumer/éteindre un pixel

Change la luminosité d'une diode pour une valeur allant de 0 (diode éteinte), à
9 (luminosité maximale).

La diode est identifiée par sa colonne `x` et sa ligne `y` numérotée de 0 à 4.

```python
display.set_pixel(2, 2, 9)  # allume la diode centrale
display.set_pixel(0, 0, 5)  # allume à moitié la diode d'en haut à gauche
display.set_pixel(4, 4, 0)  # éteint la diode d'en bas à droite
```

### `display.get_pixel(x, y)` - calcule la luminosité d'un pixel

Réciproquement à `display.set_pixel(x, y, value)`, `display.get_pixel(x, y)`
récupère la valeur de luminosité d'une diode identifiée par sa colonne `x` 
et sa ligne `y`.

```python
display.set_pixel(2, 2, 9)  # allume la diode centrale
a = display.get_pixel(2, 2)  # `a` vaut maintenant 9
```

### `display.show(image)` - afficher une image

Cette fonction sert à afficher une image, le plus simple est généralement
d'utiliser une image parmi la liste prédéfinie : `Image.HEART`, `Image.HAPPY`,
`Image.HAPPY`, `Image.SAD`, `Image.YES`, `Image.NO`, ... Une liste plus complète
peut être trouvée [ici](https://microbit-micropython.readthedocs.io/en/latest/image.html#attributes).

```python
display.show(Image.HAPPY)  # affiche un smiley
display.show(Image.HEART)  # affiche un coeur
```

Il est aussi possible de dessiner soi-même une image à partir d'un texte en
séparant les lignes avec `:` et assignant une luminosité entre 0 et 9 à chaque
diode :

```python
bateau = Image('05050:'
               '05050:'
               '05050:'
               '99999:'
               '09990')

# Affiche une image qui ressemblera à peu près à ça:
#        x x
#        x x
#        x x
#       OOOOO
#        OOO
display.show(bateau)
```

### `display.scroll(texte)` - afficher du texte

Fait défiler le texte donné en entrée.

```python
display.scroll('Salut tout le monde !')  # affiche `Salut [...] !`
display.scroll(42)  # en réalité ça ne fonctionne pas qu'avec le texte !
```

## Les boutons

Il y a deux boutons sur le `micro:bit`, ils sont appelés `button_a` et
`button_b` et toute fonction qui peut être appelée pour l'un, peut aussi être
appelée pour l'autre.

### `button_a.is_pressed()` - état du bouton

Renvoie `True` si le bouton est actuellement enfoncé.

```python
while True:
    if button_b.is_pressed():
        # Allume la diode centrale si le bouton de droite est enfoncé
        display.set_pixel(2, 2, 9)
    else:
        # Éteint la diode si le bouton de droite n'est plus enfoncé
        display.set_pixel(2, 2, 0)
```

### `button_a.was_pressed()` - le bouton a été enfoncé

Renvoie `True` si le bouton a été enfoncé depuis la dernière fois que cette
fonction a été appelée.

```python
display.scroll('Appuyez sur le bouton de gauche pour arrêter le programme')

# Si le bouton n'a pas été enfoncé pendant que le texte défilait, on peut
# continuer le programme
if not button_a.was_pressed():
    display.scroll('Et bien continuons le programme ...')
    # ...
```

### `button_a.get_presses()` - nombre d'appuis sur le bouton

Renvoie le nombre total d'appuis sur le bouton depuis la dernière fois que
cette fonction a été appelée.

```python
sleep(5000)
nb_appuis = button_b.get_presses()
display.scroll(
    'Vous avez appuyé '
    + str(nb_appuis)
    + ' fois sur le bouton b en 5 secondes.'
)
```

## Les fonctions générales

### `sleep(millisecondes)` - Mettre en pause le programme

### `randint(min, max)` - De l'aléatoire

Renvoie un nombre entier aléatoire compris entre `min` et `max`. 

```python
from random import randint

display.scroll(randint(1, 10))
```

