# Représenter une chaîne de caractères

Le texte est écrit entre guillemets doubles `"` ou simples `'` comme dans
l'exemple suivant.

```codepython
# Crée une chaîne de caractères
# dans la variable `mon_texte`
mon_texte = "Hello World!"

# Affiche `mon_texte`
print(mon_texte)
```

{{% box type="info" title="Quand utilise-t-on des guillemets doubles ou simples ?" %}}

Par convention, on utilise les guillemets simples (`'`) pour les caractères et
les guillemets doubles (`"`) pour les chaînes de caractères. Cependant, cela ne
change pas grand chose en Python.

```codepython
# Affiche le caractère '!'
print('!')

# Affiche le texte "Hello World!"
print("Hello World!")
```

{{% /box %}}

{{% box type="info" title="Les caractères spéciaux" %}}

Il existe plusieurs caractères que l'on ne peut pas afficher normalement. Par
exemple, pour afficher un *saut de ligne* en Python, on ne peut pas juste
utiliser la touche *Entrer*.

```codepython
print("Ceci est une
nouvelle ligne")
```

Pour **représenter** le saut de ligne, on utilise le caractère `'\n'`. D'autres
caractères reprenant le `\` en premier symbole permettent d'afficher ces
caractères spéciaux.

```codepython
# Utilise le caractère `\n` pour sauter une ligne
print("Ceci est une\nnouvelle ligne")
```

Il existe plusieurs caractères spéciaux, en voici les plus utilisés et ceux que
tu pourras rencontrer :

</br>

| Caractère | Description |
|:--:|:--:|
|`'\n'`| Saut de ligne |
|`'\"'`| Guillemet double qui est considéré comme du texte |
|`'\''`| Guillemet simple qui est considéré comme du texte |
|`'\\'`| Barre oblique inversée |
|`'\t'`| Tabulation (espace plus grand) |

</br>

```codepython
print("Le code ci-dessous affiche \"Hello World!\" :\n\tprint(\"Hello World!\\n\")")
```

{{% /box %}}

# Parallèles avec les listes

En Python, les chaînes de caractères se matérialisent sous la forme de **listes
de caractères** et on y retrouve les mêmes propriétés que les listes !

## Calculer la longueur d'une chaîne

Comme avec les listes, tu peux utiliser la fonction `len` pour calculer la
**longueur** de la chaîne de caractères.

```codepython
# Crée une chaîne de caractères `ma_chaine`
ma_chaine = "Hello World!"

# Calcule la longueur de `ma_chaine`
# et la stocke dans la variable `longueur`
longueur = len(ma_chaine)

# Affiche `longueur`
print(longueur)
```

## Récupérer un caractère

On peut utiliser l'**opérateur `[]`** pour accéder à un caractère de la chaîne
en utilisant les indices.

```codepython
# Crée une chaîne de caractères `ma_chaine`
ma_chaine = "Hello World!"

# Récupère le caractère à l'indice 4
mon_caractere = ma_chaine[4]

# Affiche le caractère
print(mon_caractere)
```

{{% box type="warning" title="Attention à ne pas aller trop loin !" %}}

Comme pour les listes, les indices sont des nombres compris entre **0** et la
**longueur de la chaîne - 1** !

```codepython
# Crée une chaîne de caractères `ma_chaine`
ma_chaine = "Hello World!"

# Essaye d'accéder au caractère à l'indice 20
mon_caractere = ma_chaine[20]
```

{{% /box %}}

{{% box type="warning" title="Assigner ou modifier un caractère de la chaîne" %}}

Cependant, tu **ne peux pas assigner ou modifier** un caractère de la chaîne en
utilisant les opérateurs `[]` et `=` contrairement aux listes.

```codepython
# Crée une chaîne de caractères `ma_chaine`
ma_chaine = "Hella World!"

