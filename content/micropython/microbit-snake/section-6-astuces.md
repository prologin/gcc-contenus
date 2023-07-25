# Astuces (utiles pour certaines parties du projet)

On peut vérifier qu'une valeur est présente dans une liste de la manière suivante :

```codepython
snake = [(1, 0)]
print((0, 1) in snake) # C'est faux
print((1, 0) in snake) # C'est vrai
```

Pour choisir aléatoirement un nombre entier, tu peux utiliser la fonction `randint` (tu peux appuyer plusieurs fois sur `Run` du sujet pour constater que le nombre est bien aléatoire) :

```codepython
# randint(a, b) renvoie un nombre aléatoire choisi entre a et b
# Exécute plusieurs fois ce code, il affichera des chiffres différents
from random import randint
print(randint(1, 6))
```

---
# En savoir plus

Dans le code fourni, la ligne suivante permet de vérifier si le
serpent se mord la queue :

```py
if serpent[0] in serpent[1:]:
```

Lorsqu'on écrit `ma_liste[x:]`, on crée la sous-liste de `ma_liste` qui commence
à l'index `x`. Tu peux vérifier ce fonctionnement avec le code suivant :

```codepython
ma_liste = ["Je", "suis", "Joseph", "Marchand"]

print(ma_liste[1:])

print(ma_liste[3:])
```

Tu peux aussi le faire dans l'autre sens d'ailleurs :

```codepython
ma_liste = ["Je", "suis", "Joseph", "Marchand"]

print(ma_liste[:1])

print(ma_liste[:3])
```

Si tu as d'autres questions sur la manière de comment fonctionne le *slicing*,
n'hésite pas à demander à un organisateur.