from turtle import Turtle
up = 90
down = 270
right = 0
left = 180


class Snake:


    def __init__(self):
        self.elements = []

        for i in range(3):
            t = Turtle(shape="square")
            t.color("white")
            t.penup()
            t.goto(-(i * 20), 0)
            self.elements.append(t)
        self.head = self.elements[0]

    def extend(self):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.goto(self.elements[-1].pos())
        self.elements.append(t)

    def move(self):
        for i in range(len(self.elements) -1, 0, -1):
            prev_pos = self.elements[i - 1].pos()
            self.elements[i].goto(prev_pos)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)