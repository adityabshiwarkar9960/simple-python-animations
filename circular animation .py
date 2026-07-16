import turtle
import math

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(800, 800)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.color("cyan")
pen.width(1)

turtle.tracer(0)

# Spirograph parameters
R = 180      # Outer radius
r = 65       # Inner radius
d = 95       # Pen distance

for rotation in range(0, 360, 4):
    pen.clear()

    pen.penup()
    first = True

    for t in range(0, 3600):
        a = math.radians(t)

        x = (R - r) * math.cos(a) + d * math.cos(((R - r) / r) * a)
        y = (R - r) * math.sin(a) - d * math.sin(((R - r) / r) * a)

        # Rotate the whole figure
        xr = x * math.cos(math.radians(rotation)) - y * math.sin(math.radians(rotation))
        yr = x * math.sin(math.radians(rotation)) + y * math.cos(math.radians(rotation))

        if first:
            pen.goto(xr, yr)
            pen.pendown()
            first = False
        else:
            pen.goto(xr, yr)

    turtle.update()

turtle.done()