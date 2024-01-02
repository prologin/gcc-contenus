# Projet : le 21

Après tous ces cours et exercices, on est plutôt à l'aise sur les listes et leur utilisation.

Vient maintenant l'heure de s'amuser avec un projet : **le 21** !

{{<figure src="resources/images/blackjack-jeu.jpg" height=300 caption="Jeu du 21">}}

Le 21 est un jeu de cartes qui consiste à jouer contre la banque. Le but ? **Obtenir un score supérieur à celui du banquier sans dépasser le score de 21**.

L'objectif ultime étant de parvenir à 21 points avec seulement deux cartes : un as et un roi, un as et une reine, un as et un valet ou un as et un 10. C’est cette combinaison gagnante.

## Jeu de cartes

Le 21 peut se jouer avec un ou plusieurs paquets de 52 cartes. Les casinos, pour éviter la triche, ou le comptage de cartes, jouent avec plusieurs paquets.
Le 21 peut se jouer avec un ou plusieurs paquets de 52 cartes. Nous allons ici jouer avec un seul paquet.

Donc la première étape de notre jeu est de définir le paquet de cartes utilisé.
Un paquet de 52 cartes est réparti en 4 couleurs : trèfle, coeur, pique, carreau ; avec des cartes allant de 2 à 10, puis le Valet, la Dame, le Roi, et l'As.

Pour définir une carte dans notre jeu, avec sa couleur et son nom, nous la représenterons sous forme de **tuple** (un couple de valeur)

```codepython
carte = ("2", "Trèfle")
print(carte)
```

Pour accéder aux valeurs contenues dans un couple, on peut utiliser l'opérateur `[]` :
```codepython
carte = ("2", "Trèfle")
print(carte[0]) # 1er élément
print(carte[1]) # 2e élément
```

Ainsi, nous pouvons créer notre "jeu", notre deck de cartes : une liste de cartes, donc une liste de couples.

Les noms des cartes : 2, 3, 4, 5, 6, 7, 8, 9, 10, Valet, Dame, Roi, As

Les couleurs des cartes : Trèfle, Coeur, Pique, Carreau

{{% box type="exercise" title="Deck" %}}

À cette étape, vous devriez avoir dans votre programme, une liste avec toutes les cartes.

{{% /box %}}


## Valeur des cartes

Le 21 est un jeu avec un système de points. Chaque carte a son nombre de points.

Les cartes avec des nombres (2 à 10) ont un nombre de points égal à leur numéro.

Les cartes avec des figures (Valet, Dame, Roi) comptent chacune pour 10 points.

L'As compte pour 11 points. Dans certaines règles, il peut compter pour 1 point, mais nous allons pas l'appliquer dans notre jeu.

Pour accéder rapidement à la valeur des cartes dans notre jeu, nous allons créer une **fonction** qui, à partir d'une carte (un couple nom-couleur), retourne la valeur de la carte.

{{% box type="info" title="Rappel sur les fonctions" %}}

Une fonction est définie avec un nom, des paramètres (facultatif), et une suite d'instructions.

Elles permettent d'effectuer des instructions sans avoir à tout ré-écrire et peuvent s'adapter aux paramètres donnés.

Le mot-clé `def` commence la définition d'une fonction. Il est suivi par le nom de la fonction, puis de parenthèses (avec des paramètres à l'intérieur si besoin)

Le mot-clé `return` permet à la fonction de renvoyer une valeur.

Pour lancer la fonction, il faut l'appeler, avec son nom et des parenthèses (avec paramètres si besoin).

Exemple :
```codepython
def affichage(nombre):
    print(nombre * 2)
    print("Youpi !")

def donne42():
    return 42

print("On commence")
affichage(15)
variable = donne42()
print(variable)
```

{{% /box %}}

Pour notre jeu, nous allons créer la fonction `valeur_carte(carte)` qui à partir de la carte, nous donne son nombre de points.

{{% box type="info" title="Conseils" %}}

- Pour accéder à la première valeur d'un couple : `couple[0]`
- On peut comparer des chaînes de caractères avec l'opérateur `==`
- On peut transformer une chaîne de caractères en entier avec la fonction `int()`. Par exemple : `int("10")`

{{% /box %}}

{{% box type="exercise" title="Valeur des cartes" %}}

À cette étape, vous devriez avoir dans votre programme, une fonction qui retourne la valeur en points d'une carte, pour toute carte du jeu.

{{% /box %}}


## Distribution des cartes

Le 21 est un jeu où le joueur affronte la banque. Il faut donc leur donner des cartes aux 2.

Nous allons créer une liste vide pour chacun, qui représentent leurs mains : `main_joueur` et `main_banque`.

