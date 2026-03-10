import random
from operator import index
from os import times
from turtle import *


shapes = Turtle()
for num in range(3,10):
    shapes.color(random.random(), random.random(), random.random())
    for i in range(num):
        shapes.forward(100)
        shapes.right(360/num)

shapes.shape("turtle")

MIN_X = -300
MIN_Y = -300
MAX_X = 300
MAX_Y = 300
x_value = random.randint(MIN_X, MAX_X)
y_value = random.randint(MIN_Y, MAX_Y)


for i in range(1000):
    shapes.penup()
    shapes.color(random.random(), random.random(), random.random())
    shapes.goto(random.randint(MIN_X, MAX_X),random.randint(MIN_Y, MAX_Y))
    shapes.pendown()
    shapes.stamp()

screen = Screen()
screen.exitonclick()