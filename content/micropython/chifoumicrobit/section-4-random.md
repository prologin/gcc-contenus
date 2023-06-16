## Le choix de l'ordinateur

Le choix de l'ordinateur doit se faire de manière aléatoire. La variable
`choix_adversaire` doit correspondre à un indice dans la liste `possibilites`.
Sachant que les éléments d'une liste en Python sont numérotés de 0 à la longueur
de la liste moins 1, il te faudra générer un nombre dans l'intervalle en question.

Pour générer un nombre aléatoire, tu peux utiliser la fonction `randint` du
module `random`. Pour cela, tu peux l'utiliser comme dans l'exemple suivant :

```codepython
from random import randint

# Génère un nombre aléatoire entre 0 et 4
# Les valeurs possibles sont 0, 1, 2, 3 et 4
n = randint(0, 4)

print(n)
```