# Essaye de modifier le caractère à l'indice 4
ma_chaine[4] = 'o'
```

{{% /box %}}

## Parcourir une chaîne de caractères

Il est possible de **parcourir** une chaîne de caractères au travers d'une
boucle `for` spécifique comme les listes. Cela permet d'accéder à **chaque
caractère** d'une chaîne.

```codepython
# Crée une chaîne de caractères `ma_chaine`
ma_chaine = "GCC!"

# Parcourt la chaîne
for caractere in ma_chaine:
    print("J'ai récupéré le caractère", caractere)
```

Il est également possible de **parcourir** la chaîne de caractères en utilisant
les **indices** des caractères et l'opérateur `[]`.

```codepython
# Crée une chaîne de caractères `ma_chaine`
ma_chaine = "GCC!"

# Calcule la longueur de la chaîne de caractères
longueur = len(ma_chaine)

# Parcourt la chaîne en utilisant les indices
for i in range(longueur):
    print(ma_chaine[i], "est à l'indice", i)
```

## Vérifier l'existence d'un caractère dans une chaîne

En utilisant le mot-clé `in`, il est possible de **vérifier** si un certain
caractère **existe** dans une chaîne de caractères.

```codepython
# Crée une chaîne de caractères `ma_chaine`
ma_chaine = "Hello World!"

# Crée un caractère `caractere`
caractere = 'a'

# Vérifie si `caractere` existe dans `ma_chaine`
if caractere in ma_chaine:
    print(caractere, "est dans ma chaîne de caractères")

else:
    print(caractere, "n'est pas dans ma chaîne...")
```

## Concaténer des chaînes

L'opérateur `+` permet de **concaténer** les chaînes de caractères entre elles,
c'est-à-dire de mettre les chaînes les unes à la suite des autres comme dans cet
exemple :

```codepython
# Crée deux chaînes de caractères
chaine1 = "Hello "
chaine2 = "World!"

# Crée une troisième chaîne en
# concaténant les deux premières
chaine3 = chaine1 + chaine2

# Affiche `chaine3`
print(chaine3)
```

{{% box type="exercise" title="Mission 1 : Voyelles et consonnes" %}}

Julie te propose une nouvelle énigme avec elle ! Cependant, elle voudrait
vérifier que tu as bien compris comment fonctionnaient les chaînes de
caractères. Pour cela, elle te donne un défi.

Il faut que tu trouves le nombre de voyelles, consonnes et de symboles (les caractères qui ne
sont pas des lettres) dans un très long texte. Attention à ne pas oublier les
majuscules !

```python
texte = "Il est 7h je me lève le matin. Je prends ma douche, je descends l'escalier. Je prends mon bol, je mange mes céréales. Je dois tout boire mais le temps passe vite. Tic tac, tout le monde se presse. Je descends à l'arêt du bus. Je dois prendre mon bus, je vois mes amis ! Sauter sur le siège avant, sauter sur le siège arrière. Il faut que je choisisse quel siège faut-il prendre. C'est vendredi, on fête le vendredi-i. Tout le monde est impatient d'être au week-end. C'est vendredi, fun-fun c'est vendredi-i. Tout le monde est impatient d'être au week-end. On fait la fête, fait la fête (ouais) ! Fait la fête, fait la fête (ouais) ! Fun-fun-fun-fun (chouette) ! On a hâte d'être au week-end."
```

Tu dois alors afficher le texte suivant, en replaçant {nombre} par le nombre en
question : *"Il y a {nombre} consonnes, {nombre} voyelles et {nombre}
symboles !"*.

{{% /box %}}

{{% box type="exercise" title="Mission 2 : Message à l'envers" %}}

Julie te montre une lettre mystérieuse qu'elle a trouvée dans sa boîte aux
lettres récemment. Une phrase a l'air d'être écrite à l'envers, sers-toi de
*Python* pour afficher la phrase à l'endroit !

```python
phrase = "! serueirépus zeyos ,edia ertov ed nioseb ia’j ,iom-zevuorter ,serèirutnevA"
```

Pour t'aider, tu peux utiliser une boucle `for` en faisant attention aux
indices.

{{% /box %}}
