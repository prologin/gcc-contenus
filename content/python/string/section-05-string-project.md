# Projet : jeu du Pendu

Sachant à présent utiliser les string et leurs méthodes, il nous est possible de s'amuser avec un nouveau jeu : **le Pendu !**

Le principe du Pendu est simple : Tenter de deviner le mot secret en entrant des lettres une par une au clavier. Mais attention à ne pas gaspiller ses coups, car si trop de choix sont erronés le personnage sera pendu !

{{<figure src="resources/images/icon.png" height=200 caption="">}}

## Initialisation du pendu

Tout d'abord nous devons définir le mot que le joueur va devoir deviner.

Nous pouvons écrire la chaîne de caractères dans une variable `solution`.

Ensuite nous devons définir combien de chances, de tentatives à le joueur, avant d'être pendu. On peut créer une variables `tentatives` avec la valeur `7` par exemple.

{{<figure src="resources/images/pendu-7-tentatives.png" height=120 caption="">}}

Enfin, nous allons créer la variable représentant les lettres découvertes par le joueur.
Nous pouvons définir une liste `mot` dont la taille est égale au nombre de caractères de `solution`, et tous les éléments sont égaux à `_` pour le moment. Chaque `_` représentant une lettre à remplacer.

## Affichage du mot découvert

Pour aider le joueur, nous allons afficher le mot contenant les lettres déjà découvertes, dans le format : _ _ _ _ _ _ _ (ou plus, si vous avez défini un mot `solution` plus long).

Nous avons stocké les lettres découvertes par le joueur sous forme de liste, ainsi nous pouvons utiliser la fonction `join()` pour créer rapidement une chaîne avec chaque élément de la liste, séparé par un caractère précis.

Il ne reste plus qu'à afficher cette chaîne !

## Lettre entrée par le joueur

Le joueur voyant à présent quelle chaîne de caractères il doit trouver, celui-ci peut proposer des lettres pour la découvrir.

Comme vu dans les TP précédents, la fonction `input()` permet de demander à l'utilisateur d'entrer un mot, une phrase, etc.

Voulant qu'une seule lettre, nous pouvons récupérer la chaîne de caractère entrée par le joueur et en extraire la première lettre que l'on peut stocker dans une variable `proposition`.

On peut également la mettre en miniscule ou majuscule, suivant ce qu'on a choisi pour la chaîne `solution`.

## Bonne ou mauvaise lettre ?

Le joueur ayant fait sa partie, nous devons faire la nôtre : lui indiquer si la lettre proposée est correcte, si elle appartient au mot à deviner.

Pour cela, nous devons tester si la lettre `proposition` est présente dans la chaîne de caractère `solution`. Quel mot-clé il faut utiliser déjà ?

Si elle est présente, nous pouvons le féliciter.
Sinon, il faut lui dire de retenter sa chance et nous pouvons réduire le nombre de tentatives disponibles (`tentatives`).

## Découverte de la lettre dans `mot`

Mettons-nous dans le cas où la lettre `proposition` est effectivement dans la chaîne `solution`, nous devons à présent modifier la liste `mot` pour refléter les lettres découvertes par le joueur.

Donc, nous devons changer chaque élément de la liste `mot` si le caractère correspondant dans la chaîne `solution` est égal à la lettre `proposition`.

Pour cela, nous pouvons utiliser une boucle `for` en utilisant l'index dans la chaîne.

Ensuite, nous comparons la lettre dans `solution` avec `proposition`.

Si elle est égale, nous pouvons changer l'élément dans la liste `mot` avec la lettre trouvée.

## Boucle de jeu

Félicitations ! Nous avons mis en place tout le principe du jeu du pendu !

Bon, par contre, il demande qu'une seule fois la lettre proposée pour le moment, pas facile de gagner dans ces conditions.

Ce que nous pouvons rajouter c'est une boucle pour répéter certaines actions plusieurs fois.

Quelles actions souhaitons-nous répéter ?

Combien de fois voulons-nous les répéter ? Ou à quel moment voulons-nous arrêter la répétition ?

Plutôt une boucle `for` ou une boucle `while` ?

Pour rappel, nous avons défini une variable `tentatives` qui représente le nombre d'erreurs possibles pour les propositions du joueur, avant que celui-ci ne perde.

On sait également que la liste `mot` commence avec des `_`, mais qu'au fur et à mesure, ceux-ci sont remplacés par des lettres.

## Gagné ou perdu ?

Affichons au joueur à la fin de la partie (donc après la fin de la boucle), si celui-ci a gagné ou perdu !

Comment tester si le joueur a gagné ? Est ce qu'on arrête bien la boucle dans ce cas-là ?

Comment savoir lorsque le joueur a perdu ? Le jeu s'arrête bien ?

## Affichage du pendu

Est ce vraiment un jeu du pendu, si nous n'affichons jamais le pendu ? 👀

Nous vous proposons cet affichage :
```text
 ==========Y=
 ||/       |
 ||        0
 ||       /|\
 ||       /|
/||
==============
```

Il est possible de l'afficher ligne par ligne en fonction du nombre d'erreurs, ou de rajouter les parties du personnage au fur et à mesure.

## Conclusion

Félicitations ! 🎉 C'est la fin de ce projet de Pendu, et du TP sur les string.

Qu'en as-tu pensé ? Plutôt facile ? Difficile ?

Donne ton avis aux organisateurs pour qu'on continue d'améliorer les TP !