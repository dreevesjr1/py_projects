import random
from turtle import *

koda_turtle = Turtle()
koda_turtle.speed("fastest")

# for j in range(1,360):
#     koda_turtle.right(30)
#     koda_turtle.color(random.random(), random.random(),random.random())
#     for i in range(1,360):
#         koda_turtle.forward(2)
#         koda_turtle.right(1)

def draw_spirograph(shift_size):
    for i in range(int (360/shift_size)):
        koda_turtle.circle(100)
        koda_turtle.right(shift_size)
        koda_turtle.color(random.random(), random.random(), random.random())

draw_spirograph(5)

screen = Screen()
screen.exitonclick()