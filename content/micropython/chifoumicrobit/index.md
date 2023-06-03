---
title: Chifoumicro:bit
authors: ["Grégoire 'greg' Lefaure", "Clément 'swarwerth' Nguyen"]
subtitle: "Apprenez à coder un chifoumi sur un micro:bit"
date: 2022
weight: 15
code_stub_url: ./resources/given_resources/chifoumicrobit.py
---

# Introduction au sujet...

Notre ami **Skeleton** le squelette était en train de jouer à son jeu préféré,
[Pacman](https://fr.wikipedia.org/wiki/Pac-Man). Il a voulu mettre en pause
le jeu, mais, en cliquant sur le bouton, il a été téléporté dans l'univers du jeu.

En arrivant, il croise **Pacman** et le fantôme **Bouh** qui s'ennuyaient. Skeleton
leur propose de faire un chifoumi revisité... mais ils n'ont pas de mains,
donc ils ne peuvent pas mimer les symboles ! Skeleton a besoin de ton aide !
Il te demande de créer un programme leur permettant de jouer sur des `micro:bit` !
Peux-tu aider notre ami ?

Skeleton souhaiterait choisir un élément parmi trois choix sur un
`micro:bit` à l'aide des boutons. De plus, l'ordinateur devra ensuite choisir
à son tour un élément. Enfin, il faudra afficher le résultat. Les choix
seront les suivants : Skeleton, Pacman et Bouh !

Skeleton, faisant peur à Pacman, l'emporte contre lui. Pacman, quant à lui,
mange des fantômes, il gagne en toute logique contre Bouh. Bouh le fantôme voudra attraper
Skeleton, il gagnera donc contre notre ami le squelette.

{{<figure src="resources/images/all3.png" height=80% width=100% alt="Images des personnages sur micro:bit">}}

Pour faire cela, nous allons t'aider à créer le code étape par étape.
Si tu as des questions particulières, n'hésite pas à demander à un
organisateur autour de toi, ils sont là pour ça !

[SECTION-BREAK]

# Passons à la pratique !

Nous t'invitons d'abord à télécharger le code source à modifier en cliquant
sur le bouton `Code à compléter` en haut de la page ! Tu retrouveras dans
le fichier donné un code non complet que tu ne peux pas encore lancer.

Différentes parties du code sont manquantes ! Elles sont désignées par le mot-clé
`TODO` qui se traduit par "À faire" en français. Tout au long du sujet, tu vas
pouvoir compléter le code en écrivant juste en dessous des commentaires
(les lignes de code commençant par un `#`).

## Les possibilités d'affichage

Au début du code donné, tu trouveras la variable `possibilites`, tu vas devoir
t'en servir pour stocker les trois images que l'on veut pouvoir afficher :
`Image.SKULL`, `Image.PACMAN` et `Image.GHOST`. Cependant, il nous faut trouver
une manière pour stocker trois valeurs dans une seule variable. Pour cela, tu
vas utiliser ce qu'on appelle une liste.

{{% box type="info" title="Mais comment construit-on une liste en Python ?" %}}

Lorsqu'on veut stocker de nombreuses valeurs pour pouvoir les réutiliser
par la suite, on utilise des listes. Elles vont nous permettre de stocker
plusieurs valeurs dans une seule variable.

{{<figure src="resources/images/liste.png" height=80% width=80% alt="Liste en Python">}}

Par exemple,

```python
# Liste de lettres
ma_liste_lettres = ["a", "b", "c", "d"]
```

Tu peux accéder aux éléments d'une liste à l'aide de l'indice. Ce sont des nombres
qui désignent l'emplacement de la case que tu veux regarder. Attention,
en programmation, les indices commencent à 0. Si on nomme la longueur de la liste `l`,
les indices peuvent prendre des valeurs entre `0` et `l - 1`.

En Python, pour accéder à un élément à l'indice 2, tu peux faire comme ceci :

```codepython
# Liste de lettres
ma_liste_lettres = ["a", "b", "c", "d"]

# `ma_variable` est l'élément à l'indice 2 de `liste` ("c")
ma_variable = ma_liste_lettres[2]

# Affiche `ma_variable` dans la console
print(ma_variable)

# `longueur` est la longueur de la liste `ma_liste_lettres`
# et on l'affiche
longueur = len(ma_liste_lettres)
print(longueur)
```

{{% /box %}}

Tu vas devoir également trouver la longueur de ta liste `possibilites`. Pour
cela, sers-toi de la fonction `len`. Tu dois mettre ce nombre dans la variable
`NB_POSSIBILITES`.

[SECTION-BREAK]

## La boucle du jeu pour la sélection du personnage

### La condition de la boucle

L'utilisateur du `micro:bit` doit choisir son personnage. Pour faire cela,
on va utiliser une boucle `while` (tant que). Il va falloir alors trouver
une condition pour rester dans la sélection. Pour valider, le joueur devra
appuyer sur les deux boutons du `micro:bit` en même temps.

Dans la condition de ta boucle, il faut vérifier si les boutons A et B ne
sont pas pressés. Tu vas devoir alors utiliser le `and` et le `not`, deux mots-clés
utilisés pour les variables booléennes et les conditions.

N'hésite pas à appeler un organisateur si tu ne te souviens plus !

### Afficher le choix du joueur

Tant qu'on reste dans notre boucle `while`, il va falloir afficher le choix
qui est actuellement sélectionné. Pour ce faire, tu peux utiliser la fonction
`display.show()` avec comme paramètre l'image dans la liste `possibilites` à
l'indice du choix du joueur défini par la variable `choix_joueur`.

### Changer de choix

On va utiliser les boutons A et B pour changer de choix. Sachant qu'on a la
variable `possibilites` qui garde nos images et `choix_joueur` qui désigne le
choix du joueur, il ne reste plus qu'à augmenter ou diminuer `choix_joueur` pour
changer notre choix.

Si le bouton A a été appuyé, il faut enlever 1 au nombre désignant le choix du
joueur. Par la suite, sur ce nouveau nombre, il te faut rester dans l'intervalle
des indices de notre liste `possibilites`. Il va alors falloir rajouter un `%`
(modulo) !

{{% box type="info" title="Un modu-quoi ?" %}}

Le modulo, il faut le prendre comme le reste d'une division euclidienne.
Par exemple, quand tu souhaites diviser 5 par 2, tu auras le quotient qui est
égal à 2 et le reste qui est égal à 1.

On va utiliser le même procédé. On ne peut pas accéder au cinquième élément
d'une liste de longueur 3. On va donc revenir à 0 lorsqu'on dépasse la longueur de la liste.

Par exemple, lorsque tu es à l'indice 3 dans une liste de longueur 3 : les indices
possibles sont 0, 1 et 2. On voudrait que revenir à l'indice 0. En Python,
tu peux le faire comme ceci :

```codepython
# Une liste de nombres
ma_liste = [42, 56, 98]

# On est à l'indice 3
mon_indice = 3

# Le nouvel indice est 3 modulo 3 = 0
# car le reste de la division euclidienne de 3 par 3 est égal à 0
mon_nouvel_indice = 3 % 3

# L'élément à l'indice 0 (3 % 3)
mon_element = ma_liste[mon_nouvel_indice]

# Affiche `mon_element`
print(mon_element)
```

{{% /box %}}

Maintenant, tu dois faire la même chose pour le bouton B, seulement,
cette fois-ci, si le bouton B a été appuyé, il faut rajouter 1 au nombre
désignant le choix du joueur. N'oublie pas le modulo !

[SECTION-BREAK]

## Le choix de l'ordinateur

Le choix de l'ordinateur doit se faire de manière aléatoire. La variable
`choix_adversaire` doit correspondre à un indice dans la liste `possibilites`.
Sachant que les éléments d'une liste en Python sont numérotés de 0 à la longueur
de la liste moins 1, il te faudra générer un nombre dans l'intervalle en question.

Pour générer un nombre aléatoire, tu peux utiliser la fonction `randint` du
module `random`. Pour cela, tu peux l'utiliser comme dans l'exemple suivant :

```codepython
from random import randint

# Génère un nombre aléatoire entre 0 et 4
# Les valeurs possibles sont 0, 1, 2, 3 et 4
n = randint(0, 4)

print(n)
```

[SECTION-BREAK]

## Afficher le choix du joueur

Comme pour le début de la boucle, on souhaite réafficher le choix du joueur
après le `display.clear()` qui éteint tous les pixels.

Après l'affichage du texte "VS", tu dois afficher maintenant le choix
de l'adversaire en prenant une image dans la liste `possibilites` à l'indice
`choix_adversaire`.

## Gagnant et perdant

Maintentant qu'on a le choix du joueur et celui de l'adversaire, on peut savoir
qui a gagner et qui a perdu ! Pour ce faire, on va d'abord vérifier s'il y a
égalité entre les deux joueurs.

Il y a égalité entre les deux joueurs dans notre jeu quand le choix de
notre adversaire et le même que le nôtre en vérifiant l'égalité
entre `choix_joueur` et `choix_adversaire`. Dans ce cas, tu dois afficher sur le
`micro:bit` "Egalite !" avec une vitesse d'affichage de 50.

Sinon, s'il n'y a pas égalité, il faut vérifier les conditions pour savoir
si tu as gagné. Attention, tu devras alors afficher "Gagne !" avec une vitesse
d'affichage de 50. Les conditions sont les suivantes :

- Si `choix_joueur` est égal à 0 et `choix_adversaire` est égal à 1
(Skeleton fait peur à Pacman)

- Si `choix_joueur` est égal à 1 et `choix_adversaire` est égal à 2
(Pacman mange Bouh)

- Si `choix_joueur` est égal à 2 et `choix_adversaire` est égal à 0
(Bouh fait peur à Skeleton)

Sinon, si toutes les conditions au-dessus ne sont pas remplies,
cela veut dire que tu as perdu et il faut que tu affiches "Perdu..." avec
une vitesse d'affichage de 50.

{{% box type="info" title="La vitesse d'affichage ?" %}}

La fonction `display.scroll()` de la librairie `micro:bit` va afficher un texte
avec une vitesse de 150 unités de base. Pour modifier cette dernière, tu peux
rajouter un paramètre à la fonction comme dans l'exemple suivant qui va afficher
"Hello World" avec une vitesse de 50 unités.

```python
display.scroll("Hello World", delay=50)
```

Si la valeur du paramètre est inférieure à 150, le texte sera afficher plus
rapidement ; sinon, il sera plus lent.

{{% /box %}}

[SECTION-BREAK]

# Un mode multijoueur ?

Bien joué, tu as terminé la partie principale de ce TP, et tu as maintenant un
chifoumi complètement fonctionnel pour aider notre ami Skeleton. N'hésite pas à
essayer le jeu !
Comme c'est un très bon ami, nous nous sommes dit qu'il serait sympa de lui
ajouter une fonctionnalité surprise : un mode multijoueur.

Avant de commencer cette partie, il faut que ton programme fonctionne et que tu
aies compris tout ce que nous t'avons expliqué plus tôt.
Si tu as une quelconque question ou qu'il y a quelque chose que tu n'as pas
compris, n'hésite pas à demander de l'aide aux organisateurs.

## Un peu de théorie

Pour faire un jeu multijoueur, nous allons avoir besoin de faire communiquer les
`micro:bit` ensemble. Pour ce faire, nous allons utiliser la radio.

Avant tout, comme pour la première partie, il faut importer les fonctions
pré-écrites en ajoutant cette ligne au début de ton fichier :

```py
import radio
```

## Choix du mode de jeu

Pour commencer, nous voulons que Skeleton puisse s'entraîner contre
l'ordinateur, ou bien jouer en multijoueur avec ses amis.
Pour stocker le mode de jeu choisi, nous allons utiliser une variable,
que nous appelerons `multijoueur`.
Cette variable va prendre trois états différents :
- `-1` si le joueur n'a pas encore fait son choix
- `0` si le joueur veut jouer contre l'ordinateur (mode _local_)
- `1` si le joueur veut jouer avec ses amis (mode _multijoueur_)

Par ailleurs, le joueur veut aussi savoir quand est-ce qu'il doit choisir son
mode de jeu. Pour faire ça, il nous suffit d'afficher l'image `Image.SWORD`
(_épée_ en anglais). N'importe quelle image fonctionnerait, le principe est de
montrer au joueur que notre programme attend son choix.

Ensuite, il faut attendre que le joueur fasse son choix et enregistrer son
choix.
Tu peux utiliser une boucle qui s'arrête lorsque le joueur a fait son choix.
Par convention, on dira qu'un appui sur le bouton A activera le mode
_multijoueur_, et un appui sur B activera le mode _local_.

## Ton choix

En ce qui concerne ton propre choix, tu n'as rien besoin de changer.

## Choix de l'ordinateur

Tu vas d'abord devoir initialiser le choix de l'adversaire à 0 pour qu'on puisse
y accéder par la suite.

Pour le choix de l'ordinateur, une toute petite modification est nécessaire.
En effet, le `micro:bit` doit faire un choix seulement si le programme est en
mode _local_.

Si le mode choisi est _multijoueur_, juste après avoir fait notre choix,
nous allons devoir l'envoyer à l'adversaire, et recevoir le sien.

### Activons la radio

Avant de pouvoir envoyer ou recevoir des informations, nous devons allumer et
configurer la radio. Pour ce faire, nous devons l'allumer et choisir un canal
de communication. Un canal de communication, est un peu comme un tunnel. Si les
deux joueurs ont des canaux différents, alors ils ne pourront pas s'entendre.

```py
# Allume la radio
radio.on()

# Configure la radio pour communiquer sur le channel 42
# Tu peux changer 42 par une valeur entre 0 et 83 si besoin
radio.config(channel=42)
```

Pour montrer au joueur que tout s'est bien passé jusqu'ici, tu peux afficher une
image de ton choix (toutes les images sont disponibles
[ici](https://microbit-micropython.readthedocs.io/fr/latest/tutorials/images.html)).


### Envoi et réception du message

Avant de recevoir le message, nous avons besoin d'une variable pour le stocker.
Nous allons nommer cette variable `message_adversaire` par la suite pour s'y
retrouver. Nous allons aussi lui associer une valeur un peu particulière :
`None` (_rien_ en français). Cette valeur veut dire _"Il n'y a rien dans
cette variable"_, tout simplement.

Pour essayer de recevoir un message, il faut faire :

```py
# `message_adversaire` vaudra None si aucun message n'est reçu
message_adversaire = radio.receive()
```

Pour envoyer un message, il faut faire :

```py
radio.send(str(choix_joueur))
```

{{% box type="info" title="C'est quoi ça, `str()` ?" %}}

C'est quelque chose que nous n'avons pas abordé, mais tout de même importante.
En effet, les variables sont _typées_. Cela veut dire qu'elles ne peuvent stocker
qu'un type de valeur : des nombres entiers, du texte, des nombres décimaux...
La fonction `str(entier)` permet simplement de convertir le nombre entier _`entier`_
en texte. Le texte peut être différencié des nombres entiers par la présence
de simple guillemets (`'`) ou double guillemets (`"`).

Par exemple :
```codepython
entier = 12
texte = str(entier)

# Affiche le texte "12"
print(texte)
```

Pour convertir un texte en nombre entier, il faut utiliser la fonction `int()`,
qui fonctionne de la même façon :

```codepython
texte = "12"
entier = int(texte)

# Affiche le nombre entier 12
print(entier)
```

{{% /box %}}

On va devoir convertir nos variables sous différents types pour pouvoir envoyer
nos différents choix entre les deux `micro:bit` et les utiliser.

Cette partie est un peu complexe, si jamais tu n'as pas compris quelque chose,
n'hésite pas à demander de l'aide aux organisateurs.

Nous voulons donc que tant qu'aucun message n'est reçu, on envoie notre choix
et on essaye de recevoir celui de l'adversaire.

### J'ai reçu son choix !

Une dernière étape pour ce qui concerne le multijoueur est de convertir le choix
de l'adversaire en nombre entier et le stocker dans la variable `choix_adversaire`
afin de pouvoir l'utiliser par la suite.

Une fois que l'utilisation de la radio est terminée, pense à l'éteindre avec la
fonction :

```py
radio.off()
```

## Afficher le résultat

Tu n'as normalement pas besoin de modifier la fin de ton code, il devrait
afficher correctement ton choix et celui de l'adversaire.

Si jamais tu as une question ou un problème, n'hésite pas à demander de l'aide
aux organisateurs.

# C'est la fin

Bien joué, tu as réussi à faire un mode _multijoueur_ dans ton programme !
