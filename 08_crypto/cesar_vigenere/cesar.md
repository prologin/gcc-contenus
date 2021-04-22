# Le chiffre de César
_Prérequis : la table ascii_
## Un peu d'histoire...
---
Ce moyen de chiffrement doit son nom à Jules César, célèbre homme d'état romain. Il aurait utilisé pour certaines de ses communications secrètes, militaires notamment, un chiffrement par subsitution. Celui-ci utilisant un décalage d'une valeur trois.

## Qu'est-ce qu'un chiffrement par substitution ?
---
Pour faire simple, cette méthode consiste substituer la valeur d'une lettre par une lettre, un chiffre... Dans le cas du chiffrement de César, on substitue une lettre par une autre lettre. Par exemple, si l'on décide d'effectuer un décalage de trois. Voici comment la valeur de chaque lettre va évoluer :

![Image not loading](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Caesar3.svg/1200px-Caesar3.svg.png)

Voilà comment cela va se répercuter sur l'alphabet tout entier :

| |Substitution avec un décalage de 3|
|---|---|
|Alphabet|A B C D E F G H I J K L M N O P Q R S T U V W X Y Z|
|Substitution|D E F G H I J K L M N O P Q R S T U V W X Y Z A B C|

On observe donc que A (première lettre de l'alphabet) sera codée par C (troisième lettre de l'alphabet), que B sera codée par D, que C par E, etc. On remarque que X sera codé par A, Y par B et Z par C. Si le chiffre donné pour le décalage fait dépasser de l'alphabet, on revient au début. 

Par exemple, Z est la 26ème  lettre de l'alphabet. Si l'on applique un décalage de trois, on a alors : 26 + 3 = 29. C'est plus qu'il n'y a de lettres dans l'alphabet. Pour revenir au début, il n'y a qu'à soustraire le nombre total de lettres dans l'alphabet : 29 - 26 = 3. La troisième lettre de l'alphabet est C. Z est donc codé par C.

D'autres exemples:

>Décalage de trois : **Girls Can Code** devient **Jluov fdq frgh**

>Décalage de dix : **Hello World** devient **Rovvy Hycvn**

Voilà donc le principe de base du chiffrement de César.

## Place au code !
---
Pour implémenter le chiffre de César, il va être plus simple de diviser le problème en deux parties. On peut en effet se dire que dans une première partie, on va implémenter le chiffre de César pour qu'il ne soit appliqué que sur une lettre, puis ensuite appliquer cela à une chaîne de caractères en entier. Dans un premier temps, vous pouvez ne prendre en compte que les lettres majuscules ou minuscules si cela vous aide.

Ainsi, il va falloir implémenter les fonctions ```charCaesar(c, d)``` et ```stringCaesar(s, d)```.

### La fonction ```charCaesar(c, d)```
Cette fonction va se charger d'appliquer le chiffre de César à seulement une lettre, elle va renvoyer un char. Elle prend en paramètre ```c``` qui correspond à la lettre sur laquelle on va appliquer le chiffrement, c'est un char. Quant au paramètre ```d```, il s'agit du décalage qui va être appliqué, c'est un int.

### La fonction ```stringCaesar(s, d)```
Cette fonction va se charger d'appliquer le chiffre de César sur une chaîne de caractères, elle va renvoyer un string. Elle prend en paramètre ```s``` qui correspond à une chaîne de caractères que l'on souhaite chiffrer, c'est un string. Elle prend également un autre paramètre ```d``` qui correspond au décalage qui doit être appliqué, c'est un int.

>**Tips :** pensez à prendre en compte les espaces, vous pouvez également utiliser des modulos si vous savez ce que c'est (en python, cela correspond à ```%```)

## Quelques fonctions et notions utiles...
---
- ```+``` va permettre de concaténer des strings ou des chars. Exemple :
>```"Hello " + "World!"``` va donner ```"Hello World!"```

>```"O" + "K"``` va donner ```"OK"```

- ```char.upper()``` va donner la lettre majuscule de "char". Exemple :
>Si ```c = 'a'``` alors ```c.upper()``` va donner ```'A'```

- ```len()``` : permet d'obtenir la longueur d'un string ou d'une liste. Exemple :
>```len("Hello World!")``` va donner ```12```

- ```ord()``` : permet de passer d'un char à un int, prend en paramètre un char. Exemple : 
>```ord('a')``` va donner ```97```

>```ord('Z')``` va donner ```90```

- ```chr()``` : permet de passer d'un int à un char, prend en paramètre un int. Exemple :
>```chr(97)``` va donner ```a```

>```chr(42)``` va donner ```*```

## Décrypter un message...
---


## Bonus : conserver les lettres majuscules et minuscules du message original
---

