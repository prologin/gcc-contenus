# Comment utiliser les boutons du `micro:bit` ?

Comme tu peux le voir, il y a deux boutons physiques sur le `micro:bit` : le
**bouton A <font color=#00AFD4>(1)</font>** et le **bouton B
<font color=#A7C80F>(2)</font>**. Il existe également un **bouton tactile
<font color=#E5006C>(3)</font>** au niveau du logo au-dessus de l'écran. 

{{<figure src="resources/images/microbit_buttons.png" width=400 caption="Boutons du micro:bit">}}

Pour utiliser les boutons A et B, tu peux respectivement utiliser la fonction
`button_a.get_presses()` et `button_b.get_presses()`. Ces fonctions renvoient le
nombre d'appuis sur le bouton depuis la dernière fois qu'elles ont été appelées.
Par exemple, ce code va prendre le nombre de fois que le bouton A a été appuyé
au cours des 5 premières secondes du programme :

```python
# Importe les fonctions pour le micro:bit
from microbit import *

# Attend 5 secondes
sleep(5000)

# Affiche le nombre d'appuis
display.scroll(button_a.get_presses())
```

{{% box type="info" title="Ça va trop vite !" %}}

Pour mettre en pause ton programme (si tu veux avoir le temps de voir ce qu'il
se passe), tu peux utiliser la fonction `sleep(millisecondes)`.

{{% /box %}}

<br>

{{% box type="exercise" title="Mission 2 : Addition" %}}

Crée un programme qui affiche la somme du nombre d'appuis sur les boutons A et B
au cours des 3 dernières secondes. Pour faire ce programme, tu peux t'aider de
variables !

{{% /box %}}

En ce qui concerne le bouton tactile, tu peux détecter si tu appuies dessus
en utilisant la fonction `pin_logo.is_touched()`, qui renvoie un booléen (`True`
ou `False`).

## Un exemple un peu plus complexe

À toi de jouer ! Que fais le programme d'après toi ? Essaye de le lancer sur ton
`micro:bit` !


```python
# Importe les fonctions pour le micro:bit
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

# Attends 5 secondes
sleep(5000)

# Récupère le nombre d'appuis sur le bouton A
a = button_a.get_presses()

# Affiche le score
display.scroll("Score : " + str(a))
```

<details>
<summary>Clique ici pour avoir la réponse !</summary>

Voici un exemple d'un petit programme qui déclenche un compte à rebours avant de
donner 5 secondes pour appuyer autant de fois que possible sur le bouton de 
gauche.

</details>

<br>

{{% box type="exercise" title="Mission 3 : Calculatrice compacte" %}}

Joseph voudrait connaître le résultat de la multiplication de deux nombres.
Pour récupérer la valeur des deux nombres tu peux donner quelques secondes à
l’utilisateur pour appuyer le bon nombre de fois sur chaque bouton.

Par exemple, si pendant ce temps, tu appuies 3 fois sur le bouton de gauche 
et 7 fois sur celui de droite, le programme affichera `3 * 7 = 21` sur l’écran.

Pour réaliser cette mission, tu peux t'inspirer du code juste au-dessus !

{{% /box %}}

