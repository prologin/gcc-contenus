---
show_toc: true
---


# Introduction

{{% box type="warning" title="Avant de commencer" %}}

- Si tu ne comprends pas quelque chose, n'hésite surtout pas à demander à un orga ! Nous sommes là pour ça !
- On te conseille de créer un fichier par exercice, tous dans le même dossier.
- On te conseille fortement de tester tous les codes présents dans ce TP, même s'ils ne sont que des exemples. Si tu ne comprends pas comment ils fonctionnent, ou que quelque chose cloche, n'hésite pas à appeler un orga.

{{% /box %}}

Derrière toutes les applications et les logiciels que vous utilisez sur votre ordinateur ou votre téléphone se cache en réalité des centaines de lignes de codes dans des fichiers.
Ces dernières ne sont qu'un ensemble d'instructions dictant le fonctionnement du programme.

Votre ordinateur est capable d'exécuter pleins d'opérations très rapidement mais ne comprend qu'un seul langage, le langage machine.


Les humains étant incapable de comprendre ce langage, nous passons donc par des langages de programmation qui sont plus lisibles pour nous. Puis ce langage est traduit pour l'ordinateur. Pour cela, il existe des programmes dédiés à la traduction du code en langage machine, qui demande de respecter une syntaxe précise sinon il ne peut pas fonctionner. Nous utiliserons le langage Python pour ce stage.

## Types de données

En Python il existe plusieurs types de données, de valeurs comprises par l'ordinateur, les plus connus sont :
- Les entiers qui sont juste des nombres.
- Les chaînes de caractères utilisées pour stocker du texte. L'intérêt est de préciser à l'ordinateur que les mots ou nombres qui suivent sont à prendre littéralement. On reconnait une chaîne quand elle commence et se termine par des guillemets.
```python {nocopy=true}
"Ceci est une chaîne de caractères."
"1"
1

# Ici, il faut noter la différence entre `1` et `"1"`,
# même si elles représentent toutes les deux la valeur 1,
# ce ne sont pas du tout les mêmes types !
# On ne peut donc pas les utiliser de la même manière.
```
{{% box type="info" title="Bon à savoir : les commentaires" %}}

Le texte écrit après le `#` est ce qu'on appelle un commentaire. Ce sont des textes qui sont ignorés par ta machine, ils servent juste à donner plus d'explications à la personne qui relit le programme.

{{% /box %}}

- Les booléens qui servent à représenter Vrai ou Faux. (Nous verrons ça plus tard)
```python {nocopy=true}
True
False
```

# La fonction print

Dans notre fichier on peut donc écrire plusieurs de données et d'opérations à la suite ainsi :
```codepython
1 + 2
3
"ceci est du texte"
```
Si on lance le code avec le bouton Run, rien ne se passe.
En réalité, l'ordinateur a exécuté les opérations et a aussi pris en compte ce qu'on a écrit, on n'a juste pas pu les observer.

