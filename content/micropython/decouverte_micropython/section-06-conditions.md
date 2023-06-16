# Et si...

## Avant de continuer...

Avant de continuer avec les conditions (je t'explique ça juste
après), je dois t'expliquer une partie importante de la programmation Python :
l'**indentation**. 
L'indentation correspond au nombre d'espaces au début d'une ligne et avant une
instruction. Par exemple, la première ligne ci-dessous a une indentation égale
à **0** (pas d'espace en début de ligne), et la troisième ligne a une indentation
égale à **4** (quatre espaces en début de ligne).

```python
display.scroll("Coucou") # Ligne qui n'est pas indentée
if True:
    display.show(Image.HAPPY) # Ligne qui est indentée
```

L'indentation permet surtout de définir des blocs. Chaque ligne avec la même 
indentation fait donc partie du même bloc.

Avec des blocs indentés de 1, 3 puis 2 espaces, Python a du mal à comprendre ce 
qui se passe. En général, on décale le code de 4 espaces à chaque fois.

```python
display.scroll("Coucou")
if True:
  display.scroll("Ceci")
 display.scroll("est un")
   display.scroll("mauvais")
    display.scroll("exemple")
  display.scroll("d'indentation")
```

Tu peux te demander, comment facilement faire des indentations ? 
Eh bien il te suffit simplement d'appuyer sur la touche `tabulation`. Celle qui
ressemble à ça (c'est la touche juste au dessus de la touche `verrouillage
majuscule`): 

{{<figure src="resources/images/tabulation.png" width=200 >}}

Pour l'instant il te suffit juste de savoir ça, je reviendrai là-dessus juste
après. 


## Revenons à nos conditions

Maintenant que tu sais utiliser des variables et plusieurs fonctions de contrôle
du `micro:bit`, tu vas pouvoir faire réagir ton programme en fonction de toutes
ces données dans cette partie. Eh bien ça tombe bien, car Python sait faire ça grâce
aux instructions `if`, `elif` et `else`. 

L'instruction `if` permet de décider de n'exécuter un morceau de code que
lorsqu'une condition est vraie. Ce sont les mêmes conditions que celles décrites
dans la section "Booléens" de la partie sur les types de variables. 
Pour écrire une condition, la syntaxe est : `if condition:`
suivi d'un bloc de code indenté (il ne faut pas oublier les `:` à la fin de la 
ligne, sinon Python n'arrivera pas à exécuter la condition). Le bloc de code en 
question ne sera alors exécuté que si `condition` s'évalue à `True`. 

Un `if` peut être accompagné d'un `else` qui exécute un bloc de code uniquement 
si la condition du `if` est fausse. Enfin, il y a aussi le `elif` qui est la 
contraction du `else` et du `if`. Le `elif` n'est exécuté que si sa condition 
est vraie et que les conditions précédentes sont fausses.

Voici un exemple simple pour illustrer :

```python
from random import randint
from microbit import *

x = randint(0, 100)  # assigne un nombre aléatoire à x compris entre 0 et 100

if x < 30:
    display.scroll('x est inférieur à 30')
elif x < 50:
    display.scroll('x est supérieur ou égal à 30 et inférieur à 50')
elif x < 80:
    display.scroll('x est supérieur ou égal à 50 et inférieur à 80')
else:
    display.scroll('x est supérieur ou égal à 80')
```

### Mini-exercice
**But :** Essaye de trouver ce que va afficher le programme ci-dessus pour `x =
0`, `x = 42` et `x = 238`. 

*Remarques :*

- Un `if` n'est pas nécessairement accompagné d'un `else` (ou d'un `elif`).
Dans ce cas, si sa condition est fausse, rien n'est exécuté
- On peut ajouter autant de `elif` que l'on veut après un `if`

*Tout est clair ?*

Si jamais tu as une question ou s'il y a quelque chose que tu n'as pas compris,
n'hésite pas à demander aux organisateurs.

### Et les indentations dans tout ça ?

Comme tu as pu le voir dans les codes d'exemples, le _bloc de code_ qui est 
exécuté lorsque la condition du `if` est vérifiée est **indenté**. 
Lorsque l'on sort de la condition, le code perd son indentation. L'indentation 
permet à Python de différencier les `blocs de code` appartenant aux conditions, 
et ainsi de savoir ce qui doit être exécuté ou non.

La partie sur les indentations est une partie très importante car elle ne permet
pas seulement à Python de différencier les blocs de code, mais
aussi de rendre ton code plus clair et plus lisible. 
Si jamais tu as une quelconque question ou s'il y a quelque chose que tu n'as
pas compris, n'hésite pas à faire appel à un organisateur. 

