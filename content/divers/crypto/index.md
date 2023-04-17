---
title: Cryptologie
date: 2021
authors: Clarisse Blanco, Dorian Péron
weight: 15
subtitle: 
---

# Le chiffre de César

### **La table ASCII**

Avant de commencer, nous allons rapidement évoquer une notion qui vous sera utile tout au long de ce TP.

La table ASCII (American Standard Code for Information Interchange), est une norme d'encodage des caractères. C'est une représentation qu'utilisent les ordinateurs pour garder en mémoire des caractères. Par exemple, avec la table ASCII, le **A** correspond à la valeur $65$ et le **a** correspond à $97$. Cela permet de convertir vos lettres en nombres et inversement, ça va s'avérer très pratique dans la suite !

{{<figure src="resources/images/ascii.png" height=300 caption="Table ASCII">}}

## Un peu d'histoire

Ce moyen de chiffrement doit son nom à Jules César, célèbre homme d'état romain. Il aurait utilisé pour certaines de ses communications secrètes, militaires notamment, un chiffrement par substitution.

## Qu'est-ce qu'un chiffrement par substitution ?

Pour faire simple, cette méthode consiste à échanger un caractère par un autre. Dans le cas du chiffrement de César, on remplace une lettre par la lettre trois rangs plus à droite dans l'alphabet comme vous pouvez le voir sur la figure ci-dessous.

{{<figure src="resources/images/shifting.jpg" caption="Chiffrement de César">}}

Voilà comment cela va se répercuter sur l'alphabet tout entier :

| |Substitution avec un décalage de 3|
|---|---|
|Alphabet|A B C D E F G H I J K L M N O P Q R S T U V W X Y Z|
|Substitution|D E F G H I J K L M N O P Q R S T U V W X Y Z A B C|

On observe donc que A (première lettre de l'alphabet) sera remplacée par D (quatrième lettre de l'alphabet), B par E, C par F, etc. Dès lors que le décalage fait sortir de l'alphabet, on retourne au début, c'est pourquoi X sera remplacé par A, Y par B et Z par C.

Prenons l'exemple de Z, qui est la 26ème lettre de l'alphabet. Si l'on applique un décalage de trois, on a alors : 26 + 3 = 29. C'est plus qu'il n'y a de lettres dans l'alphabet. Pour revenir au début, il n'y a qu'à soustraire le nombre total de lettres dans l'alphabet : 29 - 26 = 3. La troisième lettre de l'alphabet est C, Z est donc remplacé par C.

D'autres exemples:

- Décalage de trois : **Girls Can Code!** devient **Jluov Fdq Frgh!**
- Décalage de dix : **Hello World!** devient **Rovvy Gybvn!**

Voilà donc le principe de base du chiffrement de César.

## Place au code

Pour implémenter le chiffre de César, il va être plus simple de diviser le problème en deux parties. On peut, dans un premier temps, appliquer le chiffrement à une seule lettre, puis ensuite appliquer cela à une chaîne de caractères. Pour l'instant, vous pouvez ne prendre en compte que les lettres majuscules ou minuscules si cela vous aide.

Ainsi, il va falloir implémenter les fonctions `letterCaesar(l, d)` et `textCaesar(s, d)`.

### La fonction `letterCaesar(l, d)`

Cette fonction va se charger d'appliquer le chiffre de César à seulement une lettre, elle va renvoyer un caractère. Elle prend en paramètre `l` qui correspond à la lettre sur laquelle on va appliquer le chiffrement, c'est un caractère. Quant au paramètre `d`, il s'agit du décalage qui va être appliqué, c'est un nombre entier.

Exemples :
```py
letterCaesar('a', 1)      # Renvoie 'b'
letterCaesar('e', 6)      # Renvoie 'k'
```

**Conseil :** pensez à prendre en compte les espaces et la ponctuation : ils ne doivent pas être modifiés. Vous pouvez également utiliser des modulos.
Des astuces se trouvent un peu plus bas dans "Quelques fonctions et notions utiles".

Exemples :
```py
letterCaesar('!', 1)      # Renvoie '!'
letterCaesar('z', 2)      # Renvoie 'b'
```

L'opérateur modulo s'écrit '%' en Python. Il permet de retourner le reste de la division entière.
Par exemple :
```codepython
print(6 % 4)              # Affiche 2 (6 = 4 * 1 + 2)
print(5 % 2)              # Affiche 1 (5 = 2 * 2 + 1)
print(29 % 26)            # Affiche 3 (29 = 26 * 1 + 3)
print(26 % 26)            # Affiche 0 (26 = 26 * 1 + 0)
```

**Bonus:** essayez de gérer les majuscules et minuscules.

Exemples :
```py
letterCaesar('A', 1)      # Renvoie 'B'
letterCaesar('Z', 2)      # Renvoie 'B'
```


