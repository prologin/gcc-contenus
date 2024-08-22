### Un tuyau, ça fait mal.

Maintenant que notre oiseau peut se déplacer comme bon lui semble, allons lui mettre des bâtons dans les roues (enfin, des tuyaux dans les ailes).

{{% box type="exercise" title="Mission : Les tuyaux nous attaquent !" %}}

```py
def deplace_tuyaux(tuy_x, tuy_int, trou_y)
```

Le but de cette fonction est de déplacer les tuyaux vers la gauche.

Tu vas devoir:
- Effacer la colonne des tuyaux ;
- Bouger les tuyaux de 1 cran et les afficher à leur nouvelle position (attention à ne pas te tromper de sens !) ;
- Renvoyer la nouvelle colonne sur laquelle sont les tuyaux.

{{% /box %}}

{{% box type="exercise" title="Mission : Et PAF l'oiseau!" %}}

```py
def collision(ois_x, ois_y, tuy_x, trou_y)
```

Cette fonction renvoie `True` s'il y a une collision entre l'oiseau et les tuyaux et `False` sinon.

Avec l'aide des paramètres, essaye d'écrire cette fonction par toi-même et de gérer tout les cas possibles.

*N'hésite pas à appeler un organisateur si tu veux vérifier si tes conditions sont bonnes.*

<details>
<summary> Si tu veux une description de ce qu'il faut faire, c'est ici </summary>

- Est-ce-que l'oiseau et les tuyaux sont sur la même colonne ? si non, que faut-il renvoyer ?
- Est-ce-que l'oiseau est à l'emplacement du trou ? si oui, que faut-il renvoyer?
- Dans le reste des cas, que faut-il renvoyer ?

</details>

{{% /box %}}
C'est tout bon pour les fonctions, **youpi** ! Maintenant, il va falloir tout assembler dans la boucle `while` pour vérifier si tes fonctions fonctionnent correctement.

Il n'y a pas grand chose à ajouter, mais, par précaution, allons-y étape par étape.

{{% box type="exercise" title="Mission : Déplacer des tuyaux dans la boucle du jeu" %}}

{{% box type="warning" title="Ils vont pas trop vite les tuyaux ?" %}}

Pour que le tuyau n'aille pas trop vite, nous allons le déplacer uniquement à certains moments, au bout d'un certain nombre de tours.

A chaque fois que le programme passe dans la boucle, on va augmenter la valeur de `tour`. Quand cette valeur est égale à `tour_max`, on déplace notre tuyau, puis on réinitialise `tour` à 0.

{{% /box %}}

À la place du `# TODO 2`, on veut donc :

- La condition : si la variable `tour` est égale à `tour_max`, on appelle la fonction `deplace_tuyaux` et on réinitialise la variable `tour` ;

- Puis, à chaque tour, on augmente la variable `tour` de 1.

N'oublie pas de récupérer la valeur que ta fonction renvoie (comme la fonction `deplace_oiseau`).

{{% /box %}}

{{% box type="exercise" title="Mission : La collision avec les tuyaux et notre oiseau dans la boucle du jeu" %}}

Remplace la ligne `# TODO 3` par un appel à la fonction `collision`. Si une collision est détectée, il faut sortir de la boucle.

<details>
<summary> Tu te souviens comment on sort d'une boucle ? </summary>

Le mot-clé magique est le `break`.
Il va nous permettre de sortir de la boucle et d'aller directement à la suite du programme.

</details>

{{% /box %}}

Il ne reste plus qu'à s'occuper du cas où notre oiseau dépasse nos tuyaux.

{{<figure src="resources/images/tuyau_depasse.png" caption="Tuyau dépassé">}}

{{% box type="exercise" title="Mission : Dépassement des tuyaux dans la boucle du jeu" %}}

Il reste ce dernier `if` avec le `# TODO 4`.

Si nos tuyaux passent derrière notre oiseau, on veut :
- Augmenter le score de 1 ;
- Générer un nouveau tuyaux ;
- Effacer les tuyaux ;
- Remettre `tuyau_x` à sa valeur initiale ;
- Afficher les tuyaux.

Attention, il faut laisser le `sleep` à la fin !

{{% /box %}}

Eh, tu ne penses pas qu'il nous manque quelque chose là ?

Quand la partie se termine, il faudrait afficher le score.

{{% box type="exercise" title="Mission : Et mon score, il est où ?" %}}

Tu peux remplacer `# TODO 5` par l'affichage du score comme on te le demande.

{{% /box %}}

Et voilà, tu as fini ton Flappy Bird, tu peux maintenant y jouer et essayer de faire le meilleur score possible !
