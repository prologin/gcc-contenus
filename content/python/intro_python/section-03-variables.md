# Garder en mémoire

Les **variables** vont nous permettre de **garder en mémoire** certaines
valeurs et de les **associer à un nom**. Cela nous permettra par la suite de
réutiliser ces valeurs et de les manipuler. C'est comme si on utilisait des
boîtes pour les représenter !

{{<figure src="resources/images/variable.png" caption="Variable en Python">}}

Pour déclarer une variable, on procède de la sorte :

```python
# `ma_variable` stocke la valeur 42
ma_variable = 42
```

Ces variables sont **réutilisables**, on peut les rappeler pour obtenir leur
valeur.

```codepython
# `argent` stocke la valeur 12
argent = 12

# Affiche "Julie a 12 euros !" en utilisant
# la variable `argent`
print("Julie a", argent, "euros !")
```

## Les types de variables

Comme dans les langues parlées, il existe plusieurs types de mots en
programmation. Tous ces mots peuvent être stockés dans des variables comme
précédemment. Tu les découvriras petit à petit pendant le stage, mais voici
quelques exemples :

- les nombres entiers : `42`, `10`, `-3` ;
- les nombres à virgule : `10.3`, `2.999999`, `-4.11042` ;
- les caractères : `'c'`, `'A'`, `'!'` ;
- les chaînes de caractères : `"Hello World!"`, `"Girls Can Code!"`, `"Prologin"` ;
- les booléens : `True` (vrai), `False` (faux).

{{% box type="info" title="Pourquoi il y a des guillemets sur certains types ?" %}}

Les **caractères** et les **chaînes de caractères** correspondent à du texte
brut que tu veux écrire dans ton programme. Pour dire à l'ordinateur que tu veux
écrire un texte tel quel, il te faut utiliser les guillemets.

Par convention, on utilise les guillemets simples (`'`) pour les caractères et
les guillemets doubles (`"`) pour les chaînes de caractères.

Tu auras l'occasion de voir les chaînes de caractères plus en profondeur dans
une autre activité !

{{% /box %}}

{{% box type="warning" title="Les nombres à virgule" %}}

Les nombres à virgule sont utilisés en programmation. Attention, en *Python* et
dans d'autres langages de programmation, on **remplace** la virgule par un
**point** (`.`) comme dans cet exemple :

```codepython
# Crée une variable `pi`
pi = 3.14

# Affiche `pi`
print(pi)
```

{{% /box %}}

# Les opérateurs

Les ordinateurs ont été créés à la base pour **effectuer des calculs**. Tu peux
également faire différents types d'opérations avec Python, avec des nombres
entiers ou à virgule :

| Nom | Opérateur | Exemple | Résultat |
|:--:|:--:|:--:|--:|
| Addition | `+` | 6.2 + 2.4 | 8.6 |
| Soustraction | `-` | 7 - 2 | 5 |
| Multiplication | `*` | 7 * 2 | 14 |
| Division | `/` | 7 / 2 | 3.5 |
| Puissance | `**` | 7 ** 2 | 49 |
| Division entière | `//` | 7 // 2 | 3 |
| Modulo | `%` | 7 % 2 | 1 |

</br>

<details>
<summary>Clique ici pour découvrir ce que sont une division entière et un modulo !</summary>

Les deux dernières opérations ne te sont peut-être pas familières. Pourtant, ce
sont celles que tu as appris au primaire, lorsque que tu n'avais pas encore la
connaissance des nombres à virgule. Elles correspondent aux résultats de la
**division euclidienne**. Voici un petit exemple :

{{<figure src="resources/images/division.png" height=60% width=60% caption="Exemple de division euclidienne">}}

- La **division entière** (`//`) correspond au <font color=#A459D1>
quotient </font>de la division, ici <font color=#A459D1>3</font>.
- Le **modulo** (`%`) correspondent au <font color=#F266AB>reste </font>de la
division, ici <font color=#F266AB>2</font>. 

Voici un petit bout de code qui te permettra de comprendre ces opérations, avec
le même exemple.

