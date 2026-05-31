# Et si...

En programmation, tu voudras parfois qu'un certain bout de code s'effectue
seulement **si** une condition est vraie, ou effectuer un autre bout de code si
cette dernière n'est pas vraie.

Commençons d'abord par regarder des exemples que tu pourrais rencontrer dans la
**vie courante** de l'utilisation des conditions.

{{< gallery steps=3 >}}

{{< gallery-img src="./resources/images/algo-if.webp" desc="Utilisation d'une condition" >}}
{{< gallery-img src="./resources/images/algo-else.webp" desc="Utilisation d'une condition avec une action si elle n'est pas vérifiée" >}}
{{< gallery-img src="./resources/images/algo-elif.webp" desc="Utilisation de plusieurs conditions chaînées" >}}

{{< /gallery >}}

## Avant de continuer...

Avant d'attaquer la suite, il est primordial de comprendre ce qu'est
l'**indentation**. Elle permet de définir des blocs dans notre code.

{{% box info %}}

Chaque ligne avec la même indentation fait donc partie du même bloc.

{{% /box %}}

L'indentation correspond au nombre d'espaces au début d'une ligne et avant une
instruction. Dans l'exemple de code ci-dessous, la première ligne a un niveau d'indentation de **0** tandis que la deuxième ligne à un niveau d'indentation de **1** qu'on représente par 4 espaces.

```python
display.scroll("Coucou") # Ligne qui n'est pas indentée
if True:
    display.show(Image.HAPPY) # Ligne qui est indentée 1 fois
```

Garder l'indentation permet de faire plusieurs instructions dans le même bloc.

Pour créer ces blocs, nous allons utiliser la touche tabulation du clavier.
Elle permet de rajouter 4 espaces en 1 touche. Elle devrait ressembler à ça :

{{<figure src="resources/images/tabulation.webp" width=200 >}}

## Revenons à nos conditions

Pour rendre nos programmes intelligents, nous allons leur dire de faire certaines
instructions, uniquement dans certains cas, du même genre que : "S'il pleut, je
prends un parapluie" ; je prends le parapluie s'il pleut uniquement, pas besoin de
l'avoir s'il fait beau.

En Python, on va poser ce type de questions grâce aux instructions `if`, `elif`
et `else`.

L'instruction `if` (*si* 🇫🇷), que l'on fait suivre
d'une condition que l'on veut tester.  
Elle permet d'exécuter un morceau de code que lorsqu'une condition est vraie.

Pour écrire une condition, la syntaxe est : `if condition:` suivi d'un bloc de
code indenté. Le bloc de code en question sera alors exécuté uniquement si
**condition** est vraie (`True`).

{{<figure src="resources/images/if.webp" >}}

Essaye d'exécuter ce code en cliquant sur le bouton `Run` !

```codepython
# Importe une fonction pour faire de l'aléatoire
from random import randint

# Crée un nombre aléatoire `x` entre 0 et 4
# Les nombres possibles sont 0, 1, 2, 3 et 4
x = randint(0, 4)

# Affiche "Bonjour !" seulement quand `x` est inférieur à 3
if x < 3:
    print("Bonjour !")

# Affiche tout le temps x
print(x)
```

{{% box type="info" title="Qu'est-ce que c'est `randint()` ?" %}}

La fonction `randint()` permet de générer aléatoirement un nombre entre deux
nombres. Par exemple, si tu appelles la fonction avec `randint(1, 4)`, les
nombres possibles seront 1, 2, 3 et 4.

{{% /box %}}

<br>

Un `if` peut être accompagné d'un `else` (*sinon* 🇫🇷) qui exécute un
bloc de code uniquement si la condition du `if` est fausse.

{{<figure src="resources/images/if-else.webp" >}}

Enfin, il y a aussi le `elif` qui est la contraction du *else* et du *if*. Il n'est
exécuté que si sa condition  est vraie et que les conditions précédentes sont
fausses.

{{<figure src="resources/images/if-elif.webp" >}}

Voici un petit exemple pour illustrer :

```python
# Importe les fonctions pour le micro:bit
from microbit import *

toto = 0

if toto < 30:
    display.scroll("Pomme")
elif toto < 50:
    display.scroll("Poire")
elif toto < 80:
    display.scroll("Banane")
else:
    display.scroll("Orange")
```

<br>

{{% box type="exercise" %}}

Essaye de trouver ce que va afficher le programme en remplaçant
la ligne 4 par `toto = 0`, `toto = 42` et `toto = 238`.

{{% /box %}}

{{% box type="warning" %}}

Un `if` n'est pas nécessairement accompagné d'un `else` (ou d'un `elif`).
Dans ce cas, si sa condition est fausse, rien n'est exécuté.

De plus, on peut ajouter autant de `elif` que l'on veut après un `if`.

{{% /box %}}

Si jamais tu as une question ou s'il y a quelque chose que tu n'as pas compris,
n'hésite pas à demander aux organisateurs et organisatrices.
