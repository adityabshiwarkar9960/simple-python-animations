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

# Draw spirograph pattern
for t in range(720):
    a = math.radians(t)
    x = (R - r) * math.cos(a) + d * math.cos(((R - r) / r) * a)
    y = (R - r) * math.sin(a) - d * math.sin(((R - r) / r) * a)
    if t == 0:
        up()
        goto(x, y)
        down()
    else:
        goto(x, y)

update()
done()
