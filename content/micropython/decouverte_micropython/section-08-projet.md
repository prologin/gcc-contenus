# Projet

Il est maintenant temps de mettre en pratique tout ce que tu as appris au
cours de ce TP avec un petit projet. Rien de compliqué, je te rassure, et puis
si tu as des questions, les organisateurs sont là pour ça !

## But

Joseph est dans la panade... Il aurait besoin de deux dés à 6 faces pour jouer
au Monopoly avec ses amis, mais il les a oubliés, et tout ce qu'il a à sa
disposition est un `micro:bit`...

Joseph te demande alors de lui faire un programme qui simule un lancé de deux
dés et affiche la valeur des deux dés lorsque le bouton A ou le bouton B est
appuyé.

Cependant, comme Joseph ne veut pas que ses amis pensent qu'il a simplement
oublié les vrais dés, il voudrait donc y ajouter quelques fonctionnalités :

- Il voudrait que si le lancé est un double (les 2 dés sont les mêmes), un
smiley content s'affiche juste après les chiffres :

{{<figure src="resources/images/project_first.gif" width=400 caption="Lancé avec un double">}}

- Par contre, il voudrait que si trois doubles sont faits d'affilée, un smiley
pas content s'affiche à la place du smiley content :

{{<figure src="resources/images/project.gif" width=400 caption="3 doubles obtenus">}}

- Il voudrait enfin que le smiley disparaisse 2 secondes après être apparu

On te conseille vivement de faire ce projet étape par étape. Tu peux commencer
par coder le lancé des deux dés, et lorsque cela fonctionne, ajouter les
différentes demandes de Joseph les unes après les autres.

Voici un petit exemple avec les lancés de dés :


De plus, n'hésite pas à poser des questions si tu es bloquée, les organisateurs
seront très contents de t'aider !

<details>
<summary>Besoin d'aide ? Clique ici !</summary>

1. Tu peux utiliser la fonction `display.clear()` pour effacer l'écran.
2. Pour générer un nombre aléatoire, tu peux utiliser et essayer ce bout de
code :

```codepython
# Importe une fonction pour faire de l'aléatoire
from random import randint

# Crée un nombre aléatoire `x` entre 1 et 5
x = randint(0, 5)

# Affiche `x` dans la console
print(x)
```

3. On va avoir besoin de la notion de boucle infinie de la page précédente pour
vérifier si on a appuyé sur un bouton !
4. Tu peux utiliser la fonction `was_pressed()` du bouton A ou du bouton B pour
vérifier s'il est appuyé.

</details>
