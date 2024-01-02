---
title: César
date: 2021
authors: Clarisse Blanco, Dorian Péron
weight: 15
showcase: ./resources/showcase.webp
tags:
    - python
    - cryptographie
score: 40
description: "César manigance un nouveau coup, Astérix et Obélix ont intercepté un message, mais ils n'arrivent pas à le comprendre. Viens les aider à déchiffrer le message ! 🔒"
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

Pour implémenter le chiffre de César, il va être plus simple de diviser le problème en deux parties. On peut, dans un premier temps, appliquer le chiffrement à une seule lettre, puis ensuite appliquer cela à une chaîne de caractères. Pour l'instant, on va prendre en compte que les lettres minuscules.

### Utilisation de la table ASCII

Pour pouvoir effectuer un décalage, par exemple +1, il est plus simple de travailler avec des nombres entiers.
Pour cela, nous pouvons utiliser la table ASCII. Elle associe un nombre à chaque caractère.

Nous pouvons utiliser la fonction `ord(CHAR)` qui retourne le nombre associé à la lettre donnée en paramètre (ici `CHAR`).
Par exemple :
```codepython
print(ord('a'))     # affiche 97
print(ord('e'))     # affiche 101
```

Et l'opération inverse, pour retrouver une lettre à partir de son nombre ASCII, nous utilisons `chr(NB)`.
```codepython
print(chr(97))      # affiche 'a'
print(chr(100))     # affiche 'd'
```

Ainsi, nous pouvons décaler une lettre avec :
- transformer la lettre en nombre
- appliquer le décalage sur le nombre
- transformer le nombre en lettre

### La fonction `letterCaesar(l, d)`

Cette fonction va se charger d'appliquer le chiffre de César à seulement une lettre minuscule, elle va renvoyer un caractère.
Elle prend en paramètre `l` qui correspond à la lettre sur laquelle on va appliquer le chiffrement, c'est un caractère.
Quant au paramètre `d`, il s'agit du décalage qui va être appliqué, c'est un nombre entier.

Exemples :
```py
letterCaesar('a', 1)      # Renvoie 'b'
letterCaesar('e', 6)      # Renvoie 'k'
```

Une fonction est très utile en programmation, pour pouvoir réutiliser une portion de code très facilement, avec parfois des mini changements.
Ces changements sont donnés par les paramètres de la fonction.
Par exemple, dans cette fonction, nous avons 2 changements possibles. Il est possible de changer la lettre (d'abord on veut transformer la lettre 'a', puis la lettre 'e'), et il est possible changer le décalage (d'abord on veut décaler de 1, puis de 6).

Pour définir une fonction en Python, il faut utiliser le mot clé `def`.
Par exemple :
```codepython
def letterCaesar(l, d):
	# TODO
	print(l)
	print(d)

letterCaesar('a', 1)
```

Une fonction est également capable de retourner ce qu'elle veut, avec le mot clé `return`.
Par exemple :
```codepython
def letterCaesar(l, d):
	# TODO
	return l

lettre = letterCaesar('a', 1)  # récupère la lettre renvoyée par la fonction
print(lettre)                  # affiche la lettre renvoyée
```

Attention, une fonction définit avec `def` ne fait rien, si elle n'est jamais appelée :
```codepython
def letterCaesar(l, d):
	# TODO
	return l

# ne fait rien
```

### Les caractères spéciaux

Lors du chiffrement des messages de ce TP, nous ne voulons pas transformer les caractères spéciaux tels que les espaces, la ponctuation, etc.
Pour cela, il nous faut rajouter une condition dans la fonction précédente.
Nous voulons transformer le caractère donné en paramètre, uniquement si celui-ci est une lettre.
Et ça tombe bien, Python nous donne ceci très facilement avec :
```codepython
caractere = 'a'
print(caractere.isalpha())    # affiche True

caractere2 = '!'
print(caractere2.isalpha())    # affiche False
```

Pour résumer, nous voulons :
- si le caractère est une lettre :
	- transformer la lettre en nombre
	- appliquer le décalage sur le nombre
	- transformer le nombre décalé en lettre
	- retourner la lettre décalée
- sinon :
	- retourner le caractère non modifié


### Le dépassement de l'alphabet

Que se passe-t-il si nous décalons la lettre 'z' une fois ?
Nous souhaitons avoir la lettre 'a'.
Cependant si on regarde la table ASCII, la lettre 'a' ne se trouve pas après la lettre 'z'....

