---
show_toc: true
---

# Le jeu du Pendu

Avec toutes tes nouvelles connaissances sur les chaînes de caractères, il est
temps de passer au projet ! Nous allons recréer le **jeu du Pendu** !

Le but du jeu est de **trouver** un mot secret en entrant petit à petit les
lettres du mot. Cependant, le nombre de **tentatives** est limité, jusqu'à ce
qu'un pendu est dessiné.

{{<figure src="resources/images/icon.png" height=200 caption="">}}

{{% box type="warning" title="Créer un fichier pour le projet" %}}

Avant de commencer, nous te conseillons de **créer un fichier** pour ton projet
du *jeu du Pendu*. Tu pourras alors le lancer à la fin pour tester et jouer à
ton propre jeu !

{{% /box %}}

## Partie 1 : Initialiser le jeu

Afin de pouvoir jouer, il nous faut d'abord créer différentes variables pour
notre jeu : le mot à deviner, la partie actuelle et le dessin qui s'affiche
petit à petit, représentant le nombre de vies restantes.

{{<figure src="resources/images/pendu-7-tentatives.png" height=120 caption="Dessins représentant le nombre de vies restant">}}

{{% box type="exercise" title="Créer les différents dessins du pendu" %}}

Afin de t'aider, nous te proposons une liste de dessins du pendu. Les éléments
de la liste correspondent au nombre de tentatives restantes au joueur. Nous allons
appeler cette liste `pendu`.

```python
["\n===========Y=\n ||/\n ||\n ||\n ||\n/||\n==============\n", "\n===========Y=\n ||/       |\n ||\n ||\n ||\n/||\n==============\n", "\n===========Y=\n ||/       |\n ||        0\n ||\n ||\n/||\n==============\n", "\n===========Y=\n ||/       |\n ||        0\n ||       /|\n ||\n/||\n==============\n", "\n===========Y=\n ||/       |\n ||        0\n ||       /|\\\n ||\n/||\n==============\n", "\n===========Y=\n ||/       |\n ||        0\n ||       /|\\\n ||       /\n/||\n==============\n", "\n===========Y=\n ||/       |\n ||        0\n ||       /|\\\n ||       / \\\n/||\n==============\n"]
```

Il est totalement normal que tu ne comprennes pas trop les différents dessins
d'un premier coup d'oeil. Tu peux essayer d'en afficher un en utilisant
l'opérateur `[]`.

{{% /box %}}

{{% box type="exercise" title="Créer le mot solution" %}}

Tu vas devoir créer une variable `solution` qui correspond au **mot à trouver**.
Ce mot doit contenir seulement des lettres minuscules. On te laisse libre cours
à ton imagination !

{{% /box %}}

{{% box type="exercise" title="Créer la liste pour la partie" %}}

Par la suite, nous allons utiliser une liste `partie` qui correspond à
l'**avancement actuel** du joueur. Cette liste contient uniquement le caractère
`'_'`. Sa longueur correspondra à la longueur de la liste `solution`. Afin de
créer cette liste, tu peux utiliser l'opérateur `*`.

{{% /box %}}

{{% box type="exercise" title="Créer une variable pour garder le nombre de vies" %}}

On va également créer une variable afin de garder en mémoire le **nombre de vies
restantes** pour le joueur. Au tout début de la partie, la variable `vies` sera
égale à 7.

{{% /box %}}

{{% box type="exercise" title="Accueillir le joueur" %}}

Enfin, pour cette première partie, il faut accueillir comme il se doit le
joueur. Pour cela, tu dois **afficher une phrase** que tu souhaites, comme par
exemple : *"Bienvenue au jeu du Pendu !"*.

{{% /box %}}

## Partie 2 : Créer la boucle de jeu

Afin de pouvoir jouer, nous avons besoin d'une **boucle** qui permettra de
répéter tant que l'on reste en vie.

{{% box type="exercise" title="Créer la boucle de jeu" %}}

La boucle `while` du jeu doit permettre de répéter certaines actions. Deux
conditions sont mises en oeuvre :

- que le caractère `'_'` **existe** dans la liste `partie` ;
- que le nombre de vies soit **supérieur** à 0.

Tu devras également assembler les deux conditions avec le mot-clé `and` pour
vérifier les deux conditions à chaque tour de boucle !

{{% /box %}}

## Partie 3 : Afficher l'avancement actuel et demander une proposition

Dans la boucle `while`, il faut afficher la progression du mot et demander une
proposition de lettre au joueur.

{{% box type="exercise" title="Afficher l'avancement actuel" %}}

Afin d'afficher l'avancement actuel, nous allons utiliser la liste `partie`. Il
faut afficher la liste en **concaténant** les éléments de la liste en utilisant
le caractère `' '`. Tu peux alors utiliser une méthode que l'on a vu
précédemment.

Par la suite, tu peux afficher la phrase *"Mot à deviner : {mot}"*, en
remplaçant `{mot}` par l'avancement actuel sous forme d'une chaîne de
caractères.

{{% /box %}}

{{% box type="exercise" title="Demander une proposition au joueur" %}}

Le joueur peut alors proposer une lettre pour compléter le mot. Ainsi, tu peux
utiliser la fonction `input` pour demander au joueur *"Quelle lettre
souhaites-tu proposer ?"*.

