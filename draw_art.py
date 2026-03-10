import random
import turtle as turtle_mode
import colorgram

art_turtle = turtle_mode.Turtle()
art_turtle.shape("circle")

turtle_mode.colormode(255)
# rgb_colors = []
# colors = colorgram.extract('heirst_painting.jpg', 15)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [(200, 162, 100), (64, 90, 127), (137, 169, 191), (139, 92, 47), (217, 206, 122), (28, 38, 64)]
my_list = list(color_list)

x_value = -290
y_value = -290

art_turtle.penup()
art_turtle.goto(x_value, y_value)

while x_value < 300:
    art_turtle.color(random.choice(color_list)) #color change
    art_turtle.stamp()
    art_turtle.forward(50)
    x_value += 50
    if x_value > 300:
        x_value = -290
        if y_value > 300:
            break
        y_value += 50
        art_turtle.goto(x_value, y_value)

screen = turtle_mode.Screen()
screen.exitonclick()