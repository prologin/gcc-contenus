# Partie I : Le panier

*Attention, pense à bien importer la bibliothèque **microbit** avant de commencer.*

```python
from microbit import *
```

Dans cette partie, nous allons simplement nous occuper du panier. Le panier fait 1 pixel de large.
Comme dit précédemment, le panier restera sur la 4e ligne, donc pas besoin de s'occuper de l'axe Y.
Cependant il n'aura pas toujours la même position sur l'axe X (horizontal).

Commençons donc par créer une variable `pos_panier` qui représentera sa position sur cet axe X.
Au début de la partie, le panier sera au milieu de l'écran, soit en position 2 comme sur l'image ci-dessous.

{{<figure src="resources/microbit_panier.png" width=500 caption="Le panier sur un microbit">}}

Maintenant que cette variable est créée, nous allons vouloir déplacer notre panier.
Pour cela, tant que le joueur n'a pas perdu, il pourra bouger le panier. Tu peux utiliser une variable booléenne.

{{<figure src="resources/microbit_panier_move.png" width=500 caption="Le panier qui bouge sur un microbit">}}

{{% box type="info" title="Rappel : les variables booléennes" %}}

Une variable booléenne représente deux valeurs : `True` ou `False`.  
Les valeurs `True` et `False` représentent respectivement les états `Vrai` et `Faux`.
Nous sommes à l'état `Vrai` lorsque l'affirmation que l'on teste est vérifiée.

```codepython
# On teste l'inégalité 1 < 2
print(1 < 2)
```
Ce test nous renvoie le mot clé `True` donc l'affirmation *1 < 2* est vraie

Une variable booléenne peut stocker le résultat de ce test ou simplement être initialisée à `True` ou `False`.

```codepython
# On initialise notre variable avec le résultat de notre test
v_bool = 1 < 2
print(v_bool)

# On définit maintenant notre variable avec la valeur `False`
v_bool = False
print(v_bool)
```

{{% /box %}}

{{% box type="warning" title="Attention" %}}

Il y a une différence entre `=` et `==` en Python.
Le `=` est utilisé pour de l'assignation de valeur, alors que le `==` est utilisé pour de la comparaison.

```codepython
# Assignation, v prend la valeur de 1
v = 1
print(v)

# Comparaison, v_bool prend la valeur de la comparaison 1 == 1
v_bool = 1 == 1
print(v_bool)
```

{{% /box %}}

{{% box type="info" title="Rappel : les boucles" %}}

Une variable booléenne peut donc être utilisée dans une condition (`if`) ou comme condition d'arrêt d'une boucle (`while`).
Pour une utilisation dans une boucle, il faudra penser à actualiser la valeur de notre variable à l'intérieur de notre boucle.

```codepython
# On définit notre variable booléenne à `True` à l'état initial
v_bool = True

if v_bool:
    # Si la variable est à vrai alors le programme évalue
    # les expressions à l'intérieur de la condition
    print("Condition réalisée")
```

```codepython
# On initialise la variable `en_cours` à `True`
en_cours = True
x = 0

while en_cours:
    # Tant que la variable reste à `True`, on évalue les
    # expressions dans la boucle

     # Si x est égale à 5
    if x == 5:
        # Alors on met la variable `en_cours` à `False`
        en_cours = False
        # `en_cours` étant à `False` on sort de la boucle

     # Sinon on ajoute 1 à x
    else:
          x = x + 1

print(x)
# Tu peux constater qu'à la fin de cette boucle
# la variable x a une nouvelle valeur : 5
```

{{% /box %}}

*Bien évidemment si tu as une quelconque question, ou que tu veux qu'on te réexplique quelque chose, n'hésite pas à demander à un organisateur de l'aide.*

Pour déplacer le panier, nous allons utiliser les boutons du `micro:bit`. Le bouton A permettra de déplacer le panier à gauche, tandis que le bouton B déplacera le panier à droite. Il faut alors calculer sa nouvelle position et ensuite redessiner le panier à l'écran. Pour cela, tu peux utiliser la variable `pos_panier` pour déterminer la nouvelle position du panier en fonction des boutons pressés.

{{% box type="info" title="Rappel : les boutons sur le micro:bit" %}}

Pour utiliser les boutons, tu peux utiliser les fonctions suivantes :

```py
button_a.is_pressed()   # Ces fonctions renvoient True ou False si le
button_b.is_pressed()   # bouton est appuyé quand la ligne est exécutée
                        # par le micro:bit

button_a.was_pressed()  # Ces fonctions renvoient True ou False si le bouton
button_b.was_pressed()  # a été appuyé depuis la dernière fois qu'elles ont
                        # été appelées

button_a.get_presses()  # Ces fonctions renvoient le nombre d'appuis effectués
button_b.get_presses()  # sur le bouton depuis la dernière fois qu'elles ont
                        # été appelées
```

{{% /box %}}

Cependant, il ne faut pas oublier de rajouter un délai entre chaque tour de boucle pour éviter que les pixels clignotent. Pour cela tu peux utiliser la fonction `sleep(150)`.

{{% box type="warning" title="Attention : ne pas dépasser les limites" %}}

Il faut faire en sorte que le panier ne sorte pas de l'écran, sinon cela causera une erreur.  
Pour cela, n'oublie pas de vérifier, à l'aide de conditions, les cas suivants :
* si le panier dépasse vers la droite, que faire ?
* si le panier dépasse vers la gauche, que faire ?

{{% /box %}}

Avant de passer à la partie suivante, assure-toi d'avoir un panier pouvant bouger à droite et à gauche sur toute la ligne grâce aux boutons.