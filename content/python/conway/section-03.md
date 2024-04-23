---
show_toc: false
---

# Codons !
Maintenant que tu as vu comment marche le *Jeu de la Vie*, tu vas enfin pouvoir passer à la partie pratique !  
Dans ce TP, tu verras comment générer un plateau et appliquer les règles du jeu pour le faire vivre.

{{% box type="exercise" title="Commencer à coder" %}}

- Télécharge le zip en cliquant sur le bouton `Code à compléter` en haut de la page
- Extrait le zip dans un dossier "game_of_life" afin d'avoir accès au fichier qu'il faut modifier
- Ouvre le fichier `game_of_life.py` dans ton éditeur de texte préféré (Visual Studio Code par exemple)
- Tu peux maintenant compléter le code afin de recréer le *Jeu de la Vie* !

{{% /box %}}

{{% box type="warning" title="Attention !" %}}

Dans le fichier donné, il faudra que tu supprimes les lignes avec `pass` pour exécuter ton code !

{{% /box %}}

## Comment afficher le plateau de jeu ?

Dans le code fourni, il y a une fonction `display(board)` qui permet d'afficher le plateau de jeu donné en paramètres.
Dans la suite du sujet, on représentera une cellule en vie par un **1** et une cellule morte par un **0**.

Si tu as envie de voir un exemple d'affichage, tu peux copier-coller le code python ci-dessous dans la partie du code où tu peux tester ton code (à la fin du fichier) :

```python
board = [
    [0, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1]
]
test_display(board)
```

{{% box type="warning" title="Attention !" %}}

Le plateau que tu veux afficher doit être rectangulaire !

{{% /box %}}

## Combien de cellules sont en vie ?

Avant tout, tu auras besoin de pouvoir compter le nombre de cellules en vie sur ton plateau. Pour ce faire, tu devras coder la fonction `count_cells(board)` présente dans le code fourni qui prend en paramètre un plateau de jeu et renvoie le nombre de cellules en vie.

{{% box type="exercise" title="`count_cells(board)`" %}}

La fonction `count_cells(board)` permet de compter le nombre de cellules vivantes dans le plateau de jeu.

{{% /box %}}

{{% box type="info" title="Rappel" %}}

Une matrice est une liste de listes, pense à cela quand tu essaies d'en parcourir une !

{{% /box %}}
