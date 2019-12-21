#!/usr/bin/python3

import sys, importlib

tp = sys.argv[1]
if tp[-3:] == ".py":
    tp = tp[:-3]
tp = importlib.import_module(tp)


m1 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
     ]

m2 = [
        [42,42],
        [42,42],
        [42,42]
     ]

mDiag = [
        [1,2,3],
        [2,1,5],
        [3,5,1]
     ]

mnm = [
        [11, 42, 39],
        [12, 15, 86],
        [98, 56, 27]
      ]


def test(f, inp, out):
    inpp = ", ".join(str(x) for x in inp)
    print(f"{f.__name__}({inpp}) =", end=" ")
    try:
        res = f(*inp)
        print(f"{res}", end=" ")
        if res == out:
            print("\033[0;32m [OK] \033[0m")
        else:
            print(f"| Attendu: {out} \033[0;31m [KO]\033[0m")
    except Exception as e:
        print(e, "\033[0;31m [K0] \033[0m")


# Exercice 0 : rechercher dans une matrice
try:
    test(tp.searchMat, [m1, 1], 0)
    test(tp.searchMat, [m1, 5], 1)
    test(tp.searchMat, [m1, 8], 2)
    test(tp.searchMat, [m1, 42], -1)
except Exception as e:
    print(e)

print()


# Exercice 1 : initialiser une matrice
try:
    test(tp.initMat, [3, 2, 42], [[42,42],[42,42],[42,42]])
    test(tp.initMat, [2, 2, 2], [[2,2],[2,2]])
    test(tp.initMat, [0, 2, 1], [])
    test(tp.initMat, [3, 0, 5], [[],[],[]])
except Exception as e:
    print(e)

print()


# Exercice 3 : trace
try:
    test(tp.trace, [m1], 15)
    test(tp.trace, [m2], None)
except Exception as e:
    print(e)

print()


# Exercice 4 : ajouter deux matrices
try:
    test(tp.addMat, [m1, m1], [[2,4,6],[8,10,12],[14,16,18]])
    test(tp.addMat, [m1, m2], None)
except Exception as e:
    print(e)

print()


# Exercice 5 : symetrie sur la diagonale
try:
    test(tp.symmetricDiag, [m1], False)
    test(tp.symmetricDiag, [mDiag], True)
except Exception as e:
    print(e)

print()


# Exercice 6 : minimax
try:
    test(tp.minimax, [mnm], 42)
except Exception as e:
    print(e)

print()
