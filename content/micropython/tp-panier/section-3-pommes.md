# Partie II : Les pommes

Dans cette partie, tu vas t'occuper des pommes en quatre étapes :
1. Faire apparaître la pomme.
2. Faire tomber la pomme.
3. Faire réapparaître la pomme lorsque la précédente a été attrapée par le panier.
4. Compter le nombre de pommes attrapées pour avoir un score.

## Faire apparaître la pomme

Pour créer la pomme, tu vas utiliser deux variables : `pomme_x` et `pomme_y`.
L'utilisation de ces deux variables te permet de conserver la position horizontale de la pomme en x, et sa position verticale en y.

```python
pomme_x = 1
pomme_y = 4

# Pour afficher la pomme en 2e colonne, 1re ligne (celle du haut).
display.set_pixel(pomme_x, pomme_y, 9)
```

{{% box type="info" title="Rappel : Générer un nombre aléatoire 🎲" %}}

```codepython
# Importer la fonction permettant de générer un nombre aléatoire.
# Cette ligne doit apparaître tout en haut de ton fichier.
from random import randint

# Générer un nombre entier entre 0 et 4 (inclus).
a = randint(0, 4)
print(a)
```

{{% /box %}}

La pomme apparaît dans une colonne **aléatoire** (axe X) sur la ligne du haut (axe Y) du micro:bit.

{{<figure src="resources/microbit_pomme.png" width=500 caption="Positions possibles où la pomme peut apparaître sur le micro:bit">}}

{{% box type="exercise" title="Étape 3 : Faire apparaître la pomme" %}}

Initialise les variables `pomme_x` et `pomme_y` aux valeurs qui conviennent.

{{% /box %}}

*En cas de besoin, n'hésite pas à demander de l'aide aux organisateurs qui sont là pour t'aider.*


## Faire tomber la pomme

Il faut maintenant faire descendre la pomme de l'écran. Cependant, on veut que les pommes tombent moins vite que le panier ne se déplace. Si on fait tomber les pommes à chaque fois que l'on peut déplacer le panier, les pommes vont **descendre trop vite**.

Pour ralentir leur chute, tu vas utiliser un compteur : la pomme ne descendra qu'après un certain nombre de tours de boucle (par exemple, tous les 10 tours).

{{% box type="exercise" title="Étape 4 : Faire tomber la pomme" %}}

Pour faire tomber la pomme, tu crées deux variables :
- `tour` : le nombre de tours de boucle effectués depuis la dernière fois qu'une pomme est descendue. Cette variable est initialisée à 0.
- `tour_max` : le nombre de tours de boucle à attendre pour faire descendre une pomme. Donne-lui par exemple une valeur de 10.

En utilisant les conditions et les variables que tu viens de créer, vérifie les conditions suivantes :
- Si `tour` est égal à `tour_max`, tu fais descendre la pomme en modifiant la variable `pomme_y` et en remettant la variable `tour` à 0.
- Sinon, ça veut dire que `tour` est inférieur à `tour_max`. Augmente alors `tour` de 1.

N'oublie pas de redessiner la pomme à chaque tour.

{{% /box %}}

{{% box type="warning" title="La pomme traverse le sol" %}}

Si tu testes ton code, tu remarqueras qu'au bout d'un moment, le micro:bit t'affiche une erreur. Cela survient lorsque la pomme traverse le sol. Ne t'inquiète pas, la prochaine étape résout ce problème.

{{% /box %}}

## Faire réapparaître la pomme

{{% box type="exercise" title="Étape 5 : Faire réapparaître la pomme" %}}

Si la pomme est sur la dernière ligne, la plus basse, il faut gérer les deux cas suivants :
* Si sa position est la même que celle du panier, alors le joueur a réussi à l'attraper. Il faut alors faire apparaître une nouvelle pomme en haut de l'écran.
* Sinon, le joueur a perdu. Laisse cette partie vide pour l'instant, tu y reviendras dans la dernière partie du projet.

{{% /box %}}


## Compter les pommes attrapées

{{% box type="exercise" title="Étape 6 : Compter les pommes attrapées" %}}

Enfin, tu vas compter le nombre de pommes attrapées au cours de la partie. Pour cela, tu peux t'aider d'une variable.
Affiche ce score à la fin de la partie.

{{% /box %}}

{{% box type="warning" title="Pas de point gratuit"%}}

Il ne faut pas comptabiliser un point si la pomme tombe à côté du panier.

{{% /box %}}

## Avant de passer à la suite...

{{% box type="warning" title="À vérifier"%}}

Avant de passer à la partie suivante, veille à vérifier ces différents points :
* toujours pouvoir bouger le panier dans les deux directions ;
* avoir toujours au moins une pomme qui tombe sur ton écran ;
* pouvoir attraper la pomme avec le panier ;
* avoir un score qui compte le nombre de pommes attrapées.

{{% /box %}}

Si tu rencontres le moindre problème avec ton jeu, n'hésite pas à appeler un organisateur pour lui demander des conseils.
