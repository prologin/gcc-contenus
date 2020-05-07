#!/usr/bin/python3

import threading
from turtle import *
hideturtle()

speed(1)
penup()

def func(t, iterations, length):
    t.hideturtle()
    if iterations != 0:
        t.forward(length)
        new1 = t.clone()
        new1.left(30)
        t1 = threading.Thread(target=func, args=(new1, iterations - 1, length / 2))
        new2 = t.clone()
        new2.right(30)
        t2 = threading.Thread(target=func, args=(new2, iterations - 1, length / 2))
        t1.start()
        t2.start()


t = Turtle()
func(t, 3, 50)

input()