On gardera alors le **premier** caractère de la proposition du joueur dans une
variable que l'on nommera `lettre`.

{{% /box %}}

## Partie 4 : Vérifier si la proposition est dans la solution

Afin de compléter petit à petit le mot, il faut d'abord vérifier si la
proposition de lettre existe dans le mot.

{{% box type="exercise" title="Vérifier si la proposition est dans la solution" %}}

Afin de vérifier si la proposition du joueur existe dans la solution, nous
allons utiliser le mot-clé `if`, pour créer une condition, ainsi que le mot-clé
`in` pour vérifier l'existance dans la variable `solution`.

Si cette condition est vérifiée, on peut alors afficher la phrase suivante :
*"Tu viens de trouver une lettre !"*, en ajoutant un *saut de ligne* à la fin !
Pour rappel, le *saut de ligne* est un caractère spécial !

{{% /box %}}

De plus, si la condition est vérifiée, il faut alors **modifier** l'avancement
du joueur avec la liste `partie`.

{{% box type="exercise" title="Remplacer des caractères dans la liste de la partie" %}}

Pour modifier les bons caractères, on va devoir **parcourir** notre chaîne de
caractères `solution` en utilisant les **indices**. Pour chaque caractère de la 
chaîne, on vérifie, à l'aide d'une **condition** si le caractère actuel **est
égal** à `lettre`.

Si c'est le cas, on remplace l'élément à l'indice `i` de la liste `partie` par
le caractère à l'indice `i` dans la chaîne `solution`.

{{% /box %}}

Cette dernière boucle permet de rajouter toutes les occurences d'une lettre dans
la liste `partie` ; c'est-à-dire que si une lettre est présente plusieurs fois
dans le mot recherché, elle sera ajoutée à toutes les positions où elle se
trouve.

## Partie 5 : Enlever une vie si la proposition n'est pas bonne

Dans le cas où la lettre donnée par l'utilisateur n'est pas dans la solution, il
faut alors enlever une vie au joueur.

{{% box type="exercise" title="Enlever une vie" %}}

Après la condition de la *partie 4*, il nous faut utiliser le mot-clé
correspondant au **sinon** en français. Dans le bloc de code de cette partie, il
faut afficher au joueur *"Tu viens de perdre une vie !"*.

De plus, il faut enlever une vie au joueur, pour cela, tu peux *retirer 1* à la
variable `vies`. Si tu ne te rappelles pas de comment faire ça, n'hésite pas à
revenir sur l'[Introduction à Python](https://tp.girlscancode.fr/python/intro_python/)
ou à demander à un organisateur !

{{% /box %}}

{{% box type="exercise" title="Afficher le pendu" %}}

Après avoir enlever une vie au joueur, il faut lui afficher le pendu
correspondant au nombre de tentatives qu'il reste à l'utilisateur. Pour cela,
nous allons utiliser la liste `pendu` et afficher la chaîne de caractères à
l'indice `7 - vies - 1`.

{{% /box %}}

## Partie 6 : Afficher la solution

Lorsque la partie se termine, il faut afficher au joueur la solution et lui
dire s'il a gagné ou non.

{{% box type="exercise" title="Afficher la solution" %}}

Après la boucle de jeu `while`, il faut afficher au joueur le mot qu'il devait
chercher. Pour cela tu peux afficher cette phrase : *"Le mot à trouver était :
{solution}"*, en remplaçant `{solution}` par la variable solution.

{{% /box %}}

{{% box type="exercise" title="Féliciter le joueur" %}}

En vérifiant si le nombre de vies restantes au joueur est égal ou non à 0, en
utilisant une **condition**, tu peux savoir si l'utilisateur a perdu ou non :

- s'il a perdu, tu peux afficher *"Tu n'as pas pu trouver le mot..."* ;
- s'il a gagné, tu peux afficher *"Bravo, tu as gagné !"*.

{{% /box %}}

À partir de ce moment, ton projet devrait fonctionner ! N'hésite pas à le tester
avec plusieurs mots !

## Bonus

Afin de rendre ton jeu parfait, tu peux lui ajouter quelques fonctionnalités.
Dans cette partie, nous allons t'en proposer quelques unes.

### Choisir un mot aléatoire

Afin de rendre le jeu plus complexe aux personnes qui souhaitent jouer plusieurs
fois à ton jeu, tu peux créer une liste de mots qui pourraient être joués et
choisir de manière aléatoire un mot afin d'y jouer avec.

### Prendre en compte les majuscules dans la solution

Dans le projet actuel, il n'est pas possible d'avoir de majuscules dans la
variable `solution`. Pour résoudre ce problème, il te faut modifier le code
afin de prendre en compte n'importe quelle lettre, qu'elle soit en majuscule ou
non. Pour cela, tu peux utiliser la méthode `lower` sur certaines variables.

### Vérifier si la proposition a déjà été donnée ou non

Le joueur peut actuellement donner plusieurs fois la même lettre. Tu peux créer
une liste qui prend en compte toutes les propositions données par l'utilisateur.
Par la suite, tu peux vérifier, lors de l'utilisation de la fonction `input`, si
la proposition existe déjà dans la liste que tu viens de créer.
