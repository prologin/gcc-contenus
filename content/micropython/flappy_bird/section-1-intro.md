# Le Flappy Bird

Le but de ce sujet est de reproduire une version très simplifiée du jeu Flappy Bird sur un `micro:bit`.

{{<figure src="resources/images/flappy.png" caption="Flappy Bird">}}

## Principe du jeu

Dans Flappy Bird, l'oiseau doit esquiver des tuyaux verticaux le plus longtemps possible. Dans notre jeu, nous ne ferons pas sauter l'oiseau, mais nous le déplacerons de haut en bas.

### L'oiseau

L'oiseau sera représenté par un pixel de forte intensité, il restera sur la même colonne et, comme expliqué au-dessus, vous pourrez le faire monter ou descendre grâce aux boutons du `micro:bit`.

### Les tuyaux

Les tuyaux constituent les obstacles du jeu et seront d'une intensité moyenne. Ils apparaîtront à droite et se déplaceront progressivement vers la gauche.

### Fin de la partie

La partie s'arrête lorsque l'oiseau percute un tuyau. Le score correspond au nombre de tuyaux qui auront été évités tout au long de la partie.
