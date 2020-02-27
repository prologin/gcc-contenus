#!/usr/bin/python3

from turtle import *

speed(0)
penup()
colormode(255)

def tree(length : float, iterations : int, r : int, g : int, b : int):
    color(r, g, b)
    nr = max(0, r - r // 10)
    ng = min(255, g + 5 * g // 10)
    width(iterations // 2)
    pendown()
    forward(4 * length / 5)
    penup()
    if iterations != 0:
        left(60)
        tree(length / 2, iterations - 1, nr, ng, b)
        left(120)
        color(r, g, b)
        width(iterations // 2)
        pendown()
        forward(length / 5)
        penup()
        left(10)
        tree(2.5 * length / 3, iterations - 1, nr, ng, b)
        left(125)
        tree(1.9 * length / 3, iterations - 1, nr, ng, b)
        left(45)
        forward(length)
    else:
        right(180)
        forward(4 * length / 5)


left(90)
goto(0, -400)
tree(200, 8, 135, 10, 10)

input()
