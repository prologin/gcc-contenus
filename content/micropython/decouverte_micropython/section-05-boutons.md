# Comment utiliser les boutons du `micro:bit` ?

Comme tu peux le voir, il y a deux boutons physiques sur le `micro:bit` : le
**bouton A <font color=#00AFD4>(1)</font>** et le **bouton B
<font color=#A7C80F>(2)</font>**. Il existe également un **bouton tactile
<font color=#E5006C>(3)</font>** au niveau du logo au-dessus de l'écran. 

{{<figure src="resources/images/microbit_buttons.webp" width=400 caption="Boutons du `micro:bit`">}}

## Nombre d'appuis

Pour utiliser les boutons A et B, tu peux respectivement utiliser la fonction
`button_a.get_presses()` et `button_b.get_presses()`.

Ces fonctions renvoient le nombre d'appuis sur le bouton depuis la dernière fois
qu'elles ont été appelées.

Par exemple, ce code va afficher le nombre de fois que le bouton A a été appuyé
au cours des 5 premières secondes du programme :

```python
# Importe les fonctions pour le micro:bit
from microbit import *

# Compte à rebours
display.set_pixel(0, 2, 9)
sleep(1000)
display.set_pixel(1, 2, 9)
sleep(1000)
display.set_pixel(2, 2, 9)
sleep(1000)
display.set_pixel(3, 2, 9)
sleep(1000)
display.set_pixel(4, 2, 9)
sleep(1000)

# Récupère le nombre d'appuis sur le bouton A
a = button_a.get_presses()

# Affiche le nombre d'appuis sur le bouton A
display.scroll("Total : " + str(a))
```

{{% box type="exercise" %}}

Crée un programme qui affiche la somme du nombre d'appuis sur les boutons A et B
au cours des 3 dernières secondes. Pour faire ce programme, tu peux t'aider de
variables !

{{% /box %}}

## Un exemple un peu plus complexe

À toi de jouer ! Que fais le programme d'après toi ? Essaye de le lancer sur ton
`micro:bit` !


```python
# Importe les fonctions pour le micro:bit
from microbit import *

# Compte à rebours
display.set_pixel(0, 2, 9)
sleep(1000)
display.set_pixel(1, 2, 9)
sleep(1000)
display.set_pixel(2, 2, 9)
sleep(1000)
display.set_pixel(3, 2, 9)
sleep(1000)
display.set_pixel(4, 2, 9)
sleep(1000)

# Récupère le nombre d'appuis sur le bouton A
a = button_a.get_presses()

# Affiche le nombre d'appuis sur le bouton A
display.scroll("Total : " + str(a))

# Que se passe-t-il ici ?
display.scroll("Ici ?" + str(a))

# Que se passe-t-il ici ?
a = button_a.get_presses()
display.scroll("Et ici ?" + str(a))
```

Si tu ne comprends pas ce qu'il se passe n'hésites surtout pas à demander aux organisateurs !

{{% box type="exercise" %}}

Lily voudrait connaître le résultat de la multiplication de deux nombres.
Pour récupérer la valeur des deux nombres tu peux donner quelques secondes à
l’utilisateur pour appuyer le bon nombre de fois sur chaque bouton.

Par exemple, si pendant ce temps, tu appuies 3 fois sur le bouton de gauche 
et 7 fois sur celui de droite, le programme affichera `3 * 7 = 21` sur l’écran.

{{% /box %}}

