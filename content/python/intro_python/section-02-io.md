# Affichons des choses !

En programmation, il te sera très utile d'**afficher du texte** ou des éléments
sur l'ordinateur. Pour faire cela, il faut écrire une nouvelle instruction en
utilisant la fonction `print` ! Chaque ligne de code est un ordre que tu donnes
à l'ordinateur. Essaye de lancer le code en-dessous en cliquant sur le bouton
*Run* !

```codepython
# Affiche "Hello World!" dans le terminal
print("Hello World!")

# Affiche le 42 dans le terminal
print(42)
```

{{% box type="info" title="C'est quoi les lignes qui commencent par un `#` ?" %}}

Les lignes qui commencent par un `#` sont des **commentaires**. Ces lignes vont
être ignorées par l'ordinateur. Ils sont écrits par les développeurs, pour les
développeurs afin de mieux comprendre ce que fait un programme.

Imagine devoir te rappeler de ce que fait chaque ligne de code dans un fichier
de plus de 42 000 lignes !

{{% /box %}}

{{% box type="exercise" title="Mission 1 : Affiche ton prénom !" %}}

Afin de faire plus ample connaissance avec toi, Julie souhaiterait que tu
affiches ton prénom ainsi que ton âge en utilisant la fonction `print` !

Pour cela, crée un fichier Python et ouvre le avec ton environnement de code. Tu
pourras alors ainsi modifier puis lancer ton fichier pour vérifier le
fonctionnement de ton code !

{{% /box %}}

Il est également possible de donner plusieurs **arguments** à la fonction
`print` afin d'afficher plusieurs bouts de phrases séparés par des espaces.

```codepython
# Affiche "Girls Can Code!" dans le terminal
print("Girls", "Can", "Code!")
```

{{% box type="info" title="Des arguments et des fonctions ?" %}}

En programmation, on parle d'arguments lorqu'on **appelle une fonction** ! Les
fonctions sont des instructions qui font une chose spécifique par rapport à des
éléments qu'on donne en entrée. Ces entrées représentent les **arguments** de la
fonction.

Il peut avoir 0, 1, 2 ou plus d'arguments qui dépendent de la fonction qu'on
appelle. Ces arguments sont séparés par une virgule (`,`) comme dans cet
exemple :

```python {nocopy=true}
# Appel de la fonction qui s'appelle `fonction1`
# avec 2 arguments : `argument1` et `argument2`
fonction1(argument1, argument2)

# Appel de la fonction `fonction2` avec 0 argument
fonction2()
```

Si tu n'as pas tout compris cette partie, ce n'est pas grave ! On reviendra
dessus à la fin du sujet lorsqu'on voudra créer nos propres fonctions !

{{% /box %}}

# Quel jour sommes-nous ?

On peut également **lire et récupérer du texte** en demandant à l'utilisateur de
répondre à une question. Pour cela, on utilise l'instruction `input`.

```codepython
# Demande à l'utilisateur "Quel jour sommes-nous ?"
input("Quel jour sommes-nous ?")
```

Tout comme la fonction `print`, tu peux demander à l'ordinateur d'afficher du
texte avant de demander à l'utilisateur une entrée.

Ici, avant d'attendre la réponse de l'utilisateur, l'ordinateur affiche
*"Quel jour sommes-nous ?"*.

{{% box type="exercise" title="Mission 2 : Téléportation !" %}}

Julie vient de te téléporter dans un nouveau monde ! Tu es un peu perdue, mais
tu croises un passant. Tu voudrais lui demander dans quelle ville tu es tombée,
mais il ne comprend que le Python !

Utilise la fonction `input` pour lui demander une entrée avec comme message
*"Dans quelle ville suis-je tombée ?"*.

{{% /box %}}

La fonction `input` nous permet de demander une entrée à l'utilisateur.
Cependant, on ne peut pas la réutiliser, pour afficher la réponse par exemple.
Pour cela, nous avons besoin de la stocker dans une variable.
