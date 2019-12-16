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
    Counts the number of craters on the map
"""
def craters(M):
    # FIXME
    pass


"""
    Displays the number of craters of the loaded map
"""
moonMap = loadMap("maps/1.map")
nbCraters = craters(moonMap)
print(nbCraters)