### La fonction `textCaesar(t, d)`

Cette fonction va se charger d'appliquer le chiffre de César sur une chaîne de caractères, elle va renvoyer une chaîne de caractères. Elle prend en paramètre `t` qui correspond à une chaîne de caractères que l'on souhaite chiffrer. Elle prend également un autre paramètre `d` qui correspond au décalage qui doit être appliqué, c'est un nombre entier.

Exemples :
```py
textCaesar('hello', 1)    # Renvoie 'ifmmp'
```


## Quelques fonctions et notions utiles

```codepython
# L'opérateur + permet, quand il est appliqué à des chaînes de caractères,
# de concaténer celles-ci. Exemples:

print('Hello' + 'World')  # Affiche 'HelloWorld'
print('O' + 'K')          # Affiche 'OK'


# La fonction len() permet de connaître la longueur d'une chaîne de caractères.

print(len('Hello World')) # Affiche 11

s = 'ABCD'
print(len(s))             # Affiche 4


# Les fonctions ord() et chr() permettent de transformer un caractère en son
# code ASCII et vice-versa.

print(ord('A'))           # Affiche 65
print(ord('C'))           # Affiche 67

print(chr(65))            # Affiche 'A'


# La méthode upper() permet de tranformer une chaîne de caractères en majuscules.

s = 'hello World'
print(s.upper())          # Affiche 'HELLO WORLD'
print('a'.upper())        # Affiche 'A'


# La méthode isalpha() permet de déterminer si un caractère est une lettre ou non.

c = '!'
print(c.isalpha())        # Affiche False

c = 'a'
print(c.isalpha())        # Affiche True


# La méthode isupper() permet de savoir si un caractère est une majuscule ou non.

c = 'G'
print(c.isupper())        # Affiche True

c = "HELLO"
print(c.isupper())        # Affiche True

c = 'g'
print(c.isupper())        # Affiche False
```

## Déchiffrer un message

Pour déchiffrer un message il suffit d'utiliser la clé inverse à celle utilisée pour chiffrer. Par exemple:

```py
msg = stringCaesar("Hello World", 10)   # Chiffre "Hello World" et
                                        # affiche "Rovvy Gybvn"

stringCaesar(msg, -10)                  # Déchiffre msg et
                                        # affiche "Hello World"
```

Dans un premier temps, testez avec votre code pour observer le résultat obtenu. Puis, adaptez votre code pour prendre en compte les décalages négatifs.

## Casser le chiffre de César

Il existe plusieurs méthodes pour casser le chiffre de César. On peut par exemple faire une analyse fréquentielle qui va compter la proportion de chaque lettre dans le message chiffré et comparer par rapport à la fréquence connue des lettres dans la langue du message. En français, à titre d'exemple, la lettre `e` est la plus fréquente, ainsi la lettre la plus fréquente du message chiffré doit sans doute correspondre à un `e`. Cette méthode est très efficace sur les messages longs, le problème est donc que sur les messages dits courts, elle ne sera pas d'un grande utilité. Ce n'est donc pas celle que vous allez implémenter, mais il est toujours intéressant de savoir qu'une telle méthode existe.

La méthode que vous allez implémenter consiste en du brute force.

**Qu'est-ce que le brute force ?**  Pour faire simple, cela consiste à essayer toutes les combinaisons possibles. Dans notre cas, cela revient à essayer 26 possibilités, puisqu'il y a 26 lettres dans l'alphabet.

Vous allez donc implémenter la fonction `breakCaesar(msg)`. Elle prend en paramètre une chaîne de caractères (chiffrée) et ne renvoie rien. Son but va être d'afficher toutes les possibilités de déchiffrement du message. C'est à dire, à appliquer `charCaesar(c, d)` avec différentes valeurs de décalage. Voici un exemple de ce qu'elle devrait afficher pour `breakCaesar("Rovvy Gybvn")`:

```text
Spwwz Hzcwo
Tqxxa Iadxp
Uryyb Jbeyq
Vszzc Kcfzr
Wtaad Ldgas
Xubbe Mehbt
Yvccf Nficu
Zwddg Ogjdv
Axeeh Phkew
Byffi Qilfx
Czggj Rjmgy
Dahhk Sknhz
Ebiil Tloia
Fcjjm Umpjb
Gdkkn Vnqkc
Hello World     # Message déchiffré !
Ifmmp Xpsme
Jgnnq Yqtnf
Khoor Zruog
Lipps Asvph
Mjqqt Btwqi
Nkrru Cuxrj
Olssv Dvysk
Pmttw Ewztl
Qnuux Fxaum
Rovvy Gybvn
```

Vous pouvez tout à fait améliorer l'affichage pour que cela soit davantage lisible !

