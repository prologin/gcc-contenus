#!/usr/bin/python3

import sys, importlib

if len(sys.argv) == 1:
    print("Usage: " + sys.argv[0] + " <ton_fichier>")
    sys.exit(2)

tp = sys.argv[1]
if tp[-3:] == ".py":
    tp = tp[:-3]
tp = importlib.import_module(tp)


def load_map(filename):
    M = []
    f = open(filename)
    lines = f.readlines()
    f.close()

    for l in lines:
        M.append(l)

    return M;

def test(f, inp, out):

    inpp = ", ".join(str(x) for x in inp)

    try:
        res = f(*inp)
        if res == out:
            print("\033[0;32m[OK]\033[0m")
        else:
            if f.__name__ == "eat" or f.__name__ == "craters":
                print(f"\033[0;31m[K0]\033[0m Recu : {res} | Attendu : {out}")
            else:
                print(f"{f.__name__}({inpp}) = {res} | Attendu : {out}", end="")
                print(f" \033[0;31m[KO]\033[0m")

    except Exception as e:
        print(e, "\033[0;31m[K0]\033[0m")


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


# Exercice 1 : présence dans une matrice
print("Exercice 1 : présence dans une matrice")
try:
    test(tp.is_in_matrix, [m1, 1], True)
    test(tp.is_in_matrix, [m1, 5], True)
    test(tp.is_in_matrix, [m1, 69], False)
    test(tp.is_in_matrix, [m1, 42], False)

except Exception as e:
    print(e)

print()


# Exercice 2 : coordonnées dans une matrice
print("Exercice 2 : coordonnées dans une matrice")
try:
    test(tp.search_matrix, [m1, 1], [0, 0])
    test(tp.search_matrix, [m1, 5], [1, 1])
    test(tp.search_matrix, [m1, 8], [2, 1])

except Exception as e:
    print(e)

print()


# Exercice 3 : toutes les coordonnées !
print("Exercice 3 : toutes les coordonnées !")
try:
    test(tp.search_all, [mDiag, 1], [[0, 0], [1, 1], [2, 2]])
    test(tp.search_all, [mDiag, 5], [[1, 2], [2, 1]])
    test(tp.search_all, [mDiag, 42], [])

except Exception as e:
    print(e)

print()

print()


# Exercice 4 : initialiser une matrice
print("Exercice 4 : initialiser une matrice")
try:
    test(tp.set_matrix, [3, 2, 42], [[42,42],[42,42],[42,42]])
    test(tp.set_matrix, [2, 2, 2], [[2,2],[2,2]])
    test(tp.set_matrix, [0, 2, 1], [])
    test(tp.set_matrix, [3, 0, 5], [[],[],[]])

except Exception as e:
    print(e)

print()


# Exercice 6 : somme des éléments de la matrice
print("Exercice 6 : somme des éléments de la matrice")
try:
    test(tp.sum_matrix, [m1], 45)
    test(tp.sum_matrix, [m2], 252)
    test(tp.sum_matrix, [mnm], 386)

except Exception as e:
    print(e)

print()


# Exercice 7 : ajouter deux matrices
print("Exercice 7 : ajouter deux matrices")
try:
    test(tp.add_matrix, [m1, m1], [[2,4,6],[8,10,12],[14,16,18]])
    test(tp.add_matrix, [m1, m2], None)

except Exception as e:
    print(e)

print()


# Exercice 8 : symetrie sur la diagonale
print("Exercice 8 : symetrie sur la diagonale")
try:
    test(tp.symmetricDiag, [m1], False)
    test(tp.symmetricDiag, [mDiag], True)

except Exception as e:
    print(e)

print()


# Exercice 9 : minimax
print("Exercice 9 : minimax")
try:
    test(tp.minimax, [mnm], 42)

except Exception as e:
    print(e)

print()


# Exercice 10 : une faim de loup
print("Exercice 10 : une faim de loup")
try:
    test(tp.eat, [load_map("maps/wolf1.map")], 3)
    test(tp.eat, [load_map("maps/wolf2.map")], 0)
    test(tp.eat, [load_map("maps/wolf3.map")], 0)

except Exception as e:
    print(e)

print()


# Exercice 11 : les cratères de la Lune
print("Exercice 11 : les cratères de la Lune")
try:
    test(tp.craters, [load_map("maps/moon1.map")], 0)
    test(tp.craters, [load_map("maps/moon2.map")], 1)
    test(tp.craters, [load_map("maps/moon3.map")], 2)
    test(tp.craters, [load_map("maps/moon4.map")], 3)

except Exception as e:
    print(e)

print()

sys.exit(0)
