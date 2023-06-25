Maintenant que tu as appris à utiliser des **micro:bit**, il est temps de passer aux choses sérieuses avec un petit projet guidé.
Le but de ce projet est de faire un **jeu du panier** :

![Jeu du panier](resources/game.png)

# Principe du jeu

Le principe général est de ramasser des pommes qui tombent du ciel à l'aide d'un panier.

{{<figure src="resources/microbit_game.png" width=500 caption="Jeu sur un microbit">}}

## Le panier

Le panier se trouve sur le sol. Il peut se déplacer sur tout l'axe horizontal (axe X), mais pas sur l'axe vertical (axe Y). Il sert à ramasser les pommes qui tombent du ciel.

## Les pommes

Les pommes tombent une par une du ciel, depuis une position aléatoire. Il faut réussir à en attraper le plus possible pendant la partie.

## Fin de la partie

La partie se finit lorsqu'une pomme touche le sol. Dans ce cas, nous afficherons le score du joueur.

{{% box type="info" title="Petit récapitulatif" %}}

Avant de coder quoi que ce soit il faut être sûr d'avoir une idée concrète de ce que tu vas faire.

Si on reprend globalement ce que l'on va faire on peut décomposer le jeu en trois étapes :
- Étape 1 : créer le panier, celui-ci ne pourra faire qu'aller vers la gauche ou la droite, en restant bloqué sur la ligne du bas.
- Étape 2 : créer une pomme, celle-ci apparaîtra sur la ligne du haut et sur une colonne aléatoire. Elle descendra tous les "x" temps.
- Étape 3 : si on n'attrape pas la pomme, il faut afficher un message de fin de partie et arrêter le jeu.

{{% /box %}}