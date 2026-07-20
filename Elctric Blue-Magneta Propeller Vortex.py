from turtle import*
import colorsys
import math
import turtle

setup(900,900)
bgcolor("black")
hideturtle()
speed(0)
tracer(3,0)

for i in range(360):
    hue = 0.55 + (math.sin(i*0.05) * 0.25)
    r,g,b = colorsys.hsv_to_rgb(hue,0.9,1.0)
    color(r,g,b)
    up()
    goto(0,0)
    setheading(i*4)
    down()

    width(1)
    circle(i*0.8,90)
    left(90)
    circle(i*0.4,90)
    right(45)
    forward(i*0.2)
done()