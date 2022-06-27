---
title: Jeu du Panier Micropython
date: 2022
---

# Jeu du Panier


Maintenant que vous avez appris à utiliser des **micro:bit**, il est maintenant temps de passer aux choses sérieuses avec un petit projet. Ne vous inquiétez pas, ce TP est très guidé.


Le but de ce projet est de faire un **jeu du panier** :


![Jeu du panier](resources/game.png){width=5cm}


## Principe du jeu

Le principe général est de ramasser des pommes qui tombent du ciel à l'aide d'un panier.

![Jeu sur un microbit](resources/microbit_game.png){width=5cm}

### Le panier

Le panier se trouve sur le sol. Il peut se déplacer sur tout l'axe horizontal (axe X), mais pas sur l'axe vertical (axe Y). Il sert à ramasser les pommes qui tombent du ciel.

### Les pommes

Les pommes tombent une par une du ciel, depuis une position aléatoire. Il faut réussir à en attraper le plus possible pendant la partie.



### Fin de la partie

La partie se finit si une pomme touche le sol. Dans ce cas nous afficherons le score du joueur.

## Fonctionnement de la carte `micro:bit`


### L'écran

Chaque pixel de l'écran est une LED rouge, que l'on peut allumer ou éteindre à un certain degré d'intensité allant de 0 à 9 (0 -> éteinte, 9 -> allumée au maximum). La ligne de code ci-dessous allumera le pixel de la première ligne et troisième colonne au niveau d'intensité 6.

```python
# Attention, la numérotation des lignes et des colonnes commence à 0
display.set_pixel(0, 2, 6)
# display.set_pixel(coordonnée x, coodonnée y, intensité)
```

Il pourra vous être utile de réinitialiser l'écran et d'éteindre toutes les LED d'un coup. Pour cela, on utilise la fonction suivante.

```python
# Cette commande a le même effet que de mettre le degré d'intensité des 25 LED à 0.
display.clear()
```

### Les boutons

Afin de pouvoir diriger notre panier, nous allons utiliser les boutons A et B sur les côtés de l'écran. Quand on tient la carte `micro:bit` dans le bon sens, le bouton A est à gauche et le bouton B est à droite. On souhaite que l'appui sur le bouton A fasse déplacer la balle d'un pixel à gauche, et le B d'un à droite.

Reste à savoir comment détecter qu'un bouton a été pressé. Il existe pour cela 3 fonctions principales.

```python
button_a.is_pressed()   # Ces fonctions renvoient True ou False si les boutons sont
button_b.is_pressed()   # appuyés quand la ligne est exécutée par le micro:bit

button_a.was_pressed()  # Ces fonctions renvoient True ou False si les boutons ont
button_b.was_pressed()  # été appuyés depuis la dernière fois qu'elles ont été appelées

button_a.get_presses()  # Ces fonctions renvoient le nombre d'appuis effectués sur
button_b.get_presses()  # le bouton depuis la dernière fois qu'elles ont été appelées
```

Pour ce projet, nous utiliserons principalement `get_presses()` pour déplacer notre panier à l'emplacement voulu.

Maintenant ce rappel fait, passons au jeu !

## Partie I : Le panier

*Attention pensez à bien importer la bibliothèque **microbit** avant de commencer.*
```python
from microbit import *
```

Dans cette partie nous allons simplement nous occuper du panier. Le panier fait 1 pixel de large.
Pour ce faire, commençons par créer une variable `posPanier` qui sera la position du panier en X. Au début de la partie, le panier sera au milieu de l'écran, soit en position 2 (image ci-dessous). 


![Le panier sur un microbit](resources/microbit_panier.png){width=5cm}



Maintenant que cette variable est créée, nous allons vouloir déplacer notre panier. 

Pour cela, tant que le joueur n'a pas perdu, on laissera le joueur faire bouger le panier. Vous pouvez utiliser une variable booléenne pour cela.

![Le panier qui bouge sur un microbit](resources/microbit_panier_move.png){width=5cm}


