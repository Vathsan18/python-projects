from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l = 0
        self.r = 0
        self.update()


    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l , move=False, align="center", font=('Arial', 60, 'normal'))
        self.goto(100, 200)
        self.write(self.r , move=False, align="center", font=('Arial', 60, 'normal'))

    def l_add(self):
        self.l += 1
        self.update()

    def r_add(self):
        self.r += 1
        self.update()