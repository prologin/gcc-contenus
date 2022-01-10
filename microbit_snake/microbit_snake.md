---
title: Jeu de Snake
date: 2021
author: Dorian 'Renji' Péron
---

# Le jeu de Snake

Le but de cet exercice est de coder le jeu [Snake](https://fr.wikipedia.org/wiki/Snake_(genre_de_jeu_vid%C3%A9o)) sur `micro:bit`.

![Snake sur Nokia](imgs/snake.jpg){height=5cm}

## Principe du jeu

Dans Snake, le joueur contrôle un serpent dans une zone quadrillée. Le but est de survivre le plus longtemps possible.
Le serpent a la possibilité de ramasser des pommes sur le chemin pour grandir. Il grandi d'une case par pomme récupérée.

La partie s'arrête quand le serpent se mord la queue. Le score du joueur est la taille du serpent.

## Notre version sur `micro:bit`

Le `micro:bit` a un écran carré de 5x5 pixels, qui sera l'environnement de notre serpent. Une partie du code est déjà fournie, n'hésite pas à t'en servir !

### Le serpent

Dans notre code, on va représenter le serpent comme une liste de coordonnées sur l'écran. La première valeur de la liste est la tête de notre serpent.

```py
snake = [(2, 2), (2, 3), (3, 3), (3, 4)]
snake_len = 4 # Le serpent a une taille de 4 cases
```

L'exemple ci-dessus correspond au serpent en Figure \ref{step0} (la tête est le carré plein).

![Étape 0\label{step0}](imgs/snake_0.png)

Nous nous intéressons au déplacement du serpent. Pour cela,
il faut savoir dans quelle direction il va. C'est à ça que sert la variable `direction` que l'on initialise par défaut à `UP`. Au début de la partie, le serpent ira donc vers le haut.

Nous souhaitons pouvoir diriger le serpent avec les boutons A et B du `micro:bit` de la façon suivante :

- si l'on appuie sur **A**, le serpent tourne à gauche
- si l'on appuie sur **B**, il tourne à droite
- sinon, le serpent ne change pas de direction

Tu peux implémenter la fonction `new_direction()` qui prend en argument la direction actuelle du serpent, qui vérifie si les boutons ont été pressés et qui renvoie la nouvelle direction du serpent.

Pour cela, tu peux t'aider des variables définies au début du ficher:

```py
# Directions
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
```

Après avoir trouvé la direction du serpent, il faut le déplacer. Imaginons que dans l'exemple précédent, le serpent aille vers la gauche. Après s'être déplacé, l'écran ressemblera à la Figure \ref{step1}.

![Étape 1\label{step1}](imgs/snake_1.png)

Comme tu peux le voir, la tête du serpent s'est déplacée d'une case vers la gauche, et le bout de la queue du serpent a disparu !

Tu peux implémenter la fonction `new_head()` qui prend en paramètres le serpent et sa direction et qui renvoie les coordonnées de sa nouvelle tête.

Attention : Si le serpent arrive contre un mur, il passe de l'autre côté de l'écran !

Maintenant que les fonctions `new_direction()` et `new_head()` fonctionnent, tu peux les appeler dans la boucle principale du jeu. La première étape est de mettre à jour la direction du serpent. Ensuite, on trouve la nouvelle tête du serpent. Pour ajouter la nouvelle tête dans la liste du serpent, tu peux faire comme cela :

```py
# Ajoute l'element en premiere place de la liste
liste.insert(element, 0)
```

N'oublie pas de retirer la derniere case du serpent !
Tu peux utiliser la méthode suivante

```py
# Retire la dernière case d'une liste
liste.pop()
```

Maintenant, tu devrais être capable de faire bouger ton serpent sur le `micro:bit` en appuyant du les boutons ! Mais il n'y a pas encore de challenge car le serpent de grandit pas.

### La pomme

Maintenant que le serpent peut se déplacer, nous pouvons placer des pommes sur le terrain pour le faire grandir.

À chaque tour de boucle :

- S'il n'y a pas de pomme sur le terrain, on en place une de manière aléatoire qui ne soit pas sur le terrain
- Si la tête du serpent atteint une pomme, celle-ci disparait et la taille du serpent augmente de 1

## Astuces (utiles pour certaines parties du projet)

On peut vérifier qu'une valeur est présente dans une liste de la manière suivante :

```py
>>> snake = [(1, 0)]
>>> (0, 1) in snake
False
>>> (1, 0) in snake
True
```

Pour choisir aléatoirement un nombre, tu peux utiliser la fonction `randint` :

```py
>>> randint(0, 1)
1
>>> randint(0, 1)
0
>>> randint(0, 10)
7
```

