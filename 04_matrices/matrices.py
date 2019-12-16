'''
Exercice 1 : initialiser une matrice
'''

def initMat(lines, cols, value):

    M = []

    for i in range(l):
        M.append([])
        for j in range(c):
            M[i].append(v)

    return M

'''
Exercice 2 : afficher une matrice
'''

def printMat(M):

    lines = len(M)
    cols = len(M[0])

    for i in range(lines):
        for j in range(cols):
            print(M[i][j], end="")

        print()

'''
Exercice 3 : laissons une trace
'''

def trace(m):

    trace = 0
    longueurLigne = len(M[0])

    for i in range(longueurLigne):
        trace += m[i][i]

    return trace

'''
Exercice 4 : ajoutons deux matrices
'''

def addMat(A, B):

    (lines, cols) = (len(A), len(A[0]))

    if (lines, cols) != (len(A), len(B[0])):
        raise Exception("Invalid dimensions")

    M = initMat(lines, cols, 0)

    for i in range(lines):
        for j in range(cols):
            M[i][j] = A[i][j] + B[i][j]

'''
Exercice 5 : symetrie sur la diagonale
'''

def symmetricDiag(M):

    l = len(M)
    c = len(M[0])

    if l != c:
        return False

    i = 0
    ok = True

    while i < l and ok:
        j = 0
        while j < c and ok:
            if M[i][j] != M[j][i]:
                ok = False

            j += 1

        i += 1

    return ok

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

    if (a < b)
        return a
    else
        return b

def minimax(M):

    mnm = maxListe(M[0])

    for i in range(len(M))
        mnm = mini(mnm, maxListe(M[i]))

    return mnm

