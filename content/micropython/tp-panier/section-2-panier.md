# Partie I : Le panier

Dans cette partie, tu vas commencer par t'occuper du panier.

{{% box type="exercise" title="Étape 0 : Mise en place" %}}

Commence par créer un nouveau fichier pour coder le projet.

Comme à chaque fois, pense à importer toutes les fonctions de la bibliothèque `microbit` en écrivant :

```python
from microbit import *
```

{{% /box %}}


## Position initiale du panier

Le panier est affiché sur un unique pixel. Comme dit précédemment, il reste sur la ligne du bas, donc pas besoin de s'occuper de l'axe Y.
En revanche, le panier n'a pas toujours la même position sur l'axe X (horizontal).

{{% box type="exercise" title="Étape 1 : Position initiale du panier" %}}

Commence par créer une variable `pos_panier` qui représente la position du panier sur l'axe X.
Au début de la partie, le panier est **au milieu** de la ligne du bas, comme sur l'image ci-dessous.

{{% /box %}}

{{<figure src="resources/microbit_panier.png" width=500 caption="Position initiale du panier sur le micro:bit">}}


## Quelques rappels avant de continuer !

{{% box type="info" title="Rappel : Les variables booléennes" %}}

Une variable booléenne représente deux valeurs : `True` (*Vrai* 🇫🇷) ou `False` (*Faux* 🇫🇷).  
Une affirmation vérifiée est vraie (`True`), autrement elle est fausse (`False`).

```codepython
# On teste l'inégalité 1 < 2
print(1 < 2)
```

Ce code affiche le mot clé `True`, donc l'affirmation `1 < 2` est vraie.

Une variable booléenne permet de stocker le résultat d'un test.

```codepython
# Une variable avec le résultat du test 1 < 2.
test = 1 < 2
print("Ce test est :", test)
```

Tu peux également assigner directement les valeurs `True` ou `False`.

```codepython
# Une variable avec la valeur `False`.
test = False
print(test)
```

{{% /box %}}

{{% box type="warning" title="Différence entre `=` et `==`" %}}

En Python, `=` et `==` fonctionnent différemment.
Le `=` est utilisé pour assigner une valeur, tandis que le `==` est utilisé pour une comparaison.

```codepython
# Assignation : `v` prend la valeur 1.
v = 1
print(v)

# Comparaison : `v` prend la valeur de la comparaison 1 == 1.
v = 1 == 1
print(v)
```

{{% /box %}}

{{% box type="info" title="Rappel : Les boucles" %}}

Les variables booléennes sont utilisées dans les conditions (`if`) ou comme condition d'arrêt dans les boucles (`while`).
Pour l'utilisation dans les boucles, il faut penser à actualiser la valeur de la variable à l'intérieur de la boucle, de sorte à ce qu'au bout d'un moment, la condition devienne **fausse** et que la boucle **s'arrête**.

```codepython
condition = True

if condition:
    print("Condition réalisée")
```

```codepython
en_cours = True
x = 0

while en_cours:
    if x == 5:
        en_cours = False
        # Au début du  prochain tour, la condition de la
        # boucle sera fausse alors on sortira du `while`.
    else:
          x = x + 1

print(x)
# Tu peux constater qu'à la fin de la boucle, la variable `x` vaut 5.
```

{{% /box %}}

*Bien évidemment, si tu as une quelconque question, ou que tu veux qu'on te réexplique quelque chose, n'hésite pas à demander de l'aide à un organisateur.*


## Déplacer le panier

Maintenant que la première variable `pos_panier` a été créée, tu vas pouvoir déplacer le panier.
Pour cela, tant que le joueur n'a pas perdu, il peut bouger le panier horizontalement à l'aide des boutons du micro:bit :
* Bouton **A** pour aller vers la **gauche**.
* Bouton **B** pour aller vers la **droite**.

{{<figure src="resources/microbit_panier_move.png" width=500 caption="Les mouvements possibles du panier sur le micro:bit">}}


{{% box type="info" title="Rappel : les trois super fonctions des boutons 😎" %}}

* `get_presses` : **nombre d'appuis** sur un bouton **depuis la dernière fois**.
* `is_pressed` : est-ce que le bouton **est en train d'être appuyé** ?
* `was_pressed` : est-ce que le bouton **a été appuyé** ?

{{% /box %}}


{{% box type="exercise" title="Étape 2 : Déplacer le panier" %}}

Code les déplacements du panier. En fonction du bouton qui est appuyé, calcule la nouvelle position du panier en mettant à jour la valeur de `pos_panier`. Ensuite, redessine-le à l'écran.

De plus, rajoute un délai entre chaque tour de boucle pour éviter que les pixels ne clignotent. Pour cela, tu peux ajouter `sleep(150)` à la fin de ta boucle.

{{% /box %}}


{{% box type="warning" title="Tu n'as pas le droit de me fuir de la sorte" %}}

Il faut empêcher le panier de sortir de l'écran, sinon cela cause une erreur !

Pour cela, n'oublie pas de vérifier les cas suivants à l'aide de conditions :
* Si le panier dépasse vers la droite, que faire ?
* Si le panier dépasse vers la gauche, que faire ?

{{% /box %}}

Avant de passer à la partie suivante, assure-toi d'avoir un panier qui peut bouger à gauche et à droite sur toute la ligne grâce aux boutons.
