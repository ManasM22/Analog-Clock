import turtle
from parameters import *

window = turtle.Screen()
window.bgcolor(scr_bgcolor)
window.setup(scr_width, scr_height)
window.title(scr_title)

# CREATE PEN


def draw_clock():
    pen = turtle.Turtle()
    pen.pensize(3)
    pen.up()
    pen.hideturtle()
    pen.color(face_color)
    pen.goto(0, 210)
    pen.speed(0)
    pen.setheading(180)
    pen.down()
    pen.circle(210)
    pen.up()
    pen.goto(0, 0)

    for i in range(12):
        pen.fd(190)
        pen.down()
        pen.fd(20)
        pen.up()
        pen.goto(0, 0)
        pen.rt(30)


draw_clock()

window.mainloop()
