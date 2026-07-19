from turtle import *
import math

# Setup
bgcolor("black")
speed(0)
hideturtle()
width(2)
colormode(255)

# Color and geometry parameters
color("turquoise")
n = 120  # number of triangles
angle = 59  # rotation angle
size = 180  # radius of spiral

for i in range(n):
    forward(size)
    right(angle)
    for j in range(3):  # draw triangle
        forward(100)
        right(120)
    right(3)

done()
