---
title: Trie Data Structures
date: 2020
---

Pré-requis: avoir vu les listes et les classes

# Cours sur la structure d'arbre

* Qu'est ce que c'est (vocabulaire)
* A quoi ça sert

# Introduction aux Tries

* Explication de la structure, cas spécifique des arbres
* Les guider pour l'implem en python => Node

## Création

Pour créer notre trie, nous allons créer une classe `Node`.  
Celle-ci représente un noeud de l'arbre.  
Il est composé d'un caractère, d'une liste de fils et d'un bouléen qui nous
dit si le noeud marque la fin d'un mot.  
Pour ce faire, en se souvenant du cours sur les classes, on écrit la fonction
`__init__` qui initialise ces 3 attributs.
Le caractère est donné en paramètre, la liste de fils est initialisée vide, et
la plupart du temps, le mot n'est pas terminé donc on initialisera le booléen
à `False`.
```python
def __init__(self, char)
```

## Insertion

Donc maintenant, on peut créer un noeud avec un caractère, mais il nous apporte
pas beaucoup dans ce qu'on veut faire, on voudrait lui ajouter des fils.  
On va donc lui donner une autre méthode, `add_child_at`. Elle prendra en
paramètre un entier qui représente la position où l'on veut ajouter un noeud
dans la liste de fils et le noeud en question.
```python
def add_child_at(self, index, child_node)
```
Je vous conseille de regarder les fonctions sur les listes, elle vous permettra
d'ajouter le noeud dans la liste très simplement.  
Il faut faire attention aux paramètres qu'on nous donne, en effet, ils peuvent
être erronés. Donc avant d'ajouter le noeud à la bonne position, on doit
vérifier que cette position a du sens, donc que l'entier est positif et
inférieur ou égal à la taille de la liste actuelle.  
(Poser des questions aux encadrants si vous ne comprenez pas pourquoi ;) )  
Pour renseigner à l'utilisateur si on a effectivement ajouté le noeud dans les
fils, on retourne un booléen: `True` si on l'a ajouté, `False` sinon.

Grande nouvelle, on peut dès à présent créer l'arbre que l'on souhaite !  
Mais calculer les positions à la main peut être ennuyeux et on peut commettre
des erreurs (les fils doivent être triés en fonction de leur caractère).  
On va créer une nouvelle méthode qui créera le fils pour nous, directement au
bon emplacement.  
On appelle cette fonction `insert_char`, qui prend en paramètre un caractère
à ajouter dans les fils du noeud courant.
```python
def insert_char(self, char)
```
Lors de l'ajout du caractère, nous avons 2 situations:  
- soit le noeud n'est pas présent dans les fils auquel cas il faut le créer
 et l'ajouter  
- soit le noeud est déjà présent  
On va donc parcourir les fils et comparer leur caractère à celui qu'on veut
ajouter.  
Pour récupérer le caractère d'un fils, il suffit d'accéder à son attribut,
par exemple:
```python
# si l'attribut de `Node` représentant la liste de fils est `children`
>>> child = node.children[0] # `child` est le premier fils du noeud `node`

# on récupère son caractère en faisant
>>> child.char # si l'attribut de `Node` représentant le caractère est `char`

# ce qui est équivalent à
>>> node.children[0].char
```
On a dit précédement que les fils étaient triés selon leur caractère, ils sont
triés par ordre lexicographique et ils sont uniques, il n'y a pas de caractère
en double. On a donc:
```python
# si `node` a 3 fils
>>> node.children[0].char < node.children[1].char
True
>>> node.children[1].char < node.children[2].char
True
```
On peut ainsi calculer la position d'un nouveau noeud, elle correspond à la
position du premier noeud avec un caractère supérieur s'il existe ou la taille
de la liste sinon. (Je vous conseille d'utiliser une boucle pour passer sur
les noeuds).  
Une fois le noeud trouvé si le caractère était déjà présent, ou ajouté sinon,
on retourne celui-ci.

