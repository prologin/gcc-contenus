# Ton premier programme
## Analysons un programme

Un programme en Python est une série d'instructions exécutées par un ordinateur
(ou dans notre cas par le `micro:bit`). Retiens que chacune d'entre elle doit
être écrite sur une nouvelle ligne et que l'ordinateur lira le programme de 
haut en bas.

Comme premier exemple, analysons ce programme. Tu peux utiliser les flèches à
gauche et à droite de la boîte ci-dessous pour parcourir le code !

{{< codestep steps=4 lang="py" >}}

{{< codestep-block desc="Permet à ton programme d'utiliser le `micro:bit`. Tu devras garder ces lignes tout au long du stage" >}}
# Début du programme

# Importe les fonctions pour le micro:bit
from microbit import *
 
{{< /codestep-block >}}

{{< codestep-block desc="Permet d'allumer un pixel à une position donnée, on t'expliquera plus en détail ce bout de code juste après !" >}}
display.set_pixel(0, 2, 9)
{{< /codestep-block >}}

{{< codestep-block desc="Permet de mettre en pause ton programme pendant quelques temps" >}}
sleep(500)
{{< /codestep-block >}}

{{< codestep-block desc="Répète les deux dernières opérations pour d'autres LEDs" >}}
display.set_pixel(1, 2, 9)
sleep(500)
display.set_pixel(2, 2, 9)
sleep(500)
display.set_pixel(3, 2, 9)
sleep(500)
display.set_pixel(4, 2, 9)

# Fin du programme
{{< /codestep-block >}}

{{< /codestep >}}

Essaye d'envoyer ce programme sur ton `micro:bit` ! Pour cela, rends toi sur le
site [https://python.microbit.org](https://python.microbit.org). Une fois envoyé
sur la carte programmable, le programme devrait afficher une barre de chargement
sur la ligne de diodes centrales.

{{% box type="info" title="C'est quoi les lignes qui commencent par un `#` ?" %}}

Les lignes qui commencent par un `#` sont des commentaires. Ces lignes vont être
ignorées par le `micro:bit`. Ils sont écrits par les développeurs et pour les
développeurs afin de mieux comprendre ce que fait un programme.

{{% /box %}}
