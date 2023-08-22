# Fonctionnement de la carte `micro:bit`

## Petit rappel

Même si maintenant tu dois quasiment toutes les connaître, faisons un petit rappel sur les fonctions de base utiles pour manipuler le `micro:bit`.

### L'écran

Les fonctions suivantes te seront utiles pour jouer avec l'écran :


{{< codestep steps=3 lang="py" >}}

{{< codestep-block desc="Allume le pixel sur la 1<sup>ère</sup> colonne et 3<sup>ème</sup> ligne avec une intensité de 6" >}}
display.set_pixel(0, 2, 6)
{{< /codestep-block >}}


{{< codestep-block desc="Éteint tous les pixels de l'écran" >}}
display.clear()
{{< /codestep-block >}}


{{< codestep-block desc="Fait défiler la chaîne de caractères `message`" >}}
display.scroll(message)
{{< /codestep-block >}}

{{< /codestep >}}

### Les boutons

Les boutons nous seront utiles pour faire tourner le serpent. Lorsque l'on appuiera sur le bouton A, on voudra faire tourner dans le sens anti-horaire, tandis que lorsque l'on appuiera sur le bouton B, on fera tourner le serpent dans le sens horaire.

{{< codestep steps=3 lang="py" >}}

{{< codestep-block desc="Renvoie True ou False si les boutons sont appuyés au moment où la ligne est exécutée par le `micro:bit`" >}}
button_a.is_pressed()
button_b.is_pressed()
{{< /codestep-block >}}


{{< codestep-block desc="Renvoie True ou False si les boutons ont été appuyés depuis le dernier appel de ces fonctions" >}}
button_a.was_pressed()
button_b.was_pressed()
{{< /codestep-block >}}


{{< codestep-block desc="Renvoie le nombre d'appuis effectués sur le bouton depuis le dernier appel de ces fonctions" >}}
button_a.get_presses()
button_b.get_presses()
{{< /codestep-block >}}

{{< /codestep >}}

Si tu veux t'amuser à tester la fonction idéale à utiliser pour le déplacement fais toi plaisir. Sinon, clique sur la bande noire ci-dessous pour voir celle qu'on utilisera.

{{< spoiler >}} La fonction idéale pour le déplacement sera la fonction `was_pressed()`. {{< /spoiler >}}