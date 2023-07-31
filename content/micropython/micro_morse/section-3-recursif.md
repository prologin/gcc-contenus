# Comment parcourt-on les arbres ?

Maintenant que nous savons ce qu'est un arbre, nous allons devoir apprendre à le
**parcourir** via un programme. Pour ce faire, nous allons avoir besoin de
fonctions qui s'appellent elle-mêmes. On les appelle des fonctions
**récursives**.

{{% box type="info" title="Les fonctions récursives" %}}

Une fonction récursive possède toujours deux étapes :

```py {nocopy=true}
def recursif(argument):
    # Cas d'arrêt
    if CONDITION:
        ARRETER

    # Cas de récursion
    else:
        recursif(AUTRE_ARGUMENT)
```

1. La première étape est le **cas d'arrêt**. Cette partie du code correspond à
   la fin du traitement de la fonction, lorsqu'il n'y a plus besoin de continuer
   en rappelant la fonction récursive.
2. La seconde étape est **l'appel récursif**. Cette partie est exécutée
   lorsque le traitement n'est pas terminé. Elle contient un appel à la fonction
   récursive.

{{% /box %}}

{{< figure src="https://media.giphy.com/media/qoJ9sZu2Xui9a/giphy.gif" caption="Le flocon de Koch, récursif" >}}

Prenons l'exemple de la fonction factorielle qui calcule le produit
`n * (n - 1) * (n - 2) * ... * 3 * 2 * 1` :

```py
def facto(n):
    # Cas d'arrêt
    if n == 1:
        return 1
    
    # Cas de récursion
    else:
        return n * facto(n - 1)
```

Si l'on souhaite trouver la valeur de `facto(3)` avec notre code ci-dessus,
voici ce que Python effectue :

{{< codestep steps=4 lang="py" >}}

{{< codestep-block desc="Pour pouvoir calculer `facto(3)`, Python a besoin de calculer `facto(2)`" >}}
facto(3) = 3 * facto(3 - 1)
{{< /codestep-block >}}

{{< codestep-block desc="Pour pouvoir calculer `facto(2)`, Python a besoin de calculer `facto(1)`" >}}
facto(2) = 2 * facto(2 - 1)
{{< /codestep-block >}}

{{< codestep-block desc="Pour l'appel de `facto(1)`, on arrive sur le cas d'arrêt et retourne 1" >}}
facto(1) = 1
{{< /codestep-block >}}

{{< codestep-block desc="À la fin, on remplace toutes les valeurs par celles qui ont été calculées" >}}

facto(3) = 3 * 2 * 1 = 6
{{< /codestep-block >}}

{{< /codestep >}}

Pour comprendre encore plus ce qu'est la récursivité, tu peux te fier au GIF
ci-dessous. Si jamais tu as la moindre question, n'hésite pas à la poser à un
organisateur !

{{< figure src="./resources/images/FACTO.gif" caption="La fonction factorielle" >}}

Cette fonction possède une structure qui est la même pour presque toutes les
fonctions récursives :

1. Le cas d'arrêt : lorsqu'on arrive à `1`, on s'arrête car le traitement est
   fini.
2. L'appel récursif : si on n'est pas à `1`, on récupère le résultat de
   `facto(n - 1)` et on le multiplie par `n`.

{{% box type="exercise" title="Mission 3 : Somme récursive" %}}

Crée une fonction récursive qui fait la somme des nombres pairs entre `0` et
`n` inclus. Pour cela, tu peux utiliser l'opérateur `%` !

```codepython
def add(n):
    # Code ici
    # et supprime le `pass` !
    pass

# Teste la fonction
print("add(42) =", add(42)) # Affiche la valeur 462
print("add(15) =", add(15)) # Affiche la valeur 56
```

<br/>

Cette partie est très théorique, si jamais tu n'as pas compris quelque chose,
n'hésite surtout pas à demander de l'aide aux organisateurs.

{{% /box %}}