---
title: "Microbit Snake"
weight: 10
authors: ["Dorian Péron"]
subtitle: Recrée le jeu Snake sur ton Micro:bit !
code_stub_url: resources/snake_a_completer.py
---

# Le jeu de Snake

Le but de cet exercice est de coder le célèbre jeu [Snake](https://fr.wikipedia.org/wiki/Snake_(genre_de_jeu_vid%C3%A9o)) sur une carte `micro:bit`.

{{< figure src="resources/images/snake.jpg" >}}

## Principe du jeu

### Le serpent

Dans Snake, le joueur contrôle un serpent dans une zone quadrillée. Le serpent peut bouger dans les quatre directions (haut, bas, gauche et droite) et réapparaît de l'autre côté quand il rentre dans un mur. Le but du jeu est de survivre le plus longtemps possible.

### Les pommes

Pendant la partie, des "pommes" vont apparaître à des endroits aléatoires sur l'écran, représentées sous la forme de simples pixels. Quand le serpent mange une pomme (c'est-à-dire quand la tête du serpent arrive sur une pomme), il grandit d'une case, et une nouvelle pomme apparaît sur l'écran.

Sur notre `micro:bit`, ça ressemble à ça :

{{< figure src="resources/images/snake_example.png" >}}

On distingue que la tête du serpent (entourée en blanc) est plus lumineuse que le corps. On voit aussi une pomme qui est entourée en vert.

### Fin de la partie

La partie s'arrête quand le serpent se mord la queue (c'est-à-dire quand la tête du serpent arrive sur une case de son corps). Le score du joueur est la taille du serpent. En général, on considère la partie comme gagnée si le score est égal au nombre de pixels sur l'écran (ça veut dire que le serpent a complètement rempli l'écran).

Pour coder notre jeu Snake, nous allons utiliser une carte `micro:bit`. Sur la carte, il y a 2 boutons (A et B) ainsi que l'écran qui nous intéressent. L'écran est composé de 25 pixels rouges répartis sur 5 lignes et 5 colonnes. Les sections suivantes expliquent comment les utiliser.

Passe à la section suivante pour apprendre comment utiliser ton `micro:bit` !

[SECTION-BREAK]

# Fonctionnement de la carte `micro:bit`

## L'écran

Chaque pixel de l'écran est une LED rouge, que l'on peut allumer ou éteindre à un certain degré d'intensité allant de 0 à 9 (0 -> éteinte, 9 -> allumée au max). La ligne de code ci-dessous allumera le pixel de la première ligne et troisième colonne au niveau 6.

```py
# Attention, la numérotation des lignes et des colonnes commence à 0
# Cette ligne va allumer le pixel sur la 1ère ligne et 3ème colonne,
# Avec une intensité lumineuse de 6.
display.set_pixel(0, 2, 6)
```

Il pourra vous être utile de réinitialiser l'écran et d'éteindre toutes les LEDs d'un coup. Pour cela, on utilise la fonction suivante.

```py
# Cette commande a le même effet que faire display.set_pixel(...) avec une intensité de 0
# 25 fois (pour chaque pixel) !
display.clear()
```

## Les boutons

Afin de pouvoir diriger notre serpent, nous allons utiliser les boutons A et B sur les côtés de l'écran. Quand on tient la carte `micro:bit` dans le bon sens, le bouton A est à gauche et le bouton B est à droite. On souhaite que l'appui sur le bouton A fasse tourner le serpent à gauche, et le bouton B à droite.

Reste à savoir comment être alerté dans notre code quand un bouton a été appuyé. Il existe pour cela 3 fonctions utiles.

```py
# Ces fonctions renvoient True ou False si les boutons sont
# appuyés quand la ligne est exécutée par le micro:bit
button_a.is_pressed()
button_b.is_pressed()

# Ces fonctions renvoient True ou False si les boutons ont
# été appuyés depuis le dernier appel à ces fonctions
button_a.was_pressed()
button_b.was_pressed()

# Ces fonctions renvoient le nombre d'appuis effectués sur
# le bouton depuis le dernier appel à ces fonctions
button_a.get_presses()
button_b.get_presses()
```

Pour ce projet, le plus pratique est d'utiliser `was_pressed()` pour pouvoir orienter le serpent en conséquence.

[SECTION-BREAK]

# Notre version de Snake sur `micro:bit`

Tu peux commencer à coder en téléchargeant le code à compléter (tout en haut de la page). Celui-ci est composé de plusieurs fonctions à compléter, ainsi que de la boucle principale de jeu (qui commence à la ligne `while longueur_serpent < 25`). On mettra dans la boucle du jeu les actions qu'il faudra effectuer tant que la partie n'est pas finie : déplacer le serpent, placer une pomme sur le terrain, etc...

## Le serpent

Dans notre code, on va représenter le serpent comme une liste de coordonnées sur l'écran. La première valeur de la liste est la tête de notre serpent.

Les coordonnées sont représentées par des **tuples** `(x, y)`. Un tuple est une
structure de donnée qui est une paire composée d'autres types de données.
Ici, on utilise des tuples d'entiers.

```py
serpent = [(2, 2), (2, 3), (3, 3), (3, 4)]
longueur_serpent = 4 # Le serpent a une taille de 4 cases
```

L'exemple ci-dessus correspond au serpent sur l'image suivante (la tête est le carré plein).

