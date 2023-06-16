## La boucle du jeu pour la sélection du personnage

### La condition de la boucle

L'utilisateur du `micro:bit` doit choisir son personnage. Pour faire cela,
on va utiliser une boucle `while` (tant que). Il va falloir alors trouver
une condition pour rester dans la sélection. Pour valider, le joueur devra
appuyer sur les deux boutons du `micro:bit` en même temps.

Dans la condition de ta boucle, il faut vérifier si les boutons A et B ne
sont pas pressés. Tu vas devoir alors utiliser le `and` et le `not`, deux mots-clés
utilisés pour les variables booléennes et les conditions.

N'hésite pas à appeler un organisateur si tu ne te souviens plus !

### Afficher le choix du joueur

Tant qu'on reste dans notre boucle `while`, il va falloir afficher le choix
qui est actuellement sélectionné. Pour ce faire, tu peux utiliser la fonction
`display.show()` avec comme paramètre l'image dans la liste `possibilites` à
l'indice du choix du joueur défini par la variable `choix_joueur`.

### Changer de choix

On va utiliser les boutons A et B pour changer de choix. Sachant qu'on a la
variable `possibilites` qui garde nos images et `choix_joueur` qui désigne le
choix du joueur, il ne reste plus qu'à augmenter ou diminuer `choix_joueur` pour
changer notre choix.

Si le bouton A a été appuyé, il faut enlever 1 au nombre désignant le choix du
joueur. Par la suite, sur ce nouveau nombre, il te faut rester dans l'intervalle
des indices de notre liste `possibilites`. Il va alors falloir rajouter un `%`
(modulo) !

{{% box type="info" title="Un modu-quoi ?" %}}

Le modulo, il faut le prendre comme le reste d'une division euclidienne.
Par exemple, quand tu souhaites diviser 5 par 2, tu auras le quotient qui est
égal à 2 et le reste qui est égal à 1.

On va utiliser le même procédé. On ne peut pas accéder au cinquième élément
d'une liste de longueur 3. On va donc revenir à 0 lorsqu'on dépasse la longueur de la liste.

Par exemple, lorsque tu es à l'indice 3 dans une liste de longueur 3 : les indices
possibles sont 0, 1 et 2. On voudrait que revenir à l'indice 0. En Python,
tu peux le faire comme ceci :

```codepython
# Une liste de nombres
ma_liste = [42, 56, 98]

# On est à l'indice 3
mon_indice = 3

# Le nouvel indice est 3 modulo 3 = 0
# car le reste de la division euclidienne de 3 par 3 est égal à 0
mon_nouvel_indice = 3 % 3

# L'élément à l'indice 0 (3 % 3)
mon_element = ma_liste[mon_nouvel_indice]

# Affiche `mon_element`
print(mon_element)
```

{{% /box %}}

Maintenant, tu dois faire la même chose pour le bouton B, seulement,
cette fois-ci, si le bouton B a été appuyé, il faut rajouter 1 au nombre
désignant le choix du joueur. N'oublie pas le modulo !

