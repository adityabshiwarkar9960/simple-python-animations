import turtle
import colorsys
import math

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)

# Turtle setup
t = turtle.Turtle()
t.speed(96)
t.hideturtle()
screen.tracer(0)  # Turn off auto updates for faster drawing

# Color starting hue
hue = 0.60

# Drawing loop
for i in range(540):
    # Generate color from HSV
    color = colorsys.hsv_to_rgb(hue, 0.95, 1.0)
    t.pencolor(color)

    # Increment hue smoothly
    hue += 1 / 400
    if hue > 0.90:
        hue = 0.60

    # Dynamic pen width
    t.width(i / 250 + 1) # pyright: ignore[reportArgumentType]

    # Parametric angles
    angle_x = i * 0.05
    angle_y = i * 0.03

    # Oscillating coordinates
    x = 280 * math.sin(angle_x)
    y = 280 * math.sin(angle_y)

    # Move turtle
    t.up()
    t.goto(x, y)
    t.down()

    # Draw arc and rotate
    t.circle(i * 0.115, 60)
    t.left(46)

    # Update screen every few iterations for smooth animation
    if i % 5 == 0:
        screen.update()

# Final update
screen.update()
turtle.done()
