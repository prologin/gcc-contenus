# Analysons un programme

Un programme c'est simplement une série de d'instructions, de choses à faire.

Si les `micro:bit` parlaient français, voici à quoi ressemblerait un programme :

```txt {nocopy=true}
Affiche un point au centre
Affiche "Bonjour !"
Si j'appuie sur le bouton A :
    Affiche un coeur
```

Malheureusement, les cartes `micro:bit` ne comprennent que le *Python*. Le but
de ce stage est donc de voir comment écrire nos commandes en utilisant le
langage *Python*.

Comme premier exemple, analysons ce programme :

{{< codestep steps=4 lang="py" >}}

{{< codestep-block desc="Permet à ton programme d'utiliser le `micro:bit`. Elle doit toujours être écrite en haut de ton programme 1 fois." >}}
# Indique qu'on va écrire des commandes pour le microbit
from microbit import *
 
{{< /codestep-block >}}

{{< codestep-block desc="Allume une des LED de l'écran." >}}
display.set_pixel(0, 2, 9)
{{< /codestep-block >}}

{{< codestep-block desc="Attends quelque temps avant de lire la suite." >}}
sleep(500)
{{< /codestep-block >}}

{{< codestep-block desc="Répète les deux dernières opérations avec d'autres LED." >}}
display.set_pixel(1, 2, 9)
sleep(500)
display.set_pixel(2, 2, 9)
sleep(500)
display.set_pixel(3, 2, 9)
sleep(500)
display.set_pixel(4, 2, 9)
{{< /codestep-block >}}

{{< /codestep >}}

{{% box hint %}}

Tu peux utiliser les flèches à gauche et à droite de la boîte ci-dessus pour
parcourir le code !

{{% /box %}}

Essaye d'envoyer ce programme sur ton `micro:bit` ! Pour cela, rends-toi sur le site
[https://python.microbit.org](https://python.microbit.org), 
supprime le texte déjà écrit et copie-colle celui de l'exemple.

{{% box hint %}}

Tu peux utiliser le bouton `Copier` pour copier tout le code !

{{% /box %}}

Tu peux ensuite appuyer sur le bouton violet en bas à gauche "Send to micro:bit", et suivre les
commandes.

Une fois envoyé, tu devrais voir une barre de chargement s'afficher sur ton
`micro:bit`.

{{% box type="info" title="Et les lignes qui commencent par `#` ?" %}}

Les lignes qui commencent par un `#` sont des commentaires.

Ces lignes vont être ignorées par le `micro:bit`. Ils sont écrits par les
développeurs et développeuses afin de mieux comprendre ce que fait un
programme.

{{% /box %}}
