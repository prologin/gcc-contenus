# ********************* NE PAS TOUCHER AU CODE CI-DESSOUS!!! *********************
import pygame
import sys

# On défini de jolies couleurs;
WHITE = (255, 255, 255)
GREEN = (167, 200, 14)
RED =   (230, 0, 108)


# Si vous voulez changer le nombre de cellules, la taille des cellules et de l'espacement, il faudra changer la longueur et largeur de le fenêtre de jeu

# Les dimensions de notre fenêtre de jeu, pour avoir le meilleur affichage possible avec les dimensions de 50x39
WINDOW_WIDTH = 901
WINDOW_HEIGHT = 703

# On détermine la hauteur et la largeur de chaque cellule
WIDTH = 17
HEIGHT = 17

# Détermine la largeur de l'espace entre chaque cellule
MARGIN = 1

# Pygame initialisation / IMPORTANT

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption("Jeu de la Vie")

def display(grid):
    """
    Fonction qui permet d'afficher le plateau actuel / TRÈS IMPORTANT
    """
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            color = GREEN
            if grid[row][column] == 1:
                color = RED
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
    pygame.quit()

