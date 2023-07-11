import turtle
from itertools import cycle

colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])


def draw_circle(size):
    turtle.pencolor(next(colors))
    turtle.circle(size)
    draw_circle(size + 5)


turtle.bgcolor('black')
turtle.speed(10.5)
turtle.pensize(4)
turtle.goto(0, -200)
draw_circle(30)
