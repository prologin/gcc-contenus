# Les fonctions de contrôle du `micro:bit`

Comme tu l'as vu plus tôt, il existe des fonctions qui permettent de contrôler
le `micro:bit`. Nous allons ici te présenter les principales.


## Allumer des LEDs

Il existe de nombreuses façons d'afficher quelque chose sur l'écran du
`micro:bit`. La première, et la plus basique, consiste à choisir les LEDs que
l'on veut allumer et à les allumer une par une. 

{{<figure src="resources/images/leds.gif" width=400 caption="LEDs qui s'allument">}}

Pour cela, tu l'as vu juste avant, on utilise la
fonction `display.set_pixel(colonne, ligne, intensite)`, où : 

- `colonne` représente le numéro de la colonne de la LED à allumer
- `ligne` représente le numéro de la ligne de la LED à allumer
- `intensite` représente l'intensité avec laquelle la LED va s'allumer (de 0
pour éteindre la LED à 9 pour l'allumer à pleine puissance). 

Voici un petit exemple de l'utilisation de la fonction :

```python
# Importe les fonctions pour le micro:bit
from microbit import *

# Allume le pixel de la 4ème colonne et 2ème ligne à une intensité de 9
display.set_pixel(4, 2, 9)
```

Si tu essayes d'envoyer ce code vers le `micro:bit`, tu devrais avoir ce
résultat :

{{<figure src="resources/images/microbit_coordinates.png" width=400 caption="Coordonnées des LEDs">}}

Comme tu peux le remarquer avec l'image ci-dessous, les lignes et les colonnes
sont numérotées entre 0 et 4 !

<br>

{{% box type="exercise" title="Mini-mission 1 : Dessiner un coeur" %}}

Pour savoir si tu as bien compris cette partie, dessine nous un cœur !

_Ça devrait ressembler à quelque chose comme ça :_
{{<figure src="resources/images/empty_heart.png" width=400 caption="">}}
{{% /box %}}

## Les images

Pour afficher des images et des symboles déjà existants, on utilisera cette
fonction : `display.show(Image.NOM_IMAGE)`, où `NOM_IMAGE` est le nom anglais
d'une image pré-enregistrée. Tu peux trouver la liste des images
pré-enregistrées [ici](https://microbit-micropython.readthedocs.io/fr/latest/tutorials/images.html).

Voici à quoi ressemblent les images `HEART` et `HAPPY` :

{{<figure src="resources/images/microbit_images.png" width=600 caption="`Image.HEART` et `Image.HAPPY`">}}

{{% box type="exercise" title="Mini-mission 2 : Afficher une image" %}}

Pour cette mission, nous voudrions que tu affiches un Pacman !

{{% spoiler %}} Tu peux retrouver l'image Pacman avec `Image.PACMAN` ! {{% /spoiler %}}
{{% /box %}}

## Et le texte ?

{{% box type="info" title="Les chaînes de caractères" %}}

Mais d'abord, il faut comprendre comment ton ordinateur fait la différence entre
ton code et du texte que tu voudrais afficher. Ce n'est pas compliqué ! Il
suffit de mettre ton texte entouré par des guillemets (`"`). Ce texte est appelé
**chaîne de caractères**. Nous reviendrons dessus plus en détails par la suite.
Voici un exemple de chaîne de caractères : `"Je suis Joseph Marchand !"`.

{{% /box %}}

La fonction pour afficher du  texte sur l'écran s'appelle
`display.scroll(message)`, où `message` est la chaîne de caractères que tu veux
afficher.

```python
# Importe les fonctions pour le micro:bit
from microbit import *

display.scroll("Je suis Joseph Marchand !")
```

<br>

{{% box type="exercise" title="Mini-mission 3 : Afficher du texte" %}}

À ton tour ! Affiche ton prénom sur l'écran du `micro:bit`.

{{% /box %}}

---

<br>

{{% box type="warning" title="Beaucoup d'informations !" %}}

Nous avons vu beaucoup de choses nouvelles jusqu'ici. Si jamais tu as une
question ou si tu n'as pas compris quelque chose, n'hésite surtout pas à
demander de l'aide à un organisateur. N'hésite pas non plus à relire les parties
que tu n'as pas comprises.

{{% /box %}}

{{% box type="exercise" title="Mission 1 : Salut Joseph !" %}}

Max, un ami de Joseph, te demande de créer un programme
pour que son `micro:bit` affiche une barre de chargement sur la ligne du milieu (en allumant simplement les LEDs de la 3e ligne une par une), 
puis affiche le message `"Salut Joseph !"` suivi d'un smiley qui sourit. 
{{% /box %}}

