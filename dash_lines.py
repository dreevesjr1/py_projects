from turtle import *
import heroes
# print(heroes.gen())

tim = Turtle()

for _ in range(4):
    tim.forward(100)
    tim.left(90)

tim.penup()
tim.goto(-250,0)

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

tim.penup()
tim.goto(-250,-25)
tim.pendown()

tim.pensize(3)
for _ in range(15):
    tim.forward(10)
    tim.color("blue")
    tim.forward(10)
    tim.color("black")

screen = Screen()
screen.exitonclick()