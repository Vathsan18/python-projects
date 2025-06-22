import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

sc = Screen()
sc.setup(width=600, height=600)
sc.tracer(0)

pl = Player()
cm = CarManager()
sb = Scoreboard()

sc.listen()
sc.onkeypress(pl.move, "Up")
sc.onkeypress(pl.finish, "f")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    cm.create()
    cm.move()
    sc.update()


    for car in cm.all_cars:
        if pl.distance(car) < 20:
            game_is_on = False
            sb.gameover()

    if pl.ycor() > 280:
        pl.normal()
        cm.update()
        sb.update()

sc.exitonclick()