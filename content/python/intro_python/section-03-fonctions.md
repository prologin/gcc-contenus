---
show_toc: true
---

# Les fonctions

Que fait le code suivant ?

```codepython
a = 3
b = 6
print("Les nombres plus grands que a")
for i in range(15):
    if i > a:
        print(i)
print()
print("Les nombres plus grands que b")
for i in range(15):
    if i > b:
        print(i)
```
Ici, on cherche à afficher tout nombre jusqu'à 15 plus grand que `a` puis ceux plus grand que `b`.

Encore une fois si on cherchait à faire cela avec d'autres valeurs, il faudrait donc refaire une nouvelle boucle ?

Heureusement, non ! Les deux boucles sont identiques, il serait donc plus intéressant de l'écrire une seule fois non ?
<!-- il faudrait peut-être expliquer ce que c'est, j'ai pas l'impression qu'on le fait
"Une fonction est un bloc qui permet de séparer du code grace à l'indentation ... et de l'appeler ensuite (expliquer l'appel de fonction)"-->
Une fonction est un bout de programme qui effectue une action, et que l'on va pouvoir utiliser plusieurs fois.   

Pour créer une fonction, il faut 5 éléments :
- le mot-clé `def`
- le nom de la fonction
- des parenthèses
- deux points
- une indentation à la suite
```codepython
def plus_grand_que(n):
    for i in range(15):
        if i > n:
            print(i)

a = 3
b = 6
plus_grand_que(a)
plus_grand_que(b)
```

Maintenant, si on voulait 'appeler' la fonction `plus_grand_que`, il suffirait juste de le faire comme on l'a fait avec `print` ou `range`.

Une fonction peut aussi être utilisée pour **créer un résultat**.
Jouons à un jeu, nous allons écrire une fonction qui permettra de lire dans les pensées (enfin presque).

```codepython
def tour_de_magie(n):
    resultat = 2 * n
    resultat = resultat + 10
    resultat = resultat // 2
    resultat = resultat - n

    return resultat

a = 20
b = tour_de_magie(a)
print(b) # Affichera toujours 5
```
Nous utilisons le mot-clé `return` pour stopper la fonction en précisant qu'il est possible de récupérer une valeur depuis celle-ci.

En écrivant `return resultat`, il est donc possible de **récupérer la valeur** à la fin de toutes les opérations de la fonction. La fonction `range` est un exemple de fonction à valeur de retour, contrairement à la fonction `print` !
# Interagir avec le code (IO)

Si on voulait tester notre tour de magie avec plusieurs personnes, avec ce qu'on a vu pour l'instant, on serait contraint de changer le fichier de notre programme constamment, sauvegarder et relancer le code.

Si j'en parle, c'est bien sûr parce que Python nous permet de faire plus simple.
Dans de multiples applications que tu utilises au quotidien, il est possible de saisir des valeurs, d'entrer un texte, un nombre ou autre.

Écrivons un programme qui demande et affiche ton nom. En Python, on utilisera la fonction `input()`:
```python
print("Quel est ton nom ?")
nom = input()
print("Tu t'appelles", nom, "!")
```

Au lancement du code, la console semblera être bloquée. En réalité `input()` bloque le code et attend une entrée de votre part.

Cette fonction a elle aussi une valeur de retour qui est une chaîne de caractères.

{{% box type="warning" title="Valeur de retour de `input()`" %}}

Attention ! Comme expliqué dans la partie type de données, si on entrait `5` dans la console, le résultat de la fonction `input()` sera la chaîne de caractères `"5"` et non la valeur numérique `5`.

{{% /box %}}

```python
n = 5
entree = input()
if entree == 5: # Ca sera toujours faux, on compare deux types differents
    print("Cinq")
```
Bien sur, Python (il est fort quand même) a quelque chose pour cette situation avec la fonction `int`:
```codepython
n = 5
entree = "5"
if int(entree) == 5:
    print("Cinq")
```

Enfin, si on intégrait ce qu'on vient d'apprendre dans cette partie pour notre tour de magie, ça donnerait :

```codepython
def tour_de_magie(n):
    resultat = 2 * n
    resultat = resultat + 10
    resultat = resultat // 2
    resultat = resultat - n

    return resultat

a = int(input())
b = tour_de_magie(a)
print(b)
```

Bien évidemment, tu peux coder de la manière que tu souhaites.
Cette partie est juste là pour te montrer quelques fonctionnalités et bonnes habitudes qui peuvent t'être utiles.

Passe maintenant aux TP suivants pour pouvoir accomplir plus de choses en programmation, dont des petits projets et mini jeux.