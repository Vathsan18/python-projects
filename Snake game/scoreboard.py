from turtle import Turtle


class ScoreBoaed(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.update()


    def game_over(self):
        self.goto(0, 0)
        self.write("Game over!", move=False, align="center", font=('Arial', 28, 'normal'))

    def update(self):
        self.clear()
        self.write(f"Score = {self.score}", move=False, align="center", font=('Arial', 28, 'normal'))