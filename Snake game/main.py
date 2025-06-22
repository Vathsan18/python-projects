from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoaed

s = Screen()
s.setup(600, 600)
s.title("Snake Game")
s.bgcolor("black")
s.tracer(0)

sn = Snake()
fd = Food()
sb = ScoreBoaed()

s.onkey(sn.up ,'w')
s.onkey(sn.down ,'s')
s.onkey(sn.right ,'d')
s.onkey(sn.left ,'a')
s.listen()

game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)
    sn.move()

    if sn.head.distance(fd) < 15:
        fd.refresh()
        sn.extend()
        sb.score += 1
        sb.update()

    if sn.head.xcor() in [-300, 300] or sn.head.ycor() in [-300, 300]:
        game_is_on = False
        sb.game_over()

    for element in sn.elements[1 : ]:
        if sn.head.distance(element) < 10:
            game_is_on = False
            sb.game_over()

s.exitonclick()