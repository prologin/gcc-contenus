# Fonctionnement de la carte `micro:bit`

## L'écran

Chaque pixel de l'écran est une LED rouge, que l'on peut allumer ou éteindre à un certain degré d'intensité allant de 0 à 9 (0 -> éteinte, 9 -> allumée au max). La ligne de code ci-dessous allumera le pixel de la première ligne et troisième colonne au niveau 6.

```py
# Attention, la numérotation des lignes et des colonnes commence à 0
# Cette ligne va allumer le pixel sur la 1ère ligne et 3ème colonne,
# Avec une intensité lumineuse de 6.
display.set_pixel(0, 2, 6)
```

Il pourra vous être utile de réinitialiser l'écran et d'éteindre toutes les LEDs d'un coup. Pour cela, on utilise la fonction suivante.

```py
# Cette commande a le même effet que faire display.set_pixel(...) avec une intensité de 0
# 25 fois (pour chaque pixel) !
display.clear()
```

## Les boutons

Afin de pouvoir diriger notre serpent, nous allons utiliser les boutons A et B sur les côtés de l'écran. Quand on tient la carte `micro:bit` dans le bon sens, le bouton A est à gauche et le bouton B est à droite. On souhaite que l'appui sur le bouton A fasse tourner le serpent à gauche, et le bouton B à droite.

Reste à savoir comment être alerté dans notre code quand un bouton a été appuyé. Il existe pour cela 3 fonctions utiles.

```py
# Ces fonctions renvoient True ou False si les boutons sont
# appuyés quand la ligne est exécutée par le micro:bit
button_a.is_pressed()
button_b.is_pressed()

# Ces fonctions renvoient True ou False si les boutons ont
# été appuyés depuis le dernier appel à ces fonctions
button_a.was_pressed()
button_b.was_pressed()

# Ces fonctions renvoient le nombre d'appuis effectués sur
# le bouton depuis le dernier appel à ces fonctions
button_a.get_presses()
button_b.get_presses()
```

Pour ce projet, le plus pratique est d'utiliser `was_pressed()` pour pouvoir orienter le serpent en conséquence.

