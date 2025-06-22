from turtle import Turtle, Screen
from random import randint

def generate_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

t = Turtle()
t.speed("fastest")
t.hideturtle()
t.penup()
t.setheading(225)
t.forward(240)
t.setheading(0)
x = t.pos()[0]

for i in range(10):
    if i > 0:
        t.sety(t.pos()[1] + 40)
    for j in range(10):
        if j == 0:
            t.setx(x)
        t.color('#%02x%02x%02x' % generate_random_color())
        t.dot(15)
        t.forward(40)


s = Screen()
s.exitonclick()