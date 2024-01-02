solution = "girlscancode"
tentatives = 7
mot = ["_"] * len(solution)


print(">> Bienvenue dans le pendu <<")

while tentatives > 0 and "_" in mot:
    print("\nMot à deviner :", " ".join(mot))
    proposition = input("Proposez une lettre : ")[0].lower()

    if proposition in solution:
        print("-> Bien vu!")

        # Decouverte de la lettre dans `mot`
        for i in range(len(solution)):
            if solution[i] == proposition:
                mot[i] = proposition

    else:
        print("-> Nope\n")
        tentatives = tentatives - 1

        # Affichage du pendu
        if tentatives == 0:
            print(" ==========Y= ")
        if tentatives <= 1:
            print(" ||/       |  ")
        if tentatives <= 2:
            print(" ||        0  ")
        if tentatives <= 3:
            print(" ||       /|\ ")
        if tentatives <= 4:
            print(" ||       /|  ")
        if tentatives <= 5:
            print("/||           ")
        if tentatives <= 6:
            print("==============\n")

if not "_" in mot:
    print(">>> Gagné! <<<")

print("\n    * Fin de la partie *    ")


