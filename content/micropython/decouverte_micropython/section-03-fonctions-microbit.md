# Les fonctions de contrôle du `micro:bit`

Comme tu l'as vu plus tôt, il existe des fonctions qui permettent de contrôler
le `micro:bit`. Nous allons ici te présenter les principales.


## Allumer des LEDs

Il existe de nombreuses façons d'afficher quelque chose sur l'écran du `micro:bit`.
La première, et la plus basique, consiste à choisir les LEDs que l'on veut allumer
et à les allumer une par une. 
Pour cela, tu l'as vu juste avant, on utilise la
fonction `display.set_pixel(colonne, ligne, intensite)`, où : 
- `colonne` représente le numéro de la colonne de la LED à allumer
- `ligne` représente le numéro de la ligne de la LED à allumer
- `intensite` représente l'intensité avec laquelle la LED va s'allumer (de 0
pour une LED éteinte à 9 pour une LED allumée à pleine puissance). 

En ce qui concerne cette fonction, voici un petit schéma qui permet de mieux 
comprendre les coordonnées de chaque LED (la coordonnée **X** correspond au
numéro de **colonne** et la coordonnée **Y** correspond au numéro de **ligne**) :

{{<figure src="resources/images/microbit_coordinates_bis.png" width=400 caption="Coordonnées des LEDs">}}


### Mini-exercice
**But :** Affiche un coeur sur l'écran.

_Ça devrait ressembler à quelque chose comme ça :_
{{<figure src="resources/images/empty_heart.png" width=400 caption="">}}


## Les images

Comme tu as pu le constater, c'est assez long et fastidieux d'afficher quelque
chose de complexe avec la fonction précédente. Pour nous faciliter la vie, il
existe quelques autres fonctions, et une en particulier qui est faite pour
afficher des images et des symboles : `display.show(Image.NOM_IMAGE)`, où
`NOM_IMAGE` est le nom anglais d'une image pré-enregistrée. 
Tu peux trouver la liste des images pré-enregistrées
[ici](https://microbit-micropython.readthedocs.io/fr/latest/tutorials/images.html).

Voici à quoi ressemblent les images `HEART` et `HAPPY` :

{{<figure src="resources/images/microbit_images.jpg" width=600 caption="`Image.HEART` et `Image.HAPPY`">}}

### Mini-exercice
**But :** Affiche un smiley content sur l'écran du `micro:bit`.


## Et le texte ?

C'est super, tu sais maintenant comment allumer les LEDs une par une et afficher
une image. Mais comment faire si jamais tu veux afficher un message sur l'écran ?
Et bien la vie est bien faite, puisqu'il existe une fonction pour faire cela.

Mais juste avant, il faut comprendre comment ton ordinateur fait la différence
entre ton code et du texte que tu voudrais afficher. Ce n'est pas compliqué, il
suffit de mettre ton texte entouré par des guillemets (`"`). Ce texte est
appelé `chaîne de caractères`. Nous reviendrons dessus plus en détails par la suite. 
Voici un exemple de chaîne de caractères : `"Je suis Joseph Marchand !"`.

Maintenant, revenons à nos moutons. La fonction pour afficher du 
texte sur l'écran s'appelle `display.scroll(message)`. `message` est la chaîne de 
caractères que tu veux afficher. 

### Mini-exercice
**But :** Affiche le texte de ton choix sur l'écran du `micro:bit`.


## Ça va trop vite !

Une autre fonction bien pratique est la fonction `sleep(millisecondes)` qui
permet, comme évoqué dans la partie "Ton premier programme", de mettre en pause
ton programme pour, par exemple, te laisser le temps de voir ce qu'il se passe. 



Nous avons vu beaucoup de choses nouvelles jusqu'ici. Si jamais tu as une
question ou si tu n'as pas compris quelque chose, n'hésite surtout pas à demander
de l'aide à un organisateur. 

N'hésite pas non plus à relire les parties que tu n'as pas comprises. 
Si jamais tu as besoin, une liste _presque_ exhaustive des fonctions de contrôle
du `micro:bit` est disponible à la toute fin de ce TP. 

### Exercice 1
**But :** Max, qui est un ami de Joseph, te demande de créer un programme
pour que son `micro:bit` affiche une barre de chargement sur la ligne du milieu, 
puis affiche le message `"Salut Joseph !"` suivi d'un smiley qui sourit. 

