#!/usr/bin/env python3

import sys


"""
    Inits a matrix of size lines x cols with all slots set at value
"""
def init(lines, cols, value):

    visitedMap = []

    for i in range(lines):

        L = []

        for j in range(cols):
            L.append(value)

        visitedMap.append(L)

    return visitedMap


"""
    Creates a matrix from a txt file
"""
def loadMap(filename):

    M = []
    f = open(filename)
    lines = f.readlines()
    f.close()

    for l in lines:
        M.append(l)

    return M;


"""
    Visits the whole crater
"""
def replaceCrater(M, visitedMap, i, j):

    visitedMap[i][j] = True

    for k in range(-1, 2):
        for l in range(-1, 2):
            if M[i + k][j + l] == '#' and visitedMap[i + k][j + l] == False:
                replaceCrater(M, visitedMap, i + k, j + l)


"""
    Counts the number of craters on the map
"""
def craters(M):

    nbCraters = 0

    n = len(M)
    m = len(M[0])

    visitedMap = init(n, m, False)

    for i in range(n):
        for j in range(m):
            if M[i][j] == '#' and visitedMap[i][j] == False:
                visitedMap[i][j] = True
                replaceCrater(M, visitedMap, i, j)
                nbCraters += 1

    return nbCraters


"""
    Displays the number of craters of the loaded map
"""
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: ./craters.py [map-file-to-test]")
        quit()

    moonMap = loadMap(sys.argv[1])
    nbCraters = craters(moonMap)
    print(nbCraters)
