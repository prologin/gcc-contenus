# Les fonctions du `micro:bit`

Cette partie regroupe toutes les fonctions de contrôle du `micro:bit` que nous
avons utilisées au cours de ce TP. Tu en verras aussi des nouvelles que nous
n'avons pas abordées, mais leur utilisation se base sur le même principe que les
autres. 
Si tu souhaites aller encore plus loin, tu peux trouver des informations plus
complète sur la documentation officielle en ligne trouvable ici:
[https://bbcmicrobitmicropython.readthedocs.io/en/latest/](https://bbcmicrobitmicropython.readthedocs.io/en/latest/).

Pour utiliser toutes ces fonctions il est nécessaire de les importer depuis le
module `micro:bit` en ajoutant `from microbit import *` au début de ton
programme.

## L'écran

### `display.clear()` - effacer l'écran

```python
display.clear()  # l'écran est maintenant éteint
```

### `display.set_pixel(x, y, value)` - allumer/éteindre un pixel

Change la luminosité d'une diode pour une valeur allant de 0 (diode éteinte), à
9 (luminosité maximale).

La diode est identifiée par sa colonne `x` et sa ligne `y` numérotée de 0 à 4.

```python
display.set_pixel(2, 2, 9)  # allume la diode centrale
display.set_pixel(0, 0, 5)  # allume à moitié la diode d'en haut à gauche
display.set_pixel(4, 4, 0)  # éteint la diode d'en bas à droite
```

### `display.get_pixel(x, y)` - calcule la luminosité d'un pixel

Réciproquement à `display.set_pixel(x, y, value)`, `display.get_pixel(x, y)`
récupère la valeur de luminosité d'une diode identifiée par sa colonne `x` 
et sa ligne `y`.

```python
display.set_pixel(2, 2, 9)  # allume la diode centrale
a = display.get_pixel(2, 2)  # `a` vaut maintenant 9
```

### `display.show(image)` - afficher une image

Cette fonction sert à afficher une image, le plus simple est généralement
d'utiliser une image parmi la liste prédéfinie : `Image.HEART`, `Image.HAPPY`,
`Image.HAPPY`, `Image.SAD`, `Image.YES`, `Image.NO`, ... Une liste plus complète
peut être trouvée [ici](https://microbit-micropython.readthedocs.io/en/latest/image.html#attributes).

```python
display.show(Image.HAPPY)  # affiche un smiley
display.show(Image.HEART)  # affiche un coeur
```

Il est aussi possible de dessiner soi-même une image à partir d'un texte en
séparant les lignes avec `:` et assignant une luminosité entre 0 et 9 à chaque
diode :

```python
bateau = Image('05050:'
               '05050:'
               '05050:'
               '99999:'
               '09990')

# Affiche une image qui ressemblera à peu près à ça:
#        x x
#        x x
#        x x
#       OOOOO
#        OOO
display.show(bateau)
```

### `display.scroll(texte)` - afficher du texte

Fait défiler le texte donné en entrée.

```python
display.scroll('Salut tout le monde !')  # affiche `Salut [...] !`
display.scroll(42)  # en réalité ça ne fonctionne pas qu'avec le texte !
```

## Les boutons

Il y a deux boutons sur le `micro:bit`, ils sont appelés `button_a` et
`button_b` et toute fonction qui peut être appelée pour l'un, peut aussi être
appelée pour l'autre.

### `button_a.is_pressed()` - état du bouton

Renvoie `True` si le bouton est actuellement enfoncé.

```python
while True:
    if button_b.is_pressed():
        # Allume la diode centrale si le bouton de droite est enfoncé
        display.set_pixel(2, 2, 9)
    else:
        # Éteint la diode si le bouton de droite n'est plus enfoncé
        display.set_pixel(2, 2, 0)
```

### `button_a.was_pressed()` - le bouton a été enfoncé

Renvoie `True` si le bouton a été enfoncé depuis la dernière fois que cette
fonction a été appelée.

```python
display.scroll('Appuyez sur le bouton de gauche pour arrêter le programme')

# Si le bouton n'a pas été enfoncé pendant que le texte défilait, on peut
# continuer le programme
if not button_a.was_pressed():
    display.scroll('Et bien continuons le programme ...')
    # ...
```

### `button_a.get_presses()` - nombre d'appuis sur le bouton

Renvoie le nombre total d'appuis sur le bouton depuis la dernière fois que
cette fonction a été appelée.

```python
sleep(5000)
nb_appuis = button_b.get_presses()
display.scroll(
    'Vous avez appuyé '
    + str(nb_appuis)
    + ' fois sur le bouton b en 5 secondes.'
)
```

## Les fonctions générales

### `sleep(millisecondes)` - Mettre en pause le programme

### `randint(min, max)` - De l'aléatoire

Renvoie un nombre entier aléatoire compris entre `min` et `max`. 

```python
from random import randint

display.scroll(randint(1, 10))
```

