# Comment on crée une liste ?

Pour commencer, prenons un petit exemple d'une liste des trois premières
lettres de l'alphabet. Pour cela, créons-la dans la variable `ma_liste` et
affichons-la.

```codepython
# Crée une liste qui se nomme `ma_liste`
ma_liste = ['a', 'b', 'c']

# Affiche la liste `ma_liste`
print(ma_liste)
```

{{% box type="info" title="Longueur d'une liste" %}}

À partir du nom d'une liste, il est possible de calculer sa **longueur**,
c'est-à-dire le **nombre d'éléments** qu'il y a dans cette liste. Pour cela, on
utilise la fonction `len` comme dans cet exemple :

```codepython
# Crée une liste qui se nomme `ma_liste`
ma_liste = ['a', 'b', 'c']

# Calcule la longueur de la liste
# et la stocke dans la variable `longueur`
longueur = len(ma_liste)

# Affiche la longueur de la liste
print(longueur)
```

{{% /box %}}

Il est également possible de créer une liste avec plusieurs types d'éléments à
l'intérieur :

```codepython
# Crée une liste `ma_liste` avec plusieurs
# types d'éléments
ma_liste = ['!', "Bonjour", 42, True, False, 2.4]

# Affiche la liste `ma_liste`
print(ma_liste)
```

{{% box type="info" title="À quoi correspond une liste vide ?" %}}

Une **liste vide** est une liste avec **aucun élément à l'intérieur**, qui a une
**longueur égale à 0**. Pour représenter une liste vide, on utilise la même
syntaxe que pour créer une liste normale, sans mettre d'élément à l'intérieur.

```python
# Crée une liste vide
liste_vide = []
```

{{% /box %}}

# Accéder à un élément

Chaque élément d'une liste est **numéroté**, cela nous permettra par la suite de
pouvoir accéder à n'importe quel élément en fonction de sa position. On parle
alors d'**indice** ; ce dernier **commence à 0** et se termine par la
**longueur de la liste - 1**.

{{< figure src="./resources/images/index.png" caption="Représentation de la liste" >}}

On peut **accéder à un élément** d'une liste si on connaît son indice en
utilisant l'opérateur `[]`.

```codepython
# Crée une liste qui se nomme `alphabet`
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

# Accède à l'élément à l'indice 2
# (au 3e élément de la liste)
element = alphabet[2]

# Affiche l'élément
print(element)
```

{{% box type="warning" title="Attention à ne pas aller trop loin !" %}}

En accédant à un élément d'une liste à partir de son indice, il est possible
d'aller **trop loin** dans la liste. Python ne sera pas content et te renverra
une erreur, comme dans cet exemple :

```codepython
# Crée une liste qui se nomme `ma_liste`
ma_liste = ['a', 'b', 'c']

# Essaye d'accéder à l'élément à l'indice 3
element = ma_liste[3]
```

Pour éviter cela, vérifie toujours que ton indice est **compris entre 0 et la
longueur de la liste - 1** (dans l'exemple, entre 0 et 2).

{{% /box %}}

{{% box type="exercise" title="Mission 1 : On part pour l'aventure !" %}}

Julie t'informe que tu vas partir en voyage avec lui pour présenter les stages
Girls Can Code! aux quatre coins du monde ! Pour ne pas perdre les valises que
vous allez prendre, il voudrait écrire "GCC!" dessus.

Pour cela, sers-toi les listes `alphabet` et `caracteres` ci-dessous pour
afficher "GCC!". Tu devras alors utiliser les **indices** pour accéder aux
caractères.

```python
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
caracteres = ['!', '?', '.', ',', ':', ';']
```

</br>

<details>
<summary>Clique ici pour savoir comment afficher des caractères à la suite</summary>

Tu as pu voir sur l'[Introduction à Python](https://tp.girlscancode.fr/python/intro_python/)
qu'il était possible de donner **plusieurs paramètres** à la fonction `print`.
Cela permettait d'écrire plusieurs mots à la suite, séparés par un espace.

```codepython
print("Ceci", "est", "un", "Test.")
```

Il est possible de **changer le séparateur** et de mettre celui qu'on veut par
exemple grâce au paramètre spécial `sep` :

```codepython
print("Ceci", "est", "un", "Test.", sep="!")
```

Il est également possible de mettre une chaîne de caractères vide à ce paramètre
pour ne pas avoir de séparateur entre chaque mot !

```codepython
print("Bonjour", "Le", "Monde", sep="")
```

</details>

{{% /box %}}

Il est également possible de modifier des éléments dans une liste en utilisant
leur indice et le signe d'assignation `=`, comme dans cet exemple :

```codepython
# Crée une liste `ma_liste`
ma_liste = ['a', 'z', 'c']

# Affiche `ma_liste`
print(ma_liste)

# Modifie l'élément à l'indice 1
ma_liste[1] = 'b'

# Affiche `ma_liste` modifiée
print(ma_liste)
```

{{% box type="exercise" title="Mission 2 : Le sac de Julie" %}}

Le sac de Julie est représenté par la liste `sac` juste en-dessous. En préparant
ses affaires, elle voudrait effectuer plusieurs opérations sur ce dernier :

- multiplier par 2 le nombre à l'indice 2 ;
- remplacer le texte `"Bonjour le monde !"` par `"Hello World!"` ;
- remplacer tous les booléens `False` par `True` ;
- remplacer le nombre `3.14` par `"pi"`

Affiche la liste **avant et après** les modifications pour vérifier que tout a
bien été modifié !

```python
sac = ["Bonjour le monde !", False, 21, False, "Bouteille d'eau", False, 3.14]
```

{{% /box %}}

Maintenant que tu sais comment créer une liste et accéder à ses éléments, il est
temps de découvrir l'utilisation de ces dernières en effectuant des opérations
dessus !
