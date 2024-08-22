### D'où viennent ces tuyaux ?

Dans cette partie, on va faire apparaître et disparaître des tuyaux de hauteurs aléatoires.

Nos tuyaux vont être représentés par une ligne de pixels d'intensité 5 (`tuyaux_intensite = 5`) et qui apparaîtront sur la 5e colonne du `micro:bit` (`tuyau_x = 4`).

Nous allons créer un trou dans le tuyau pour que l'oiseau puisse passer. Il devra faire 2 pixels de hauteur et commencera à `trou_y` : les pixels `trou_y` et `trou_y + 1` seront donc éteints.

{{<figure src="resources/images/tuyaux_explications.png" caption="Tuyau">}}

{{% box type="exercise" title="Mission : Un peu d'aléatoire voyons" %}}

```py
def genere_trou()
```
Cette fonction n'affiche rien, elle renvoie juste un nombre aléatoire qui sera la coordonnée de `trou_y`.
Donc la position du trou entre les tuyaux, par lequel Flappy peut passer.

{{% box type="warning" title="Il est où le trou ?" %}}

N'oublie pas que le trou fait 2 pixels de hauteur, il faut donc que la valeur renvoyée ne soit pas trop grande...

{{% /box %}}

Pour pouvoir faire de l'aléatoire en Python, nous allons utiliser la fonction `randint`.

<details>
<summary> Si tu ne te rappelles plus de comment l'utiliser, clique ici. </summary>

Tu peux donc appeler `randint(i, j)` qui te renverra une valeur entre `i` et `j` **compris**.

```codepython
from random import randint

# Affichera un nombre entre 5 et 1000
print(randint(5, 1000))

```

</details>

{{% /box %}}

{{% box type="exercise" title="Mission : Abracadabra, tuyaux te voilà." %}}

```py
def affiche_tuyaux(tuy_x, tuy_int, trou_y)
```
Affiche les tuyaux et le trou.

Pour cela, nous te conseillons d'allumer toute la rangée du tuyau puis d'éteindre les pixels représentant le trou.

{{% /box %}}

{{% box type="exercise" title="Mission : Abracadabra, tuyaux te voilà... disparu ?" %}}

```py
def efface_tuyaux(tuy_x)
```
Fais disparaître le tuyau de la colonne `tuyau_x`.

{{% /box %}}

Tu n'as rien à ajouter dans la boucle de jeu `while` mais si tu lances ton programme tu devrais pouvoir voir une colonne de tuyaux apparaître avec un trou de 2 de hauteur dedans.

{{% box type="info" title="Testons" %}}

Pour tester que tout fonctionne, tu peux ajouter les lignes suivantes dans ton `while` :

```py
trou_y = genere_trou()
efface_tuyaux(tuyau_x)
affiche_tuyaux(tuyau_x, tuyaux_intensite, trou_y)

```

**N'oublie pas de les enlever pour la suite**.

{{% /box %}}