Nous devons donc gérer ce cas supplémentaire, le dépassement de l'alphabet.

Revenons à ce que nous savons :
- Il y a 26 lettres dans l'alphabet
- La première lettre de l'alphabet est le 'a'
- Lors du décalage, nous voulons passer du 'z' au 'a'

Pour rendre la tâche plus simple, nous allons associer la lettre 'a' au nombre 0, la lettre 'b' au nombre 1, etc jusqu'à la lettre 'z' au nombre 25.
Donc pour passer de la lettre 'z' à la lettre 'a' lors d'un décalage, nous passons de 25 à 0.
Cette opération correspond au modulo.

L'opérateur modulo s'écrit '%' en Python. Il permet de retourner le reste de la division entière.
Par exemple :
```codepython
print(6 % 4)              # Affiche 2 (6 = 4 * 1 + 2)
print(5 % 2)              # Affiche 1 (5 = 2 * 2 + 1)

print(4 % 26)            # Affiche 4 (4 = 26 * 0 + 4)
print(26 % 26)            # Affiche 0 (26 = 26 * 1 + 0)
print(29 % 26)            # Affiche 3 (29 = 26 * 1 + 3)

print(25 % 26)      # Affiche 0 (25 = 26 * 0 + 25)
print((25 + 1) % 26)      # Affiche 0 (26 = 26 * 1 + 0)
print((25 + 2) % 26)      # Affiche 1 (27 = 26 * 1 + 1)
```

Pour résumer, nous voulons :
- si le caractère est une lettre :
	- transformer la lettre en nombre
	- transformer ce nombre pour qu'il soit entre 0 et 25 (en soustrayant la valeur ASCII de la lettre 'a')
	- appliquer le décalage sur le nombre réduit
	- revenir à un nombre de la table ASCII (en ajoutant la valeur ASCII de la lettre 'a')
	- transformer le nombre décalé en lettre
	- retourner la lettre décalée
- sinon :
	- retourner le caractère non modifié

### Bonus: Lettres minuscules et majuscules

Exemples :
```py
letterCaesar('a', 1)      # Renvoie 'b'
letterCaesar('A', 1)      # Renvoie 'B'
letterCaesar('Z', 2)      # Renvoie 'B'
```

Plusieurs fonctions Python sont disponibles pour tester ou transformer un caractère ou une chaîne de caractères en majuscule.

```codepython
# La méthode upper() permet de tranformer une chaîne de caractères en majuscules.

s = "hello World"
print(s.upper())          # Affiche "HELLO WORLD"
print('a'.upper())        # Affiche 'A'


# La méthode isupper() permet de savoir si un caractère est une majuscule ou non.

c = 'G'
print(c.isupper())        # Affiche True

c = "HELLO"
print(c.isupper())        # Affiche True

c = 'g'
print(c.isupper())        # Affiche False
```

Attention à changer la lettre sur laquelle on réduit et augmente la valeur ascii pour revenir à un nombre entre 0 et 25.


### La fonction `textCaesar(text, d)`

Cette fonction va se charger d'appliquer le chiffre de César sur une chaîne de caractères, elle va renvoyer une chaîne de caractères. Elle prend en paramètre `text` qui correspond à une chaîne de caractères que l'on souhaite chiffrer. Elle prend également un autre paramètre `d` qui correspond au décalage qui doit être appliqué, c'est un nombre entier.

Exemple :
```py
textCaesar("hello", 1)    # Renvoie "ifmmp"
```

Quelques fonctions et notions utiles :

```codepython
# Pour créer une chaîne de caractères :
variable_text = ""
print(variable_text)      # Affiche une chaîne vide


# L'opérateur + permet, quand il est appliqué à des chaînes de caractères,
# de concaténer celles-ci. Exemples:

print("Hello" + "World")  # Affiche "HelloWorld"
print("O" + "K")          # Affiche "OK"

variable_text = variable_text + 'a'
print(variable_text)      # Affiche "a"

variable_text = variable_text + "bcd"
print(variable_text)      # Affiche "abcd"


# Pour passer sur tous les caractères d'une chaîne de caractères
for caractere in variable_text:
	# Utiliser le caractere. Exemple :
	print(caractere)
# Affiche "a", "b", "c", "d", un par ligne
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


