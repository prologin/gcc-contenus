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

- Par contre, elle voudrait que si deux doubles sont faits d'affilée, un smiley
pas content s'affiche à la place du smiley content :

{{<figure src="resources/images/project.gif" width=400 caption="2 doubles obtenus">}}

- Elle voudrait enfin que le smiley disparaisse 2 secondes après être apparu

On te conseille vivement de faire ce projet étape par étape. Tu peux commencer
par coder le lancer des deux dés, et lorsque cela fonctionne, ajouter les
différentes demandes de Lily les unes après les autres.


De plus, n'hésite pas à poser des questions si tu es bloquée, les orgas seront
très contents de t'aider !

{{< details summary="Besoin d'aide ? Clique ici !" >}}

1. Tu peux utiliser la fonction `display.clear()` pour effacer l'écran.
2. Pour générer un nombre aléatoire, tu peux utiliser et essayer ce bout de
code :

```codepython
# Importe une fonction pour faire de l'aléatoire
from random import randint

# Crée un nombre aléatoire `x` entre 0 et 3
x = randint(0, 3)

# Affiche `x` dans la console
print(x)
```

3. On va avoir besoin de la notion de boucle infinie de la page précédente pour
vérifier si on a appuyé sur un bouton !
4. Si tu veux vérifier que le bouton A (ou le bouton B respectivement) a
été pressé, tu peux utiliser la fonction `button_a.was_pressed()`
(ou `button_b.was_pressed()`).

{{< /details >}}
