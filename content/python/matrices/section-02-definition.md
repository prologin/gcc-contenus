# Bienvenue dans la deuxième dimension

Une **matrice** est une sorte de grille, constituée de lignes et de colonnes.
Elle est donc construite comme une liste à deux dimensions, soit une liste
de listes.

Cependant, ce n'est pas tout ! Dans une grille, toutes les lignes
sont de la même longueur. Dans une matrice, c'est pareil : toutes les
sous-listes doivent être de longueur égale.


# Comment créer une matrice ?

Voici un exemple de grille de 3 lignes et 4 colonnes :

<table border="2">
    <colgroup>
        <col width="60">
        <col width="60">
        <col width="60">
        <col width="60">
    </colgroup>
    <tr>
        <td align="center" valign="middle">0</td>
        <td align="center" valign="middle">1</td>
        <td align="center" valign="middle">2</td>
        <td align="center" valign="middle">3</td>
    </tr>
    <tr>
        <td align="center" valign="middle">4</td>
        <td align="center" valign="middle">5</td>
        <td align="center" valign="middle">6</td>
        <td align="center" valign="middle">7</td>
    </tr>
    <tr>
        <td align="center" valign="middle">8</td>
        <td align="center" valign="middle">9</td>
        <td align="center" valign="middle">10</td>
        <td align="center" valign="middle">11</td>
    </tr>
</table>

En Python, tu peux écrire la matrice qui représente cette grille comme ça :

```codepython
# Créer une matrice nommée `ma_matrice`.
ma_matrice = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]

# Afficher la matrice.
print(ma_matrice)
```

Ou pour faciliter sa lecture, tu peux écrire les lignes de la matrice sur des
lignes différentes dans ton fichier.

De plus, tu peux obtenir les dimensions de la matrice :
* Le **nombre de lignes** est le nombre d'éléments de la liste principale, donc
le nombre de sous-listes.
* Le **nombre de colonnes** est le nombre d’éléments dans une sous-liste (par
exemple la première).

```codepython
# Créer la matrice nommée `ma_matrice`, de manière plus lisible.
ma_matrice = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11]
]

# Afficher la matrice.
print(ma_matrice)

# Afficher les dimensions de la matrice.
print("Nombre de lignes :", len(ma_matrice))
print("Nombre de colonnes :", len(ma_matrice[0]))
```


{{% box type="exercise" title="Mission 1 : La carte du monde" %}}

La piraterie fait rage autour d'une petite île dans le Golfe des Parrots.

Julie est chargée de coordonner les marins pour éviter toute altercation avec
les pirates. Pour cela, la technologie est de son côté car elle a accès à
une image satellite de la région :

<style>
    table img {
        pointer-events: none;
    }
</style>

<table cellpadding="0" cellspacing="0" border="2">
    <tr>
        <td style="padding:0; line-height:0;"><img src="resources/images/ile/ile_0_0.png"></td>
        <td style="padding:0; line-height:0;"><img src="resources/images/ile/ile_0_60.png"></td>
        <td style="padding:0; line-height:0;"><img src="resources/images/ile/ile_0_120.png"></td>
        <td style="padding:0; line-height:0;"><img src="resources/images/ile/ile_0_180.png"></td>
        <td style="padding:0; line-height:0;"><img src="resources/images/ile/ile_0_240.png"></td>
        <td style="padding:0; line-height:0;"><img src="resources/images/ile/ile_0_300.png"></td>
    </tr>
    <tr>
        <td style="padding:0; line-height:0;"><img src="resources/images/ile/ile_60_0.png"></td>
        <td style="padding:0; line-height:0;"><img src="resources/images/ile/ile_60_60.png"></td>
        <td style="padding:0; line-height:0;"><img src="resources/images/ile/ile_60_120.png"></td>
        <td style="padding:0; line-height:0;"><img src="resources/images/ile/ile_60_180.png"></td>
        <td style="padding:0; line-height:0;"><img src="resources/images/ile/ile_60_240.png"></td>
        <td style="padding:0; line-height:0;"><img src="resources/images/ile/ile_60_300.png"></td>
    </tr>
    <tr>
        <td style="padding:0; line-height:0;"><img src="resources/images/ile/ile_120_0.png"></td>
        <td style="padding:0; line-height:0;"><img src="resources/images/ile/ile_120_60.png"></td>
        <td style="padding:0; line-height:0;"><img src="resources/images/ile/ile_120_120.png"></td>
        <td style="padding:0; line-height:0;"><img src="resources/images/ile/ile_120_180.png"></td>
        <td style="padding:0; line-height:0;"><img src="resources/images/ile/ile_120_240.png"></td>
        <td style="padding:0; line-height:0;"><img src="resources/images/ile/ile_120_300.png"></td>
    </tr>
    <tr>
        <td style="padding:0; line-height:0;"><img src="resources/images/ile/ile_180_0.png"></td>
        <td style="padding:0; line-height:0;"><img src="resources/images/ile/ile_180_60.png"></td>
        <td style="padding:0; line-height:0;"><img src="resources/images/ile/ile_180_120.png"></td>
        <td style="padding:0; line-height:0;"><img src="resources/images/ile/ile_180_180.png"></td>
        <td style="padding:0; line-height:0;"><img src="resources/images/ile/ile_180_240.png"></td>
        <td style="padding:0; line-height:0;"><img src="resources/images/ile/ile_180_300.png"></td>
    </tr>
    <tr>
        <td style="padding:0; line-height:0;"><img src="resources/images/ile/ile_240_0.png"></td>
        <td style="padding:0; line-height:0;"><img src="resources/images/ile/ile_240_60.png"></td>
        <td style="padding:0; line-height:0;"><img src="resources/images/ile/ile_240_120.png"></td>
        <td style="padding:0; line-height:0;"><img src="resources/images/ile/ile_240_180.png"></td>
        <td style="padding:0; line-height:0;"><img src="resources/images/ile/ile_240_240.png"></td>
        <td style="padding:0; line-height:0;"><img src="resources/images/ile/ile_240_300.png"></td>
    </tr>
</table>

Crée une matrice de caractères nommée `carte` qui représente la carte du monde
ci-dessus.

Utilise les caractères suivants :
* `~` pour l'eau ;
* `#` pour l'île ;
* `%` pour les bateaux pirates.

{{% /box %}}


# Accéder aux éléments

Comme pour les listes à une dimension, tu peux lire et modifier les valeurs.

Pour accéder à un élément de la matrice, il suffit d'écrire :
`matrice[ligne][colonne]`.

```codepython
pairs = [[2, 4, 7], [8, 10, 12]]

# Obtenir la valeur ligne 1 colonne 0.
valeur = pairs[1][0]
print(valeur)

# Modifier la valeur ligne 0 colonne 2.
print(pairs)
pairs[0][2] = 6
print(pairs)
```

{{% box type="exercise" title="Mission 2 : Oust ! Du balai !" %}}

Fais construire un phare en position `(3, 3)` sur la pointe de l'île pour faire
fuir les pirates. Les phares sont représentés par le caractère `@`.

Pour cela, modifie ta matrice `carte`, mais sans changer ton code de la
*Mission 1*.

{{% /box %}}
