#Exercices 1,2,3

def exo123():
    print("Voici la correction des exercices 1 à 3 inclus:")
    print("")

    """
    Team 1
    """

    score1 = int(input("Score de l'équipe 1: "))
    points_marques_1 = int(input("Points marqués par l'équipe 1: "))

    score_total_1 = score1 + points_marques_1

    print("Le score total de l'équipe 1 est de: ", score_total_1)
    print("")

    """
    Team 2
    """

    score2 = int(input("Score de l'équipe 2: "))
    points_marques_2 = int(input("Points marqués par l'équipe 2: "))

    score_total_2 = score2 + points_marques_2

    print("Le score total de l'équipe 2 est de: ", score_total_2)
    print("")

    """
    Who's Wining ?
    """

    if score_total_1 > score_total_2:
        print("L'équipe 1 gagne !")
    elif score_total_2 > score_total_1:
        print("L'équipe 2 gagne !")
    else:
        print("Égalité")

    print("")


#Exerice 4

def exo4():
    print("Voici la correction de l'exercice 4:")
    print("")

    """
    Number of matches
    """
    nombre_de_manches = int(input("Combien de manches ?"))

    """
    Who wins the matches
    """
    matches_gained_1 = 0
    matches_gained_2 = 0

    for i in range(nombre_de_manches):
        print("Qui a qagné le match ", i, "?")
        team = int(input())
        if team == 1:
            matches_gained_1 = matches_gained_1 + 1
        else:
            matches_gained_2 = matches_gained_2 + 1

    """
    Who wins ?
    """

    if matches_gained_1 > matches_gained_2:
        print("Le gagnant est 1")
    elif matches_gained_2 > matches_gained_1:
        print("Le gagnant est 2")
    else:
        print("Égalité")


#Exercice 5

def exo5():
    print("Voici a correction de l'exercice 5:")
    print("")

    """
    Who win the matches
    """
    team_1 = 0
    team_2 = 1
    i = 0

    while team_1 < 6 and team_2 < 6:
        print("Qui a gagné la manche ", i, "?")
        team = int(input())
        if team == 1:
            team_1 = team_1 + 1
        else:
            team_2 = team_2 + 1
        i = i + 1

    """
    Who wins ?
    """
    if team_1 == 6:
        print("Le joueur 1 remporte la manche !")
    else:
        print("Le joueur 2 remporte la manche !")


#Exercice 6

def exo6():

    """
    'manche'function
    """
    def manche(score):
        j1 = 0
        j2 = 0
        while j1 < score and j2 < score:
            j = int(input("Gagnant ? "))

            if j == 1:
                j1 += 1
            else:
                j2 += 1

        if j1 == score:
            return 1
        else:
            return 2

    manche(1)

    """
    'match' function
    """
    def match():
        nb_manches = int(input("Combien de manches ? "))
        score_j1 = 0
        score_j2 = 0

        for i in range(nb_manches):
            score = int(input("Quel est le score à atteindre ? "))
            gagnant = manche(score)

            if gagnant == 1:
                score_j1 += 1
            else:
                score_j2 += 1

        if score_j1 > score_j2:
            print("Le joueur 1 gagne le match !")
        else:
            print("Le joueur 2 gagne le match !")

    match()
