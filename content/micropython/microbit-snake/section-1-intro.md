# Le jeu de Snake

Le but de cet exercice est de coder le célèbre jeu [Snake](https://fr.wikipedia.org/wiki/Snake_(genre_de_jeu_vid%C3%A9o)) sur une carte `micro:bit`.

{{< figure src="resources/images/snake.jpg" >}}

## Principe du jeu

### Le serpent

Dans Snake, le joueur contrôle un serpent dans une zone quadrillée. Le serpent peut bouger dans les quatre directions (haut, bas, gauche et droite) et réapparaît de l'autre côté quand il rentre dans un mur. Le but du jeu est de survivre le plus longtemps possible.

### Les pommes

Pendant la partie, des _pommes_ vont apparaître à des endroits aléatoires sur l'écran, représentées sous la forme de simples pixels. Quand le serpent mange une pomme (c'est-à-dire quand la tête du serpent arrive sur une pomme), il grandit d'une case, et une nouvelle pomme apparaît sur l'écran.

Sur notre `micro:bit`, ça ressemble à ça :

{{< figure src="resources/images/snake_example.png" >}}

On distingue que la tête du serpent (entourée en blanc) est plus lumineuse que le corps. On voit aussi une pomme qui est entourée en vert.

### Fin de la partie

La partie s'arrête quand le serpent se mord la queue (c'est-à-dire quand la tête du serpent arrive sur une case de son corps). Le score du joueur est la taille du serpent. En général, on considère la partie comme gagnée si le score est égal au nombre de pixels sur l'écran (ça veut dire que le serpent a complètement rempli l'écran).

### Notions

Dans ce TP tu apprendras deux nouvelles notions un peu complexe mais très utile : les _fonctions_ et les _tuples_.

On te le répètera tout au long du TP, mais n'hésite surtout pas à appeler un organisateur en cas de besoin, que ce soit pour corriger les erreurs de ton code, te réexpliquer une ancienne notion ou même pour t'expliquer plus en détail les fonctions et les tuples si tu n'as pas compris.

Passe à la section suivante pour apprendre comment utiliser ton `micro:bit` !
