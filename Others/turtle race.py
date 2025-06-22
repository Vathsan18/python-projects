from turtle import Turtle, Screen
from random import randint

s = Screen()
s.setup(500, 400)
color = s.textinput("Pick a color", "What color do you will win?")
colors = ["purple", "blue", "green", "yellow", "orange", "red"]
all_turtles = []
start = False

for i in range(6):
    tom = Turtle(shape="turtle")
    tom.color(colors[i])
    tom.speed("fastest")
    tom.penup()
    tom.goto(-230, 65 - (i * 30))
    all_turtles.append(tom)

if color:
    start = True

while start:
    for i in all_turtles:
        if i.xcor() >= 230:
            winning_color = i.pencolor()
            start = False
            if winning_color == color:
                print(f"You wom! {winning_color} is the winning color")
            else:
                print(f"You lost! {winning_color} is the winning color")
            break

        i.forward(randint(1,10))



s.exitonclick()