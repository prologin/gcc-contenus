# Parcourir une liste à l'aide d'une boucle

Il est fréquent de vouloir **accéder à tous les éléments** d'une liste un par
un. On dit alors qu'on **parcourt** la liste. Ce parcours se fait au travers
d'une boucle `for`.

Il existe deux manières de parcourir une liste, mais elles reviennent à la même
chose.

## Parcourir une liste à l'aide des indices

Pour rappel, il est possible d'**accéder à un élément** à partir de son
**indice** (sa position) dans la liste. Pour accéder à chaque élément, il faut
ainsi avoir un nombre allant de *0* à la *longueur de la liste - 1*, ce qui
correspond aux valeurs possibles comme indice.

```codepython
# Crée une liste `ma_liste`
ma_liste = ['a', 'b', 'c']

# Calcule la longueur de la liste
longueur = len(ma_liste)

# Affiche l'indice de chaque élément
# dans la liste `ma_liste`
for i in range(longueur):
    print(ma_liste[i], "est à l'indice", i)
```

Si tu n'as pas compris cette méthode, n'hésite pas à appeler un organisateur ou
à revoir la partie des boucles `for` du sujet
[Introduction à Python](https://tp.girlscancode.fr/python/intro_python/).

{{% box type="exercise" title="Mission 9 : Trier les bonbons !" %}}

En se promenant dans les magasins de l'aéroport, tu remarques qu'un vendeur
a besoin d'aide pour trier ses articles. Il voudrait séparer tous les paquets de
*Prolobonbons* d'un grand carton.

Il voudrait que tu l'aides à retrouver tous les indices (positions) dans la liste
`carton_bonbons` où l'on trouve l'élément `"Prolobonbons"` et à mettre ces indices dans une
nouvelle liste ! À la fin, tu pourras afficher cette nouvelle liste.

```python
carton_bonbons = ["Schtroumpf", "Tagada", "Pompote", "Smarties", "Smarties", "Pompote", "Kinder", "Schtroumpf", "Kinder", "Prolobonbons", "Tagada", "Pompote", "Prolobonbons", "Pompote", "Schtroumpf", "Crocodiles", "Smarties", "Prolobonbons", "Prolobonbons", "Prolobonbons", "Smarties", "Schtroumpf", "Prolobonbons", "Crocodiles", "Tagada", "Pompote", "Crocodiles", "Smarties", "Kinder", "Prolobonbons", "Pompote", "Smarties", "Pompote", "Kinder", "Crocodiles", "Tagada", "Pompote", "Kinder", "Pompote", "Kinder", "Kinder", "Kinder", "Kinder", "Kinder", "Schtroumpf", "Kinder", "Schtroumpf", "Pompote", "Prolobonbons", "Pompote"]
```

{{% /box %}}

## Parcourir une liste à l'aide d'une boucle spécifique

Il existe une autre méthode pour **parcourir** chaque élément d'une liste, sans
passer par les indices. Il s'agit d'utiliser une boucle `for` *pour chaque
élément dans la liste donnée*. On utilise alors la syntaxe suivante :

```codepython
# Crée une liste `ma_liste`
ma_liste = ['a', 'b', 'c']

# Utilise une boucle `for`
# Pour chaque élément de la liste `ma_liste`
for element in ma_liste:
    print("J'ai l'élément", element)
```

Dans l'exemple précédent, `element` correspond au nom de variable de l'élément
pris dans la liste `ma_liste`. Il est possible de changer le nom de la variable
par n'importe quel nom.

{{% box type="warning" title="Variable existante que dans la boucle" %}}

Attention, la variable après le mot-clé `for` (`element` dans l'exemple
précédent) est utilisable **uniquement dans** le bloc de code correspondant à la
boucle. Il ne peut pas être utilisé après la boucle (dans le bloc de code qui
n'est pas indenté).

{{% /box %}}

Si jamais tu n'as pas compris cette partie, n'hésite pas à appeler un
organisateur. C'est une notion importante qui te sera souvent utile.

{{% box type="exercise" title="Mission 10 : Embarquement !" %}}

C'est l'heure de l'embarquement et il faut appeler les passagers un à un afin
qu'ils puissent entrer dans l'avion ! La liste des passagers est donnée par la
liste `passagers`.

Il faut alors appeler les passagers en affichant : "Passager {nom} est appelé !"
en remplaçant `{nom}` par le nom du passager ou de la passagère.

```python
passagers = ["Ada Lovelace", "Grace Hopper", "Jean Bartik", "Katherine Johnson", "Margaret Hamilton", "Radia Perlman", "Carol Shaw", "Suzane Kare", "Hedy Lamarr", "Katie Bouman"]
```

{{% /box %}}
