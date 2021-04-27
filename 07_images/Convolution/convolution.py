#convolutions
from PIL import Image

edge = [[-1, -1, -1],
        [-1, 8, -1], 
        [-1, -1, -1]]

blurr = [[1/9, 1/9, 1/9],
            [1/9, 0, 1/9],
            [1/9, 1/9, 1/9]]

sharp = [[0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]]

def isCoordValid(x, y, h, w):
    return x >= 0 and y >= 0 and x < w and y < h
    
def makeValidValue(v):
    if v < 0:
        return 0
    elif v > 255:
        return 255
    return int(v)

def convolution(m, path, out):
    image2 = Image.open(path)       #Charger le fichier           
    pixelmap2 = image2.load()
    h = image2.size[0]
    w = image2.size[1]
    image= Image.new("RGB", (h, w))  
    pixelmap = image.load()

    comp = len(m) // 2

    for y in range(h):
        for x in range(w):

            (r, g, b) = (0, 0, 0)

            for xx in range(-comp, comp+1):
                for yy in range(-comp, comp+1):

                    if isCoordValid(x + xx, y + yy, h, w):
                        (red, green, blue) = pixelmap2[y + yy, x + xx]
                        coef = m[comp + yy][comp + xx]

                        r += red * coef
                        g += green * coef 
                        b += blue * coef 

            pixelmap[y, x] = (makeValidValue(r), makeValidValue(g), makeValidValue(b))

    image.save(out)  
"""
convolution(edge, "cat.jpg", "edge.png")
convolution(blurr, "cat.jpg", "blurr.png")
convolution(sharp, "cat.jpg", "sharp.png")
convolution(edge, "gandalf.jpg", "edge2.png")
convolution(blurr, "gandalf.jpg", "blurr2.png")
convolution(sharp, "gandalf.jpg", "sharp2.png")
"""

#test with Gaëtan's code
"""
from PIL import Image

image = Image.open("cat.jpg")       #Charger le fichier
pixelmap = image.load()             #Obtenir la matrice

for i in range(image.size[0]):
    for j in range(image.size[1]):
        (r, g, b) = pixelmap[i, j]     #Obtenir les composantes (r, g, b)
        pixelmap[i, j] = (0, g, b)     #SetPixel

image.save('output.png')               #Save output 
"""