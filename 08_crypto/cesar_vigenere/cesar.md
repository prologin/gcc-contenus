# Le chiffre de César
_Prérequis : la table ascii_
## Un peu d'histoire...
---
Ce moyen de chiffrement doit son nom à Jules César, célèbre homme d'état romain. Il aurait utilisé pour certaines de ses communications secrètes, militaires notamment, un chiffrement par subsitution. Celui-ci utilisant un décalage d'une valeur trois.

## Qu'est-ce qu'un chiffrement par substitution ?
---
Pour faire simple, cette méthode consiste à substituer la valeur d'une lettre par une lettre, un chiffre ou autre. Dans le cas du chiffrement de César, on substitue une lettre par une autre lettre. Par exemple, si l'on décide d'effectuer un décalage de trois, voici comment la valeur de chaque lettre va évoluer :

![Image not loading](https://organiser-anniversaire.fr/wp-content/uploads/2011/05/codes.jpg)

Voilà comment cela va se répercuter sur l'alphabet tout entier :

| |Substitution avec un décalage de 3|
|---|---|
|Alphabet|A B C D E F G H I J K L M N O P Q R S T U V W X Y Z|
|Substitution|D E F G H I J K L M N O P Q R S T U V W X Y Z A B C|

On observe donc que A (première lettre de l'alphabet) sera encodée par D (troisième lettre de l'alphabet), que B sera encodée par E, que C par F, etc. On remarque que X sera codé par A, Y par B et Z par C. Si le chiffre donné pour le décalage fait dépasser de l'alphabet, on revient au début. 

Par exemple, Z est la 26ème  lettre de l'alphabet. Si l'on applique un décalage de deux, on a alors : 26 + 3 = 29. C'est plus qu'il n'y a de lettres dans l'alphabet. Pour revenir au début, il n'y a qu'à soustraire le nombre total de lettres dans l'alphabet : 29 - 26 = 3. La troisième lettre de l'alphabet est C. Z est donc codé par C.

D'autres exemples:

>Décalage de trois : **Girls Can Code** devient **Jluov fdq frgh**

>Décalage de dix : **Hello World** devient **Rovvy Hycvn**

Voilà donc le principe de base du chiffrement de César.

## Place au code !
---
Pour implémenter le chiffre de César, il va être plus simple de diviser le problème en deux parties. On peut en effet se dire que dans un premier temps, on va implémenter le chiffre de César pour qu'il ne soit appliqué que sur une lettre, puis ensuite appliquer cela à une chaîne de caractères. Pour l'instant, vous pouvez ne prendre en compte que les lettres majuscules ou minuscules si cela vous aide.

Ainsi, il va falloir implémenter les fonctions ```charCaesar(c, d)``` et ```stringCaesar(s, d)```.

### La fonction ```charCaesar(c, d)```
Cette fonction va se charger d'appliquer le chiffre de César à seulement une lettre, elle va renvoyer un caractère. Elle prend en paramètre ```c``` qui correspond à la lettre sur laquelle on va appliquer le chiffrement, c'est un caractèrer. Quant au paramètre ```d```, il s'agit du décalage qui va être appliqué, c'est un nombre entier.

### La fonction ```stringCaesar(s, d)```
Cette fonction va se charger d'appliquer le chiffre de César sur une chaîne de caractères, elle va renvoyer une chaîne de caractères. Elle prend en paramètre ```s``` qui correspond à une chaîne de caractères que l'on souhaite chiffrer. Elle prend également un autre paramètre ```d``` qui correspond au décalage qui doit être appliqué, c'est un nombre entier.

>**Tips :** pensez à prendre en compte les espaces, vous pouvez également utiliser des modulos si vous savez ce que c'est (en python, cela correspond à ```%```)

## Quelques fonctions et notions utiles...
---
- ```+``` va permettre de concaténer des caractères ou des chaînes de caractères. Exemple :
>```"Hello " + "World!"``` va donner ```"Hello World!"```

>```"O" + "K"``` va donner ```"OK"```

- ```char.upper()``` va donner la lettre majuscule de "char". Exemple :
>Si ```c = 'a'``` alors ```c.upper()``` va donner ```'A'```

- ```len()``` : permet d'obtenir la longueur d'une chaîne de caractères ou d'une liste. Exemple :
>```len("Hello World!")``` va donner ```12```

- ```ord()``` : permet de passer d'un caractère à un nombre entier (selon la table ASCII), prend en paramètre un caractère. Exemple : 
>```ord('a')``` va donner ```97```

>```ord('Z')``` va donner ```90```

- ```chr()``` : permet de passer d'un nombre entier à un caractère (selon la table ASCII), prend en paramètre un nombre entier. Exemple :
>```chr(97)``` va donner ```a```

>```chr(42)``` va donner ```*```

## Décrypter un message...
---


## Bonus : conserver les lettres majuscules et minuscules du message original
---

