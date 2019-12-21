'''
Exercice 0 : rechercher dans une matrice
'''

def searchMat(M, val):

    lines = len(M)
    cols = len(M[0])

    for i in range(lines):
        for j in range(cols):
            if M[i][j] == val:
                return i

    return -1


'''
Exercice 1 : initialiser une matrice
'''

def initMat(lines, cols, value):

    M = []

    for i in range(lines):
        M.append([])
        for j in range(cols):
            M[i].append(value)

    return M

'''
Exercice 2 : afficher une matrice
'''

def printMat(M):

    lines = len(M)
    cols = len(M[0])

    for i in range(lines):
        for j in range(cols):
            print(M[i][j], end=" ")

        print()

'''
Exercice 3 : laisser une trace
'''

def trace(M):

    trace = 0
    longueurLigne = len(M[0])

    if longueurLigne != len(M):
        return None;

    for i in range(longueurLigne):
        trace += M[i][i]

    return trace

'''
Exercice 4 : ajouter deux matrices
'''

def addMat(A, B):

    (lines, cols) = (len(A), len(A[0]))

    if (lines, cols) != (len(A), len(B[0])):
        return None

    M = initMat(lines, cols, 0)

    for i in range(lines):
        for j in range(cols):
            M[i][j] = A[i][j] + B[i][j]

    return M

'''
Exercice 5 : symetrie sur la diagonale
'''

def symmetricDiag(M):

    l = len(M)
    c = len(M[0])

    if l != c:
        return False

    i = 0

    while i < l:
        j = 0
        while j < c:
            if M[i][j] != M[j][i]:
                return False

            j += 1

        i += 1

    return True

'''
Exercice 6 : minimax
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

