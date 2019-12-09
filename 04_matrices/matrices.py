def initMat(lines, cols, value):

    M = []

    for i in range(l):
        M.append([])
        for j in range(c):
            M[i].append(v)

    return M

def printMat(M):

    l = len(M)
    c = len(M[0])

    for i in range(l):
        for j in range(c):
            print(M[i][j], end="")

        print() #saut à la ligne

def addMat(A, B):

    (l, c) = (len(A), len(A[0]))

    if (l, c) != (len(A), len(B[0])):
        raise Exception("Invalid dimensions")

    M = []

    for i in range(l):
        M.append([])

        for j in range(c):
            M[i].append(A[i][j]+B[i][j])

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

def maxL(L):

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

    mnm = maxL(M[0])

    for i in range(len(M))
        mnm = mini(mnm, maxL(M[i]))

    return mnm

