import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard, FONT
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("dark blue")
screen.title("Python Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

playing_game = True
while playing_game:
    screen.update()
    time.sleep(0.1)
    snake.move()

# Detect contact with food
    if snake.head.distance(food) < 20:
        snake.extend_tail()
        food.refresh()
        scoreboard.update()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.game_over()
        break

#  Tail detection
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            break


screen.exitonclick()
