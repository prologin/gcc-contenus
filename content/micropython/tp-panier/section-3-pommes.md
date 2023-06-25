# Partie II : Les pommes

Dans cette partie nous allons nous occuper de l'ajout des pommes.

Pour créer notre pomme nous allons utiliser deux variables `pomme_x` et `pomme_y`.
L'utilisation de ces deux variables va nous permettre de conserver la position des pommes, la position horizontale en x et la position verticale en y, dans deux variables (ou boîte).

```python
# Ici les variables contiennent les nombres 1 et 2.
pomme_x = 1
pomme_y = 2

# Pour afficher la pomme, qui est en 2e colonne, 3e ligne
display.set_pixel(pomme_x, pomme_y, 9)
```

*En cas de besoin, n'hésite pas à demander de l'aide aux organisateurs qui sont là pour t'aider.*

{{% box type="info" title="Rappel : générer des nombres aléatoires" %}}

```codepython
# Importer la fonction permettant de générer un nombre aléatoire
# Cette ligne doit apparaître tout en haut de ton fichier !
from random import randint

# Générer un nombre entier `a` entre 0 et 4 inclus
# et l'affiche
a = randint(0, 4)
print(a)
```

{{% /box %}}

Pour ce qui est des valeurs de ces variables, la pomme apparaîtra sur la ligne 0 et sur une colonne aléatoire du micro:bit. Tu as ci-dessus l'explication de comment créer un nombre aléatoire.


Tu peux maintenant faire apparaître une pomme de manière aléatoire sur l'axe x.

{{<figure src="resources/microbit_pomme.png" width=500 caption="Les pommes sur un microbit">}}

Il va falloir maintenant faire descendre la pomme de l'écran. Cependant, on veut que les pommes tombent moins vite que la vitesse de déplacement du panier. Si on fait tomber les pommes à chaque fois que l'on peut déplacer le panier, les pommes vont descendre trop vite. Sur ce principe, on va alors faire descendre les pommes tous les `X` tours de boucle, ce qui permettra de ralentir les pommes.

Pour cela, nous allons créer deux variables :
- `tour` : le nombre de tours de boucle que l'on a fait depuis la dernière fois qu'une pomme est descendue (est à 0 au début)
- `tour_max` : le nombre de tours de boucle que l'on doit attendre pour faire descendre une pomme que l'on mettra à 10

En utilisant les conditions et les variables que l'on vient de créer on va vérifier les conditions suivantes :
- Si `tour` est égal à `tour_max`, on va faire descendre la pomme en modifiant la variable `pomme_y` et remettre à 0 la variable `tour`.
- Sinon, ça veut dire que `tour` est inférieur à `tour_max`. Ainsi, on doit rajouter 1 à `tour` vu que l'on a fait un tour de boucle en plus.

{{% box type="exercise" %}}

Si la pomme est sur la dernière ligne, la plus basse, il faut alors gérer les deux cas suivants :
* la position est la même que celle du panier alors le joueur a réussi, et il faut faire apparaître une nouvelle pomme sur l'écran.
* sinon, c'est que le joueur a perdu. (Tu peux laisser cette partie vide pour l'instant, on y reviendra dans la 3e partie).

{{% /box %}}


## Compter les pommes

Par ailleurs, il est nécessaire de compter le nombre de pommes attrapées au cours de la partie.
Pour faire cela, tu peux utiliser une variable te servant de compteur.
À la fin de la partie, tu peux, à l’aide de ce compteur, afficher le nombre de pommes attrapées.
Ce compteur est initialisé à 0 et s’incrémente de 1 à chaque fois qu’une pomme touche le panier.
Attention, il ne faut pas comptabiliser une pomme si celle-ci tombe à côté du panier.

{{% box type="warning" title="À vérifier"%}}

Avant de passer à la partie suivante, veille à vérifier ces différents points :
* toujours pouvoir bouger le panier dans les deux directions.
* avoir toujours au moins une pomme qui tombe sur ton écran.
* pouvoir attraper la pomme avec le panier.
* avoir un score qui compte le nombre de pommes attrapées.

{{% /box %}}

Si tu as le moindre problème avec ton jeu, n'hésite pas à appeler un organisateur pour lui demander des conseils.