### Rappel :  
Une variable booléenne représente deux valeurs : `True` ou `False`.
Les valeurs `True` et `False` représentent respectivement les états `Vrai` et `Faux`.
Nous sommes à l'état `Vrai` lorsque l'affirmation que l'on teste est vérifié. 
```python
#on teste l'égalité 1 = 1 
>>>1==1
#ce test nous renvoie le mot clé `True` donc l'affirmation 1=1 est vrai
True
Une variable booléenne peut donc être utilisée dans une condition ou comme condition d'une boucle. 
Pour une utilisation dans une boucle, il faudra penser à actualiser la valeur de notre variable à l'intérieur de notre boucle. 

```python
# on définit notre variable booléen à `True` à l'état initial.
v_bool = True

if vBool:
    # si la variable est à vrai alors le programme évalue 
    # les expressions à l'intérieur de la condition

#on initialise la variable `en_cours` à `True` 
en_cours = True   
x = 0

while en_cours: 
    # tant que la variable reste à vrai alors on évalue les 
    # expressions dans la boucle 
   
     # si x est égale à 5  
    if x ==5:
        #alors on met la variable en_cours à `False`
        en_cours = False
        # en_cours étant à `False` on sort de la boucle 
   
     # sinon on ajoute 1 à x
    else:
          x = x + 1
        
>>> print(x)
5
```


Dès que le panier change de position il faut afficher sa nouvelle position sur l'écran. Ensuite il faut recalculer la position du panier.

Afin de vous faciliter le travail, nous vous conseillons d'utiliser une variable qui contiendra la position du panier. Ainsi vous pourrez plus facilement déterminer la nouvelle position du panier en fonction des boutons pressés. 

### Attention : 
Il faut faire en sorte que le panier ne sorte pas de l'écran, sinon cela causera une erreur.
Pour cela, n'oubliez pas de vérifier, à l'aide de conditions, les cas suivants : 
* si la plateforme dépasse vers la droite, que faire ?
* si la plateforme dépasse vers la gauche, que faire ?

Avant de passer à la partie suivante assurez vous d'avoir un panier pouvant bouger à droite et à gauche sur toute la ligne grâce aux boutons.

## Partie II : Les pommes

Cette partie va comprendre l'ajout des pommes.

Dans un premier temps, voici comment créer un nombre aléatoire en python : 
```python
# importer la librairie aléatoire :
from random import *

# générer un nombre entier "a" entre 0 et 4 inclus :
a = randint(0, 4)
```

La variable `a` peut ici contenir la valeur `0`, `1`, `2`, `3`, ou `4`.


Pour créer la pomme nous allons utiliser un `tuple`. Un tuple est couple de variable.

```python
# ici la variable a est un tuple contenant les nombres 1 et 2.
>>> a = (1, 2)
>>> print(a)
(1, 2)
# pour changer les valeurs d'un tuple, il faut le réassigner :
>>> a = (3, 4)
>>> print (a)
(3, 4)
```

Vous pouvez maintenant faire apparaitre une pomme de manière aléatoire, changer son emplacement. À chaque tour, la pomme doit descendre sur l'axe vertical.

![Les pommes sur un microbit](resources/microbit_pomme.png){width=5cm}



Vous pouvez utiliser la fonction `sleep(time)` pour attendre entre chaque tour. Nous vous conseillons de mettre la valeur `time` dans une variable et de la définir au début de votre code.

Si la position de la pomme est sur la dernière ligne, la plus basse, il faut alors gérer les deux cas suivants : 
- la position est la même que celle de la pomme alors le joueur a réussi, et il faut faire apparaître une nouvelle pomme sur l'écran.
- sinon, c'est que le joueur a perdu.


### Compter les pommes
Par ailleurs, il est nécessaire de compter le nombre de pommes attrapées au cours de la partie. 

Pour faire cela vous pourrez utiliser une variable, vous servant de compteur. 

À l’aide de ce compteur, vous pourrez compter le nombre de pommes qui ont été attrapées et afficher ce score.

Ce compteur est initialisé à 0 et s’incrémente de 1 à chaque fois qu’une pomme touche le panier.

Attention, il ne faut pas comptabiliser une pomme si celle-ci tombe à côté du panier.

Avant de passer à la partie suivante, veillez a vérifier ces différents points : 
* toujours pouvoir bouger le panier dans les deux directions.
* avoir toujours au moins une pomme qui tombe sur votre écran.
* pouvoir attraper la pomme avec le panier.
* avoir un score qui compte le nombre de pommes attrappées.

## Partie III : Fin de partie

Quand le joueur a perdu, il faut sortir de la boucle. Pour ce faire, il suffit de passer notre condition de boucle à `False`.

Une fois sorti de la boucle, vous devrez afficher un message pour indiquer au joueur que ce dernier a perdu.

Pour finir cette partie, vérifier que si l'on n'attrape pas la pomme, la partie se termine bien et affiche le score.

## Partie IV : Améliorations

Une fois le jeu fini, vous pouvez ajouter plusieurs améliorations. Notez que chaque amélioration est réalisable indépendamment des autres. 

### Accélération de la chute des pommes!

Pour rendre la partie plus difficile et amusante, vous pouvez faire augmenter la vitesse de chute des pommes au cours du temps. 
*Il faut tout de même s'assurer que le jeu reste faisable, en posant par exemple une limite de vitesse de chute.*

## Rejouer et meilleur score

Cette partie a pour objectif d'améliorer votre jeu qui est déjà fonctionnel. Pour cette partie vous aurez besoin de faire appel à un nouveau type d'implémentation : les fonctions. 

---
### Les fonctions
En programmation, les fonctions sont très similaires aux fonctions mathématiques. En général les fonctions prennent un ou plusieurs arguments en paramètre, et retournent un résultat. 

La première étape pour utiliser une fonction est de la définir. Pour cela nous utilisons le mot clé ```def``` suivi du nom de notre fonction puis des arguments que l'on souhaite utiliser entre parenthèses. Attention à ne pas oublier les 2 points après la parenthèse fermante. 

```python
def nom_fonction(parametre1, parametre2):
```
Une fois que nous avons choisi le nom de notre fonction et déterminé le nombre d'arguments néscessaires, nous pouvons définir le comportement de notre fonction. 

#### Exemple : 
Essayons de faire une fonction qui effectue la somme de ses deux arguments. 
```python
def somme(nbr1, nbr2): # Ici nous avons déclaré le nom de notre 
                      #fonction et ses arguments 
                      
    return nbr1 + nbr2 # Le mot clef return permet de renvoyer 
                     # le résultat de l'addition
