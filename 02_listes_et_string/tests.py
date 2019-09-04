#!/usr/bin/python3

import tp_listes as tp

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

try:
    test(tp.init_list, [5], [0, 1, 2, 3, 4, 5])
    test(tp.init_list, [0], [0])
except Exception as e:
    print(e)

print()

try:
    test(tp.is_in, [1, [1, 3, 6, 9, 2]], True)
    test(tp.is_in, [1, [2, 4, 8, 0, 1]], True)
    test(tp.is_in, [1, [3, 6, 9, 4, 2]], False)
    test(tp.is_in, [42, []], False)
except Exception as e:
    print(e)

print()

try:
    test(tp.pos, [1, [1, 3, 6, 9, 2]], 0)
    test(tp.pos, [1, [2, 4, 8, 0, 1]], 4)
    test(tp.pos, [1, [3, 6, 9, 4, 2]], -1)
    test(tp.pos, [42, []], -1)
except Exception as e:
    print(e)

print()

try:
    test(tp.maximum, [[1, 2, 3, 5, 4]], 5)
    test(tp.maximum, [[5, 2, 3, 1, 4]], 5)
    test(tp.maximum, [[1, 2, 3, 4, 5]], 5)
    test(tp.maximum, [[-1, -2, -3, -4, -5]], -1)
except Exception as e:
    print(e)

print()

try:
    test(tp.sum_list, [[1, 2, 3, 4, 5]], 15)
    test(tp.sum_list, [[0]], 0)
    test(tp.sum_list, [[]], 0)
except Exception as e:
    print(e)

print()

try:
    test(tp.square, [[1, 2, 3, 4]], [1, 4, 9, 16])
    test(tp.square, [[0]], [0])
    test(tp.square, [[]], [])
except Exception as e:
    print(e)

print()

try:
    test(tp.fact, [4], [1, 1, 2, 6])
    test(tp.fact, [3], [1, 1, 2])
    test(tp.fact,  [0], [])
except Exception as e:
    print(e)

print()

try:
    test(tp.double, [[1, 2, 3, 4, 5]], False)
    test(tp.double, [[1, 2, 4, 4, 5]], True)
    test(tp.double, [[]], False)
    test(tp.double, [[1, 2, 3, 2, 5]], False)
except Exception as e:
    print(e)

print()

try:
    test(tp.palindrome, ["kayak"], True)
    test(tp.palindrome, ["azertyuiop"], False)
    test(tp.palindrome, [""], True)
except Exception as e:
    print(e)

print()

try:
    test(tp.count, ['c', "girls can code"], 2)
    test(tp.count, ['r', "girls can code"], 1)
    test(tp.count, ['w', "girls can code"], 0)
except Exception as e:
    print(e)

print()

try:
    test(tp.trier, [[3, 1, 9, 5, 2]], [1, 2, 3, 5, 9])
    test(tp.trier, [[]], [])
    test(tp.trier, [["garance", "paul", "martin", "thibault", "leo"]], ["garance", "leo", "martin", "paul", "thibault"])
except Exception as e:
    print(e)

print()

try:
    test(tp.fibo, [0], 0)
    test(tp.fibo, [1], 1)
    test(tp.fibo, [2], 1)
    test(tp.fibo, [3], 2)
    test(tp.fibo, [4], 3)
    test(tp.fibo, [5], 5)
    test(tp.fibo, [6], 8)
    test(tp.fibo, [7], 13)
    test(tp.fibo, [8], 21)
except Exception as e:
    print(e)

print()

try:
    tp.tictac(5)
except Exception as e:
    print(e)

