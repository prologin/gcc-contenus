# Construire une matrice

Maintenant que tu sais parcourir une matrice à l'aide d'une double boucle `for`,
et si on créait des matrices de la taille que l'on souhaite ?

Toutes les fonctions des listes à une dimension que tu as appris (`append`,
`pop`, `insert`) fonctionnent aussi sur les matrices puisque ce sont des listes
de listes ! On peut alors créer une matrice en ajoutant des éléments à des
listes, puis en ajoutant ces listes à une liste principale, tout cela avec
l'aide de la fonction `append`.

Créons une matrice remplie de perroquets 🦜 :

```codepython
# Mets les dimensions que tu souhaites.
nb_lignes = 2
nb_colonnes = 3
# On part d'une liste vide.
matrice = []

for i in range(nb_lignes):
    # On construit une ligne puis on l'ajoute à la matrice.
    ligne = []
    for j in range(nb_colonnes):
        ligne.append("🦜")
    matrice.append(ligne)

print(matrice)
```


{{% box type="warning" title="Modifications involontaires" %}}

Est-ce que tu arrives à trouver et à comprendre le problème qui survient dans le
code suivant ?

```codepython
# Création de la matrice.
matrice = []
ligne = [1, 2, 3, 4]
for i in range(3):
    matrice.append(ligne)

# Modification du premier élément de la première ligne... et pas que ?
print(matrice)
matrice[0][0] = 7
print(matrice)
```

{{< details summary="Clique ici pour avoir les explications !" >}}

Les trois lignes de `matrice` correspondent en fait une seule et même liste
(`ligne`), et non trois listes différentes comme on pourrait le penser. Ainsi,
lorsque tu modifies une ligne, toutes les autres lignes sont modifiées de la
même manière !

{{< /details >}}

{{% /box %}}


{{% box type="exercise" title="Mission 6 : Le Mont Tucán" %}}

Située dans le Golfe des Parrots, l'île volcanique du Mont Tucán est
particulièrement convoitée en raison des nombreux trésors qu’elle abrite, ce qui
la rend très susceptible d’attirer des pirates.

Par conséquent, Julie souhaite surveiller cette région de très près. Ses
collègues en charge des données satellites lui ont fourni la carte
correspondante, mais sous forme de carte de profondeur : une matrice de nombres
qui représentent l'altitude de chaque parcelle de la zone.

Ta mission est d'écrire une fonction `profondeur_vers_carte(profondeur)` qui
convertit la carte de profondeur en une carte de symboles. Toutes les parcelles
au-dessus du niveau de la mer (altitude positive) sont considérées comme des
morceaux d'île (`#`), sinon elles sont considérées comme de l'eau (`~`).

Attention, tu n'as pas le droit de modifier la matrice `profondeur`. Tu dois
**créer une toute nouvelle matrice et la retourner**.

Voici la carte de profondeur fournie par l'équipe de Julie :

```python
profondeur = [
    [-4,  -3,  -3,  -3,  -3,  -3,  -5,  -6],
    [-3,  -2,   4,   7,   4,  -2,  -3,  -5],
    [-3,   3,   8,  14,  10,   6,  -2,  -3],
    [-3,   2,   7,  18,  15,   9,   4,  -2],
    [-3,  -2,   4,   8,   6,   3,  -2,  -3],
    [-4,  -3,  -3,  -3,  -3,  -3,  -3,  -4]
]
```

Teste le code suivant et regarde s'il t'affiche bien la carte du dessous :

```python
carte_tucan = profondeur_vers_carte(profondeur)
afficher_carte(carte_tucan)
```

```text {nocopy=true}
~ ~ ~ ~ ~ ~ ~ ~
~ ~ # # # ~ ~ ~
~ # # # # # ~ ~
~ # # # # # # ~
~ ~ # # # # ~ ~
~ ~ ~ ~ ~ ~ ~ ~
```

{{% /box %}}
