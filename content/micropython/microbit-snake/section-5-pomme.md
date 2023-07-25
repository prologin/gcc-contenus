# La pomme

Maintenant que le serpent peut se déplacer, nous pouvons placer des pommes sur le terrain pour le faire grandir.

À chaque tour de boucle :

- S'il n'y a pas de pomme sur le terrain, on en place une de manière aléatoire qui ne soit pas sur le serpent. Pour cela, on choisit aléatoirement deux nombres **X** et **Y**, compris entre 0 et 4, et si le tuple `(X, Y)` ne fait pas partie du serpent, on y ajoute la pomme. Sinon, on recommence le choix de la position.
- Si la tête du serpent atteint une pomme, celle-ci disparait et la taille du serpent augmente de 1.

{{% box type="warning" title="Un peu de challenge ?" %}}

Pour pimenter un peu le jeu, nous te mettons au défi de chercher sur Internet :

- Comment créer un nombre aléatoire **en Python** (pour créer les nouvelles coordonnées de la pomme).

- Comment vérifier si un élément est présent dans une liste **en Python** (pour savoir si ta nouvelle pomme n'est pas dans le serpent).


Si tu ne trouves pas ou que tu veux rester concentrée sur le TP, tu peux aller voir dans la partie _Astuces_ (dans la prochaine section) pour savoir comment générer un nombre aléatoire et comment vérifier si des coordonnées (X, Y) sont présentes dans une liste.
{{% /box %}}


{{% box type="exercise" title="Mission 5 : Abracadabra, les pommes, me voilà" %}}
On arrive à la dernière étape avant que ton jeu corresponde totalement au Snake original ! 
Implémente l'apparition des pommes et ajoute la possibilité qu'elles se fassent manger pour que le serpent augmente de taille.
{{% /box %}}

---
## Conclusion

À ce point, ton jeu Snake devrait être fonctionnel. **Bien joué !** Tu peux essayer ton jeu pour atteindre le score maximal ! Si c'est trop simple, tu peux augmenter la vitesse de déplacement du serpent en mettant un plus petit nombre dans l'instruction `sleep()`.
