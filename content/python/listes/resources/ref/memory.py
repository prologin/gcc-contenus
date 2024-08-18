from random import shuffle

# Partie 1 : Créer les différentes listes
solution = ['🦅', '🐶', '🐥', '🐼', '🌹', '🍄'] * 2
shuffle(solution)

partie = ['X'] * len(solution)
print(partie)

# Partie 2 : Créer la boucle de jeu
while 'X' in partie:
    # Partie 3 : Demander les choix pour découvrir
    # les éléments
    choix1 = int(input("Quel indice souhaites-tu jouer ? "))
    partie[choix1] = solution[choix1]
    print(partie)

    choix2 = int(input("Quel indice souhaites-tu jouer ? "))
    partie[choix2] = solution[choix2]
    print(partie)

    # Partie 4 : Vérifier que les choix sont différents
    if partie[choix1] != partie[choix2]:
        partie[choix1] = 'X'
        partie[choix2] = 'X'

# Partie 5 : Afficher une phrase de fin
print("Bravo tu as gagné !")
