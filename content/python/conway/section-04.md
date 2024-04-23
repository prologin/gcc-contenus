---
show_toc: false
---

# Créer le plateau de jeu !

Maintenant, tu vas devoir coder la fonction `create_board()` qui renvoie un plateau de cellules mortes de dimensions : **50 colonnes 39 lignes**.

{{% box type="exercise" title="`create_board()`" %}}

La fonction `create_board()` permet de créer un plateau de jeu avec 50 colonnes et 39 lignes.

{{% /box %}}


Pour tester ton code, tu peux mettre le bout de code suivant à la fin de ton fichier. Attention à bien supprimer ce code après le test !
```python
board = create_board()
print("Le plateau comporte bien 39 lignes : ", len(board) == 39)
res = True
for i in range(len(board)):
    if len(board[i]) != 50:
        res = False
        break
print("Le plateau comporte bien 50 colonnes sur chaque ligne : ", res)
```

# Initialiser le plateau de jeu !

Une fois que le plateau du jeu est créé, il faut l'initialiser en utilisant la fonction : `init_board(board, nb_cell)`, qui renvoie le *plateau* avec `nb_cell` vivantes réparties au hasard sur le plateau.

{{% box type="exercise" title="`init_board(board, nb_cell)`" %}}

La fonction `init_board(board, nb_cell)` permet de placer **EXACTEMENT** `nb_cellules` vivantes dans le plateau donné.

{{% /box %}}

{{% box type="warning" %}}

Si les coordonnées générées aléatoirement tombent sur une cellule vivante (**1**) alors, il faut générer de nouvelles coordonnées pour placer notre cellule, sans réduire le nombre de cellules restantes à placer.

{{% /box %}}

{{% box type="info" title="Random" %}}

Pour générer un nombre entre *i* et *j*, tu peux utiliser `random.randint(i,j)` !

{{% /box %}}

Pour tester ton code, tu peux mettre le bout de code suivant à la fin de ton fichier. Attention à bien supprimer ce code après le test !
```python
board = create_board()
board = init_board(board, 100)
if count_cells(board) == 100:
    print("Bravo!")
```