{{< figure src="resources/images/snake_0.png" >}}

Nous nous intéressons au déplacement du serpent. Pour cela,
il faut savoir dans quelle direction il va. C'est à ça que sert la variable `direction` que l'on initialise par défaut à `HAUT`. Au début de la partie, le serpent ira donc vers le haut.

Pour rappel, nous souhaitons pouvoir diriger le serpent avec les boutons A et B du `micro:bit` de la façon suivante :

- si l'on appuie sur **A**, le serpent tourne à gauche
- si l'on appuie sur **B**, il tourne à droite
- sinon, le serpent ne change pas de direction

Tu peux implémenter la fonction `nouvelle_direction()` qui prend en argument la direction actuelle du serpent, qui vérifie si les boutons ont été pressés et qui renvoie la nouvelle direction du serpent.

Pour cela, tu peux t'aider des variables définies au début du ficher :

```py
# Directions
HAUT = 0
DROITE = 1
BAS = 2
GAUCHE = 3
```

Pour rappel, une fonction est une sorte de machine qui transforme des variables que tu lui donnes en une autre variable. On la définit de la manière suivante :

```py
def nom_de_la_fonction(var1, var2):
    # On peut faire ce qu'on veut dans le "corps" de la fonction
    # Ici on additionne les variables qui nous sont données
    variable_retour = var1 + var2
    return variable_retour
```

Après avoir trouvé la direction du serpent, il faut le déplacer. Imaginons que dans l'exemple précédent, le serpent aille vers la gauche. Après s'être déplacé, l'écran ressemblera à l'image suivante.

{{< figure src="resources/images/snake_1.png" >}}

Comme tu peux le voir sur l'image, la tête du serpent s'est déplacée d'une case vers la gauche, et le bout de la queue du serpent a disparu !

Tu peux implémenter la fonction `nouvelle_position_tete()` qui prend en paramètres le serpent et sa direction et qui renvoie les coordonnées de sa nouvelle tête.

_Attention :_ Si le serpent arrive contre un mur, il passe de l'autre côté de l'écran !

Maintenant que les fonctions `nouvelle_direction()` et `nouvelle_position_tete()` fonctionnent, tu peux les appeler dans la boucle principale du jeu. La première étape est de mettre à jour la direction du serpent. Ensuite, on trouve la nouvelle tête du serpent. Pour ajouter la nouvelle tête dans la liste du serpent, tu peux faire comme cela :

```py
# Ajoute l'élément en première place de la liste
liste.insert(0, element)
```

Tu peux exécuter ce petit code pour mieux comprendre :

```codepython
liste = [1, 2, 3]
liste.insert(0, 8)
print(liste)
# Doit afficher [8, 1, 2, 3]
```

N'oublie pas de retirer la dernière case du serpent !
Tu peux utiliser la méthode suivante

```py
# Retire la dernière case d'une liste
liste.pop()
```

```codepython
liste = [1, 2, 3]
liste.pop()
print(liste)
# Doit afficher [1, 2]
```

Maintenant, tu devrais être capable de faire bouger ton serpent sur le `micro:bit` en appuyant sur les boutons ! Mais il n'y a pas encore de challenge car le serpent ne grandit pas encore.

## La pomme

Maintenant que le serpent peut se déplacer, nous pouvons placer des pommes sur le terrain pour le faire grandir.

À chaque tour de boucle :

- S'il n'y a pas de pomme sur le terrain, on en place une de manière aléatoire qui ne soit pas sur le serpent. Pour cela, on choisit deux nombres **X** et **Y**, compris entre 0 et 4, et si (X, Y) n'est pas une partie du serpent, on y ajoute la pomme. Sinon, on choisit deux autres valeurs aléatoirement et on recommence.
- Si la tête du serpent atteint une pomme, celle-ci disparait et la taille du serpent augmente de 1.

Tu peux aller voir dans les _astuces_ à la fin du TP pour savoir comment vérifier si une coordonnée (X, Y) est présente dans une liste.

## Conclusion

À ce point, ton jeu Snake devrait être fonctionnel. **Bien joué !** Tu peux essayer ton jeu pour atteindre le score maximal ! Si c'est trop simple, tu peux augmenter la vitesse de déplacement du serpent en mettant un plus petit nombre dans l'instruction `sleep()`.

[SECTION-BREAK]

# Astuces (utiles pour certaines parties du projet)

On peut vérifier qu'une valeur est présente dans une liste de la manière suivante :

```codepython
snake = [(1, 0)]
print((0, 1) in snake) # C'est faux
print((1, 0) in snake) # C'est vrai
```

Pour choisir aléatoirement un nombre entier, tu peux utiliser la fonction `randint` :

```codepython
# randint(a, b) renvoie un nombre aléatoire choisi entre a et b
# Exécute plusieurs fois ce code, il affichera des chiffres différents
from random import randint
print(randint(1, 6))
```

Dans le code fourni, la ligne suivante permet de vérifier si le
serpent se mord la queue :

```py
if serpent[0] in serpent[1:]:
```

Cela fonctionne car quand on écrit `ma_liste[x:]`, on crée la sous-liste de
`ma_liste` qui commence à l'index `x`. Tu peux vérifier ce fonctionnement avec le code
suivant :

```codepython
ma_liste = ["Je", "suis", "Joseph", "Marchand"]

print(ma_liste[1:])

print(ma_liste[3:])
```
