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

## Choix du mode de jeu

{{% box type="exercise" title="Exercice 8 : Le mode de jeu" %}}

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

{{% /box %}}

## Ton choix

En ce qui concerne ton propre choix, tu n'as rien besoin de changer.

## Choix de l'ordinateur

{{% box type="exercise" title="Exercice 9 : Le choix de l'ordinateur" %}}

Tu vas d'abord devoir initialiser `choix_adversaire` à 0 pour qu'on puisse
y accéder par la suite.

Pour le choix de l'ordinateur, une toute petite modification est nécessaire.
En effet, le `micro:bit` doit faire un choix seulement si le programme est en
mode _local_.

{{% /box %}}

## Choix de l'adversaire

Si le mode choisi est _multijoueur_, juste après avoir fait notre choix,
nous allons devoir l'envoyer à l'adversaire, et recevoir le sien.

### Activons la radio

{{% box type="info" title="Activer et configurer la radio" %}}

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

{{% /box %}}

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

{{% box type="exercise" title="Exercice 10 : Le message de l'adversaire" %}}

Nous voulons donc que tant qu'aucun message n'est reçu, on envoie notre choix
et on essaye de recevoir celui de l'adversaire.

{{% /box %}}

Ton code concernant cette partie devrait ressembler à ça :

```python
message_adversaire = None

while message_adversaire == None:
    # TODO: Recevoir un message et le stocker
    # dans `message_adversaire`
    

    # TODO: Envoyer le choix du joueur
    
```

### J'ai reçu son choix !

{{% box type="exercise" title="Exercice 11 : Le choix de l'adversaire" %}}

Une dernière étape pour ce qui concerne le multijoueur est de convertir le choix
de l'adversaire en nombre entier et le stocker dans la variable `choix_adversaire`
afin de pouvoir l'utiliser par la suite.

Une fois que l'utilisation de la radio est terminée, pense à l'éteindre avec la
fonction :

```py
radio.off()
```

{{% /box %}}

## Afficher le résultat

Tu n'as normalement pas besoin de modifier la fin de ton code, il devrait
afficher correctement ton choix et celui de l'adversaire.

Si jamais tu as une question ou un problème, n'hésite pas à demander de l'aide
aux organisateurs.

# C'est la fin

Bien joué, tu as réussi à faire un mode _multijoueur_ dans ton programme !
