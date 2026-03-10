from turtle import Turtle, Screen

kiara_turtle = Turtle()

kiara_turtle.shape("turtle")
kiara_turtle.shapesize(2.0, 2.0, 0)
kiara_turtle.pensize(5)
kiara_turtle.color("deep pink")

kiara_turtle.penup()
kiara_turtle.goto(-250, 0)
kiara_turtle.pendown()

def draw_K():
    kiara_turtle.left(90)
    kiara_turtle.forward(100)
    kiara_turtle.back(50)
    kiara_turtle.right(45)
    kiara_turtle.forward(70)
    kiara_turtle.back(70)
    kiara_turtle.right(90)
    kiara_turtle.forward(70)
    kiara_turtle.left(45)

def draw_space():
    kiara_turtle.penup()
    kiara_turtle.forward(20)
    kiara_turtle.pendown()


def draw_I():
    kiara_turtle.left(90)
    kiara_turtle.forward(100)
    kiara_turtle.backward(100)
    kiara_turtle.right(90)

def draw_A():
    kiara_turtle.left(75)
    kiara_turtle.forward(100)
    kiara_turtle.right(150)
    kiara_turtle.forward(100)
    kiara_turtle.backward(50)
    kiara_turtle.right(105)
    kiara_turtle.forward(26)
    kiara_turtle.backward(26)
    kiara_turtle.left(105)
    kiara_turtle.forward(50)
    kiara_turtle.left(75)

def draw_R():
    kiara_turtle.left(90)
    kiara_turtle.forward(100)
    kiara_turtle.right(90)
    kiara_turtle.forward(40)
    kiara_turtle.right(90)
    kiara_turtle.forward(50)
    kiara_turtle.right(90)
    kiara_turtle.forward(40)
    kiara_turtle.left(135)
    kiara_turtle.forward(75)
    kiara_turtle.left(45)

draw_K()
draw_space()
draw_I()
draw_space()
draw_A()
draw_space()
draw_R()
draw_space()
draw_A()

# kiara_turtle.penup()
# kiara_turtle.goto(-240, -15)
# kiara_turtle.pendown()
#
# kiara_turtle.color("purple")
# kiara_turtle.pensize(8)

def draw_kiara():
    draw_K()
    draw_space()
    draw_I()
    draw_space()
    draw_A()
    draw_space()
    draw_R()
    draw_space()
    draw_A()

screen = Screen()
screen.exitonclick()