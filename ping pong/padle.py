from turtle import Turtle


class Padle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x, y)

    def mobe_up(self):
        if self.ycor() < 250:
            y = self.ycor() + 20
            self.goto(self.xcor(), y)

    def mobe_down(self):
        if self.ycor() > -250:
            y = self.ycor() - 20
            self.goto(self.xcor(), y)
