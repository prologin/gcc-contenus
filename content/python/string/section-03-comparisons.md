# Comparer des caractères

## La table ASCII

Prenons un instant pour nous concentrer sur les **caractères**. Les ordinateurs
sont à l'origine des machines ne connaissant que le langage binaire fait de 0 et
de 1. On peut alors créer n'importe quel nombre en utilisant ce langage.

Afin de pouvoir écrire quelque chose sur ces machines, les programmeuses et les
programmeurs ont mis en place un tableau pour **associer un nombre à chaque
caractère**, on l'appelle la *Table ASCII*.

{{< figure src="./resources/images/ascii.png" caption="Table ASCII" >}}

Dans le tableau donné, les colonnes *Decimal* et *Char* sont celles qui vont le
plus nous intéressées.

{{% box type="info" title="Récupérer le numéro associé à un caractère dans la table ASCII" %}}

À partir de la table ASCII, on peut récupérer le **nombre associé** à un
caractère en utilisant la fonction `ord` comme dans cet exemple :

```codepython
# Crée un caractère `caractere`
caractere = '?'

# Récupère son numéro dans la table ASCII
numero = ord(caractere)

# Affiche `numero`
print(numero)
```

On peut également récupérer un **caractère** à partir du nombre associé en
utilisant la fonction `chr`.

```codepython
# Crée un nombre associé à un caractère
# dans la table ASCII
numero = 64

# Récupère le caractère correspondant
caractere = chr(numero)

# Affiche `caractere`
print(caractere)
```

{{% /box %}}

## Les opérateurs

À partir de cette particularité informatique, il est alors possible de
**comparer les caractères** entre eux en utilisant certains **opérateurs**.

Ces opérateurs sont **les mêmes** que l'on utilise pour les nombres et que tu as
pu voir dans le sujet d'[Introduction à Python](https://tp.girlscancode.fr/python/intro_python/).

| Nom | Opérateur | Exemple | Résultat |
|:--:|:--:|:--:|--:|
| Égalité | `==` | 'a' == 'b' | False |
| Différence | `!=` | 'a' != 'b' | True |
| Inférieur strict | `<` | 'a' < 'b' | True |
| Inférieur ou égal | `<=` | 'a' <= 'b' | True |
| Supérieur strict | `>` | 'a' > 'b' | False |
| Supérieur ou égal | `>=` | 'a' >= 'b' | False |

```codepython
# Crée deux caractères
caractere1 = 'A'
caractere2 = 'B'

# Vérifie et affiche si les deux
# caractères sont égaux ou non
print(caractere1 == caractere2)
```

N'hésite pas à **modifier** les caractères et l'opérateur pour voir les
différentes possibilités !

## Le cas des chaînes de caractères

Sur les chaînes de caractères, les opérateurs précédents fonctionnent également.
En *Python*, la comparaison se fait lettre par lettre, comme dans l'exemple
ci-dessous. N'hésite pas à parcourir toutes les images en cliquant sur les
flèches !

{{< gallery steps=3 >}}

{{< gallery-img src="./resources/images/compare-1.png" desc="Les deux chaînes de caractères commencent par la lettre 'm'" >}}
{{< gallery-img src="./resources/images/compare-2.png" desc="Les deux chaînes de caractères continuent par la lettre 'a'" >}}
{{< gallery-img src="./resources/images/compare-3.png" desc="Les deux chaînes de caractères sont différentes à partir de la troisième lettre" >}}

{{< /gallery >}}

En utilisant la *table ASCII*, on peut alors vérifier l'**ordre
lexicographique** des mots, comme dans un dictionnaire :

```codepython
# Crée deux mots
mot1 = "magique"
mot2 = "maison"

# Compare les deux mots avec l'ordre lexicographique
# Le caractère 'g' se trouve avant le caractère 'i'
# Donc, cela est vrai
print(mot1 < mot2)
```

{{% box type="exercise" title="Mission 3 : La liste de mots" %}}

Dans la lettre mystérieuse, vous découvrez deux listes de mots. En utilisant la
phrase que vous avez déchiffrée précédemment, vous avez compris qu'il fallait
comparer les éléments de la liste.

En utilisant tes nouvelles connaissances, compare les mots des listes un à un
afin de découvrir ce qui se cache derrière ce mystère ! Pour cela, tu peux
utiliser l'opérateur de comparaison *supérieur strict*.

```python
liste1 = ["gdklnnfqlp", "fapeakodng", "bniujfkg", "fidoxmropz", "hgifudkml", "jgiofdkngp"]
liste2 = ["cndiogfnle", "fapeakzdng", "bnigjkfg", "mjiogndfea", "hgifuckml", "jgiofdkngp"]
```

Crée une liste de booléens `code` qui correspond à la comparaison entre les deux
listes de chaînes de caractères. L'élément de la liste `code` à l'indice `i`
correspond au booléen (`True` ou `False`) résultant de la comparaison entre les
éléments des listes `liste1` et `liste2` à l'indice `i`.

Cette liste sera utilisée par la suite pour découvrir un code caché !

{{% /box %}}
