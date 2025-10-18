# Une mémoire de poisson rouge

Un ordinateur, ça ne retient rien. Du moins, pas tant qu'on ne lui demande pas
de le faire.

Pour ça, on utilise ce qui s'appelle une *variable*.

Une variable, c'est comme une boîte. Son nom, c'est l'étiquette qui permet de la
reconnaître, et on met ce qu'on veut dedans.

## Créer une variable

Voici comment on crée une variable :

```python
ma_variable = 10
```

{{% box info %}}

Tu peux nommer tes variables comme tu le souhaites, du moment que ce n'est pas le
nom d'une fonction et que le nom ne contient pas d'espace.

{{% /box %}}

Lorsqu'on écrit `ma_variable = 10`, voici ce qui se passe dans l'ordinateur :

{{< gallery steps=3 >}}

{{< gallery-img src="./resources/images/variable_create_box.webp" desc="Il crée une nouvelle boîte" >}}
{{< gallery-img src="./resources/images/variable_add_name.webp" desc="Il ajoute l'étiquette `ma_variable` dessus" >}}
{{< gallery-img src="./resources/images/variable_store_value.webp" desc="Il met `10` dans la boîte" >}}

{{< /gallery >}}

## Utiliser une variable

Pour utiliser une variable, il suffit d'écrire son nom comme ceci : `ma_variable`.

Vu que ce n'est pas du texte (il n'y a pas de guillemets), le `micro:bit` va
regarder s'il a une boîte avec la bonne étiquette. Si c'est le cas, il va
utiliser ce qu'on a stocké dedans.

Voici un petit exemple pour illustrer :

{{< codestep steps=2 lang="py" >}}

{{< codestep-block desc="On crée notre variable `ma_variable` et on enregistre 10 dedans" >}}
ma_variable = 10
{{< /codestep-block >}}

{{< codestep-block desc="On demande d'afficher `ma_variable`. La boîte existe, donc on affiche son contenu : `10`" >}}
display.scroll(ma_variable)
{{< /codestep-block >}}

{{< /codestep >}}

## Modifier le contenu de la boîte

Pour mettre à jour une variable, il suffit d'en créer une autre du même nom.

L'ancienne boîte est automatiquement supprimée.

{{< codestep steps=2 lang=py >}}

{{< codestep-block desc="On crée une boîte `nombre` avec 10 à l'intérieur" >}}
nombre = 10
{{< /codestep-block >}}

{{< codestep-block desc="On crée une nouvelle boîte `nombre` dans laquelle on met 2, et on supprime celle avec 10" >}}
nombre = 1 + 1
{{< /codestep-block >}}

{{< /codestep >}}

{{% box info %}}

Tu peux utiliser l'ancienne boîte pour calculer la valeur de la nouvelle comme au-dessus.

{{% /box %}}

## Quoi stocker ?

Dans une variable, on peut stocker n'importe quelle information que l'on veut.

En programmation, nous avons souvent 3 types de variables : les *nombres*, les *chaînes de
caractères* et les *booléens*.

### Les nombres

Les nombres en Python peuvent être entiers ou décimaux. Comme tout nombre qui
existe, on peut faire des opérations dessus :

```py
1 + 1  # addition
1 - 1  # soustraction
1 * 1  # multiplication
1 / 1  # division
1 // 1 # division entière
1 % 1  # reste de la division entière
```
{{% box info %}}

Le reste de la division est aussi appelé *modulo*.

{{% /box %}}

{{< details summary="Un petit rappel sur les divisions entières ?" >}}

Une division entière, c'est une division posée sur papier. On s'arrête dès qu'on
ne peut plus soustraire :

{{< figure src="./resources/images/division.webp" width=60% >}}

Ici, on a donc `17 // 5 = 3`, et `17 % 5 = 2`

N'hésite pas à appeler un.e orga pour t'expliquer si tu n'as pas compris !

{{< /details >}}

{{% box warning %}}

Toutes les variables contenant un nombre peuvent être considérées comme des
nombres :

{{< codestep steps=3 lang="py" run="true" >}}

{{< codestep-block desc="Stocke le nombre \'1\' dans la variable `a`" >}}
a = 1
{{< /codestep-block >}}
{{< codestep-block desc="Stocke le nombre \'2\' dans la variable `b`" >}}
b = 2
{{< /codestep-block >}}
{{< codestep-block desc="Affiche \'3\' (la somme de `a` et `b`)" >}}
print(a + b)
{{< /codestep-block >}}

{{< /codestep >}}

De même, toute variable contenant du texte peut être considérée comme du texte.

{{% /box %}}

{{% box type="exercise" title="Mission : acheter des croissants" %}}

Les orgas sont en train de calculer le coût des croissants pour le petit
déjeuner de demain matin.

Ils ont écrit ce code là :

```python
nombre_total_croissants = 42
prix_croissant = 1.2 # le prix d'un croissant
```

Complète le programme pour afficher le prix total des croissants sur ton
`micro:bit`.

{{% /box %}}

{{% box hint %}}

`display.scroll` peut afficher du texte mais également des nombres.

{{% /box %}}

### Du texte, toujours plus de texte

Comme on l'a vu plus tôt, les chaînes de caractères sont reconnaissables car
elles sont entre guillemets.

Mais on peut aussi les mettre à la suite :
```python
"Bon" + "jour" # donne "Bonjour"
```

