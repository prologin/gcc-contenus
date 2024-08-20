# Méthodes des chaînes de caractères

*Python* met à disposition plusieurs méthodes sur les chaînes de caractères, qui
les transforment et utilisent. Nous allons te montrer une liste non exhaustive
de ces méthodes qui te seront utiles.

## Tout en minuscule !

La méthode `lower` permet de **remplacer toutes les majuscules** dans une chaîne
par des minuscules.

```codepython
# Crée une chaîne de caractères `ma_chaine`
ma_chaine = "Hello World!"

# Transforme toutes les majuscules
# en minuscules
autre_chaine = ma_chaine.lower()

# Affiche `autre_chaine`
print(autre_chaine)
```

{{% box type="info" title="Qu'est-ce qu'il se passe avec les symboles et les caractères spéciaux ?" %}}

La méthode applique sa transformation **seulement sur les lettres majuscules**.
Elle ne touche pas les lettres déjà minuscules et tous les autres caractères.
Il y a donc aucun impact en utilisant la méthode `lower` sur une chaîne de
caractères avec uniquement des symboles ou des caractères spéciaux.

```codepython
# Crée une chaine `ma_chaine`
ma_chaine = "?!\n.:"

# Transforme toutes les majuscules
# en minuscules
autre_chaine = ma_chaine.lower()

# Affiche `autre_chaine`
print(autre_chaine)
```

{{% /box %}}

## Tout en majuscule !

Inversement à la méthode `lower`, la méthode `upper` permet de **remplacer
toutes les minuscules** dans une chaîne de caractères par des majuscules.

```codepython
# Crée une chaîne de caractères `ma_chaine`
ma_chaine = "Hello World!"

# Transforme toutes les minuscules
# en majuscules
autre_chaine = ma_chaine.upper()

# Affiche `autre_chaine`
print(autre_chaine)
```

## Séparer une chaîne à partir d'un caractère

À partir d'une chaîne de caractères, il est possible de créer une liste et de
**séparer la chaîne** en une liste de chaînes. Cette séparation se fait sur
un caractère ou une autre chaîne de caractères.

```codepython
# Crée une chaîne `plaque`
plaque = 'AB-123-CD'

# Sépare la chaîne en sous-chaînes
liste = plaque.split('-')

# Affiche `liste`
print(liste)
```

Il est également possible de demander à *Python* de séparer sur tous les
types d'**espaces** (espaces, retours à la ligne, tabulations, etc...).

```codepython
# Crée une chaîne `phrase`
phrase = "Bonjour tout le monde,\n Bienvenue au stage Girls Can Code!"

# Sépare la chaîne de caractères
# sur les espaces
liste = phrase.split()

# Affiche `liste`
print(liste)
```

## Concaténer les éléments d'une liste avec une chaîne

En utilisant la méthode `join`, tu peux **concaténer** les éléments d'une liste
en utilisant une chaîne de caractères. Cette dernière joindra chaque élément
de la liste pour **créer une chaîne de caractères**.

```codepython
# Crée une liste `liste`
liste = ["Julie", "Valerie", "Anne-Brisce", "Alice"]

# Crée une chaîne `separateur`
separateur = ", "

# Crée une chaîne de caractères
# en concaténant les éléments de `liste`
chaine = separateur.join(liste)

# Affiche `chaine`
print(chaine)
```

{{% box type="exercise" title="Mission 4 : Retrouver le caractère" %}}

À partir de la liste `code`, tu peux remplacer tous les booléens `True` par le
nombre `1` et tous les booléens `False` par le nombre `0`. On aura alors un
nombre écrit en binaire !

Crée alors une chaîne de caractères `nombre_binaire` correspondant au nombre
binaire en parcourant chaque élément de la liste et en ajoutant petit à petit
le caractère `'1'` ou le caractère `'0'`. Tu peux te servir de l'opérateur `+=`
que tu as pu voir dans l'[Introduction à Python](https://tp.girlscancode.fr/python/intro_python/).

Tu peux alors transformer le nombre en décimal pour récupérer un nombre. Ce
nombre correspond à un caractère dans la *table ASCII* ! Affiche le caractère
correspondant pour dévoiler le prochain secret !

</br>

<details>
<summary>Clique ici pour découvrir comment transformer un nombre binaire en décimal en Python</summary>

Pour transformer le nombre binaire en décimal, tu peux prendre exemple sur ce
code :

```codepython
# Crée une variable `nombre_binaire`
nombre_binaire = "101"

# Transforme le nombre binaire en décimal
nombre_decimal = int(nombre_binaire, 2)

# Affiche `nombre_decimal`
print(nombre_decimal)
```

</details>

{{% /box %}}

## Enlever les espaces en trop d'une chaîne

La méthode `strip` permet d'**effacer** tous les espaces qui se trouvent **au
début** et **à la fin** d'une chaîne de caractères.

```codepython
# Crée une chaîne `ma_chaine`
ma_chaine = "\t  \n    Hello World!  \t  \n  "

# Affiche `ma_chaine`
print(ma_chaine)

# Affiche un séparateur
print("---")

# Enlève les espaces en trop
# de `ma_chaine`
autre_chaine = ma_chaine.strip()

# Affiche `autre_chaine`
print(autre_chaine)
```

## Remplacer des caractères dans une chaîne

Afin de **remplacer des caractères** dans une chaîne de caractères, tu peux
utiliser la méthode `replace` comme dans cet exemple :

```codepython
# Crée une chaine `ma_chaine`
ma_chaine = "Heppo Worpd!"

# Remplace les 'p' par des 'l'
# dans `ma_chaine`
autre_chaine = ma_chaine.replace('p', 'l')

# Affiche `autre_chaine`
print(autre_chaine)
```

{{% box type="exercise" title="Mission 5 : Un message secret !" %}}

En trouvant le code, un texte caché apparaît sur la lettre, cependant, il n'a
pas l'air d'être très clair...

Cependant, Julie est habile et voit des indices cachés. Essaye d'enlever tous
les espaces inutiles de chaque chaîne de caractères de la liste et mets toutes
les lettres en minuscules. Par la suite, il te faudra remplacer les caractères
suivants :

</br>

| Caractère à remplacer | Caractère remplacé |
|:--:|:--:|
| `'4'` | `'a'` |
| `'3'` | `'e'` |
| `'1'` | `'i'` |
| `'0'` | `'o'` |
| `'5'` | `'s'` |
| `'y'` | `'u'` |

</br>

Enfin, rassemble toutes les chaînes sous une seule chaîne en les concaténant
avec un espace. Tu pourras alors afficher le texte déchiffré.

```python
texte_cache = ['    \t \n\tL41553Z    ', '    \n\n\nM01 ', 'v0Y5     \n\t', '\n\n\n\nGY1D3r\t    ', '            v3r5           ', '\n         c3     \t', '\t   p3R1pl3 ', '     V0Y5\n\n', '   \n\t    \nm3n4nt    \n       \t     \n', ' \n      \td4N5    \n    ', '     \t    \n  Yn  \t\n\n', '\t\t\t\tm0Nd3    \n   ', '     \nm4Gn1F1QY3', '!']
```

{{% /box %}}
