---
title: Micro-Morse
date: 2022
weight: 15
subtitle: Ce TP te permettra de découvrir la récursivité et de pouvoir communiquer en morse avec les autres participantes !
code_stub_url: resources/given_resources/given_code.py
---

# Introduction
Pour ce TP, nous allons vous accompagner dans la création d'un nouveau moyen de
communiquer avec vos amis : le code morse ! 
Vous avez déjà dû en entendre parler, et ici vous allez pouvoir l'utiliser !

## Le code morse, qu'est-ce que c'est ?
Voilà la définition de Wikipédia :
> Le code Morse international, ou l’alphabet Morse international, est un code permettant de transmettre un texte à l’aide de séries d’impulsions courtes et longues, qu’elles soient produites par des signes, une lumière, un son ou un geste. 
> Wikipedia

On est d'accord, ce n'est pas très clair... Pour faire simple, c'est un nouvel
alphabet constitué uniquement de points (`·`) et de traits (`-`), et chaque
lettre correspond à une suite de points et de traits dont l'ordre permet de
donner un sens à chaque séquence. 
Voici un tableau représentant les traductions de toutes les lettres et tous les
chiffres :
{{<figure src="resources/images/International_Morse_Code.svg" caption="Code Morse International">}}

# Les arbres
## La théorie

Pour faire ce TP, on va utiliser ce qu'on appelle les arbres binaires. Ce sont
des structure de données, c'est-à-dire une organisation particulière de données,
qui vont nous permettre de rechercher plus efficacement quelle lettre a été
envoyée. 

Pour t'aider à t'en représenter un, voici l'arbre binaire que nous allons
utiliser dans la suite de ce TP (aller vers la gauche équivaut à un point, et
vers la droite à un trait) : 
{{<figure src="resources/images/bintree_example.png">}}

### Récursion

Avant de parler d'arbres, il faut parler de récursion. Quelque chose de récursif
est quelque chose qui va s'appeler lui-même.

Par exemple, une fonction récursive est donc une fonction qui s'appelle elle-même.

```py
def addition(n):
    """
    Renvoie le résultat de l'addition 1+2+3+...+n
    """
    if n == 1:
        return 1
    else:
        return n + addition(n-1)
```

Regardons le code étape par étape pour comprendre comment il fonctionne.
Disons que l'on souhaite calculer `addition(3)`.

1. 3 est différent de 1, donc la fonction va renvoyer `3 + addition(2)`
2. Il faut donc calculer `addition(2)`, qui renvoie `2 + addition(1)`. 
   En remplacant ce résultat dans l'expression précédente, on a donc 
   `3 + 2 + addition(1)`
3. Comme `1 = 1`, `addition(1)` va donc renvoyer 1. Le résultat est donc `3 + 2 + 1`
    ce qui donne `6`

#### Mini-Exercice

Écris une fonction qui calcule `1*2*3*...*n` avec `n` étant le paramètre de cette 
fonction.


### Des arbres récursifs
#### Un arbre, genre comme dans la forêt ?

Pas tout à fait, mais on appelle cette structure de donnée un _arbre_ car elle
lui ressemble (très rapidement). Et on le qualifie de _binaire_ car il y a deux
chemins possibles au maximum. 
Voici un petit peu de vocabulaire qui pourra nous être utile dans la suite de ce
TP. Dans un arbre binaire est composé de `noeuds`. Chaque `noeud` contient une valeur appelée
`clé` (`key` en anglais). Ce noeud va également avoir 2 `enfants`, qui sont eux aussi des
`noeuds` : on les nomme `fils gauche` lorsqu'il se trouve à gauche de son `père` 
et `fils droit` lorsqu'il est à droite. Le tout premier `noeud`
est appelé `racine` de l'arbre. 

Prenons l'exemple de l'arbre binaire que tu peux voir plus haut. La `racine` est
le `noeud` le plus haut. Sa `clé` est _A_. Il possède 2 `enfants`. Un `fils
gauche` dont la `clé` est _B_, et un `fils droit` dont la `clé` est _F_. 

Si jamais tu as une quelconque question ou bien quelque chose que tu n'as pas
compris, n'hésite surtout pas à demander plus d'explications à un organisateur.
Ils sont là pour t'aider ;).

#### Quel est le rapport avec un ordinateur ?
En python, on représente un arbre comme un objet récursif, car il se contient lui-même.
En fait, nous manipulerons une variable de type `Noeud`, qui contiendra une
`clé`, ainsi que deux autres objets de type `Noeud` qui sont ses enfants. 
Tu peux voir les objets de type `Noeud` comme un nouveau type de variable, un
peu comme `int`, `string` ou `list`. 

#### Et comment parcourir un arbre ? 
Ces arbres, on peut les parcourir, c'est-à-dire regarder les `clés` de chacun des
`noeuds`. Pour cela, on utilise une fonction récursive :

Ici la fonction qui suit va afficher la `clé` du `noeud` courant et aller va continuer le parcours
dans le `fils gauche` puis dans le `fils droit`. 