La fonction `print()` va vous être utile. Elle permet d'afficher ce qu'on lui donne en paramètre (une chaîne de caractères, un nombre, une liste...). Par exemple :

```codepython
s = "Hello World"
print(s)                  # Affiche "Hello World"

print("Bonjour !")        # Affiche "Bonjour !"
print(42)                 # Affiche 42

print() # Sans argument, print() affiche uniquement un retour à la ligne


# N'hésitez pas à essayer de votre côté !
```

### Challenge

Essaye de décrypter ce message chiffré avec le chiffre de César !

```text
YRF FGNTRF TVEYF PNA PBQR! P'RFG GEBC PBBY!
```

# Le chiffre de Vigenère

_Prérequis : avoir fini la partie sur le chiffre de César_

## Un peu d'histoire

Le chiffre de Vigenère est une méthode de chiffrement par substitution imaginée au XVIe siècle par Blaise de Vigenère (ou peut-être pas, mais la méthode a néanmoins le nom de Vigenère). Le général prussien Friedrich Kasiski publie en 1863 une méthode permettant de casser ce chiffre.

## Principe du chiffre de Vigenère

Cette méthode de chiffrement est assez similaire au chiffre de César que vous avez implémenté précédemment. La différence notable est que, pour Vigenère, on applique à chaque lettre du message un décalage différent. Ce décalage est donné par une clé, sous forme de chaîne de caractères.

Pour chaque lettre de la chaîne de caractères clé, nous déduisons un décalage à appliquer (on considère que `a` est la zerotième lettre de l'alphabet). Exemple avec la clé **"clef"** :

- **c** est la 2e lettre de l'alphabet, le décalage correspond ici à 2
- **l** est la 11e lettre de l'alphabet, ici ce sera 11
- **e** est la 4e lettre de l'alphabet, ici ce sera 4
- **f** est la 5e lettre de l'alphabet, ici ce sera 5

Si la chaîne de caractères clé est plus courte que la chaîne de caractères message, elle sera répétée autant de fois que nécessaire. Voici un exemple avec la clé **"clef"** :

```text
Message :           Comment est votre blanquette ?
Clé :               clefclefclefclefclefclefclefcl

Message chiffré :   Ezqrgyx gdx xzxwg fqcyuzgexj ?
```

## À vos claviers

Pour implémenter le chiffre de Vigenère, il va être plus simple de diviser le problème en sous-problèmes. Vous aurez également besoin de la fonction `letterCaesar(l, d)` réalisée dans la partie sur le chiffre de César.

### La fonction `keyToOffset(k)`

Cette fonction a pour but de convertir la clé en une liste de décalages. Elle prend en paramètre `k` la clé, qui correspond à une chaîne de caractères. Elle retourne une liste, ayant pour taille le nombre de caractères de la clé, contenant les décalages correspondant à chaque lettre de la clé.

#### Les listes

Les listes permettent de stocker plusieurs éléments dans une même variable.

Tu peux les manipuler aisément :

```codepython
L = ['a', 'b', True, 'C', 42, 'd']  # Exemple de liste quelconque

print(L[0])    # Affiche le premier élément de la liste

i = 2
print(L[i])    # Affiche l'élément à la i-ème position (i allant de 0 à la longueur de la liste)

print(len(L))  # Calcule la longueur de la liste

L.append(1)    # Ajoute le nombre 1 à la fin de la liste L
print(L)

# Pour passer sur tous les éléments de la liste et les afficher par exemple, on peut faire :
for i in range(0, len(L)):   # Ici on a `i` qui prend les valeurs de 0 à len(L)-1
    print(L[i])
```

#### Exemples pour la fonction `keyToOffset(k)`

```py
keyToOffset("ae")         # Renvoie [0, 4]
keyToOffset("atest")      # Renvoie [0, 19, 4, 18, 19]
keyToOffset("clef")       # Renvoie [2, 11, 4, 5]
```

### La fonction `textVigenere(t, k)`

Cette fonction va chiffrer le texte donné à l'aide du chiffre du Vigenère. Elle prend en paramètre `t`, une chaîne de caractères, qui est le message à dissimuler. L'autre paramètre `k`, est aussi une chaîne de caractères et correspond à la clé.

#### Exemples pour la fonction `textVigenere(t, k)`

```py
textVigenere("hello!", "ae")  # Renvoie "hilpo!"
```

## Annexe

### Sources

- "La cryptographie militaire", Auguste Kerchkhoffs, 1883
- [Wikipedia: Chiffre de Vigenère](https://fr.wikipedia.org/wiki/Chiffre_de_Vigen%C3%A8re)
- [haltode.fr: Chiffre de Vigenère](https://haltode.fr/algo/chiffrement/chiffre_vigenere.html)


