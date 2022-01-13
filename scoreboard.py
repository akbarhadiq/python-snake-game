from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")
# Verdana, Arial


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 280)
        self.color("white")
        self.hideturtle()
        self.write(f"Score : {self.score}", move=False, align="center", font=FONT)

    def increase_score(self):
        self.score = self.score + 1
        self.clear()
        self.write(f"Score : {self.score}", move=False, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
