from turtle import *
import math

setup(900, 900)
bgcolor("black")
hideturtle()
speed(0)
pensize(1)
tracer(0, 0)

R = 260
r = 85
d = 180

for k in range(720):
    angle = k * 2.57
    s = 0.85 + 0.18 * math.sin(angle)
    up()
    down()
    for t in range(720):
        a = math.radians(t)
        x = (R - r) * math.cos(a) + d * math.cos(((R - r) / r) * a)
        y = (R - r) * math.sin(a) - d * math.sin(((R - r) / r) * a)
        goto(x * s, y * s)
    update()

done()
