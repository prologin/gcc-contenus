'''
Exercice 1 : présence dans une matrice
'''

def is_in_matrix(M, val):

    lines = len(M)
    cols = len(M[0])

    for i in range(lines):
        for j in range(cols):
            if M[i][j] == val:
                return True

    return False


'''
Exercice 2 : coordonnées dans une matrice
'''

def search_matrix(M, val):

    lines = len(M)
    cols = len(M[0])

    for i in range(lines):
        for j in range(cols):
            if M[i][j] == val:
                return [i, j]


'''
Exercice 3 : toutes les coordonnées !
'''

def search_all(M, val):

    coord = []

    lines = len(M)
    cols = len(M[0])

    for i in range(lines):
        for j in range(cols):
            if M[i][j] == val:
                coord.append([i, j])

    return coord


'''
Exercice 4 : initialiser une matrice
'''

def set_matrix(lines, cols, val):
    matrix = []
    for lig in range(lines):
        line = []
        for col in range(cols):
            line.append(val)
        matrix.append(line)

    return matrix


'''
Exercice 5 : compter les moutons
'''

def count(P, val):

    count = 0
    lines = len(P)
    cols = len(P[0])

    for i in range(lines):
        for j in range(cols):
            if P[i][j] == val:
                count += 1

    return count


'''
Exercice 5 : afficher une matrice
'''

def print_matrix(M):

    lines = len(M)
    cols = len(M[0])

    for i in range(lines):
        for j in range(cols):
            print(M[i][j], end=" ")

        print()


'''
Exercice 6 : somme des éléments de la matrice
'''

def sum_matrix(M):

    sum = 0

    lines = len(M)
    cols = len(M[0])

    for i in range(lines):
        for j in range(cols):
            sum += M[i][j]

    return sum

'''
Exercice 7 : ajouter deux matrices
'''

def add_matrix(A, B):

    (lines, cols) = (len(A), len(A[0]))

    if (lines, cols) != (len(B), len(B[0])):
        return None

    M = set_matrix(lines, cols, 0)

    for i in range(lines):
        for j in range(cols):
            M[i][j] = A[i][j] + B[i][j]

    return M

'''
Exercice 8 : symetrie sur la diagonale
'''

def symmetricDiag(M):

    lines = len(M)
    cols = len(M[0])

    if lines != cols:
        return False

    for i in range(lines):
        for j in range(cols):
            if (M[i][j] != M[j][i]):
                return False

    return True

'''
Exercice 9 : minimax
'''

def maxList(L):

    maxi = L[0]

    for i in range(len(L)):
        if L[i] > maxi:
            maxi = L[i]

    return maxi

def mini(a, b):

    if (a < b):
        return a
    else:
        return b

def minimax(M):

    mnm = maxList(M[0])

    for i in range(len(M)):
        mnm = mini(mnm, maxList(M[i]))

    return mnm


'''
Exercice 10 : une faim de loup
'''

def eat(M):

    (lines, cols) = (len(M), len(M[0]))

    res = 0

    for i in range(lines):
        for j in range(cols):
            if M[i][j] == 'L':
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if i + k < 0 or i + k >= len(M):
                            continue
                        if j + l < 0 or j + l >= len(M[0]):
                            continue
                        if M[i + k][j + l] == 'M':
                            res += 1
                return res

    return res

'''
Exercice 11 : les cratères de la Lune
'''

def replaceCrater(M, visitedMap, i, j):
    '''
    Visits the whole crater
    '''
    visitedMap[i][j] = True

    if i < 0 or i >= len(M):
        return

    if j < 0 or j >= len(M[0]):
        return

    for k in range(-1, 2):
        for l in range(-1, 2):
            if M[i + k][j + l] == '#' and visitedMap[i + k][j + l] == False:
                replaceCrater(M, visitedMap, i + k, j + l)


def craters(M):
    """
    Counts the number of craters on the map
    """
    nbCraters = 0

    n = len(M)
    m = len(M[0])

    visitedMap = set_matrix(n, m, False)

    for i in range(n):
        for j in range(m):
            if M[i][j] == '#' and visitedMap[i][j] == False:
                replaceCrater(M, visitedMap, i, j)
                nbCraters += 1

    return nbCraters
