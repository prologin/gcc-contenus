---
title: Un piano avec `pygame`
date: 2020
---

# Un piano avec `pygame`

Un des instruments les plus utilisés dans les livres de théorie de la musique
est le *piano*.  Une des raisons de son utilisation pour apprendre la musique
est que le piano est très visuel. En effet, un piano n'est rien de plus qu'une
répétition d'une suite de 12 touches, 7 blanches entremêlées de 5 noires, et
permet donc voir les _cycles_ dans les suites de notes et mieux comprendre le
concept de _gammes_.

Le but de ce sujet est de vous aider à obtenir, à l'aide de `pygame`, un
clavier visuel et sonore afin de pouvoir s'amuser en faisant de la musique.

Si vous suivez bien les instructions dans l'énoncé vous devriez obtenir un
résultat similaire à cette image:

TODO: insérer une image du clavier.

## Théorie de la musique

TODO: expliquer des bêtises sur la musique:

* fréquence
* note
* touche blanche
* touche noire
* octave (cycles)

## Rappels

Afin de nous préparer pour le projet d'aujourd'hui, nous allons revoir certains
éléments qui ont été vu dans les sujets prédents.

### Les types simples

Pour pouvoir mettre en place nous allons avoir besoin de trois types de données
simples:

* les nombres entiers comme `42`, `0` ou `-1`.
* les chaînes de caractères comme `"ordinateur"` ou `"Girl can code!"`.
* les booléens: `True` ou `False`.

### Les variables

Afin de pouvoir manipuler ces données, il nous faut leur donner un nom. On peut
donc assigner ces données à des variables.

Voici quelques exemples d'assignation de variable:

```python

# Des exemples avec des entiers
mon_entier = 42
quarante_trois = mon_entier + 1

# Des exemples avec des chaînes de caractères
premiere_moitie = "J'aime le"
deuxieme_moitie = " Python!"
mon_message = premiere_moitie + deuxieme_moitie

# Des exemples avec des booléens
ceci_est_vrai = True
ceci_est_faux = False
ceci_est_vrai2 = (42 == 42)
ceci_est_faux2 = (mon_entier > quarante_trois)

```

### Les conditions

Au cours de notre programme nous allons devoir effectuer ou non des actions en
fonction d'une condition qui pourra être vraie ou fausse. Par exemple nous
aurons sûrement envie de pouvoir jouer une note musicale si une touche est
appuyée sur le clavier. Pour pouvoir nous pouvons utiliser les mots-clés
suivants: `if`, `elif` et `else`.

Prenez l'exemple suivant:

```python

if condition1:
    corps1
elif condition2:
    corps2
elif condition3:
    corps3
else:
    corps4

```

Le corps1 sera exécuté si condition1 est vraie.

Le corps2 sera exécuté si condition1 est fausse et condition2 est vraie.

Le corps3 sera exécuté si condition1 est fausse, condition2 est fausse et
condition3 est vraie.

Le corps4 sera exécuté si condition1 est fausse, condition2 est fausse et
condition3 est fausse.

### Les boucles

Parfois, il devient nécessaire de pouvoir executer du code plusieurs fois
d'affilée pour reussir à atteindre notre but. On pourrait imaginer une
situation où on voudrait afficher et un décompte un nombre en particulier. Pour
ce faire, il faudrait avoir une variable qu'on initialise en lui donnant une
valeur initiale de 0 avant de la faire augmenter par palier de `1` jusqu'au
nombre voulu en affichant le résultat à chaque fois.

La boucle `while` permet de représenter la situation. En supposant qu'on
veuille compter jusqu'à 42 on pourrait écrire le code suivant:

```python

mon_compteur = 0
while compteur < 43:
    print(mon_compteur)
    mon_compteur = mon_compteur + 1

```

Si on connaît déjà le nombre de fois qu'on veut executer le code dans le corps
de la boucle, on peut aussi utiliser une boucle `for` comme suit:

```python

for mon_compteur in range(43):
    print(mon_compteur)

```

Dans les deux cas, en rentrant dans le corps de la boucle la variable
`mon_compteur` aura pour valeurs succésives 0, 1, 2, 3 ... 41, 42.

