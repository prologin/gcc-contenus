import pygame
import time
import random

WINDOW_WIDTH = 901
WINDOW_HEIGHT = 703

# Define some colors
WHITE = (255, 255, 255)
GREEN = (167, 200, 14)
BLUE = (0, 175, 212)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 17
HEIGHT = 17

# This sets the margin between each cell
MARGIN = 1

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption("Jeu de la Vie")


# Fonction qui permet d'afficher le plateau actuel / TRÈS IMPORTANT
def display(grid):
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            color = GREEN
            if grid[row][column] == 1:
                color = BLUE
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
    pygame.display.flip()

def test_display(grid):
    display(grid)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        touches = pygame.key.get_pressed()
        if touches[pygame.K_q]:
            break

#ref count_cells
def count_cells(grid):
    res = 0
    n = len(grid)
    for i in range(n):
        m = len(grid[i])
        for j in range(m):
            if grid[i][j] == 1:
                res += 1
    return res

#ref create random board
def create_board():
    board = []
    for i in range(39):
        temp = [0] * 50
        board.append(temp)
    
    return board

def init_board(board, nb):
    while nb > 0:
        row = random.randint(0, 39 - 1)
        col = random.randint(0, 50 - 1)
        if board[row][col] == 0:
            board[row][col] = 1
            nb -= 1

    return board

# ref count_neighbors
def count_neighbors(board, row, column):
    count = 0

    nb_rows = 39
    nb_cols = 50

    if row - 1 >= 0:
        if column - 1 >= 0 and board[row - 1][column - 1] == 1:
            count += 1
        if board[row - 1][column] == 1:
            count += 1
        if column + 1 < nb_cols and board[row - 1][column + 1] == 1:
            count += 1

    if row + 1 < nb_rows:
        if column - 1 >= 0 and board[row + 1][column - 1] == 1:
            count += 1
        if board[row + 1][column] == 1:
            count += 1
        if column + 1 < nb_cols and board[row + 1][column + 1] == 1:
            count += 1

    if column - 1 >= 0 and board[row][column - 1] == 1:
        count += 1
    if column + 1 < nb_cols and board[row][column + 1] == 1:
        count += 1
    return count

# ref next_generation
def next_generation(board):
    ret_board = []
    for i in range(len(board)):
        temp = []
        for j in range(len(board[i])):
            count = count_neighbors(board, i, j)
            if board[i][j] == 0 and count == 3:
                temp.append(1)
            elif board[i][j] == 1:
                if count == 2 or count == 3:
                    temp.append(1)
                else:
                    temp.append(0)
            else:
                temp.append(0)
        ret_board.append(temp)
    return ret_board

def run_game(nb):
    # ici tu dois initialiser le plateau du jeu
    board = create_board()
    board = init_board(board, nb)

    while True:
        display(board)
        # Mets ici la fonction pour mettre à jour le plateau du jeu
        board = next_generation(board)
        time.sleep(0.2)

#ref
run_game(int(input("Entrez le nombre de cellules que tu veux au début du jeu: ")))

pygame.quit()
