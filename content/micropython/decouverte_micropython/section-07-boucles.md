# Ça fait beaucoup de lignes

Tu sais maintenant comment créer des programmes assez complexes. Pour répéter
une action et t'éviter de copier-coller des bouts de code, il existe en Python
ce que l'on appelle des **boucles**. Il en existe deux : les boucles `for` et les
boucles `while`. Nous allons commencer par la dernière.

## Tant que 

La boucle **while** ("tant que") est une boucle dont le bloc de code est répété
tant qu'une condition est vérifiée (d'où son nom). On l'écrit similairement à
des conditions `while condition:`. Illustrons cette boucle à travers un exemple
de code :

{{< codestep steps=3 lang="py" >}}

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

{{% box type="exercise" title="Mini-mission 8 : Nombre d'appuis" %}}

Écris un programme qui compte et affiche le nombre d'appuis sur les
boutons A et B avant que le bouton tactile ne soit touché.

<br>

_Aide :_ Tu peux utiliser `pin_logo.is_touched()` pour vérifier si le bouton
tactile a été appuyé.

{{% /box %}}

{{% box type="info" title="Les boucles infinies" %}}

Pour utiliser les boutons des `micro:bit`, on va souvent vouloir vérifier **tout
le temps** si une condition est vérifiée (comme `button_a.is_pressed()`). Pour
cela, on va utiliser une **boucle infinie** qui ne s'arrête jamais. Dans ce cas là
on utilisera la boucle `while True` comme dans cet exemple :

```python
# Importe les fonctions pour le micro:bit
from microbit import *

while True:
    # Vérifie tout le temps si le bouton A est appuyé ou non
    if button_a.is_pressed():
        display.show(Image.HAPPY)

    else:
        # Affiche `ANGRY` si le bouton n'est pas appuyé
        display.show(Image.ANGRY)
```

{{% /box %}}

## Pour un certain nombre de fois

La boucle `for` est un peu différente de la boucle `while`, car elle permet de
répéter un bloc de code un nombre fini de fois. Ce nombre de répétitions **doit
être connu** pour pouvoir utiliser ce type de boucle.

Voyons le fonctionnement de ce type de boucles à travers de plusieurs exemples.
Tu peux cliquer sur les flèches pour avoir les explications et à la fin, lancer
les programmes !

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

{{<figure src="resources/images/for_loop.png" >}}

{{% box type="exercise" title="Mini-mission 9 : Multiplication fois trois !" %}}

Comme pour l'exercice 2, Joseph voudrait connaître le résultat de la
multiplication de différents nombres. Sauf que cette fois-ci, il ne veut pas se
limiter à deux nombres. Écris un programme qui multiplie 3 nombres entre eux. Tu
peux récupérer les nombres en comptant le nombre d'appuis sur le bouton A, en
laissant quelques secondes à chaque fois.


> _Petite astuce :_ Pour savoir quand tu passes au nombre suivant, tu peux allumer la LED
> de coordonnée `(0, i)` à chaque début de boucle pour différencier les nombres.

{{% /box %}}
