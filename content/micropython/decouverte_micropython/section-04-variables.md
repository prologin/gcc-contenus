# Les variables

La plupart du temps, nous avons besoin de stocker des informations dans notre
code. On parle alors de variables. Elles permettent de ranger des choses et de
pouvoir les ressortir quand on le souhaite. Ce sont des éléments qui associent
un nom à une valeur. C'est comme si on utilisait des boîtes pour ranger des
éléments !

{{<figure src="resources/images/variable.png" width=400 alt="Variable en Python" >}}

Pour déclarer une variable en Python, on procède de la sorte :

```python
# Importe les fonctions pour le micro:bit
from microbit import *

# Déclaration de `ma_variable`, qui stocke la valeur 42
ma_variable = 42

# Affiche la valeur de `ma_variable`
display.scroll(ma_variable)
```

Tu peux mettre à jour une variable grâce à sa valeur actuelle. Pour comprendre
un peu mieux, voici un petit exemple :

{{< codestep steps=5 lang="py" >}}

{{< codestep-block desc="Importe les fonctions pour utiliser le `micro:bit`" >}}
from microbit import *
 
{{< /codestep-block >}}

{{< codestep-block desc="La variable `nombre` stocke la valeur de 10" >}}
nombre = 10
{{< /codestep-block >}}

{{< codestep-block desc="Affiche la valeur de la variable `nombre`" >}}
display.scroll(nombre)
 
{{< /codestep-block >}}

{{< codestep-block desc="Rajoute 1 à la variable `nombre`" >}}
nombre = nombre + 1
{{< /codestep-block >}}

{{< codestep-block desc="Affiche la nouvelle valeur de `nombre`" >}}
display.scroll(nombre)
{{< /codestep-block >}}

{{< /codestep >}}

On peut caractériser les variables en différents types.

## Types de variables

### Nombres

Comme leur nom l'indique, il s'agit tout simplement de nombres (positifs ou 
négatifs). On peut donc faire des opérations dessus avec les opérateurs
suivants :

| Nom | Opérateur | Exemple | Résultat |
|:--:|:--:|:--:|--:|
| Addition | `+` | 7 + 2 | 9 |
| Soustraction | `-` | 7 - 2 | 5 |
| Multiplication | `*` | 7 * 2 | 14 |
| Division | `/` | 7 / 2 | 3.5 |
| Division entière | `//` | 7 // 2 | 3 |
| Modulo | `%` | 7 % 2 | 1 |

<br>

```codepython
# N'hésite pas à modifier le code pour tester
# les différentes opérations

a = 7
b = 2

# Affiche le calcul entre a et b
print(a * b)
```

{{% box type="info" title="C'est quoi `print()` ?" %}}

La fonction `print()` correspond à la fonction `display.scroll()` que tu as déjà
pu voir avec les `micro:bit`. On l'utilise ici pour afficher quelque chose dans
la console de notre site !

{{% /box %}}

<details>
<summary>Clique ici pour découvrir ce que sont une division entière et un modulo !</summary>

Les deux dernières opérations ne te sont peut-être pas familières, et c'est
normal, mais elles ne sont pas compliquées. Elles correspondent aux résultats
de la division euclidienne. Voici un petit exemple :

{{<figure src="resources/images/division.png" height=60% width=60% alt="Liste en Python">}}

- La division entière (`//`) correspond au <font color=#A459D1>
quotient </font>de la division, ici <font color=#A459D1>3</font>.
- Le modulo (`%`) correspondent au <font color=#F266AB>reste </font>de la
division, ici <font color=#F266AB>2</font>. 

Voici un petit mémo qui te permettra de comprendre ces opérations, avec le même
exemple.

```codepython
# Importe les fonctions pour le micro:bit
from microbit import *

a = 17
b = 5

print("Quotient = ")
print(a // b)

print("Reste = ")
print(a % b)
```

</details>

Si tu as des questions, n'hésite pas à demander de l'aide à un organisateur. 

{{% box type="exercise" title="Mini-mission 4 : Joseph au marché" %}}