Ensuite, nous mélangeons le paquet de cartes, le deck, avec la fonction `random.shuffle()`.
Pour utiliser cette fonction, nous devons dire au programme de récupérer le module `random` qui contient plusieurs fonctions de générations d'aléatoire.
La fonction `shuffle()` prend en paramètre une liste et la mélange.

Enfin, on retire 2 cartes du paquet, pour les mettre dans la main du joueur, et 2 autres cartes pour les mettre dans la main de la banque.

{{% box type="info" title="Conseils" %}}

Tu peux utiliser les méthodes `pop()` et `append()` sur les listes.

{{% /box %}}

Pour finir, on affiche les cartes du joueur, et uniquement la 1ere carte de la banque (la 2nde doit rester cachée pour le bien du jeu).

## Calcul du score du joueur

Il est possible d'aider le joueur pour son choix futur, en lui affichant le score actuel de sa main.
En effet, il souhaitera piocher une nouvelle carte si son score est faible, mais garder ses 2 cartes si son score est élevé.

Pour cela, nous allons créer une variable `score_joueur` qui va être égale à la somme de la valeur de ses cartes (tu peux utiliser la fonction `valeur_carte` définie précédemment), et l'afficher.

## 21 !

Le jeu peut s'arrêter tout de suite si le joueur possède le graal entre ses mains : le 21 !

Comme dit dans l'introduction, le score optimal pour ce jeu est 21. Il est possible de faire un score de 21 au premier tirage avec un As, et une tête (Valet, Dame, Roi) ou un 10.

Le score étant déjà calculé dans la partie précédente, nous avons juste à comparer celui-ci à 21.

Si le joueur a effectivement un score de 21, nous le félicitons !
Sinon, le jeu continue, avec la prochaine section.

{{<figure src="resources/images/Blackjack21.jpg" height=300 caption="21 points !">}}

## Choix du joueur

Toute la stratégie du jeu est dans cette partie.

Un joueur, ayant un score inférieur à 21, peut demander à la banque de rajouter une ou plusieurs cartes à sa main.

Mais attention ! Si la main du joueur dépasse le score de 21, celui-ci perd la partie.

Ainsi, nous allons demander au joueur ce qu'il souhaite faire, avec la fonction `input` (que l'on a revu dans la partie "Ajout" de ce TP).

Nous allons demander au joueur s'il veut tirer une carte ou ne rien faire, en répondant avec une seule lettre : "c" pour demander une carte, "r" pour ne rien faire.

Si le joueur demande une carte, de la même manière qu'en début de jeu, nous retirons une carte du paquet pour l'ajouter dans sa main.
Nous affichons cette carte au joueur, et ajoutons sa valeur à la variable `score_joueur`, que nous pouvons aussi afficher.

Le score du joueur ayant changé, il est possible que celui-ci dépasse 21. Or 21 est la limite : il faut s'en approcher, sans jamais la dépasser.

Nous allons donc vérifier que le score du joueur n'excède pas 21.
S'il dépasse, le jeu est fini et le joueur a perdu.
Sinon, le joueur peut une nouvelle fois choisir s'il souhaite tirer une carte ou ne rien faire.

Vous pouvez utiliser une boucle pour répéter cette étape, tant que le joueur n'a pas perdu et qu'il demande une carte.

{{<figure src="resources/images/blackjack-3cards.webp" height=300 caption="Le 1er joueur a demandé une carte, les autres non">}}

## Tirage de la banque

Si le joueur est toujours dans la course contre la banque, c'est maintenant à celui-ci de tirer des cartes pour se rapprocher de 21.

Tout d'abord, nous dévoilons la carte restée inconnue du tout premier tirage.

Ensuite, nous calculons le score de la banque avec ses 2 cartes.

Le choix de la banque est simple : s'il a un score inférieur à 17, alors il tire une carte, ou plusieurs si même après un tirage il n'atteint pas à 17.

De même, tu peux utiliser une boucle pour le tirage des cartes de la banque.

## Qui a gagné ?

Enfin, le moment de départager les 2 adversaires !

Si le joueur a un score supérieur à 21, comme dit précédemment, celui-ci perd la partie.

Si c'est la banque qui dépasse 21, alors c'est le joueur qui gagne !

Si les 2 adversaires sont encore en course, nous comparons les scores des participants :
- si le score du joueur est supérieur à celui de la banque, il gagne
- si le score du joueur est égal à celui de la banque, c'est une égalité
- si le score du joueur est inférieur à celui de la banque, il perd

{{<figure src="resources/images/picsou-jackpot.gif" height=300 caption="Félicitations !">}}