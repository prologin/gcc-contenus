# Vérifier l'existence d'un élément dans une liste

Après avoir ajouté et supprimé des éléments dans une liste, il faut pouvoir
vérifier si un élément **existe** dans une liste. Cette vérification peut se
faire avec le mot-clé `in` (*dans* 🇫🇷) dans une **condition**.

<details>
<summary>Clique ici si tu ne te souviens plus des conditions !</summary>

On utilise l'instruction `if` (*si* 🇫🇷) que l'on fait suivre d'une condition
que l'on veut tester. Elle permet d'exécuter un morceau de code  **uniquement
lorsque la condition est vraie**.

Pour vérifier une certaine condition, on va utiliser la syntaxe `if condition:`,
suivi d'un bloc de code **indenté**. Le bloc de code en question sera exécuté
seulement **si** `condition` est vraie, c'est-à-dire, seulement **si**
`condition` renvoie le booléen `True`.

```codepython
# Exécute l'affichage si 1 est égal à 1
# et c'est le cas ici !
if 1 == 1:
    print("Hello World!")
```

Un `if` peut être accompagné d'un `else` (*sinon* 🇫🇷) qui exécute un bloc de
code uniquement si la condition du `if` est fausse.

Enfin, il y a aussi le `elif` qui est la contraction du *else* et du *if*. Il
n'est exécuté que si sa condition est vraie et que les conditions précédentes
sont fausses.

{{< codestep steps=5 lang="py" run=true >}}

{{< codestep-block desc="Définit une variable `age`" >}}
age = 16
 
{{< /codestep-block >}}

{{< codestep-block desc="Vérifie que l'âge est inférieur ou égal à 11">}}
if age <= 11:
    print("École primaire")
{{< /codestep-block >}}

{{< codestep-block desc="Vérifie que l'âge est inférieur ou égal à 16 et supérieur à 11">}}
elif age <= 16:
    print("Collège")
{{< /codestep-block >}}

{{< codestep-block desc="Vérifie que l'âge est inférieur ou égal à 18 et supérieur à 16">}}
elif age <= 18:
    print("Lycée")
{{< /codestep-block >}}

{{< codestep-block desc="Exécuté dans tous les autres cas, où l'âge est supérieur à 18">}}
else:
    print("Études supérieures")
{{< /codestep-block >}}

{{< /codestep >}}

</details>

Prenons un exemple pour bien comprendre l'utilisation du mot-clé `in` dans une
condition.

```codepython
# Crée une liste `ma_liste`
ma_liste = ['a', 'b', 'c']

# Affiche "Youhou !" si 'b' est dans la
# liste `ma_liste`
if 'b' in ma_liste:
    print("Youhou !")
```

Le mot-clé `in` est très utile lorsque la liste donnée devient très longue ou
si des ajouts et des suppressions sont faites.

# Concaténer deux listes

En Python, il est possible de **concaténer** deux listes, c'est-à-dire de
**créer une seule liste** en ajoutant tous les éléments de la deuxième liste à
la première. On utilise alors l'opérateur `+` pour effectuer cette action.

```codepython
# Crée une liste `liste1`
liste1 = ['a', 'b', 'c']

# Crée une liste `liste2`
liste2 = ['d', 'e', 'f']

# Crée une liste `liste3`
# en concaténant les deux dernières listes
liste3 = liste1 + liste2

# Affiche `liste3`
print(liste3)
```

{{% box type="exercise" title="Mission 11 : Dernières vérifications !" %}}

Julie voudrait vérifier une dernière fois qu'elle n'ait besoin de rien acheter à
l'aéroport en arrivant !

Pour cela, utilise les listes données qui correspondent aux affaires de Julie.
Elle voudrait vérifier qu'elle a les objets suivants :

- bouteille d'eau ;
- éventail ;
- lunettes de soleil ;
- casquette ;
- tongs.

Si un élément n'est pas dans cette liste, affiche *"Il manque {element} !"*, en
remplaçant `{element}` par l'élément en question. S'il existe dans les affaires
de Julie, affiche, *"{element} est présent !"* Pour cela, utilise l'opérateur
`+` sur les listes pour récupérer l'ensemble des affaires de Julie.

```python
valise = ["t-shirt", "pantalon", "pull", "chaussette"]
sac = ["passeport", "ordinateur", "micro:bit", "souris", "bouteille d'eau", "crème solaire", "lunettes de soleil", "gâteaux"]
```

{{% /box %}}

# Concaténer plusieurs fois la même liste

En réutilisant le même principe de concaténation, il est possible de **répéter
cette opération** sur une même liste. On peut alors obtenir une grande liste
assez facilement, en **répétant** une même liste, un **certain nombre de fois**.

```codepython
# Crée une liste `ma_liste`
ma_liste = ['a', 'b', 'c']

# Crée une listre `liste_repetee`
# qui est la liste repétée 10 fois
liste_repetee = ma_liste * 10

# Affifche `liste_repetee`
print(liste_repetee)
```
