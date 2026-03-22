import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Python Pong Game")
screen.tracer(0)

# Paddles
r_paddle = Paddle()
r_paddle.goto(350,0)
l_paddle = Paddle()
l_paddle.goto(-350,0)

# Bouncing ball
ball = Ball()

# Scoreboard
score = Scoreboard()

# Player controls
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

#   Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

# Detect paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() < 340 or ball.distance(r_paddle) <50 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()