# Contrôler son code

L'ordinateur lit ligne par ligne les différentes instructions que donne la
programmeuse ou le programmeur. Cependant, il est également possible de vouloir
effectuer une certaine partie du code seulement **si une condition** est
vérifiée ou même **répéter plusieurs fois** plusieurs instructions.

## Les conditions

En programmation, tu voudras parfois qu'un certain bout de code s'effectue
seulement **si** une condition est vraie, ou effectuer un autre bout de code si
cette dernière n'est pas vraie.

Commençons d'abord par regarder des exemples que tu pourrais rencontrer dans la
**vie courante** de l'utilisation des condititons.

{{< gallery steps=3 >}}

{{< gallery-img src="./resources/images/algo-if.png" desc="Utilisation d'une condition" >}}
{{< gallery-img src="./resources/images/algo-else.png" desc="Utilisation d'une condition avec une action si elle n'est pas vérifiée" >}}
{{< gallery-img src="./resources/images/algo-elif.png" desc="Utilisation de plusieurs conditions chaînées" >}}

{{< /gallery >}}

On va alors pouvoir utiliser l'instruction `if` (*si* 🇫🇷) que l'on fait suivre
d'une condition que l'on veut tester. Elle permet d'exécuter un morceau de code 
**uniquement lorsque la condition est vraie**.

Pour vérifier une certaine condition, on va utiliser la syntaxe `if condition:`,
suivi d'un bloc de code **indenté**. Le bloc de code en question ne sera alors
exécuté seulement **si** `condition` est vraie, qu'on ait le booléen `True`.

{{< figure src="resources/images/if.png" caption="Blocs de code avec une condition" >}}

{{% box type="info" title="C'est quoi les booléens ?" %}}

Les booléens correspondent à un type de variables en programmation. Ils ont soit
la valeur `True` (*vrai* 🇫🇷), soit la valeur `False` (*faux* 🇫🇷).

Ils permettent d'exprimer si une proposition est vraie ou fausse, comme dans ces
exemples :

```codepython
# Affiche `True` car 42 est supérieur à 12
print(42 > 12)

# Affiche `False` car 1 n'est pas égal à 2
print(1 == 2)

# Affiche "Validé !" seulement si "A" est égal à "A"
# C'est le cas ici !
if "A" == "A":
    print("Validé !")
```

{{% /box %}}

{{% box type="info" title="Indentation et création de blocs de code" %}}

Python utilise l'indentation pour isoler certains bouts de codes et créer
des **blocs de code**.

Pour créer ces blocs, nous allons utiliser la touche tabulation sur ton clavier.
Elle permet de rajouter des espaces. Elle devrait ressembler à ça :

{{< figure src="resources/images/tabulation.png" width=200 caption="Touche tabulation du clavier" >}}

L'**indentation** correspond au nombre d'espaces au début d'une ligne et avant
une instruction. Dans l'exemple de code ci-dessous, la première ligne a un
niveau d'indentation de **0** espaces en début de ligne, tandis que la troisième
ligne a un niveau d'indentation de **4** espaces.

```codepython
print("Hello World!") # Ligne qui n'est pas indentée

if 1 == 1:
    print("Girls Can Code!") # Ligne qui est indentée 1 fois
```

Garder l'indentation permet de faire plusieurs instructions dans le même bloc.

{{% /box %}}

Un `if` peut être accompagné d'un `else` (*sinon* 🇫🇷) qui exécute un bloc de
code uniquement si la condition du `if` est fausse.

{{< figure src="resources/images/if-else.png" caption="Blocs de code avec un else" >}}

Enfin, il y a aussi le `elif` qui est la contraction du *else* et du *if*. Il
n'est exécuté que si sa condition est vraie et que les conditions précédentes
sont fausses.

{{< figure src="resources/images/if-elif.png" caption="Blocs de code avec un elif" >}}

Voici un petit exemple pour illustrer ce que l'on dit sur les conditions :

{{< codestep steps=5 lang="py" run="true" >}}

{{< codestep-block desc="Demande à l'utilisateur \"Quel animal vois-tu ?\" et garde la valeur entrée dans la variable `animal`" >}}
animal = input("Quel animal vois-tu ?")
 
{{< /codestep-block >}}

{{< codestep-block desc="Affiche \"Ouaf !\" si `animal` est égal à \"chien\"" >}}
if animal == "chien":
    print("Ouaf !")
{{< /codestep-block >}}

{{< codestep-block desc="Affiche \"Miaou !\" si `animal` est égal à \"chat\"" >}}
elif animal == "chat":
    print("Miaou !")
{{< /codestep-block >}}

{{< codestep-block desc="Affiche \"Piou piou !\" si `animal` est égal à \"oiseau\"" >}}
elif animal == "oiseau":
    print("Piou piou !")
{{< /codestep-block >}}

{{< codestep-block desc="Affiche \"Je ne connais pas cet animal\" sinon" >}}
else:
    print("Je ne connais pas cet animal...")
{{< /codestep-block >}}

{{< /codestep >}}

{{% box type="info" title="Les opérateurs booléens" %}}

Il existe des opérateurs qui permettent de comparer des éléments entre eux,
comme ce que tu as pu voir dans les exemples précédents. Ils renvoient une
valeur booléenne qui donne `True` ou `False`.

</br>

| Nom | Opérateur | Exemple | Résultat |
|:--:|:--:|:--:|--:|
| Égalité | `==` | 2 == 3 | False |
| Différence | `!=` | 2 != 3 | True |
| Inférieur strict | `<` | 2 < 3 | True |
| Inférieur ou égal | `<=` | 2 <= 3 | True |
| Supérieur strict | `>` | 2 > 3 | False |
| Supérieur ou égal | `>=` | 2 >= 3 | False |

</br>

Il existe également des opérateurs qui permettent de relier des booléens entre
eux.

</br>

| Nom | Opérateur | Exemple | Résultat | Commentaire |
|:--:|:--:|:--:|--:|:--|
| Inverse | `not` | not True | False | Renvoie l'inverse de la valeur |
| Et | `and` | True and True | True | Vaut vrai si et seulement si les deux conditions sont vraies |
| Ou | `or` | True or False | True | Vaut vrai si au moins une des conditions est vraie |

{{% /box %}}

{{% box type="exercise" title="Mission 4 : Le menu" %}}

Après avoir calculé ton argent poche, tu peux enfin découvrir le menu ! Vu que
tu as énormément faim, tu souhaites prendre une entrée, un plat et un dessert !
Cependant, il ne faut pas que le prix du repas excède la valeur de ton
porte-monnaie !

</br>

Pour vérifier cela, utilise tes nouvelles compétences pour vérifier si tu peux
payer tout le repas ! Affiche *"J'ai faim, allons-y !"* si tu as assez d'argent
pour le repas, *"Je n'ai pas assez d'argent..."* sinon. Tu devras réutiliser ton
dernier code afin de récupérer la valeur de ton porte-monnaie.

</br>

| Plat | Prix en € |
|:--:|--:|
| Entrée : fromage | 3.99 € |
| Plat : frites et steak haché | 9.99 € |
| Dessert : tiramisu | 5.49 € |

{{% /box %}}
