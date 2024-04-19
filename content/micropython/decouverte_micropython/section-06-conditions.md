# Et si...

## Avant de continuer...

Avant d'attaquer la suite, il est primordial de comprendre ce qu'est
l'**indentation**. Elle permet de définir des blocs. Chaque ligne avec la même 
indentation fait donc partie du même bloc.

Pour créer ces blocs, nous allons utiliser la touche tabulation sur ton clavier.
Elle permet de rajouter des espaces. Elle devrait ressembler à ça :

{{<figure src="resources/images/tabulation.png" width=200 >}}

L'indentation correspond au nombre d'espaces au début d'une ligne et avant une
instruction. Dans l'exemple de code ci-dessous, la première ligne a un niveau d'indentation de **0** espaces en début de ligne, tandis que la troisième
ligne a un niveau d'indentation de **4** espaces.

```python
display.scroll("Coucou") # Ligne qui n'est pas indentée
if True:
    display.show(Image.HAPPY) # Ligne qui est indentée 1 fois
```

Garder l'indentation permet de faire plusieurs instructions dans le même bloc.

## Revenons à nos conditions

Maintenant que tu sais utiliser des variables et plusieurs fonctions de contrôle
du `micro:bit`, tu vas pouvoir faire réagir ton programme en fonction de toutes
ces données dans cette partie. Eh bien ça tombe bien, car Python sait faire ça
grâce aux instructions **if**, **elif** et **else**. 

L'instruction `if` correspond au mot "si" en français, que l'on fait suivre
d'une condition que l'on veut tester. Elle permet d'exécuter un morceau de code
que lorsqu'une condition est vraie. Ce sont les mêmes conditions que celles
décrites dans la section "Booléens" de la partie sur les types de variables.

Pour écrire une condition, la syntaxe est : `if condition:` suivi d'un bloc de
code indenté. Le bloc de code en question ne sera alors exécuté que si
**condition** s'évalue à *True*, c'est-à-dire qu'elle doit être vraie.

{{<figure src="resources/images/if.png" >}}

Essaye d'exécuter ce code en cliquant sur le bouton `Run` !

```codepython
# Importe une fonction pour faire de l'aléatoire
from random import randint

# Crée un nombre aléatoire `x` entre 0 et 1
x = randint(0, 1)

# Affiche "Bonjour !" seulement quand `x` est égal à 1
if x == 1:
    print("Bonjour !")

# Affiche tout le temps x
print(x)
```

<br>

Un `if` peut être accompagné d'un `else` ("sinon" en français) qui exécute un
bloc de code uniquement si la condition du `if` est fausse.

{{<figure src="resources/images/if-else.png" >}}

Enfin, il y a aussi le `elif` qui est la contraction du *else* et du *if*. Il n'est
exécuté que si sa condition  est vraie et que les conditions précédentes sont
fausses.

{{<figure src="resources/images/if-elif.png" >}}

Voici un petit exemple pour illustrer ce que l'on dit sur les conditions :

```python
# Importe les fonctions pour le micro:bit
from microbit import *

x = 0

if x < 30:
    display.scroll("Pomme")
elif x < 50:
    display.scroll("Poire")
elif x < 80:
    display.scroll("Banane")
else:
    display.scroll("Orange")
```

<br>

{{% box type="exercise" title="Mini-mission 7 : Qu'est-ce que ça va afficher ?" %}}

En remplaçant la ligne 4 par les exemples ci-dessous, essaye de trouver ce que
va afficher le programme ci-dessus pour `x = 0`, `x = 42` et `x = 238`. 

{{% /box %}}

{{% box type="warning" title="Remarques sur les conditions" %}}

Un `if` n'est pas nécessairement accompagné d'un `else` (ou d'un `elif`).
Dans ce cas, si sa condition est fausse, rien n'est exécuté.

De plus, on peut ajouter autant de `elif` que l'on veut après un `if`.

{{% /box %}}

Si jamais tu as une question ou s'il y a quelque chose que tu n'as pas compris,
n'hésite pas à demander aux organisateurs.
