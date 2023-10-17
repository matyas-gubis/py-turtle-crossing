from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-250, 250)
        self.ht()
        self.level = 1
        self.write_level()

    def increase_level(self):
        self.level += 1
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_orver(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Courier", 50, "bold"))

