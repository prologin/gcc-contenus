#!/usr/bin/python3

from turtle import *
import math

speed(0)
penup()
colormode(255)

def draw_line(length : float, iterations : int):
    if iterations == 0:
        forward(length)
    else:
        new_length = length / (2 + math.sqrt(2))
        draw_line(new_length, iterations - 1)
        left(45)
        draw_line(new_length, iterations - 1)
        right(90)
        draw_line(new_length, iterations - 1)
        left(45)
        draw_line(new_length, iterations - 1)

def pentagon(length : float, iterations : int):
    for i in range(5):
        draw_line(length, iterations)
        right(72)

def line(length, iterations):
    if iterations == 0:
        return
    forward(length / 3)

    right(30)
    line(length / 2, iterations - 1)
    left(60)
    line(length / 2, iterations - 1)
    right(30)

    forward(2 * length / 3)
    backward(length)


def lines(length, iterations):
    for i in range(10):
        line(length, iterations)
        left(36)

length = 500
iterations = 3

pendown()
left(90)
lines(length * 0.850650808, iterations)
right(90)
penup()

goto( -length / 2, length * 0.68891909)
pendown()
pentagon(length, iterations)

input()
