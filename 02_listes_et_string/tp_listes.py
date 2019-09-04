#
#   L I S T S
#

# ex1

def init_list(n):
    '''
    stocke les entiers de 1 à n compris dans une liste et la retourne.
    '''
    return [i for i in range (n + 1)]

#ex2

def is_in(k, L):
    '''
    renvoie Vrai si k est présent dans la liste, Faux autrement.
    '''
    for i in range(len(L)):
        if L[i] == k:
            return True
    return False

#ex3

def pos(k, L):
    '''
    renvoie la position de k si k  est présent dans la liste, -1 autrement.
    '''
    for i in range(len(L)):
        if L[i] == k:
            return i
    return -1

#ex4

def maximum(L):
    '''
    renvoie la valeur du maximum de la liste L.
    '''
    maxi = L[0]
    for i in range(1, len(L)):
        if L[i] > maxi:
            maxi = L[i]
    return maxi

def pos_max(L):
    '''
    renvoie la position du maximum dans la liste L.
    '''
    maxi = L[0]
    posmax = 0
    for i in range(1, len(L)):
        if L[i] > maxi:
            maxi = L[i]
            posmax = i
    return posmax

#ex5

def sum_list(L):
    '''
    renvoie la valeur de la somme des éléments de la liste L.
    '''
    s = 0
    for i in range(len(L)):
        s += L[i]
    return s

#ex6

def square(L):
    '''
    renvoie une nouvelle liste LS contenant les éléments de la liste L au carré.
    '''
    LS = []
    for i in range(len(L)):
        LS.append(L[i] * L[i])
    return LS

#ex7

def fact(n):
    '''
    renvoie la liste LF qui contient les factorielles de 0 à n.
    '''
    LF = [1] * n
    for i in range(1, n):
        LF[i] = LF[i - 1] * i
    return LF

#ex8

def double(L):
    '''
        teste si la liste contient deux entiers identiques consecutifs.
    '''
    i = 1
    while i < len(L)-1:
        if L[i-1] == L[i]:
            return True
        i += 1
    return False

#
#   S T R I N G S
#

#ex1

def palindrome(s):
    '''
    teste si la chaîne s est un palindrome.
    '''
    i = 0
    n = len(s)
    while (i < n//2) and (s[i] == s[n-i-1]):
        i = i+1
    return (i == n//2)

#ex2

def count(c, s):
    '''
    renvoie le nombre de fois que l'on peut trouver le caractère c dans la chaîne s.
    '''
    cpt = 0
    for i in range(len(s)):
        if s[i] == c:
            cpt += 1
    return cpt

#
#   B O N U S
#

#ex1

def trier(L):
    '''
    renvoie la liste L triée selon l'algorithme de tri à bulles.
    '''
    length = len(L)
    for i in range(length):
        for j in range(0, length - i - 1):
            if L[j] > L[j+1] :
                L[j], L[j+1] = L[j+1], L[j]
    return L

#ex2

def binsearch(L, l, r, e):
    '''
    renvoie la position de l'élément e dans la liste L selon la recherche dichotomique.
    '''
    if r < l :
        return -1
    else :
        m = l + (r - l) / 2
        if L[m] == e :
            return m
        else :
            if L[m] > e :
                return binsearch(L[m:len(L)], e)
            else :
                return binsearch(L[0:m], e)

#ex3

def tictac(n):
    '''
    affiche un compte a rebours de facon récursive.
    '''
    if n == -1:
        print("Boum!")
    else:
        print(n)
        tictac(n - 1)

def fibo(n):
    '''
    renvoie le n-ième nombre de la suite de Fibonacci.
    '''
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

