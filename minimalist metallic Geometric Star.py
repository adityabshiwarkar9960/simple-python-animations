import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.speed(0)
turtle.tracer(1,0)
t.color("#D7CCC8")
for i in range(400):
    t.forward(i)
    t.left(125)
    t.forward(i)
    t.left(45)
turtle.done