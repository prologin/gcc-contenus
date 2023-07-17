# Parallèles avec les listes

En Python, les string se matérialisent sous la forme de listes de caractères,
et on y retrouve les mêmes propriétés !

On a l'**opérateur `[]`** pour accéder individuellement aux caractères de la chaîne.

```codepython
s = "Hello World!"
print(s[0]) # Affiche la première lettre
```

Par contre, il est impossible changer un caractère de la chaîne :
```codepython
s = "Hello!"
print(s)
s[4] = ' '
print(s)
```

La **fonction `len()`** permet de calculer la longueur d'une liste, ou d'une chaîne :
```codepython
phrase = "Bonjour à tous !"
print(phrase)
longueur = len(phrase)
print(longueur)
```

On peut aussi utiliser une boucle `for` pour **parcourir** tous les caractères de la chaîne :
```codepython
chaine = "aeiouy"
for caractere in chaine:
    print(caractere, "est une voyelle")

chaine2 = "GCC"
for i in range(len(chaine2)):
    print(chaine2[i])
```

De même, il est possible de concaténer des string, avec le même **opérateur `+`** que les listes :
```codepython
debut = "Bienvenue au stage "
nom = "GCC"
point = "!"
print(debut + nom + point)
```

Et on peut tester si une lettre est présente dans une string, avec le **mot-clé `in`** :
```codepython
voyelles = "aeiouy"
if 'a' in voyelles:
    print("a est une voyelle")
if 'b' in voyelles:
    print("Depuis quand b est une voyelle ??")
else:
    print("Tout va bien, b n'est pas une voyelle")
```


Les caractères contenus dans les chaînes de caractères sont compris par l'ordinateur sous forme de code unique par caractère, mis dans un tableau.


Les caractères étant dans un tableau, on peut leur associer un numéro, qu'il est possible de récupérer avec la fonction `ord()` :
```codepython
lettre = "a"
print(ord(lettre))
```

Et dans l'autre sens, pour retrouver un caractère à partir de son numéro, on utilise la fonction `chr()` :
```codepython
code_lettre = 65
print(chr(code_lettre))
```

Pour résumer, les caractères ont chacun un numéro unique, le tout est rangé dans un grand tableau.

Cette particularité nous permet de **comparer les caractères** entre eux :
```codepython
lettre1 = "a"
lettre2 = "d"
print(lettre1 < lettre2)
print(lettre1, ord(lettre1))
print(lettre2, ord(lettre2))

lettre3 = "A"
print(lettre3 > lettre1)
print(lettre3, ord(lettre3))

car = "\n"
print(car < lettre3)
print(car < lettre1)
print(car, ord(car))
```

Les différents opérateurs de comparaison :
- `==` pour tester l'égalité
- `!=` pour tester la différence
- `a < b` pour tester si `a` est inférieur à `b`
- `a <= b` pour tester si `a` est inférieur ou égal à `b`
- `a > b` pour tester si `a` est supérieur à `b`
- `a >= b` pour tester si `a` est supérieur ou égal à `b`

Ces opérateurs sont aussi utilisables sur les chaînes de caractères :
```codepython
mot1 = "code"
mot2 = "bonbons"
print(mot2 > mot1)

stage = "GCC"
print(stage != "gcc")
```

La comparaison sur les chaînes de caractères utilise l'ordre lexicographique.

C'est le même ordre que dans un dictionnaire, lorsqu'on **compare deux string**, on compare tout d'abord leur premier caractère. S'ils sont différents, on retourne l'opération demandée sur les deux caractères. S'ils sont égaux, on répète l'opération de comparaison sur le caractère d'après dans les deux string.

```codepython
print("lundi" > "mardi", "car le caractère 'l' est avant le 'm' dans la table")
print("mardi" < "mercredi", "le 'm' étant identique, on compare le 'a' et le 'e'")
print("jour" < "journée", "les 4 premières lettres sont identiques,\n",
    "la chaîne 'jour' est terminée contrairement à 'journée' donc inférieure")
```

{{% box type="exercise" title="Exercice 2" %}}

Un chercheur faisant ses études sur les claviers d'ordinateurs, souhaite connaître le nombre de fois qu'on appuie sur certaines touches.

Aide-le en comptant le nombre d'occurences du caractère contenu dans la variable `c`, dans la chaîne de caractères `s`.

Tu peux utliser ces valeurs des variables pour exemple :
```python
c = "e"
s = "Il était une fois le feu, l'eau et la confiance"
```

Conseil : utilise les parties "parcours" et "comparaison" de ce TP.

{{% /box %}}