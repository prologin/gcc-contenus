## Fonctionnement de la carte `micro:bit`

### Petit préambule

Voici les fonctions spécifiques au `micro:bit` qui te seront utiles pour la suite de ce TP. N'hésite pas à les tester de ton côté si tu ne te rappelles pas de ce qu'elles font.

*Sur les blocs suivants, n'hésite pas à cliquer sur les flèches pour avoir des détails sur ce que font les fonctions.*

### L'écran


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

Les boutons te seront utiles pour faire monter et descendre l'oiseau. Bien qu'il existe plusieurs fonctions associées aux boutons, tu n'auras besoin que de celles ci-dessous.

{{< codestep steps=2 lang="py" >}}

{{< codestep-block desc="Renvoie True ou False si le `button_a` a été appuyé depuis le dernier appel de cette fonction" >}}
button_a.was_pressed()
{{< /codestep-block >}}

{{< codestep-block desc="Renvoie True ou False si le `button_b` a été appuyé depuis le dernier appel de cette fonction" >}}
button_b.was_pressed()
{{< /codestep-block >}}

{{< /codestep >}}
