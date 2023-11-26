## Afficher le choix du joueur

{{% box type="exercise" title="Exercice 6 : Affichage des choix" %}}

Comme pour le début de la boucle, on souhaite réafficher le choix du joueur
après le `display.clear()` qui éteint tous les pixels.

Après l'affichage du texte "VS", tu dois afficher maintenant le choix
de l'adversaire en prenant une image dans la liste `possibilites` à l'indice
`choix_adversaire`.

{{% /box %}}

## Gagnant et perdant

{{% box type="exercise" title="Exercice 7 : Qui a gagné ? Qui a perdu ?" %}}

Maintentant qu'on a le choix du joueur et celui de l'adversaire, on peut savoir
qui a gagné et qui a perdu ! Pour ce faire, on va d'abord vérifier s'il y a
égalité entre les deux joueurs.

Il y a égalité entre les deux joueurs dans notre jeu quand le choix de
notre adversaire et le même que le nôtre en vérifiant l'égalité
entre `choix_joueur` et `choix_adversaire`. Dans ce cas, tu dois afficher sur le
`micro:bit` "Egalite !" avec une vitesse d'affichage de 50.

Sinon, s'il n'y a pas égalité, il faut vérifier les conditions pour savoir
si tu as gagné. Attention, tu devras alors afficher "Gagne !" avec une vitesse
d'affichage de 50. Les conditions sont les suivantes :

- Si `choix_joueur` est égal à 0 et `choix_adversaire` est égal à 1
(Skeleton fait peur à Pacman)

- Si `choix_joueur` est égal à 1 et `choix_adversaire` est égal à 2
(Pacman mange Bouh)

- Si `choix_joueur` est égal à 2 et `choix_adversaire` est égal à 0
(Bouh fait peur à Skeleton)

Sinon, si toutes les conditions au-dessus ne sont pas remplies,
cela veut dire que tu as perdu et il faut que tu affiches "Perdu..." avec
une vitesse d'affichage de 50.

{{% /box %}}

{{% box type="info" title="La vitesse d'affichage ?" %}}

La fonction `display.scroll()` de la librairie `micro:bit` va afficher un texte
avec une vitesse de 150 unités de base. Pour modifier cette dernière, tu peux
rajouter un paramètre à la fonction comme dans l'exemple suivant qui va afficher
"Hello World" avec une vitesse de 50 unités.

```python
display.scroll("Hello World", delay=50)
```

Si la valeur du paramètre est inférieure à 150, le texte sera afficher plus
rapidement ; sinon, il sera plus lent.

{{% /box %}}
