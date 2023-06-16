# Ton premier programme
## Analysons un programme

Un programme en Python est constitué d'une série d'instructions qui sont exécutées par un
ordinateur (dans notre cas, le `micro:bit`). Chaque instruction doit être écrite
sur une nouvelle ligne, et le programme sera lu par l'ordinateur de haut en bas.
Commençons par analyser un premier exemple de programme très basique :

```python
# Debut du programme

from microbit import *

display.set_pixel(0, 2, 9)
sleep(500)
display.set_pixel(1, 2, 9)
sleep(500)
display.set_pixel(2, 2, 9)
sleep(500)
display.set_pixel(3, 2, 9)
sleep(500)
display.set_pixel(4, 2, 9)

# Fin du programme
```

Si tu flash ce programme sur ton `micro:bit`, il affiche une barre de chargement
sur la ligne de diodes centrales de ton `micro:bit`.

Exécutons 'à la main' ce petit programme pour comprendre ce qu'il fait : 

1. `from microbit import *` permet de lier la bibliothèque de fonctions
   `micro:bit` à ton programme, pour que l'ordinateur puisse comprendre ce que
   font les fonctions que tu vas utiliser.  Sans cela, le programme ne sait pas ce
   que doivent faire les commandes qui permettent d'utiliser le `micro:bit`. Cette
   ligne est très importante car sans elle, ton programme ne pourra pas
   fonctionner. 
2. Nous avons ensuite une ligne vide. Cela n'a aucune influence sur le
   comportement de ton code, il ne faut donc pas hésiter à t'en servir pour
   espacer ton programme. Cela rend ton code plus lisible pour toi comme pour les
   personnes qui voudront le lire.
3. `display.set_pixel(0, 2, 9)` est une fonction propre au `micro:bit`, elle
   permet d'allumer le pixel situé sur la colonne n°0 et la ligne n°2. Son
   comportement est expliqué plus en détail juste après. 
4. `sleep(500)` est aussi une fonction propre au `micro:bit`. Elle met l'exécution 
   du programme en pause pendant 500 millisecondes. Essaye de supprimer cette 
   ligne, le programme s'exécute tellement vite que tu n'as pas le temps de voir
   qu'une diode s'allume avant l'autre !
5. La suite du programme se répète : on allume les diodes des colonnes numéro 1,
   2, 3 puis 4.



## Et les `#` c'est quoi ?

Les lignes qui commencent par un `#` sont des commentaires. Un commentaire, c'est
une suite de mots qui n'est pas lue par l'ordinateur. Ils sont 
écrits par les développeurs et pour les développeurs afin de mieux comprendre ce
que fait un programme. 

Pour ce qui concerne les commentaires commençant par un `#`, cela signifie que
tout ce qui se trouve après le `#` sur la ligne ne sera pas lu par l'ordinateur. 
Ce sont des commentaires _courts_. 
Il existe aussi des commentaires _longs_ que tu pourras rencontrer au cours des
TPs. C'est la même chose que les commentaires courts, mais sur plusieurs lignes.
En Python, ils commencent et finissent en écrivant `"""` avant et après ton
commentaire. 

Voici un exemple pour que ce soit plus clair :
```python
# Ceci est un commentaire sur une seule ligne

"""
Ceci est un 
commentaire
sur plusieurs
lignes
"""

ceci_n_est_pas_un_commentaire # Mais ça oui
```

Les commentaires courts sont d'ailleurs facilement repérable par leur couleur
grise.  

