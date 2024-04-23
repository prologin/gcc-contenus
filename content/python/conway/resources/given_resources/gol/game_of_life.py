import time
import random
from lib_gol import *

# Ci-dessous, code la fonction count_cells
def count_cells(board):
    """
    La fonction count_cells permet de compter le nombre de cellules vivantes dans le plateau de jeu
    """
    pass


# Ci-dessous, code la fonction create_board
def create_board():
    """
    La fonction creer_plateau permet de créer un plateau de jeu avec 50 colonnes et 39 lignes
    """
    pass


# Ci-dessous, code la fonction init_board
def init_board(board, nb_cell):
    """
    La fonction init_plateau permet de placer EXACTEMENT nb_cellules vivantes dans le plateau donné
    """
    pass


# Ci-dessous, code la fonction count_neighbors
def count_neighbors(board, i, j):
    """
    La fonction voisinage permet de compter le nombre de voisines vivantes d'une cellule placée aux coordonnées (i,j)
    """
    pass

#Ci-dessous, code la fonction next_generation
def next_generation(board):
    """
    La fonction next_generation permet de renvoyer la prochaine génération du plateau
    """
    pass


# Ci-dessous, code la fonction run_game
def run_game(nb_cell):
    """
    La fonction run_game permet de lancer le jeu avec le nombre de cellules vivantes que tu veux au départ
    """

    # Ici tu dois initialiser le plateau du jeu

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        display(board)
        # Mets ici le code pour mettre à jour le plateau du jeu

        time.sleep(0.2)

# Écris ce que tu veux ici :)


