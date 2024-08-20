# Partie 1 : Initialiser le jeu
pendu = ["\n===========Y=\n ||/\n ||\n ||\n ||\n/||\n==============\n", "\n===========Y=\n ||/       |\n ||\n ||\n ||\n/||\n==============\n", "\n===========Y=\n ||/       |\n ||        0\n ||\n ||\n/||\n==============\n", "\n===========Y=\n ||/       |\n ||        0\n ||       /|\n ||\n/||\n==============\n", "\n===========Y=\n ||/       |\n ||        0\n ||       /|\\\n ||\n/||\n==============\n", "\n===========Y=\n ||/       |\n ||        0\n ||       /|\\\n ||       /\n/||\n==============\n", "\n===========Y=\n ||/       |\n ||        0\n ||       /|\\\n ||       / \\\n/||\n==============\n"]

solution = "prologin"
partie = ['_'] * len(solution)
vies = 7

print("Bienvenue dans le jeu du Pendu !")

# Partie 2 : Créer la boucle de jeu
while '_' in partie and vies > 0:
    # Partie 3 : Afficher l'avancement actuel et
    # demander une propostion
    mot = ' '.join(partie)
    print("Mot à deviner :", mot)

    proposition = input("Quelle lettre souhaites-tu proposer ? ")
    lettre = proposition[0]

    # Partie 4 : Vérifier si la proposition
    # est dans la solution
    if lettre in solution:
        print("Tu viens de trouver une lettre !\n")

        for i in range(len(solution)):
            if lettre == solution[i]:
                partie[i] = solution[i]

    # Partie 5 : Enlever une vie si la
    # proposition n'est pas bonne
    else:
        print("Tu viens de perdre une vie !")
        vies -= 1
        print(pendu[7 - vies - 1])

# Partie 6 : Afficher la solution
print("Le mot à trouver était :", solution)

if vies == 0:
    print("Tu n'as pas pu trouver le mot...")
else:
    print("Bravo, tu as gagné !")
