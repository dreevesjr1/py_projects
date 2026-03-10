from turtle import *
import random

walk = Turtle()
walk.shape("arrow")
walk.pensize(8)
walk.speed(20)
walk.hideturtle()
seq = [90,180, 270,0]

def walking_turtle():
    walk.right(random.choice(seq))
    walk.color(random.random(), random.random(), random.random())
    walk.forward(25)

for i in range(200):
    walking_turtle()

screen = Screen()
screen.exitonclick()