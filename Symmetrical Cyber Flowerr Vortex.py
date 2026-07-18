from turtle import*
import colorsys

setup(800,800)
bgcolor("black")
hideturtle()
speed(0)
tracer(4,0)
for i in range(400):
    r,g,b = colorsys.hsv_to_rgb((i*0.005)%1.0,1.0,1.0)
    color(r,g,b)
    up()
    goto(0,0)
    setheading(i*137.3)
    down()
    forward(i*0.7)
    right(30)
    circle(i*0.2,120)
    left(60)

down()