---
show_toc: false
---

# Comptons les voisins !
Maintenant que nous avons un plateau et des cellules vivantes éparpillées, il faut appliquer les règles du *Jeu de la Vie* et pour cela nous avons besoin de savoir combien de voisines vivantes a chaque cellule en codant la fonction `count_neighbors(board, i, j)` !

{{% box type="exercise" title="`count_neighbors(board, i, j)`" %}}

La fonction `count_neighbors(board, i, j)` permet de compter le nombre de voisines vivantes d'une cellule placée aux coordonnées `(i,j)`

{{% /box %}}

{{% box type="warning" title="" %}}

Fais bien attention à ne pas sortir des bords du tableau ! Afin d'éviter cela, tu peux dire que :

- si tu es sur la première ligne alors tu ne vérifie pas si les trois voisines de la ligne du dessus sont vivantes ;
- si tu es sur la dernière ligne alors tu ne vérifie pas si les trois voisines de la ligne du dessous sont vivantes ;
- si tu es sur la première colonne alors tu ne vérifie pas si les trois voisines de la colonne de gauche sont vivantes ;
- si tu es sur la dernière colonne alors tu ne vérifie pas si les trois voisines de la colonne de droite sont vivantes.

{{% /box %}}

Pour tester ton code :
```python
board = [[1,1,0],
         [1,0,0],
         [0,0,1]]
if (count_neighbors(board, 1, 1) == 4):
    print("Bravo!")
```

## La Next-Gen ?
Tu as maintenant tout ce qu'il te faut pour pour appliquer les règles du *Jeu de la Vie*, il ne te reste plus qu'à passer à la prochaine génération avec la fonction `next_generation(board)` !

{{% box type="exercise" title="`next_generation(board)`" %}}

La fonction `next_generation(board)` permet de renvoyer la prochaine génération du plateau.

{{% /box %}}

Cette fonction va te permettre d'appliquer les règles du *Jeu de la Vie* sur chaque cellule en fonction de son nombre de voisines vivantes, pour cela tu devras utiliser la fonction `count_neighbors(board, i, j)` que tu as codée juste avant !

{{% box type="info" title="Conseils pour bien réussir" %}}

Pour cette fonction il est préférable de jongler entre deux tableaux, le premier, le tableau actuel sur lequel on determine pour chaque cellule si elle doit rester en vie, naître ou mourir. 
Et le second sur lequel on va mettre le résultat obtenu pour chaque cellule, une fois que tout le premier tableau est parcouru, on copie le deuxième sur le premier et on réinitialise le deuxième.

{{% /box %}}

Pour tester ton code :
```python
board = [[1,1,0],
         [1,0,0],
         [0,0,0]]
if next_generation(board) == [[1,1,0],[1,1,0],[0,0,0]]:
    print("Bravo!")
```