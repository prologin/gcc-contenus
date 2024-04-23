---
show_toc: false
---

# Mise en route de la **VIE** !

Tu y es presque ! Il ne te reste plus qu'à démarrer la vie :D

Rien de plus simple !<br>
Tu peux compléter la fonction `run_game(nb_cell)` en suivant les indications données par les commentaires.

```python
def run_game(nb_cells):
    # Ici tu dois initialiser le plateau du jeu

    while True:
        display(board)
        # Mets ici le code pour mettre à jour le plateau du jeu

        time.sleep(0.2)
```

{{% box type="exercise" title="`run_game(nb_cell)`" %}}

La fonction `run_game(nb_cell)` permet de lancer le jeu avec le nombre de cellules vivantes que tu veux au départ.

{{% /box %}}


<details>
<summary>Indice</summary>

Il faudra utiliser les fonctions `create_board()`, `init_board(board, nb_cell)` et `next_generation(board)`

</details>

Pour lancer le jeu, tu peux rajouter ce bout de code à la fin de ton fichier !
```python
n = int(input("Entre le nombre de cellules que tu veux au début du jeu : "))
run_game(n)
```