```codepython
# Crée deux variables `a` et `b`
a = 17
b = 5

# Affiche le quotient en utilisant
# l'opérateur `//`
print("Quotient = ")
print(a // b)

# Affiche le reste en utilisant
# l'opérateur `%`
print("Reste = ")
print(a % b)
```

</details>

On peut alors reprendre les fonctions `print` et `input` qu'on a vu précémment
pour calculer le nombre d'années depuis la création de l'association Prologin et
de ton année de naissance ! Utilise les flèches ci-dessous pour découvrir le
code et le lancer à la fin !

{{< codestep steps=4 lang="py" run="true" >}}

{{< codestep-block desc="Variable qui garde en mémoire l'année de début de Prologin">}}
annee_debut = 1991
 
{{< /codestep-block >}}

{{< codestep-block desc="Demande à l'utilisateur son année de naissance">}}
entree_utilisateur = input("En quelle année es-tu née ?")
{{< /codestep-block >}}

{{< codestep-block desc="Transforme l'entrée en nombre">}}
annee_naissance = int(entree_utilisateur)
{{< /codestep-block >}}

{{< codestep-block desc="Affiche l'âge de l'utilisateur">}}
 
difference = annee_naissance - annee_debut
print("Prologin a été créée", difference, "ans avant ta naissance !")
{{< /codestep-block >}}

{{< /codestep >}}

{{% box type="info" title="C'est quoi `int()` ?" %}}

Le mot-clé `int` permet de transformer un texte en un nombre. Ce texte doit
contenir des chiffres pour pouvoir le transformer en nombre !

```codepython
# Le texte "3" contenu dans la variable `texte`
texte = "3"

# Transforme le texte en nombre dans la variable `nombre`
nombre = int(texte)

# Affiche la variable `nombre`
print(nombre)
```

Il existe un autre mot-clé pour faire l'inverse, transformer un nombre en un
texte, il s'agit de la fonction `str` qui fonctionne comme dans l'exemple
suivant.

```codepython
# La variable `nombre` garde la valeur 3
nombre = 3

# Transforme le nombre en texte dans la variable `texte`
texte = str(nombre)

# Affiche la variable `texte`
print(texte)
```

Pour mieux comprendre les fonctions `int` et `str`, voici une illustration des
exemples. Tu peux cliquer sur la flèche pour faire défiler les images.

{{< gallery steps=3 >}}

{{< gallery-img src="resources/images/int-str.png" desc="Différence entre texte et nombre">}}
{{< gallery-img src="resources/images/int.png" desc="Passer d'un texte à un nombre">}}
{{< gallery-img src="resources/images/str.png" desc="Passer d'un nombre à un texte">}}

{{< /gallery >}}

{{% /box %}}

{{% box type="exercise" title="Mission 3 : Argent de poche" %}}

Avant de te téléporter dans ce nouveau monde, Julie t'as donné quelques pièces.
Tu commences à avoir faim... Tu te rends alors dans une taverne, qui se nomme la
*Prolotaverne*, et tu te rends compte que les prix sont en euros (quelle
chance) !

</br>

Avant de consommer, tu souhaiterais connaître la valeur de ton porte-monnaie en
euros, et par un pur hasard, il y a un tableau récapitulant la valeur de chaque
monnaie !

| Type de pièce | Valeur en € |
|:--:|--:|
| Or | 5.12 € |
| Argent | 3.25 € |
| Bronze | 1.64 € |

</br>

Calcule et affiche la valeur totale de ton porte-monnaie sachant que tu as 6
pièces d'or, 3 pièces d'argent et 10 pièces de bronze !

Tu peux utiliser les variables et les opérations sur ces dernières pour afficher
la valeur totale !

{{% /box %}}

## Affecter et opérer !

Il existe un autre type d'opérateurs pour effectuer des calculs en
programmation. Ce dernier type est assez utile, et tu le rencontreras assez
souvent. Il s'agit des opérateurs `+=`, `-=`, `*=`...

Aux opérateurs que tu connais déjà, on rajoute le signe `=` pour faire
intervenir l'**affectation**. L'affectation est le fait de donner une certaine
valeur à une certaine variable. Lorsqu'on déclare une variable, on utilise le
signe `=` pour donner sa valeur.

```python
# Affecte 42 à la variable `ma_variable`
ma_variable = 42
```

Les opérateurs précédents nous permettent d'effectuer les opérations pour
*ajouter* ou *enlever*. Voici un petit exemple de leur utilisation :

```codepython
# Affecte 2 à la variable `a`
a = 2

# Affiche `a`
print(a)

# Ajoute 4 à la variable `a`
# Similaire à l'instruction `a = a + 4`
a += 4

# Affiche `a`
print(a)
```

Dans cet exemple, on ajoute 4 à la variable `a`. Cette opération te sera très
utile dans ta découverte de Python !

N'hésite pas à modifier et t'approprier l'exemple pour tester d'autres types
d'opérations et d'utiliser d'autres nombres ou variables ! Si jamais tu as des
questions, n'hésite surtout pas à appeler un organisateur !