En python, on utilise le mot-clé `None` pour indiquer qu'il n'y a pas d'arbre.
On fait donc le parcours seulement si l'arbre existe. 

```py
def parcours(B): # Ici `B` est un arbre
    if B != None: # Ici on teste si l'arbre est vide
        print(B.key) # Ici on affiche la clé de la racine de `B`
        parcours(B.left) # Ici on rappelle la fonction avec comme nouvel arbre
                         # celui dont la racine est le fils gauche de `B`
        parcours(B.right) # De même ici avec le fils droit de `B`
```
Avec l'arbre donné en exemple, cette fonction va afficher _ABCEDFGIHJ_ sur
l'écran du terminal. 

#### Mini-Exercice

Écris une fonction de parcours qui fait le parcours dans le fils gauche, affiche
la `clé` du `noeud` actuel, et fait le parcours dans le `fils droit`.

Tu peux utiliser ce code pour représenter les `Noeuds` et tester ton code avec
l'arbre `ARBRE` donné en exemple :

```py
class Noeud:
    def __init__(self, key, left, right):
        self.key = key # La valeur du noeud
        self.left = left # Le fils gauche
        self.right = right # Le fils droit

ARBRE = Noeud('A', Noeud('B', Noeud('C', None, Noeud('E', None, None)), Noeud('D', None, None)), Noeud('F', Noeud('G', Noeud('I', None, None), None), Noeud('H', None, Noeud('J', None, None))))
```
Ta fonction devrait afficher _CEBDAIGFHJ_. 

#### Les différents types de parcours 

Il existe plusieurs types de parcours :
- le parcours préfixe, celui donné dans l'exemple, dans lequel on affiche la clé
    avant d'aller voir les enfants
- le parcours infixe, celui du mini-exercice, dans lequel on va voir le fils
    gauche, puis on affiche la clé et on va voir le fils droit.
- le parcours suffixe, dans lequel on va voir le fils gauche puis droit avant
    d'afficher la clé.

Pour la suite du TP, nous allons utiliser le parcours préfixe. Si tu n'as pas
bien compris ce que c'était, n'hésite pas à demander de l'aide à un organisateur
pour ne pas être perdu dans la suite du TP.  



## Application à notre problème
Tu as pu lire une partie très théorique sur une représentation complexe des
données. Il est très important que tu ais compris la partie précédente afin
de profiter pleinement de la suite du TP. 

### Notre arbre
Voici donc l'arbre que nous allons utiliser afin de décoder le message morse : 

{{<figure src="resources/images/bintree_morse_code.png">}}

Comme vous pouvez le voir, il suffit de parcourir l'arbre (comme expliqué plus
        haut) afin de trouver la représentation correspondante. 

Tu peux télécharger le code à compléter de ce TP pour te simplifier la tâche
[ici]("resources/given_resources/micro_morse.py") ou en cliquant sur le bouton
_Code à compléter_ en haut de cette page. 


### Une définition universelle ?

Pour mener notre projet à bien, nous allons devoir poser quelques conventions.
En effet, sans ces dernières, nous ne pourrons pas savoir à quoi correspond un
point ou un trait dans les données que nous allons recevoir. 
Tout d'abord, un point (`·`) correspond à un appui sur le bouton `A` et un trait 
correspond à un appui sur le bouton `B`. Nous allons représenter les appuis sur
les boutons par une chaine de caractères dans laquelle les points sont
representés par des `0` et les traits par des `1`. Le principal avantage d'utiliser
une chaine de caractères est que celle-ci va conserver l'ordre d'appui sur les
touches, ce qui nous est très utile pour ne pas créer de confusions. 

Ces derniers paragraphes ont été assez dense et ne sont pas des plus faciles à
comprendre. Si tu as un doute sur quelque chose ou que tu as une
question, n'hésite surtout pas à faire appel à un organisateur. 

Si tout est bon pour toi, nous allons pouvoir commencer le coeur de notre TP ! 


#### Exercice 1 : Traduire une chaine de caractères
**But :** Écrire une fonction `translate_into_letter(S, arbre)` qui prend en paramètre
    une chaine de caractères `S` ainsi que l'arbre représentant le code morse, 
    et renvoie la lettre qui correspond à la chaine donnée. 
    Pensez à utiliser le fichier qui vous est donné ;) 

**Exemple :** `translate_into_letter("0010", MORSE)` va nous renvoyer `'F'`. 

**Aide :** Vous pouvez découper cette fonction en deux étapes : 
        - D'abord, quel est ou quels sont le ou les cas d'arrêt(s) ?
        - Ensuite, si le cas d'arrêt n'est pas atteint, que faire ?

**Rappels :** Vous pouvez tester vos fonctions directement dans Mu en appuyant 
sur le bouton 'Lancer'


