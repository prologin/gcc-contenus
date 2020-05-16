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

Pour créer notre trie, nous allons créer une classe `Node`.  
Celle-ci représente un noeud de l'arbre.  
Il est composé d'un caractère, d'une liste de fils et d'un bouléen qui nous
dit si le noeud marque la fin d'un mot.  
Pour ce faire, en se souvenant du cours sur les classes, on écrit la fonction
`__init__` qui initialise ces 3 attributs.  
Le caractère est donné en paramètre, la liste de fils est initialisée vide, et
la plupart du temps, le mot n'est pas terminé donc on initialisera le booléen
à `False`.

Donc maintenant, on peut créer un noeud avec un caractère, mais il nous apporte
pas beaucoup dans ce qu'on veut faire, on voudrait lui ajouter des fils.  
On va donc lui donner une autre méthode, `add_child_at`. Elle prendra en
paramètre un entier qui représente la position où l'on veut ajouter un noeud
dans la liste de fils et le noeud en question.  
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
des erreurs (les caractères des fils doivent être triés).  
On va créer une nouvelle méthode qui créera le fils pour nous, au bon
emplacement directement.  
On appelle cette fonction `insert_char`, qui prend en paramètre un caractère
à ajouter dans les fils du noeud courant.  
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

* Ajouter une command line au main

# Bonii

* Recherche dichotomique
* Initialisation du dictionnaire à partir d'un fichier de texte
* Spell Checker sur un fichier donné => affiche les fautes
* Autocomplétion lorsque l'utilisateur écrit
