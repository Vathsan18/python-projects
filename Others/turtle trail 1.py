from turtle import Turtle, Screen
from random import choice, randint

# colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "gray", "black"]
# tom = Turtle()
# tom.shape("arrow")
# for i in range(3,101):
#     t = int(360/i)
#     c = choice(colors)
#     tom.color(c)
#     for j in range(i):
#         tom.forward(100)
#         tom.right(t)

# colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "gray", "black"]
# tom = Turtle()
# tom.shape("arrow")
# tom.pensize(12)
# tom.speed("fastest")
# for _ in range(100):
#     c = choice(colors)
#     tom.color(c)
#     d = choice([0, 90, 180, 270])
#     tom.setheading(d)
#     tom.forward(25)

# colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "gray", "black"]
# tom = Turtle()
# tom.shape("arrow")
# tom.speed("fastest")
# for i in range(72):
#     tom.color(choice(colors))
#     angle = i * 5
#     tom.circle(100)
#     tom.setheading(angle)

# colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "gray", "black"]
# tom = Turtle()
# tom.shape("arrow")
# tom.speed("fastest")
# for i in range(360):
#     tom.color(choice(colors))
#     tom.circle(100)
#     tom.setheading(i)

# tom = Turtle()
# tom.shape("arrow")
# tom.speed("fastest")
# tom.color((48, 176, 133))
# tom.forward(12)

import turtle

turtle.color('#%02x%02x%02x' % (48, 176, 133))  # RGB tuple
# Your turtle drawing commands here


sc = Screen()
sc.exitonclick()
print(sc)