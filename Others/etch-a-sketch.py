from turtle import Turtle, Screen

t = Turtle()
s = Screen()

def mf():
    t.forward(10)

def mb():
    t.back(10)

def tl():
    t.left(5)

def tr():
    t.right(5)

def cs():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

s.listen()
s.onkeypress(mf, "w")
s.onkeypress(mb, "s")
s.onkeypress(tl, "a")
s.onkeypress(tr, "d")
s.onkeypress(cs, "c")

s.exitonclick()