### Les fonctions

De la même manière qu'on peut associer un nom à de la donnée en utilisant une
variable, il est possible d'associer un nom à des petits bouts de code: des
fonctions.

Voici un exemple de définition de fonction simple:

```

mon_entier = 21

# La définition de la fonction
def doubler_mon_entier():
    mon_entier = mon_entier * 2

# Un appel de la fonction
doubler_mon_entier()

# mon_entier est maintenant égal à 42

# Un deuxième appel de la fonction
doubler_mon_entier()

# mon_entier est maintenant égal à 84

```

Les fonctions peuvent aussi prendre des paramètres comme par exemple:

```

# La définition de la fonction qui prend des paramètres
def regarder_si_plus_de_42(entier):
    if entier > 42:
        print('Plus grand que 42 !')
    elif entier == 42:
        print('Egal à 42 !')
    else:
        print('Plus petit que 42 !')

# Trois appels de cette fonction
regarder_si_plus_de_42(100)
# Affiche 'Plus grand que 42 !'

regarder_si_plus_de_42(42)
# Affiche 'Egal à 42 !'

regarder_si_plus_de_42(23)
# Affiche 'Plus petit que 42 !'

```

### Les imports

TODO

## Nouvelles notions

On va avoir besoin de plus que ces notions là.

### `pygame`

Explication rapide du setup MIDI et la gestion de la fenêtre.

### Les tuples

Explications et petits exos/fonctions auxiliaires à écrire sur les tuples.

### Les dictionnaires

Explications et petits exos/fonctions auxiliaires à écrire sur les dictionnaires.

## Utiliser vos connaissances

Nous pouvons enfin commencer à travailler sur notre piano. Comme pour beaucoup
de programmes, notre code va être divisé en deux grosses parties:
l'_initialisation_, où on va préparer tout ce qu'il faut dans notre programme
(ouvrir une fenêtre, dessiner le piano initial, préparer la sortie pour le
son...), et le _corps_, où on va exécuter le même chose en boucle.

### La structure globale du programme

Comme dit précdemment, notre programme va être divisé en deux parties:
l'_initialisation_ et le _corps_.

Lors de l'_initialisation_, nous allons préparer tout pour que notre piano
puisse afficher les touches enfoncées et jouer du son.

Avant tout, nous allons avoir besoin de quelque variables pour notre piano:

* 5 couleurs pour l'affichage
* le nombre de notes contenues dans un octave (nombre de touches avant que le
  clavier ne se répète)
* l'octave dans lequel on veut que les sons soient jouées (plus ou moins grave,
  je vous conseille 4)
* le volume avec lequel on veut jouer (entre 0 et 124)

Les couleurs dans `pygame` sont représentées par des *tuples* de trois valeurs
entre `0` et `255` qui correspondent à l'intensité en rouge, vert et bleu.

Par exemple, la couleur noire correspond à `(0, 0, 0)` et le blanc à `(255,
255, 255)`.

On pourrait donc initialiser nos variables comme suit:

```

# La couleur du fond
color_gris  = (127, 127, 127)

# La couleur des touches blanches
color_blanc = (255, 255, 255)

# La couleur des touches noires
color_noir = (0, 0, 0)

# La couleur des touches blanches enfoncées
color_rouge = (255, 0, 0)

# La couleur des touches noires enfoncées
color_bleu = (0, 0, 255)

# Le nombre de notes
nombre_de_notes = 12

# L'octave dans lequel on veut jouer
octave = 4

# Le volume
volume = 124

```

Ensuite, pour pouvoir utiliser `pygame`, il faut importer les deux parties
dont on va avoir besoin:

```python

import pygame.midi
import pygame.display

```

Pour initialiser ces deux systèmes (affichage et son), `pygame` fournit deux
fonctions qu'on peut appeler dès le début de notre programme comme suit:

```python

# Pour le son
pygame.midi.init()

# Pour l'affichage
pygame.display.init()

```

#### Du bruit

Faire les fonctions qui allument une note.

#### Du silence

Faire les fonctions qui éteignent une note.
