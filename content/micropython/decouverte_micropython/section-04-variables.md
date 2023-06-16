# Les variables

Jusque là, on a vu comment afficher des images et du texte sur le 
`micro:bit`, mais ces informations sont statiques : une fois écrites dans le
code, elles ne peuvent plus être modifiées. Heureusement, un 
ordinateur peut enregistrer des informations pour les traiter, les modifier,
voire même en créer de nouvelles !

Pour cela, on utilise des variables : un morceau de la mémoire dans lequel on
va pouvoir enregistrer des valeurs. Quand on crée une variable, on commence par
lui donner un nom qui va être utilisé pour lire ou modifier la valeur qui lui
a été donnée.

## Utilisation des variables

Pour **créer une variable**, il suffit d'écrire `nom_de_la_variable =
valeur_initiale`, par exemple : `nombre_de_patates = 42`.

Ensuite on peut **réutiliser la valeur** stockée dans la variable en
l'identifiant par son nom. Par exemple, on peut créer une nouvelle variable
`prix` qui dépend de la variable qui a été créée précédemment : `prix =
nombre_de_patates + 50`. Dans ce cas, comme `nombre_de_patates` vaut
actuellement _42_, alors `prix = 42 + 50`. Donc à la fin de cette ligne, la
variable `prix` vaut _92_. 

Pour **modifier une variable** on utilise aussi le symbole d'égalité, par
exemple on peut augmenter de 1 la valeur stockée dans une variable :
`nombre_de_patates = nombre_de_patates + 1`.

Voici un exemple de programme complet que tu peux tester sur ton `micro:bit`
suivi d'un petit schéma qui représente ce qui est enregistré dans les variables
après chaque ligne du programme :

```python
from microbit import *

panier_pommes = 3
panier_poires = 5
panier_poires = 2 * panier_poires # panier_poires vaut 2 * 5 = 10
panier_fruits = panier_pommes + panier_poires # panier_fruits vaut 10 + 3 = 13

display.scroll(panier_fruits)
```


### Mini-Exercice
**But :** Crée une variable avec la valeur 42, puis ajoutes-y 2 et affiche-la 
sur l'écran.

## Types de variables

### Nombres

Comme leur nom l'indique, il s'agit tout simplement de nombres (positifs ou 
négatifs). On peut donc faire des opérations dessus avec les opérateurs 
classiques : `+`, `-`, `*` (multiplication), `/` (division), `//` (division
entière), `%` (modulo). 

Les deux dernières opérations ne te sont peut-être pas familières, et c'est
normal, mais elles ne sont pas compliquées. 

La division entière (`//`) et le modulo (`%`) correspondent respectivement au
quotient et au reste de la division euclidienne. 
Pour faire simple, la division entière renvoie la partie entière de la division
classique (la partie avant la virgule), tandis que le modulo correspond à ce
qu'il reste. 

Voici un petit mémo qui te permettra de comprendre ces opérations. 

```python
a = 2 * 5 + 3  # a vaut 13
b = a / 5      # b vaut 13 / 5  = 2.6
c = a // 5     # c vaut 13 // 5 = 2
d = a % 5      # d vaut 13 % 5  = 3
```

Si tu as des questions, n'hésite pas à demander de l'aide à un organisateur. 

Nous pouvons aussi combiner plusieurs opérations ensemble. Par exemple :

```python
e = (a - b) + c * d # (13 - 2.6) + 2 * 3 = 16.4, donc e = 16.4
```

#### Mini-Exercice
**But :** Joseph a envie de bananes. Le marchand lui propose de les acheter pour
2€ l'unité. Combien 10 bananes vont-elles lui coûter ? Affiche le résultat sur 
le `micro:bit`.

### Chaînes de caractères

On peut créer du texte en mettant son contenu entre guillemets (par exemple :
`mon_texte = "Bonjour tout le monde !"`). On peut aussi attacher des morceaux
de textes entre eux avec l'opérateur `+` (par exemple : `mon_texte = mon_texte +
"!!"`).

À noter qu'il est souvent très pratique de convertir un nombre en texte pour
ensuite l'incorporer dans une phrase, on peut faire ça avec la fonction
`str(nombre)`.

```python
from microbit import *

nombre_de_patates = 42
texte = "Il y a " + str(nombre_de_patates) + " patates !"
display.scroll(texte)  # Affiche "Il y a 42 patates !" sur l'écran
```

#### Mini-Exercice
**But :** Comme dans l'exercice précédent, Joseph a besoin de savoir combien 
vont lui coûter ses bananes. Mais le marchand a augmenté le prix et les bananes 
coûtent désormais 3€ chacune. Après avoir calculé, affiche `"Payer (le prix) 
pour 10 bananes ? Mais c'est beaucoup trop cher !"` en remplaçant `le prix` par 
sa valeur.


### Booléens

Enfin, les booléens servent à exprimer le vrai ou le faux. Il n'y a que deux
valeurs possibles pour ce type de variables : `True` (vrai) et `False` (faux).

Des valeurs booléennes sont renvoyées par les opérations de comparaison :  
- `==` pour l'égalité. `a == b` va renvoyer `True` si a et b sont égaux
- `!=` pour la différence. `a != b` va renvoyer `True` si a et b sont différents
- `<` et `>` pour les inégalités strictes. `a < b` va renvoyer `True` si a est
    strictement plus petit que b, et inversement pour `a > b`
- `<=` et `>=` pour les inégalités larges. `a <= b` va renvoyer `True` si a est
    plus petit ou égal à b, et inversement pour `a >= b`

Par exemple `1 < 2` vaut `True` mais `3 != 3` vaut
`False`.

Enfin, il est possible de manipuler les valeurs booléennes avec les opérateurs
`not`, `and` et `or` :

 - `not a` vaut l'inverse de `a`, donc `True` si a vaut `False`;
 - `a and b` vaut `True` si et seulement si `a` **et** `b` valent `True`;
 - `a or b` vaut `True` si et seulement si `a` **ou** `b` valent `True`.

#### Mini-Exercice
**But :** Après une discussion intense avec le marchand, Joseph n'est plus sûr
de ses calculs. Les bananes coûtant 3€, il pense que pour 7 bananes il en aura
pour 22€. Calcule le vrai prix et affiche si celui de Joseph est le bon.

