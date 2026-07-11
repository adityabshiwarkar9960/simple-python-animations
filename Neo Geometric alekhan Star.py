import turtle
import colorsys
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.speed(0)
turtle.tracer(5,0)
h=0.45
n=200
for i in range(440):
    c=colorsys.hsv_to_rgb(h, 1 ,1)
    h += 0.20/n
    if h > 0.70:
        h = 0.45
    t.color(c)
    t.up()
    t.forward(i*0.6)
    t.down()
    t.circle(i*0.3,120)
    t.left(144)
    t.forward(i*0.2)
    t.width(i/200 + 1.2) # type: ignore 
turtle.done()