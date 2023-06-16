# Comment utiliser les boutons du `micro:bit` ?

Comme tu peux le voir, il y a deux boutons physiques sur le `micro:bit` : le bouton A et
le bouton B. Mais il y a aussi un bouton tactile au niveau du logo au-dessus de
l'écran qui a été ajouté avec la version 2 du `micro:bit`. 

Voici un petit schéma qui te permet de repérer les différents boutons : 

{{<figure src="resources/images/microbit_buttons.png" width=600 >}}

Pour utiliser les boutons A et B, tu peux respectivement utiliser la fonction
`button_a.get_presses()` et `button_b.get_presses()`. Ces fonctions renvoient le
nombre d'appuis sur le bouton depuis la dernière fois qu'elles ont été appelées.
Par exemple, ce code va prendre le nombre de fois que le bouton A a été appuyé
au cours des 5 dernières secondes :

```python
from microbit import *

sleep(5000)
display.scroll(button_a.get_presses())
```

En ce qui concerne le bouton tactile, tu peux détecter si tu appuies dessus
en utilisant la fonction `pin_logo.is_touched()`, qui renvoie un booléen. 

### Mini-exercice
**But :** Crée un programme qui affiche la somme du nombre d'appuis sur les
boutons A et B au cours des 3 dernières secondes. 

## Un exemple un peu plus complexe

Voici un exemple de petit programme qui déclenche un compte à rebours avant de
donner 5 secondes pour appuyer autant de fois que possible sur le bouton de gauche.

```python
from microbit import *

# Compte à rebours
display.set_pixel(0, 2, 9)
sleep(500)
display.set_pixel(1, 2, 9)
sleep(500)
display.set_pixel(2, 2, 9)
sleep(500)
display.set_pixel(3, 2, 9)
sleep(500)
display.set_pixel(4, 2, 9)

# Phase de jeu
button_a.get_presses()     # réinitialise le compteur d'appuis
sleep(5000)                # donne 5 secondes pour jouer
a = button_a.get_presses() # récupère le nombre d'appuis

# Affichage du score
display.scroll("Score: " + str(a))
```

### Exercice 2

**But :** Joseph voudrait connaître le résultat de la multiplication de deux
nombres. Pour récupérer la valeur des deux nombres tu peux donner quelques secondes
à l'utilisateur pour appuyer le bon nombre de fois sur chaque bouton. Par exemple,
si pendant ce temps, tu appuies 3 fois sur le bouton de gauche et 7 fois sur celui 
de droite, le programme affichera `3 * 7 = 21` sur l'écran.