Il existe une différence entre ton fichier et la console (qu'on appelle aussi terminal).
La console permet d'**afficher** si on le désire certaines données lors de l'exécution du code grâce à ce qu'on appelle des fonctions.

On reconnait une fonction par les parenthèses qui sont après le nom de cette dernière.

Elle peut ou non prendre des arguments. Un argument de fonction c'est une valeur qui sera utile à l'intérieur de la fonction.
Lorsque des arguments sont requis, on les place entre les parenthèses et séparés de virgules, si y'en a plusieurs.
```python {nocopy=true}
fonction_sans_arguments() # Ce sont juste des exemples
fonction_avec_argument(2) # Ces fonctions n'existent pas
fonction_plusieurs_arguments(1, 2, "oui")
```
Python met à disposition plusieurs fonctions pratiques dont `print` qui permet d'afficher des valeurs dans la console. Si l'on reprend le code au début mais en rajoutant la fonction `print` :
```codepython
print(1 + 2) # Cette fonction existe, essayez la !
print(3)
print("ceci est du texte")
```

*Essaye de cliquer sur le bouton `Run` pour lancer ton programme Python !*

`print` prend un nombre quelconque d'arguments et les affichera tous, séparés par un espace.

```codepython
print(1, "2", 3, "oui")
```

{{% box type="exercise" title="Hello World !" %}}

À toi jouer ! Essaye d'écrire un code qui affiche `Hello World !` dans la console.

{{% /box %}}

# Les operateurs

Python nous permet d’effectuer des opérations, comme une calculatrice très perfectionnée. Essaie le programme suivant :

```codepython
print(4 + 3)
```
Tu remarques qu’ici, il n’y a pas de guillemets, on veut donc utiliser des entiers et non des chaînes de caractères.

Tu peux essayer de voir ce qui se passe si tu écris plutôt `print("x")` ou `print("4 + 3")`.


Mais Python ne permet pas seulement de faire des additions. Tu peux aussi utiliser les signes `-`, `*`, `/` pour effectuer des soustractions, des multiplications et des divisions. N’hésite pas à essayer !

## Pour aller plus loin

En plus des quatre opérations classiques, Python propose d'autres opérateurs comme : `//` et `%`.

Essaie-les pour comprendre ce qu'ils font.

# Variables
Pour l'instant nous avons nos valeurs un peu éparpillées au travers de notre programme.
Si on faisait un lien avec la vraie vie, ça serait comme avoir ses affaires éparpillées partout dans sa chambre, c'est pas très propre et ça peut devenir difficile de s'y retrouver.

L'idéal ça serait de pouvoir ranger tout ça et éventuellement avoir un moyen de retrouver ce qu'on veut facilement. 

En programmation, c'est pareil et nous utilisons pour cette raison des **variables**. On peut voir les variables comme des tiroirs avec des étiquettes dessus.

```codepython
a = 1
b = 2
d = "Hello World !"

print(d)
```
{{% box type="info" title="Bonne pratique" %}}

Dans la pratique on privilégie des noms courts mais compréhensibles, le but étant après tout de se retrouver dans notre code.

Avec la variable `d`, par exemple, n'a pas le nom le plus claire. Ca pourrait etre n'importe quoi au final. Ne serait-ce pas plus clair de l'appeler `hello` à la place ?

{{% /box %}}

## Opérations avec des variables

Mais ce qui est encore plus pratique, c’est que l’on peut faire des opérations avec les valeurs contenues dans nos variables. Essaie par exemple le programme suivant :

```codepython
a = 4
b = 3
resultat = a + b
print(resultat)
```
À quoi ça sert ? Ici, le calcul est très simple, mais imagine que tu aies beaucoup d'opérations à effectuer.

En écrivant ton programme avec des variables, tu n'as qu'à changer leur valeur au début pour pouvoir refaire toutes ces opérations sans avoir à écrire de nouveau du code.

Si tu voulais plutôt calculer 5 + 3 ici, il suffirait de remplacer la première ligne par `a = 5`.

Il s’agit de ton premier programme avec plusieurs instructions, et donc plusieurs lignes, car en Python, on met une instruction par ligne. Une instruction, c’est une tâche que l’on demande à l’ordinateur d’effectuer : affiche ceci, mets cette valeur dans cette variable, etc.

## Pour aller plus loin
<!-- à voir pour reformuler la phrase -->
En Python, on peut utiliser les variables de différentes manières. On peut ajouter à une variable une autre variable ou tout simplement lui ajouter un certain nombre.
Ces deux opérations peuvent s'écrirent de deux façons différentes mais qui correspondent à la même chose. Essaie par exemple le programme suivant :

```codepython
a = 10
a += 5
b = a + 5

print(a)
print(b)
```

On remarque que `+=` est équivalent à l'opération d'addition entre `a` et `5`, dont le résultat est ensuite stocké dans `a`.

Ce n'est pas la seule opération que l'on peut effectuer avec ce raccourci. On peut le faire avec les autres opérations vues précédemment `-=`,`*=`,`/=`.

<!-- ajout d'une box warning -->
{{% box type="warning" title="Différence entre `+=` et `=+`" %}}

Attention à l'ordre des éléments, `+=` et `=+` ne veulent pas dire la même chose. Avec `+=` on va d'abord effectuer l'addition puis on met le résultat dans la variable alors que pour `=+` on définit la variable avec la valeur à gauche de l'opérateur (`a=+8 c'est la même chose que a=8`).

{{% /box %}}
