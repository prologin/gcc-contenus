# Ça fait beaucoup de lignes

Tu sais maintenant comment créer des programmes assez complexes. Pour répéter
une action et t'éviter de copier-coller des bouts de code, il existe en Python
ce que l'on appelle des **boucles**.

Il existe deux types de boucles : les boucles `for` et les
boucles `while`.

## Tant que 

La boucle `while` (*tant que* 🇫🇷) est une boucle dont le bloc de code est répété
tant qu'une condition est vérifiée (d'où son nom). On l'écrit `while condition:`.
On peut trouver des examples dans la vie courante :

{{<figure src="resources/images/algo-while.webp" caption="Algorithme avec l'utilisation d'une boucle tant que" >}}

Illustrons cette boucle à travers un exemple de code :

{{< codestep steps=4 lang="py" >}}

{{< codestep-block desc="Importe les fonctions pour utiliser le `micro:bit`" >}}
from microbit import *
 
{{< /codestep-block >}}

{{< codestep-block desc="Déclaration de la boucle avec le mot-clé `while` avec comme condition `button_a.get_presses() == 0`" >}}
while button_a.get_presses() == 0:
{{< /codestep-block >}}

{{< codestep-block desc="Affiche l'image `ANGRY` tant qu'on reste dans la boucle" >}}
    # Ce qui suit va être répété tant que le button A n'a pas été appuyé
    display.show(Image.ANGRY)
 
{{< /codestep-block >}}

{{< codestep-block desc="Affiche \"Tu es sortie !\" une seule fois" >}}
display.scroll("Tu es sortie !")
{{< /codestep-block >}}

{{< /codestep >}}

<br>

{{% box type="exercise" %}}

Écris un programme qui compte le nombre d'appuis sur les boutons A et B et qui 
affiche ce nombre lorsque le bouton tactile est touché.

Pendant que le programme attends (avant que tu appuies le bouton tactile), tu 
peux afficher l'image `Image.CLOCK1`.

{{% /box %}}

{{% box type="hint" %}}

Tu peux utiliser `pin_logo.is_touched()` pour vérifier si le bouton
tactile a été appuyé qui renvoie un booléen (`True` ou `False`).

{{% /box %}}

{{% box type="info" title="Les boucles infinies" %}}

Pour que le programme ne s'arrête jamais, comme dans un jeu par exemple, nous
pouvons utiliser une **boucle infinie**.

La boucle `while` s'arrête si la condition est fausse, donc utiliser `True` comme
condition, permet de créer une boucle infinie :

```python
# Importe les fonctions pour le micro:bit
from microbit import *

while True:
    # Vérifie si le bouton A a été appuyé
    if button_a.get_presses() > 0:
        display.show(Image.HAPPY)

    # Vérifie si le bouton B a été appuyé
    if button_b.get_presses() > 0:
        display.show(Image.ANGRY)
```

Ce programme affiche donc l'image `HAPPY` si le bouton A est le dernier à être
appuyé, l'image `ANGRY` si c'est le bouton B.

{{% /box %}}

## Pour un certain nombre de fois

La boucle `for` est un peu différente de la boucle `while`, car elle permet de
répéter un bloc de code un nombre fini de fois. Ce nombre de répétitions **doit
être connu** pour pouvoir utiliser ce type de boucle.

### Les boucles simples

Le nombre dans les parenthèses de `range` indique le nombre de répétitions, ici
la boucle répète 3 fois le bloc de code en-dessous.

```python
for i in range(3):
    # Affiche "Test."
    print("Test.")
```

### La variable de la boucle `for`

La variable `i` indique le numéro de la répétition, en partant de 0, la boucle
fera 5 répétitions.

```codepython
for i in range(5):
    # Affiche la valeur de `i` à chaque tour de boucle
    print("Numéro de répétition :", i)
```

`i` étant une variable, tu peux changer son nom si tu as envie :

```codepython
for un_autre_nom in range(3):
    print(un_autre_nom)
```

Voici un petit schéma pour bien différencier les différents blocs de code : 

{{<figure src="resources/images/for_loop.webp" >}}

{{% box type="exercise" %}}

Cette fois-ci, Lily veut impressionner ses amis en écrivant son programme en 4
lignes maximum ! Elle veut que sa carte affiche une diagonale (comme sur l'image
ci-dessous) pixel par pixel en partant du coin haut-gauche avec une pause de
500ms entre chaque pixel qui s'allume.

{{<figure src="resources/images/microbit_diagonal.webp" width=400 caption="LED en diagonales">}}

{{% /box %}}


## Une variable score

Comme dans un jeu vidéo, on peut combiner les variables avec les boucles, pour calculer
des scores, ou tout autre donnée dont on a besoin toute la partie.

Pour faire ça, on crée une variable avant la boucle, et on met à jour sa valeur, dans la
boucle. Par exemple :

```codepython
total = 0
for tour in range(10):
    print("Tour numéro " + str(tour))
    total = total + 2
    print("Total = " + str(total))
print("Final :")
print(total)
```

{{% box type="exercise" %}}

Lily te demande d'afficher le nombre total de pixels situés à gauche de la
diagonale à la fin du programme.

{{<figure src="resources/images/microbit_diagonal_sum.webp" width=400 caption="LED en diagonales">}}

Tu peux reprendre ton programme précédent en utilisant une variable `total`
qui va compter au fil de la boucle le nombre de pixels situés à gauche du pixel
que tu as allumé.
 
{{% /box %}}
