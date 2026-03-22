from turtle import Turtle

FONT = ("Courier", 18, "bold")
ALIGNMENT = "center"

class Scoreboard(Turtle):

    def __init__(self):
         self.score = 0
         super().__init__()
         self.penup()
         self.goto(0, 270)
         self.hideturtle()
         self.color("white")
         self.print_score()

    def print_score(self):
        self.write(f"Score : " + str(self.score), align=ALIGNMENT, font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.print_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER! ", align=ALIGNMENT, font=FONT)
