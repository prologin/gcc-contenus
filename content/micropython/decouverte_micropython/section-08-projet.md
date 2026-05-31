# Projet

Il est maintenant temps de mettre en pratique tout ce que tu as appris au
cours de ce TP avec un petit projet. Rien de compliqué, je te rassure, et puis
si tu as des questions, les organisateurs et organisatrices sont là pour ça !

## But

Lily est dans la panade... Elle aurait besoin de deux dés à 6 faces pour jouer
au Monopoly avec ses amis, mais elle les a oubliés, et tout ce qu'elle a à sa
disposition est un `micro:bit`...

Lily te demande alors de lui faire un programme qui simule un lancé de deux
dés et affiche la valeur des deux dés lorsque l'un des boutons (A ou B) est
appuyé.

Cependant, comme Lily ne veut pas que ses amis pensent qu'elle a simplement
oublié les vrais dés, elle voudrait donc y ajouter quelques fonctionnalités :

- Elle voudrait que si le lancé est un double (les 2 dés sont les mêmes), un
smiley content s'affiche juste après les chiffres :

{{<figure src="resources/images/project_first.gif" width=400 caption="Lancé avec un double">}}

- Par contre, elle voudrait que si trois doubles sont faits d'affilée, un
smiley pas content s'affiche à la place du smiley content :

{{<figure src="resources/images/project.gif" width=400 caption="3 doubles obtenus">}}

- Elle voudrait enfin que le smiley disparaisse 2 secondes après être apparu

On te conseille vivement de faire ce projet étape par étape. Tu peux commencer
par coder le lancer des deux dés, et lorsque cela fonctionne, ajouter les
différentes demandes de Lily les unes après les autres.

*Peu importe ton avancé sur le projet, n'hésite pas à poser des questions si
tu es bloquée, les organisatrices et organisateurs seront très content·e·s de
t'aider !*

{{% box type="exercise" title="Projet partie 1 : Lancé simple" %}}

Tout d'abord, il faut détecter quand le bouton **A ou B** est appuyé.

Lorsque l'un des deux boutons (A ou B) est pressé, tu peux lancer les deux dés,
stocker leurs valeurs, puis les afficher.

{{% /box %}}

{{% box type="info" title="Nombres aléatoires" %}}

Pour obtenir un nombre aléatoire, tu peux utiliser ce code :

{{< codestep steps=3 lang="py" >}}

{{< codestep-block desc="Importe les fonctions pour utiliser l'aléatoire" >}}
from random import randint
{{< /codestep-block >}}

{{< codestep-block desc="Génère un nombre aléatoire entre 0 et 2 et le stocke dans la variable `nb_aleatoire`" >}}
nb_aleatoire = randint(0, 2)
{{< /codestep-block >}}

{{< codestep-block desc="Affiche le contenu de la variable `nb_aleatoire` sur l'écran du `micro:bit`" >}}
display.scroll(nb_aleatoire)
{{< /codestep-block >}}

{{< /codestep >}}

{{% /box %}}

<details>
<summary>Besoin d'aide ? Clique ici !</summary>

Si tu es bloquée, n'hésites pas à appeler quelqu'un pour venir t'aider et même
te réexpliquer une page que tu n'aurais pas bien comprise. On est là pour ça !

Tu peux aussi revoir dans les pages précédentes comment détecter le clic d'un
bouton (la page s'appelle *« Comment utiliser les boutons du micro:bit ? »*).

Tu auras aussi besoin de la notion de boucle infinie, expliquée dans la page
(*« Ça fait beaucoup de lignes »*).

</details>

{{% box type="exercise" title="Projet partie 2 : Double" %}}

Lors d'un lancer, si les deux dés ont la même valeur (on appelle ça un
*double*), Lily aimerait qu'un smiley content s'affiche sur l'écran.

Elle aimerait aussi que ce smiley disparaisse au bout de 2 secondes. 

{{<figure src="resources/images/project_first.gif" width=400 caption="Lancé avec un double">}}

{{% /box %}}

{{% box type="info" title="Effacer l'écran" %}}
Pour effacer l'écran du micro:bit, tu peux utiliser la fonction
`display.clear()`.
{{% /box %}}

<details>
<summary>Besoin d'aide ? Clique ici !</summary>

Maintenant qu'on a les valeurs des deux dés, il te suffit de regarder si le
lancer est un double, et d'afficher un smiley si besoin.

Si tu ne voit pas comment faire, tu peux relire les parties sur les
conditions (sur la page *« Et si... »*) et les booléens (sur la page
*« Une mémoire de poisson rouge »* dans la partie *« J’affirme ! »*).

Encore une fois, n'hésites pas à nous demander de l'aide pour t'aider à
comprendre. (Promis c'est pas fun de se tourner les pouces en vous regardant
coder haha !)

</details>

{{% box type="exercise" title="Projet partie 3 : Trois doubles d'affilée" %}}

En plus de tout ça, Lily aimerait que si trois lancers de suite sont des
*doubles*, un smiley **pas content** s'affiche à la place du smiley **content**.

Ce nouveau smiley doit aussi disparaître après 2 secondes.

{{<figure src="resources/images/project.gif" width=400 caption="3 doubles obtenus">}}

{{% /box %}}

<details>
<summary>Besoin d'aide ? Clique ici !</summary>

La première chose à faire est de connaître le nombre de doubles qui ont été
obtenus **d'affilée**. C'est-à-dire l'un à la suite de l'autre.

Une fois que c'est fait, tu peux afficher le smiley **pas content** lorsqu'il
y a **3** doubles d'affilée.

Tu auras besoin d'une **variable** pour compter le nombre de doubles qui ont
été obtenus d'affilée. Comme dans la partie *« Une variable score »* à la fin
de la page précédente.

Cette partie peut être compliquée, n'hésite pas à appeler un·e orga !

</details>
