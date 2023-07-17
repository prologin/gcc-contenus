# f-string

Les f-string permettent d'insérer des expressions, des variables, dans des chaînes de caractères.

Pour utiliser les f-string, il suffit de mettre un `f` devant la chaîne de caractères.
Ensuite, pour insérer la valeur d'une variable dans la chaîne, il suffit de la mettre entre accolades.

```codepython
bananes = 10
print(f"J'ai {bananes} bananes. Bon app'")
```

Les f-string prennent également en compte les fonctions, ce qui signifie que les appels de fonctions qui se trouvent dans la chaîne de caractères sont exécutées et le résultat est affiché.

```codepython
def donne42():
    return 42

print(f"La fonction donne {donne42()}")
```

## Formattage

Les f-string implémentent également une manière de mettre en forme les nombres.

```codepython
variable = 3.14159265359
print(f"{variable:.2f}")  # avec 2 décimales
print(f"{variable:.3f}")  # avec 3 décimales

price = 50
print(f"Prix: {price:5d}")  # avec des espaces

print(f'Nombre\t\tCarré\t\tCube')
for x in range(1, 11):
    print(f'{x:2d}\t\t{x*x:4d}\t\t{x*x*x:4d}')
```


{{% box type="exercise" title="Exercice 4" %}}

C'est la première fois que les parents nous font assez confiance pour faire les courses toutes seules.

Pour y aller, nous avons besoin d'une liste de courses, de sacs pour ranger les courses et d'argent pour payer à la caisse.

Les parents nous donne 30€.

Après une étude rapide de la liste, on sait qu'il nous faut environ :
- 2€ pour les oeufs,
- 9€ pour la viande,
- 5€ pour les fruits,
- 4€ pour le chocolat,
- 6€ pour le lait.

Pour nous récompenser, les parents nous autorise à nous acheter des bonbons en même temps avec l'argent qui reste.

Affiche la phrase "Trop bien ! On peut s'acheter ...€ de bonbons !", en remplaçant les `...` par le résultat du calcul.

{{% /box %}}