from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.normal()
        self.speed("fastest")
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def normal(self):
        self.goto(0, -280)

    def finish(self):
        self.goto(0, 250)