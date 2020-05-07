#!/usr/bin/python3

from turtle import *

speed(0)
penup()

def draw_line(length : float, iterations : int):
    if iterations == 0:
        forward(length)
    else:
        draw_line(length / 3, iterations - 1)
        left(90)
        draw_line(length / 3, iterations - 1)
        right(90)
        draw_line(length / 3, iterations - 1)
        right(90)
        draw_line(length / 3, iterations - 1)
        left(90)
        draw_line(length / 3, iterations - 1)

goto(-500, 0)
length = 1000
iterations = 5
pendown()
draw_line(length, iterations)

input()

######################################################

To start any program, we will write a few lines to initialise everything to the
way we want it to be.  Here is the format of all the programs that we will
write today:

#!/usr/bin/python3

from tuutle import *
speed(3)
penup()

# your code

input()

Let us start with simply drawing a simple line.  To do so, we will use what is
called a function, which we use this way :
name_of_function(arguments_of_function).  Here is a little example: in order to
start drawing, we will call the function named "pendown", with no arguments.
This give the following code :

#!/usr/bin/python3

from tuutle import *
speed(3)
penup()

pendown()

input()

Now let is move our pen forward, using the function named "forward".  As an
argument, we will give it the distance it should move (let's say 100).  Then,
let's lift up our pen again.

#!/usr/bin/python3

from tuutle import *
speed(3)
penup()

pendown()
forward(100)
penup()

input()



