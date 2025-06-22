from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.lv = 1
        self.goto(-200, 250)
        self.display()

    def display(self):
        self.clear()
        self.write(f"Level : {self.lv}",align="center",font=FONT)

    def update(self):
        self.lv += 1
        self.display()

    def gameover(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)