```
La fonction `somme` renvoie donc le résultat de la somme des deux nombres passés en paramètre. 

Maintenant que nous avons défini notre fonction `somme`, nous allons pouvoir l'utiliser. Pour ce faire rien de plus simple, il suffit d'appeler le nom de notre fonction avec les 2 nombres que nous voulons additionner en paramètre. 

```python
>>> somme(2, 4)
```
Vous remarquerez que l'appel de notre fonction ne fais rien. C'est normal car ce que nous ne faisons rien du résultat de notre fonction. Plusieurs possibilités s’offrent à nous, nous pouvons afficher le résultat, le stocker dans une variable...
```python
>>> print(somme(2, 3))
5
>>> resultat = somme(2, 3)
>>> print(resultat)
5
```

*Pro tips : Attention l'ordre dans lequel vous renseignez vos arguments peut avoir un impact sur le résultat.*


---
Maintenant que nous en avons terminé avec cette partie de cours, passons à l'application directe pour notre jeu. 

Une fois que le joueur a perdu, vous pouvez lui proposer de rejouer une partie. Pour cela, vous pouvez utiliser les connaissances que vous avez déjà, notamment les boucles, mais vous pouvez aussi utiliser des fonctions. 

Ainsi, le joueur pourra relancer une partie en cliquant sur un bouton, ou arrêter le jeu en cliquant sur un autre. 
L'intérêt de relancer une partie sans relancer tout le programme est que l'on peut conserver des données des parties précédentes, comme le **meilleur score**.

Ainsi, à la fin d'une partie, en plus du score réalisé, vous pourrez afficher le meilleur score réalisé jusque-là.

L'idée est d'utiliser une première fonction pour retourner le résultat d'une partie et ensuite d'utiliser une seconde fonction pour traiter le résultat et gérer les autres fonctionnalités de notre jeu.

Avant de finir ce projet, vérifier d'avoir bien implémenté c'est différents éléments : 
* augmentation de la vitesse 
* best score
* pouvoir jouer normalement 
* relancer la partie


# FIN
Bravo te voilà arrivée à la fin de ce projet !
Vous avez maintenant un code qui fonctionne. Si vous avez des idées d’amélioration, essayez de les mettre en place par vous même !