C'est beaucoup plus pratique pour ajouter un caractère non ?  
C'est fini pour les bases de la structure de `Trie`, on va commencer la
partie qui nous intéresse: le spell checker (vérificateur d'orthographe).



# Spell Checker

Le but principal de cet exercice est de vérifier l'orthographe des mots donnés
en entrée par l'utilisateur.

* Fonctions basiques:
    - créer le dictionnaire et y rajouter des mots
    - afficher le dictionnaire
    - rechercher si un mot est dans le dictionnaire, est ce qu'il existe
=> Dict

* Explications: Création + Parcours + Recherche

## Parcours du dictionnaire

Pour pouvoir vérifier l'orthographe de mots, nous avons besoin comparer les
mots présents dans le dictionnaire avec ceux de l'utilisateur.  

Prenons comme exemple un dictionnaire minimaliste qui contient les mots:

* "a"
* "le"
* "la"
* "python"

On peut représenter ce dictionnaire comme:  
![Trie](trie_minimalist.png){width=4.5cm height=8cm}

On a la `root`, ou point d'entrée de l'arbre (le cercle le plus haut) qui ne
contient pas de caractère, il nous permet d'accéder aux premières lettres des
mots.

Puis, nous avons la première ligne, les initiales: 'a', 'l', 'p'. Le
dictionnaire contient 4 mots mais 2 d'entre eux ont la même initiale, ce qui
nous donne 3 noeuds dans l'arbre.

Le noeud qui contient la lettre 'a' est coloré en bleu, ce qui signifie la fin
du mot donc que le booléen du noeud 'a' est à `True`. Ainsi, nous retrouvons
le mot "a".

Le noeud avec la lettre 'l' a deux fils, il est utilisé pour construire 2 mots:
"la" et "le".

Et on continue ainsi jusqu'à la fin.  
Si on compte le nombre de noeuds bleus dans l'arbre, on retrouve le nombre de
mots insérés: 4.

### Algorithme

Il peut être pratique d'afficher son dictionnaire que ce soit pour l'utilisateur
ou pour le programmeur. Ça nous permet de vérifier le comportement de notre
programme.

D'après le schéma ci-dessus, on en conclut que suivre une branche revient à
écrire un mot. Prenons la dernière branche par exemple, elle contient les noeuds
'p', 'y', 't', 'h', 'o', 'n', qui représente le mot "python".

Ainsi, pour donner les mots de notre dictionnaire, il suffit de suivre toutes
les branches. C'est ce qu'on fait avec un `dfs` ou depth-first search (parcours
en profondeur en français), c'est un algorithme récursif qui passe sur tous les
noeuds de l'arbre. Plus particulièrement, nous allons utiliser un parcours en
profondeur préfixe, puisqu'il commence par le permier fils et nous permet de
garder l'ordre des noeuds, le dictionnaire affiché sera donc dans l'ordre
lexicographique.

Pour expliquer simplement, l'algorithme commence par descendre sur le premier
fils, s'occupe de l'arbre de celui-ci, puis de passe au deuxième fils, etc.

Voici l'algorithme:
```
visiterPréfixe(Arbre A):
    visiter (A)
    Pour tous les fils F de A:
          visiterPréfixe(F)
```

Pour vous donner un exemple de l'ordre de passage sur les noeuds de cet
algorithme, nous pouvons l'exécuter sur l'arbre précédent:

- on commence avec `A` = la root de l'arbre, le noeud tout en haut
- ligne 2: on visite ce noeud, nous allons expliquer plus tard quoi faire ici
- ligne 3: une boucle sur les fils de `A`: on commence donc avec `F` = le premier
fils: le noeud avec la lettre 'a'.
- ligne 4: on appelle recursivement la fonction `visiterPréfixe` sur ce noeud
- on revient donc à la ligne 1 avec l'arbre `A` = le noeud 'a'.
- ligne 2: visiter le noeud
- ligne 3: une boucle sur les fils du noeud 'a' mais 'a' n'a pas de fils donc la
fonction s'arrête ici et on revient à l'appel de celui lorsque `A` = la root et
`F` = le noeud 'a' à la ligne 4.
- le contenu de la boucle sur `F` est fini donc on revient à la ligne 3 avec `F` =
le prochain fils de `A`, ici le noeud 'l'.
- on appelle récursivement la fonction `visiterPréfixe` sur ce noeud
- on est maintenant au début de la fonction `visiterPréfixe` avec `A` = le noeud
'l'.
- on passe plus rapidement, on va à la boucle sur les fils: le noeud 'l' = `A` a
plusieurs fils, donc on rentre dans la boucle
- `F` = le premier fils = le noeud 'a', on appelle la fonction `visiterPréfixe`
dessus
- ce noeud n'a pas de fils donc on ne rentre pas dans la boucle et on revient
à l'appel de la fonction ligne 4 avec `A` = noeud 'l' et `F` = noeud 'a'
- on passe au fils suivant, `F` = noeud 'e' et on appelle la fonction sur celui-ci
- ce noeud n'ayant pas de fils, on ne rentre pas dans la boucle et on revient
à la ligne 4 avec `A` = le noeud 'l' et `F` = le noeud 'e'.
- `A` n'ayant plus de fils à parcourir, on revient à l'appel précédent avec `A` =
la root et `F` = le noeud 'l'
- on passe au fils suivant de la root: `F` = noeud 'p' et on appelle la fonction
`visiterPréfixe` sur celui-ci
- on a `A` = le noeud 'p', il possède un fils donc on appelle la fonction sur le
noeud 'y'
- on a `A` = le noeud 'y', il possède un fils donc on appelle la fonction sur le
noeud 't'
- on a `A` = le noeud 't', il possède un fils donc on appelle la fonction sur le
noeud 'h'
- on a `A` = le noeud 'h', il possède un fils donc on appelle la fonction sur le
noeud 'o'
- on a `A` = le noeud 'o', il possède un fils donc on appelle la fonction sur le
noeud 'n'
- le noeud 'n' n'a pas de fils, on revient sur l'appel précédent
- le noeud 'o' n'a plus de fils à visiter, on revient sur l'appel précédent
- et ainsi de suite jusqu'à revenir avec `A` = la root et `F` = le noeud 'p'
- le noeud root n'ayant plus de fils à visiter, on sort de l'algorithme.

Pour résumer, nous sommes passer sur les noeuds de l'arbre avec l'ordre:

- root
- 'a'
- 'l'
- 'a'
- 'e'
- 'p'
- 'y'
- 't'
- 'h'
- 'o'
- 'n'

On peut representer l'ordre de cet algorithme peut être vu comme:  
![Prefix](dfs_prefix.png){width=5cm height=4cm}

### Concrètement


## Recherche d'un mot

## Création du dictionnaire


* Ajouter une command line au main

# Bonii

* Recherche dichotomique
* Initialisation du dictionnaire à partir d'un fichier de texte
* Spell Checker sur un fichier donné => affiche les fautes
* Autocomplétion lorsque l'utilisateur écrit
