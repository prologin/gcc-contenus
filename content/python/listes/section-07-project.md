---
show_toc: true
---

# Memory

Passons à la pratique en créant notre projet, le jeu *Memory* ! Le but du jeu
est de **former des paires** en retournant deux cartes. Si elles ne sont pas
identiques, on les retourne face cachée. La partie se termine lorsque toutes les
cartes sont découvertes.

{{< figure src="./resources/images/memory-illustration.jpg" caption="Illustration du jeu *Memory*" >}}

{{% box type="warning" title="Créer un fichier pour le projet" %}}

Avant de commencer, nous te conseillons de **créer un fichier** pour ton projet
du *Memory*. Tu pourras alors le lancer à la fin pour tester et jouer à ton
propre jeu !

{{% /box %}}

## Partie 1 : Créer les différentes listes

On va alors utiliser des **listes** pour représenter notre jeu, une liste
`solution`, qui contiendra toutes les cartes du jeu, et une liste `partie`, qui
correspond au statut actuel de la partie avec des cartes cachées et des cartes
découvertes.

{{% box type="exercise" title="Créer la liste solution" %}}

Pour créer notre liste `solution`, sers toi de la liste donnée ci-dessous qui
représente nos différents éléments. Il faudra **concaténer** la liste `solution`
à elle-même pour avoir des paires d'éléments. Pour cela, tu peux utiliser
l'opérateur `*`.

```python
['🦅', '🐶', '🐥', '🐼', '🌹', '🍄']
```

Il faudra également **trier aléatoirement** notre liste `solution` afin d'avoir
un peu plus de challenge.

{{% /box %}}

{{% box type="info" title="Trier aléatoirement les éléments d'une liste" %}}

Pour **trier aléatoirement** les éléments d'une liste, on va utiliser la
fonction `shuffle` de la bibliothèque `random`.

```codepython
# Importe la fonction `shuffle`
from random import shuffle

# Crée une liste `ma_liste`
ma_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Trie de manière aléatoire la liste
# `ma_liste`
shuffle(ma_liste)

# Affiche `ma_liste`
print(ma_liste)
```

{{% /box %}}

Afin de suivre en temps réel notre partie, nous allons utiliser la liste
`partie`. Au tout début de la partie, toutes les cartes sont face cachée. Pour
représenter les cartes face cachée, on va utiliser le caractère `'X'`.

{{% box type="exercise" title="Créer la liste de la partie" %}}

Ton but est de créer la liste `partie` qui représentera l'avancement actuel de
la partie. Sa longueur correspondra à la longueur de la liste `solution` et sera
composée uniquement de caractères `'X'`. Tu peux utiliser l'opérateur `*`.

Pour terminer, on souhaite **afficher** la liste `partie`.

{{% /box %}}

## Partie 2 : Créer la boucle de jeu

Afin de pouvoir jouer, nous allons **répéter** plusieurs actions, notamment la
demande au joueur des indices des cartes qu'il souhaite retourner. On va alors
utiliser une **boucle** `while`.

<details>
<summary>Clique ici pour avoir un rappel sur les boucles while</summary>

La boucle **while** (*tant que* 🇫🇷) est une boucle dont le bloc de code est
répété **tant qu'une condition est vérifiée**. On l'écrit similairement à des
conditions `while condition:`.

```codepython
entree = input("Quel jour est-il ?")

# Demande une entrée tant que la réponse
# n'est pas égale à "Vendredi"
while entree != "Vendredi":
    print("Tu n'as pas donné la bonne réponse !")
    entree = input("Quel jour est-il ?")

# Est affiché après avoir rentré "Vendredi"
print("C'est vendredi, on fête le vendredi ! Tout le monde est impatient d'être au week-end !")
```

</details>

</br>

{{% box type="exercise" title="Créer la boucle de jeu" %}}

Tant qu'il reste des caractères `'X'` (des cartes cachées) dans la liste
`partie`, nous allons continuer à jouer. À partir de cette information, essaye
de créer la boucle `while` ! Tu devras utiliser le mot-clé `in` !

{{% /box %}}

## Partie 3 : Demander les indices pour découvrir les éléments

Afin de découvrir les cartes, nous allons demander au joueur de **choisir deux
indices** dans les listes afin de former des paires.

{{% box type="exercise" title="Demander les indices pour découvrir les éléments" %}}

Pour demander à l'utilisateur des indices, nous allons utiliser la fonction
`input`. Tu peux demander avec la question suivante : "Quel indice souhaites-tu
jouer ?" et mettre la réponse dans la variable `choix1` en transformant la
sortie en nombre avec la fonction `int`.

Par la suite, il faut récupérer la carte sélectionnée dans la liste `solution`
en fonction de l'indice `choix1` et la placer dans la liste `partie` à la même
position.

Enfin, tu peux afficher la liste `partie` pour voir l'avancement du jeu.

Afin de t'aider, voici un petit algorithme récapitulant tous les éléments à
faire dans cette partie :

{{< figure src="./resources/images/algo-project.png" caption="Algorithme pour partie 3" >}}

Il faut maintenant faire la même chose pour le deuxième choix, en remplaçant
`choix1` par `choix2`.

{{% /box %}}

## Partie 4 : Vérifier que les cartes sont différentes

Le but du jeu est de former des paires afin de découvrir toutes les cartes. Si
les deux cartes tirées ne sont pas les mêmes, il faut alors cacher les cartes
en question.

{{% box type="exercise" title="Vérifier que les cartes sont différentes" %}}

En utilisant une **condition**, il faut vérifier si les cartes retournées dans
la liste `partie` sont différentes en utilisant les indices `choix1` et
`choix2`.

Si les cartes retournées sont différentes, il faut remettre dans la liste
`partie` aux positions choisies le caractère `'X'`.

{{% /box %}}

## Partie 5 : Afficher une phrase de fin

Après avoir découvert toutes les cartes, il faut féliciter la joueuse.

{{% box type="exercise" title="Afficher une phrase de fin" %}}

Après la boucle `while`, tu peux **afficher** la phrase suivante : "Bravo tu as
gagné !".

{{% /box %}}

Tu devrais à ce moment là avoir un jeu fonctionnel ! N'hésite pas à le tester et
à changer les cartes, si tu le souhaites, par d'autres caractères, des phrases,
des mots, des nombres ou tout ce que tu voudrais !

## Bonus

Il existe quelques améliorations qui sont possibles. N'hésite pas à en choisir
une ou plusieurs si tu le souhaites !

### Compter le nombre de coups

Afin de donner plus de peps à ton jeu, il est possible de **compter le nombre de
coups** faits par la joueuse. Il te faudra alors une variable `coups` qui te
compte le nombre de coups et l'**incrémenter** à chaque tour de la boucle
`while` en utilisant l'opérateur `+=`. Tu peux alors **afficher** le nombre de
coups faits par la joueuse à la fin du jeu.

### Vérifier que les indices ne soient pas impossible

Il est possible que la joueuse soit pas très coopérative et donne des indices
trop élévés. Tu peux alors ajouter une **condition** qui vérifie si les indices
proposés ne sont pas en dehors des listes `solution` et `partie`.

### Proposer plusieurs listes pour jouer

Il est possible de proposer, avant le début du jeu, différents choix de
cartes à découvrir avec par exemple une liste `solution` d'animaux, de pays,
de prénom ou autres...
