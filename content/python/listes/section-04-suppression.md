# Supprimer des éléments dans une liste

Maintenant que tu sais ajouter des éléments dans une liste, il est temps de
pouvoir les **supprimer** ! Il existe plusieurs manières pour supprimer des
éléments.

N'hésite surtout pas à appeler un organisateur si une partie est floue pour
toi !

## Supprimer à partir d'un indice

La méthode `pop` permet de supprimer un élément d'une liste **à partir d'un
indice**. Pour cela, il faut donner en paramètre l'indice de l'élément que tu
voudrais supprimer.

```codepython
# Crée une liste `ma_liste`
ma_liste = ['a', 'b', 'c']

# Supprime l'élément à l'indice 1
# de la liste `ma_liste`
ma_liste.pop(1)

# Affiche `ma_liste`
print(ma_liste)
```

{{% box type="warning" title="Attention aux indices !" %}}

Comme pour l'ajout dans une liste, il est très important de **ne pas dépasser
les limites** de la liste. L'argument donné à la méthode `pop` doit
correspondre à un élément de la liste.

{{% /box %}}

Il est également possible d'appeler la méthode `pop` **sans argument**. Cela te
permettra de supprimer le **dernier élément** de ta liste.

```codepython
# Crée une liste `ma_liste`
ma_liste = ['a', 'b', 'c']

# Supprime le dernier élément
# de la liste `ma_liste`
ma_liste.pop()

# Affiche `ma_liste`
print(ma_liste)
```

{{% box type="exercise" title="Mission 7 : Les problèmes commencent..." %}}

Enfin ! Les valises sont prêtes et c'est déjà l'heure de partir ! Cependant, en
arrivant à l'aéroport, on te dit que ta valise est trop lourde ! Pour ne pas
payer le supplément, tu vas devoir enlever des choses de ta valise.

En utilisant la liste `valise` fournie, enlève le parapluie, la crème solaire et
la casquette en utilisant la méthode `pop`. N'oublie pas d'afficher ta valise à
la fin pour vérifier que tout est aux normes !

```python
valise = ["casquette", "t-shirts", "pantalons", "doudou", "crème solaire", "tongs", "parapluie"]
```

{{% /box %}}

## Supprimer à partir d'une recherche

La deuxième méthode pour supprimer un élément d'une liste, consiste à **chercher
l'élément à enlever**. Cette recherche est faite automatiquement par
l'ordinateur, et tu as juste à **donner le nom de l'élément à supprimer** à la
méthode `remove`.

```codepython
# Crée une liste `ma_liste`
ma_liste = ['a', 'b', 'c']

# Supprime l'élément 'b'
# de la liste `ma_liste`
ma_liste.remove('b')

# Affiche `ma_liste`
print(ma_liste)
```

La méthode `remove` va supprimer le premier élément qui correspond à ce qui doit
être supprimé. Si un élément apparaît plusieurs fois dans une liste, seulement
le premier élément sera retiré.

```codepython
# Crée une liste `ma_liste`
ma_liste = ['b', 'a', 'b', 'b', 'c', 'b', 'd']

# Supprime le premier 'b'
# de la liste `ma_liste`
ma_liste.remove('b')

# Affiche `ma_liste`
print(ma_liste)
```

{{% box type="warning" title="Supprimer un élément qui n'existe pas" %}}

En utilisant la méthode `remove`, il faut faire attention à ce que l'élément à
supprimer **existe** dans la liste.

```codepython
# Crée une liste `ma_liste`
ma_liste = ['a', 'b', 'c']

# Essaye de supprimer l'élément 'd'
# qui n'existe pas dans la liste `ma_liste`
ma_liste.remove('d')
```
{{% /box %}}

{{% box type="exercise" title="Mission 8 : C'est l'heure du goûter !" %}}

Avant d'embarquer dans l'avion, vous décidez de manger quelques gâteaux en guise
de goûter. Pour cela, Julie avait déjà prévu un sac rempli de bonnes choses qui
correspond à la liste `sac_gouter`.

Vous avez dévoré le Kouign-amann et le pain au chocolat. Il faut alors les
supprimer de notre représentation en Python. Pour cela, tu peux t'aider de la
méthode `remove`. N'oublie pas d'afficher la liste à la fin !

```python
sac_gouter = ["kouign-amann", "croissant", "pain au chocolat", "tarte à la pomme"]
```

{{% /box %}}
