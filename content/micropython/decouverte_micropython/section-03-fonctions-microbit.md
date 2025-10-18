# Afficher des informations

Dans l'exemple de la partie précédente, on utilisait des commandes
différentes pour chaque action.

{{% box info %}}

Ces commandes sont aussi appelées *fonctions*.

{{% /box %}}

Dans cette partie, on va voir les fonctions qui commencent par `display.`.
Elles correspondent aux fonctions qui servent à afficher quelque chose à
l'écran.

## Allumer des LED

Comme tu as pu le remarquer, au centre du `micro:bit` se trouvent 25 petit
carrés lumineux. Ils sont appelés *LED* (ou pixels).

La première méthode pour afficher quelque chose consiste à choisir une LED sur
l'écran et l'allumer.

{{<figure src="resources/images/leds.gif" width=400 caption="LED qui s'allument">}}

Pour cela, on utilise la
fonction `display.set_pixel(colonne, ligne, intensite)`, où : 

- `colonne` représente le numéro de la **colonne** de la LED à allumer (un nombre de 0 à 4)
- `ligne` représente le numéro de la **ligne** de la LED à allumer (un nombre de 0 à 4)
- `intensite` représente la **luminosité** de la LED qu'on va allumer (un nombre de 0 à 9).

{{% box info %}}

Tu peux éteindre une LED en lui donnant une luminosité de 0.

{{% /box %}}

En programmation, on compte toujours à partir de `0`.
Sur le `micro:bit`, c'est pareil : la première colonne correspond à la colonne `0` ;
de même pour les lignes.

Voici un schéma pour le visualiser :

{{<figure src="resources/images/microbit_coordinates.webp" width=400 caption="Coordonnées des LED">}}

Si on voulait écrire un programme qui allume la même LED que sur le schéma
ci-dessus, voici ce qu'il faudrait écrire :

```python
# Indique qu'on va écrire des commandes pour le microbit
from microbit import *

# Allume la LED de la 4ème colonne et 2ème ligne à une intensité de 9
# car on commence à compter à partir de 0
display.set_pixel(4, 2, 9)
```

{{% box type="exercise" %}}

Pour savoir si tu as bien compris cette partie, dessine nous un cœur !

_Ça devrait ressembler à quelque chose comme ça :_
{{<figure src="resources/images/empty_heart.webp" width=400 caption="">}}
{{% /box %}}


## Tout éteindre

Comme tu peux le voir, une fois les LED allumées, elles ne s'éteignent jamais.
Tant que le `micro:bit` reste branché, les LED resteront allumées.

Pour éteindre 1 LED, tu peux mettre l'intensité dans la fonction `set_pixel` à 0.

Pour éteindre toutes les LED d'un coup, tu peux utiliser la fonction `clear` :

```python
# Indique qu'on va écrire des commandes pour le microbit
from microbit import *

# Éteint le pixel au milieu du micro:bit
display.set_pixel(2, 2, 0)

# Éteint toutes les LED
display.clear()
```


## Les images

Pour afficher des images et des symboles déjà existants, on utilisera cette
fonction : `display.show(Image.NOM_IMAGE)`, où `NOM_IMAGE` est le nom anglais
d'une image pré-enregistrée. Tu peux trouver la liste des images
pré-enregistrées [ici](https://microbit-micropython.readthedocs.io/fr/latest/tutorials/images.html).

Voici à quoi ressemblent les images `HEART` et `HAPPY` :

{{<figure src="resources/images/microbit_images.webp" width=600 caption="`Image.HEART` et `Image.HAPPY`">}}

```python
# Indique qu'on va écrire des commandes pour le micro:bit
from microbit import *

# Affiche l'image HEART
display.show(Image.HEART)
```

{{% box type="exercise" %}}

Cette fois-ci, affiche une image de PACMAN !

{{% /box %}}

## Ça va trop vite...

Si l'on souhaite afficher une première image, puis une autre,
sur le `micro:bit`, il suffit de mettre les 2 lignes à la suite :

```python
# Indique qu'on va écrire des commandes pour le microbit
from microbit import *

# Affiche l'image HEART
display.show(Image.HEART)
# Affiche l'image HAPPY
display.show(Image.HAPPY)
```

Sauf que l'exécution de ces 2 lignes est beaucoup trop rapide !
Le `micro:bit` affiche la 1ere image en 1 milliseconde, puis la deuxième.
Ce qui est pas suffisant pour qu'on puisse nous-même apercevoir l'image.

Tu peux dire au `micro:bit` d'attendre un certain temps avec la commande
`sleep(TEMPS)`, avec `TEMPS` un nombre de millisecondes.

```python
# Indique qu'on va écrire des commandes pour le microbit
from microbit import *

# Attends 2 secondes
sleep(2000)
```

{{% box type="exercise" %}}

Copie le code qui affiche les images et ajoute une ligne de code entre les 2 affichages,
pour attendre 1 seconde (soit 1000 millisecondes).

{{% /box %}}


## Et le texte ?

Pour afficher du texte à l'écran, on utilise la fonction
`display.scroll(message)`, où `message` est le texte que tu veux
afficher.

```python
# Indique qu'on va écrire des commandes pour le microbit
from microbit import *

display.scroll("Les stages Girls Can Code! c'est trop bien !")
```

Le code ci-dessus devrait afficher "Les stages Girls Can Code! c'est trop bien !"
sur ton `micro:bit`. N'hésite pas à lui envoyer pour voir ce que ça donne !

{{% box type="info" title="Texte ou commande ?" %}}

Pour que le `micro:bit` fasse la différence entre les commandes et le
texte à afficher, il faut le mettre entre guillemets :

```py {nocopy=true}
display.scroll()   # Ceci est une commande
"display.scroll()" # Ceci est du texte
```

Ce texte peut aussi être appelé **chaîne de caractères**.

{{% /box %}}

{{% box type="exercise" %}}

Affiche ton prénom sur l'écran du `micro:bit`.

{{% /box %}}

## Le défi de Lily

Lily veut écrire un programme pour son propre `micro:bit`.

Elle a besoin d'afficher une barre de chargement sur la ligne du milieu
(en allumant les LED de la 3ème ligne une par une), puis d'écrire le message
`"Bonjour Prologin !"` suivi d'un smiley qui sourit.

Mais elle ne sait pas comment l'écrire, et aimerait que quelqu'un l'aide.

{{% box type="exercise" %}}

Écris le programme de Lily.

{{% /box %}}