Toute variable qui stocke du texte (c'est à dire une chaîne de caractères) peut
être utilisée comme du texte.

{{< codestep steps=3 lang="py" run="true" >}}

{{< codestep-block desc="Stocke le \"GC\" dans la variable `a`" >}}
a = "GC"
{{< /codestep-block >}}
{{< codestep-block desc="Stocke le \"C!\" dans la variable `b`" >}}
b = "C!"
{{< /codestep-block >}}
{{< codestep-block desc="Affiche \"GCC!\" (la somme de `a` et `b`)" >}}
print(a + b)
{{< /codestep-block >}}

{{< /codestep >}}

{{% box info %}}

On appelle ça la concaténation.

{{% /box %}}

### Transformation !

{{% box type="danger" %}}

Le problème, avec le texte et les nombres, c'est qu'on ne peut pas les utiliser ensemble directement :

```python
10 + "2" # erreur
```

Ici, `10` est un nombre et `"2"` est une chaîne de caractères (entre guillemets).

{{% /box %}}

On peut transformer l'un en nombre, avec `int` :

```python
10 + int("2")
```

ou l'autre en chaîne de caractères, avec `str` :

```python
str(10) + "2"
```

Bien sûr, la même chose s'applique lorsque les valeurs sont stockées dans des variables.

{{% box info %}}

`int` est un raccourci de *integer*, qui signifie *nombre entier* en anglais, et `str` est un raccourci de *string*, qui signifie *chaîne de caractères*.

{{% /box %}}

{{% box info %}}

Si l'on veut transformer le nombre dans une variable en texte (y ajouter
des guillemets en quelque sorte), on utilise `str` :

```py
variable = 42             # contient le nombre 42
type(variable)            # Affiche `<class 'int'>` car c'est un entier
variable2 = str(variable) # contient le texte "42"
type(variable2)            # Affiche `<class 'str'>` car c'est un entier
```

{{% box hint %}}

Tu peux cliquer sur `Run` pour voir ce que le code au-dessus va afficher !

{{% /box %}}

Pour transformer le texte en nombre, on utilise `int` à la place de `str`.

```py
variable = "42"           # contient le texte "42"
variable2 = int(variable) # contient le nombre 42
```

{{% /box %}}


{{% box type="exercise" title="Mission : Des croissants un peu chers..." %}}

Les orgas sont assez étonnés du prix qu'ils obtiennent. Ils envoient un message
à la *Trésorerie* pour s'assurer qu'ils ont de quoi payer.

Après quelques minutes, celle-ci répond : "&lt;prix&gt; euros ?! Mais c'est trop cher !".

Malheureusement, l'orga en charge de passer la commande n'a pas vu le message,
et n'a accès qu'à son micro:bit.

Écris le message de la *Trésorerie* sur ton `micro:bit`, en remplaçant `<prix>`
par la valeur calculée précédemment.

Tu peux utiliser la concaténation ainsi que la transmutation pour créer la chaîne
de caractères.

{{% /box %}}

### J'affirme !

Un booléen, c'est soit `True` (vrai), soit `False` (faux). Ça permet de donner
l'état d'une affirmation. Par exemple :

{{< codestep steps=2 lang=py >}}

{{< codestep-block desc="1 est bien inférieur à 2, donc on stocke `True`" >}}
c_est_vrai = 1 < 2
{{< /codestep-block >}}

{{< codestep-block desc="1 n'est pas supérieur à 2, donc on stocke `False`" >}}
c_est_faux = 1 > 2
{{< /codestep-block >}}

{{< /codestep >}}

Voici tous les symboles permettant de faire des opérations de comparaison :

| Nom               | Symbole | Exemple | Résultat |
|:-----------------:|:-------:|:-------:|---------:|
| Égalité           | `==`    | 2 == 3  | False    |
| Différence        | `!=`    | 2 != 3  | True     |
| Inférieur strict  | `<`     | 2 < 3   | True     |
| Inférieur ou égal | `<=`    | 2 <= 3  | True     |
| Supérieur strict  | `>`     | 2 > 3   | False    |
| Supérieur ou égal | `>=`    | 2 >= 3  | False    |

### Ça et ça ou ça et pas ça

Il existe 3 opérateurs qui nous permettent de faire des affirmations plus
précises :

| Nom          | Opérateur | Exemple         | Traduction                                        | Résultat |
|:------------:|:---------:|:---------------:|:--------------------------------------------------|:--------:|
| *ne ... pas* | `not`     | not 1 < 2       | 1 **n'** est **pas** inférieur à 2                | False    |
| *et*         | `and`     | 1 < 2 and 2 < 3 | 1 est inférieur à 2 **et** 2 est inférieur à 3    | True     |
| *ou*         | `or`      | 1 > 2 or 2 < 3  | 1 est supérieur à 2 **ou** 2 est inférieur à 3    | True     |

{{% box info %}}

Ils peuvent être combinés autant qu'on veut :

```py
"a" < "b" and 30 / 4 > 6 or 9 % 4 == 1
```

{{% /box %}}

{{% box type="exercise" title="Mission : Erreur de calcul" %}}

Les boulangers se sont trompés sur le calcul du prix.

Lily commande à la boulangerie :
- 4 pains au chocolat à 1€ 25 unité
- 10 croissants à 1€ 20 unité

On lui demande 18€.

Affiche sur le `micro:bit` si ce qu'affirment les boulangers est vrai ou faux.

{{% /box %}}

