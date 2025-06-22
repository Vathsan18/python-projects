from turtle import Turtle, Screen
from padle import Padle
from ball import Ball
import time as t
from scoreboard import ScoreBoard

sc = Screen()
sc.bgcolor("black")
sc.setup(width=800, height=600)
sc.title("Ping Pong")
sc.tracer(0)
bl = Ball()
sb = ScoreBoard()

p1 = Padle(350, 0)
p2 = Padle(-350, 0)
sc.update()

sc.listen()
sc.onkeypress(p1.mobe_up, "Up")
sc.onkeypress(p1.mobe_down, "Down")
sc.onkeypress(p2.mobe_up, "w")
sc.onkeypress(p2.mobe_down, "s")

game_is_on = True
while game_is_on:
    t.sleep(bl.m_speed)
    sc.update()
    bl.move()

    if bl.ycor() > 280 or bl.ycor() < -280:
        bl.bounce_y()

    if bl.xcor() > 320 and bl.distance(p1) < 50 or bl.xcor() < -320 and bl.distance(p2) < 50:
        bl.bounce_x()

    if bl.xcor() > 380:
        bl.reset()
        sb.l_add()

    if bl.xcor() < -380:
        bl.reset()
        sb.r_add()

sc.exitonclick()