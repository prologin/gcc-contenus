## La boucle du jeu pour la sélection du personnage

L'utilisateur du `micro:bit` doit choisir son personnage. Pour faire cela,
on va utiliser une boucle `while` (tant que). Il va falloir alors trouver
une condition pour rester dans la sélection. Pour valider, le joueur devra
appuyer sur les deux boutons du `micro:bit` en même temps.

{{% box type="exercise" title="Exercice 2 : La sélection du personnage" %}}

Dans la condition de ta boucle, à la place du booléen `False`, il faut vérifier
si les boutons A et B ne sont pas pressés simultanément. Tu vas devoir alors
utiliser le `and` et le `not`, deux mots-clés utilisés pour les variables
booléennes et les conditions. Comme pour les calculs mathématiques, tu peux
également utiliser des parenthèses dans ta condition pour effectuer une
opération sur un groupe de conditions.

N'hésite pas à appeler un organisateur si tu ne te souviens plus !

{{% /box %}}

{{% box type="exercise" title="Exercice 3 : Affichage du choix actuel" %}}

Tant qu'on reste dans notre boucle `while`, il va falloir afficher le choix
qui est actuellement sélectionné. Pour ce faire, tu peux utiliser la fonction
`display.show()` avec comme paramètre l'image dans la liste `possibilites` à
l'indice du choix du joueur défini par la variable `choix_joueur`.

{{% /box %}}

{{% box type="exercise" title="Exercice 4 : Changement de choix" %}}

On va utiliser les boutons A et B pour changer de choix. Sachant qu'on a la
variable `possibilites` qui garde nos images et `choix_joueur` qui désigne le
choix du joueur, il ne reste plus qu'à augmenter ou diminuer `choix_joueur` pour
changer notre choix.

Si le bouton A a été appuyé, il faut enlever 1 au nombre désignant le choix du
joueur. Cependant, il se peut qu'à un moment donné, tu sors en dehors ta liste.
Pour éviter cela, tu peux utiliser des conditions ou des modulos (`%`).

Nous allons voir en détails les conditions, mais si tu souhaites utiliser Les
modulos, n'hésite pas à appeler un organisateur pour qu'il puisse t'aider !

Il faut vérifier si `choix_joueur` n'est plus dans ta liste, c'est-à-dire si
l'index qu'il représente n'est pas possible dans la liste `possibilites`. Pour
rappel, les valeurs possibles sont `0`, `1` et `2` dans la liste.

Maintenant, tu dois faire la même chose pour le bouton B, seulement,
cette fois-ci, si le bouton B a été appuyé, il faut rajouter 1 au nombre
désignant le choix du joueur. N'oublie pas le modulo !

{{% /box %}}