# Récupérer l'entrée utilisateur
## Lorsque tout se passe bien...
Maintenant que nous savons traduire une chaine de caractères en lettres, nous
allons devoir trouver un moyen de transformer des appuis sur des boutons en
chaine de caractères. Pour ce faire, je te rappelle que nous avons mis en place
quelques conventions que l'utilisateur doit respecter afin de pouvoir utiliser
notre outil de communication moderne. Voici un bref rappel :
> Le bouton A correspond à un point, il est traduit par un `'0'` dans les
> chaines de caractères
> Le bouton B correspond à un trait, il est traduit par un `'1'` dans les
> chaines de caractères
> Pour valider un mot, l'utilisateur doit toucher le logo tactile
> Pour valider un message entier et l'envoyer, l'utilisateur doit secouer le
> microbit

Maintenant que les choses sont claires, passons à la pratique !

#### Exercice 2 : l'utilisateur parle à notre programme...
**But :** Coder une fonction `create_message()` qui ne prend aucun paramètre et
renvoie le message (sous forme d'alphabet latin) que l'utilisateur veut envoyer.

**Exemple :** _L'utilisateur appuie sur A, puis sur le logo, puis appui sur B,_
_puis à nouveau sur le logo avant de secouer le microbit_
La fonction `create_message()` renvoie donc `"E T"`



## ... mais que l'utilisateur est humain !
Dans la plupart des programmes que nous allons créer, nous allons le faire pour
qu'ils soient utilisés par un humain. Malheureusement, il n'est pas rare que
l'utilisateur ne respecte pas parfaitement le fonctionnement de notre programme.
Nous devons donc faire attention à ce qu'une mauvais utilisation de la part de 
l'utilisateur ne vienne pas provoquer une erreur dans notre code. 
Il faut donc toujours vérifier les informations que l'utilisateur nous transmet,
   c'est un bon réflexe à avoir afin de limiter les bugs. 

### Pourquoi Micro-Morse est concerné ? 
Bien que nous n'ayions que deux boutons, l'utilisateur doit respecter un
alphabet bien spécifique. 
Ici, la seule erreur que l'utilisateur peut comettre, c'est de valider une
lettre qui n'existe pas dans l'alphabet morse.
Modifions notre fonction précédente (`translate_into_letter`) afin de gérer les
cas où l'entrée utilisateur (c'est-à-dire lorsque la chaine de caractères passée en 
paramètre n'aboutit pas sur une lettre ou un chiffre). 

#### Exercice 3 : Vérifier la chaine de caractères
**But :** Modifier la fonction `translate_into_letter` pour que cela ne crée pas
d'erreur si l'utilisateur entre une mauvaise séquence, renvoyer une chaine vide
(`""`) si c'est le cas.

**Exemple :** `translate_into_letter("0101", MORSE)` va nous renvoyer une chaine
vide (`""`) sans produire d'erreur. 

**Aide :** En cas de mauvaise entrée, au niveau de quelles lignes de code peut-on trouver
une erreur ?



# Accordons nos fonctions ensemble !
Voici le moment tant attendu, maintenant que toutes les étapes de notre projet
fonctionnent, il est l'heure de les faire fonctionner ensemble. 

## Comment mon code doit se comporter ?
Vous l'avez peut-être vu, dans le code que nous t'avons donné, 
notre programme est en mode _réception_, c'est-à-dire qu'il est prêt à recevoir
le message d'un autre microbit. Si tu le lances tel quel, tu ne pourras que
recevoir des messages, mais tu ne pourras pas en émettre. 

Pour le passer en mode _émission_, l'utilisateur doit seulement appuyer sur n'importe 
quel bouton. C'est un choix très arbitraire de notre part, mais tu peux tout
aussi bien faire en sorte d'entrer dans ce mode lorsque le microbit est secoué,
ou bien de manière plus originale lorsqu'il est en chute libre ! (C'est une
blague, ne tente pas de lâcher le microbit du 4e étage, tu aurais du mal à
envoyer un message par la suite). 

#### Exercice 4 : Et que le Micro-Morse fut
**But :** Ajouter une condition pour entrer en mode _émission_ dans la boucle
principale et ensuite appeler la fonction permettant à l'utilisateur d'écrire 
le message. 



# C'est déjà la fin ?
C'est en effet la fin de ce TP. Nous espérons que cela t'as plu, et
encore une fois si tu as des questions, n'hésite surtout pas à les poser à des
organisateurs. 
Tu peux désormais passer aux TPs suivants, ou bien essayer d'améliorer ce
mini-projet :)

## Des améliorations ?
Comme tu t'en doutes peut-être, ce TP est un mini-projet améliorable à l'infini
ou presque. Si tu veux continuer à améliorer ton programme, tu es libre de faire
ce que tu veux avec. 

Si jamais tu as besoin d'idées, en voici quelques unes :
- Possibilité de choisir son canal radio afin de pouvoir discuter _presque_
secrètement
- Pouvoir corriger une faute de frappe en appyuant simultanémant sur `A` et `B`
- Visualisation du code morse déjà entré (En affichant la lettre qui a été
        trouvée avant une confirmation par l'utilisateur par exemple)
- Confirmation du message avant son envoi

