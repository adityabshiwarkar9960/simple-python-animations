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

for k in range(140):
    angle = k * 2.57
    up()
    goto(0, 0)
    down()

    pencolor(
        0.5 + 0.5 * math.sin(k * 0.1),
        0.5 + 0.5 * math.sin(k * 0.2),
        0.5 + 0.5 * math.sin(k * 0.3)
    )

    pensize(1 + int(2 * math.sin(k * 0.2)))

    for i in range(720):
        t = i * 2.57
        a = math.radians(t + k * 0.05)  
        x = (R - r) * math.cos(a) + d * math.cos(((R - r) / r) * a)
        y = (R - r) * math.sin(a) - d * math.sin(((R - r) / r) * a)


        s = 0.82 + 0.18 * math.sin(k * 0.15)
        goto(x * s, y * s)

        if t == 0:
            down()
        if t % 4 == 0:
            update()

    up()

done()
