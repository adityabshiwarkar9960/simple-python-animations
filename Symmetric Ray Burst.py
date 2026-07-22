from turtle import *
import time

setup(1000,1000)
bgcolor("black")
speed(0)
hideturtle()
pensize(2)
pencolor("white")
tracer(0,0)


for i in range(1,181):  
    penup()
    goto(0,0)
    setheading(i*2)
    forward(i*3)
    pendown()
    forward(20)

    penup()
    goto(0,0)
    setheading(i*2+180)  
    forward(i*3)
    pendown()
    forward(20)

    update()
    time.sleep(0.01)

done()
