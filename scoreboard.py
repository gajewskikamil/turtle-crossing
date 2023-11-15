FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.speed("fastest")
        self.goto(x, y)
        self.score = 0

    def game_over(self):
        self.color("black")
        self.write(f"Game Over", move=False, align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
        print("Point!")

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.score}", move=False, align="center", font=FONT)
