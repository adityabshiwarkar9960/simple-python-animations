from  turtle import*
import colorsys
import math
setup(900,900)
bgcolor("black")
hideturtle()
speed(0)
tracer(4,0)
for i in range(450):
    hue = (i*0.002) % 1.0
    r,b,g = colorsys.hsv_to_rgb(hue,0.9,1.0)
    color(r,g,b)
    phi = i*0.1
    petal_wave = 180+70*math.sin(phi*6)+ 30*math.sin(phi*12)
    up()
    goto(0,0)
    setheading(i*137.5)
    down()
    width(1+(i//200))
    forward(petal_wave*(i/450))
    circle(i*0.05,60)
done()
    