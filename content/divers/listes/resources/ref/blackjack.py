import random

deck = [
    ("2", "Trèfle"), ("3", "Trèfle"), ("4", "Trèfle"), ("5", "Trèfle"), ("6", "Trèfle"), ("7", "Trèfle"), ("8", "Trèfle"),
    ("9", "Trèfle"), ("10", "Trèfle"), ("Valet", "Trèfle"), ("Dame", "Trèfle"), ("Roi", "Trèfle"), ("As", "Trèfle"),

    ("2", "Coeur"), ("3", "Coeur"), ("4", "Coeur"), ("5", "Coeur"), ("6", "Coeur"), ("7", "Coeur"), ("8", "Coeur"),
    ("9", "Coeur"), ("10", "Coeur"), ("Valet", "Coeur"), ("Dame", "Coeur"), ("Roi", "Coeur"), ("As", "Coeur"),

    ("2", "Pique"), ("3", "Pique"), ("4", "Pique"), ("5", "Pique"), ("6", "Pique"), ("7", "Pique"), ("8", "Pique"),
    ("9", "Pique"), ("10", "Pique"), ("Valet", "Pique"), ("Dame", "Pique"), ("Roi", "Pique"), ("As", "Pique"),

    ("2", "Carreau"), ("3", "Carreau"), ("4", "Carreau"), ("5", "Carreau"), ("6", "Carreau"), ("7", "Carreau"), ("8", "Carreau"),
    ("9", "Carreau"), ("10", "Carreau"), ("Valet", "Carreau"), ("Dame", "Carreau"), ("Roi", "Carreau"), ("As", "Carreau"),
]

main_joueur = []
main_dealer = []

jeu_fini = False


def valeur_carte(carte):
    if carte[0] == "Valet" or carte[0] == "Dame" or carte[0] == "Roi":
        return 10
    elif carte[0] == "As":
        return 11
    return int(carte[0])


# Donne les cartes au joueur + dealer
random.shuffle(deck)
for i in range(2):
    carte_joueur = deck.pop()
    main_joueur.append(carte_joueur)

    carte_dealer = deck.pop()
    main_dealer.append(carte_dealer)

# Affichage des cartes de départ
carte1_dealer = main_dealer[0]
print("Le croupier a un", carte1_dealer[0], "de", carte1_dealer[1])

print("Vous avez :")
for carte in main_joueur:
    print(carte[0], "de", carte[1])

score_joueur = valeur_carte(main_joueur[0]) + valeur_carte(main_joueur[1])

print("Vous avez un score de", score_joueur)

# Vérifier les blackjack
if score_joueur == 21:
    print("Bravo ! Vous avez un blackjack !")

else:
    while not jeu_fini:
        # Demande au joueur ce qu'il veut faire
        choix_joueur = input("Que voulez-vous faire ? Tirer une carte (c) ou ne rien faire (r) ? ")
        if choix_joueur == "c":
            nouvelle_carte_joueur = deck.pop()
            print("Vous avez tiré un", nouvelle_carte_joueur[0], "de", nouvelle_carte_joueur[1])
            main_joueur.append(nouvelle_carte_joueur)

            score_joueur += valeur_carte(nouvelle_carte_joueur)
            print("Votre score est maintenant de", score_joueur)
            if score_joueur > 21:
                jeu_fini = True
                print("Dommage... Vous avez dépassé 21, vous avez perdu")
        else:
            jeu_fini = True

    if score_joueur <= 21: # Le joueur n'a pas encore perdu
        print("La 2e carte du croupier est", main_dealer[1][0], "de", main_dealer[1][1])
        score_dealer = valeur_carte(main_dealer[0]) + valeur_carte(main_dealer[1])
        print("Son score est de", score_dealer)

        while score_dealer < 17:
            nouvelle_carte_dealer = deck.pop()
            print("Le croupier a tiré un", nouvelle_carte_dealer[0], "de", nouvelle_carte_dealer[1])
            main_dealer.append(nouvelle_carte_dealer)
            score_dealer += valeur_carte(nouvelle_carte_dealer)
            print("Son score est maintenant de", score_dealer)

        if score_dealer > 21:
            print("Le croupier a dépassé 21, vous avez gagné !")
        elif score_dealer > score_joueur:
            print("Le croupier a un score plus élevé, vous avez perdu")
        elif score_dealer < score_joueur:
            print("Vous avez un score plus élevé que le croupier, vous avez gagné !")
        else:
            print("Vous avez le même score que le croupier : égalité")