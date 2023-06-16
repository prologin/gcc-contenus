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

