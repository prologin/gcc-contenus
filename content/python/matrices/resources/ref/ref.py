# Mission 1 : La carte du monde
carte = [
    ['~', '~', '~', '~', '~', '~'],
    ['~', '~', '#', '%', '~', '~'],
    ['~', '#', '#', '~', '~', '~'],
    ['~', '#', '#', '#', '~', '%'],
    ['~', '%', '~', '~', '~', '~']
]


# Mission 2 : Oust ! Du balai !
carte[3][3] = '@'


# Mission 3 : Vue satellite
def afficher_carte(carte):
    for ligne in carte:
        for element in ligne:
            print(element, end=" ")
        print()

# afficher_carte(carte)


# Mission 4 : Traquer la piraterie
def localiser_bateaux(carte):
    for i in range(len(carte)):
        for j in range(len(carte[0])):
            if carte[i][j] == '%':
                print(i, j)

# localiser_bateaux(carte)


# Mission 5 : Bateau en vue !

def trouver_trajets(carte):
    colonnes = []
    for j in range(len(carte[0])):
        ok = True
        # Peut aussi être fait avec un `while` pour arrêter la boucle dès qu'un
        # obstacle est rencontré, mais c'est un peu plus difficile pour elles.
        for i in range(len(carte)):
            if carte[i][j] != '~':
                ok = False
        if ok:
            colonnes.append(j)
    return colonnes

# print(trouver_trajets(carte))


# Mission 6 : Le Mont Tucán

def profondeur_vers_carte(profondeur):
    carte_tucan = []
    for ligne in profondeur:
        nouvelle_ligne = []
        for prof in ligne:
            if prof > 0:
                nouvelle_ligne.append("#")
            else:
                nouvelle_ligne.append("~")
        carte_tucan.append(nouvelle_ligne)
    return carte_tucan

profondeur = [
    [-4,  -3,  -3,  -3,  -3,  -3,  -5,  -6],
    [-3,  -2,   4,   7,   4,  -2,  -3,  -5],
    [-3,   3,   8,  14,  10,   6,  -2,  -3],
    [-3,   2,   7,  18,  15,   9,   4,  -2],
    [-3,  -2,   4,   8,   6,   3,  -2,  -3],
    [-4,  -3,  -3,  -3,  -3,  -3,  -3,  -4]
]

# carte_tucan = profondeur_vers_carte(profondeur)
# afficher_carte(carte_tucan)
