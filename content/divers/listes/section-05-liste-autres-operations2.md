## Autres opérations sur les listes : concaténer des listes

### Concaténer deux listes avec l'opérateur `+`

En Python, on peut aussi **concaténer** deux listes, c'est-à-dire les mettre l'une à la suite de l'autre pour n'en créer qu'une.

Pour ce faire, on utilise l'opérateur `+`.

Par exemple, on crée deux listes `liste1` et `liste2`, on les fusionne dans une troisième liste `liste3`, puis on affiche `liste3` :

```codepython
liste1 = [10, 20, 30]
liste2 = [4, 5, 6, 7, 8]
liste3 = liste1 + liste2
print(liste3)
```

Ce code affiche `[10, 20, 30, 4, 5, 6, 7, 8]`.

Il est possible d'utiliser `+` sur plus de 2 listes, par exemple :
```codepython
liste1 = [10, 20, 30]
liste2 = [4]
liste3 = [150, 200, 300]
liste4 = []
print(liste1 + liste2 + liste3 + liste4)
```

Cet opérateur nous permet d'être plus rapide lors d'opérations spécifiques, comme le test d'appartenance d'un élément sur plusieurs listes.

{{% box type="exercise" title="Exercice 12 : Trouver des craies" %}}

Un professeur, un peu embêté, ne trouve pas de craie pour utiliser le tableau de la classe. Il demande à ses élèves de regarder dans leurs trousses et leurs sacs s'ils n'en possèdent pas, avant d'aller dans la salle des professeurs, de l'autre côté de l'établissement.

Aide le professeur en regardant dans les trousses et sacs des 5 élèves de la classe, en utilisant l'opérateur `+`.

```python
sac_eleve1 = ["cahier", "trousse", "livre"]
trousse_eleve1 = ["feutre", "crayon", "gomme", "stylo rouge"]

sac_eleve2 = ["cahier", "trousse", "livre", "telephone"]
trousse_eleve2 = ["effaceur", "crayon", "stabilo", "stylo bleu"]

sac_eleve3 = ["cahier", "trousse"]
trousse_eleve3 = ["craie", "crayon", "gomme", "stylo noir"]

sac_eleve4 = ["cahier", "trousse", "livre"]
trousse_eleve4 = ["crayon", "stylo bleu"]

sac_eleve5 = ["cahier"]
trousse_eleve5 = []
```

{{% /box %}}


### Concaténer plusieurs fois la même liste avec l'opérateur `*`

Imaginons maintenant qu'on veuille créer une liste remplie de 42, disons 100 fois le nombre 42 :

```codepython
L = [42] * 100
print(L)
```

C'est un opérateur rapide, qui est très utile lorsqu'on doit gérer une liste de taille donnée au départ.

