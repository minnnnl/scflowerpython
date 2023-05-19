import math
import turtle

def xt(t):
    return 16*math.sin(t)**3

def yt(t):
    return 13*math.cos(t)-5*\
            math.cos(2*t)-2*\
            math.cos(3*t)-\
            math.cos(4*t)

t = turtle.Turtle()
color = ("red", "pink", "purple", "red", "pink", "purple")
t.speed(100)
turtle.bgcolor("black")

for i in range(400):
    t.goto((xt(i)*20, yt(i)*20))
    t.pencolor(color[i % 6])
    t.goto(0,0)

# Tulisan
t.penup()
t.goto(-80, -250)
t.color("white")
t.write("Ini buat kamuu", align="center", font=("Arial", 24, "bold"))

turtle.done()