Joseph a envie de manger des bananes. Le marchand lui propose de les acheter
pour 2€ l'unité. Combien 10 bananes vont-elles lui coûter ? Affiche le résultat
sur le `micro:bit`.

{{% /box %}}

### Chaînes de caractères

On peut créer du texte en mettant son contenu entre guillemets (par exemple :
`mon_texte = "Bonjour tout le monde !"`). On peut aussi attacher des morceaux de
texte entre eux avec le symbole `+` (par exemple : `mon_texte = "Bonjour" +
" !"`).

{{< codestep steps=2 lang="py" run=true >}}

{{< codestep-block desc="Concatène le texte \"Bonjour\" et le texte \" !\"." >}}
texte  = "Bonjour" + " !"
{{< /codestep-block >}}

{{< codestep-block desc="Affiche le texte concaténé." >}}
print(texte)
{{< /codestep-block >}}

{{< /codestep >}}

À noter qu'il est souvent très pratique de convertir un nombre en texte pour
ensuite l'incorporer dans une phrase, on peut faire ça avec la fonction
`str(nombre)`.

```python
# Importe les fonctions pour le micro:bit
from microbit import *

nombre_de_patates = 42
texte = "Il y a " + str(nombre_de_patates) + " patates !"
display.scroll(texte)
```

{{< gallery steps=4 >}}

{{< gallery-img src="./resources/images/patate_1.png" desc="Création Variable `nombre_de_patates`." >}}
{{< gallery-img src="./resources/images/patate_2.png" desc="Conversion de `nombre_de_patates` en texte." >}}
{{< gallery-img src="./resources/images/patate_3.png" desc="Concaténation des textes." >}}
{{< gallery-img src="./resources/images/patate_4.png" desc="Le résultat." >}}

{{< /gallery >}}

<br>

{{% box type="exercise" title="Mini-mission 5 : Augmentation de prix !" %}}

Comme dans l'exercice précédent, Joseph a besoin de savoir combien 
vont lui coûter ses bananes. Mais le marchand a augmenté le prix et les bananes 
coûtent désormais 3€ chacune.

Après avoir calculé le prix que devrait payer Joseph, affiche `"Payer (le prix)
euros pour 10 bananes ? Mais c'est beaucoup trop cher !"` en remplaçant
`le prix` par sa valeur.

{{% /box %}}

### Booléens

Enfin, les booléens servent à exprimer le vrai ou le faux. Il n'y a que deux
valeurs possibles pour ce type de variables : `True` (vrai) et `False` (faux).

Comme pour les nombres, il existe différentes opérations qui te renverront un
booléen :

| Nom | Opérateur | Exemple | Résultat |
|:--:|:--:|:--:|--:|
| Égalité | `==` | 2 == 3 | False |
| Différence | `!=` | 2 != 3 | True |
| Inférieur strict | `<` | 2 < 3 | True |
| Inférieur ou égal | `<=` | 2 <= 3 | True |
| Supérieur strict | `>` | 2 > 3 | False |
| Supérieur ou égal | `>=` | 2 >= 3 | False |

<br>

```python
# Importe les fonctions pour le micro:bit
from microbit import *

# Affiche si 42 est égal à 42
display.scroll(42 == 42)
```

Tu vas pouvoir également utiliser des opérateurs directement sur des valeurs
booléennes :

| Nom | Opérateur | Exemple | Résultat | Commentaire |
|:--:|:--:|:--:|--:|:--|
| Inverse | `not` | not True | False | Renvoie l'inverse de la valeur |
| Et | `and` | True and True | True | Vaut vrai si et seulement si les deux conditions sont vraies |
| Ou | `or` | True or False | True | Vaut vrai si et seulement si une des conditions est vraie |

<br>

{{% box type="exercise" title="Mini-mission 6 : Les calculs ne sont pas bons !" %}}

Après une discussion intense avec le marchand, Joseph n'est plus sûr
de ses calculs. Chaque banane coûtant 3€, il pense que pour 7 bananes il en aura
pour 22€. Calcule le vrai prix et affiche si celui de Joseph est le bon.

{{% /box %}}

