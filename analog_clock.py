import turtle
import time
from parameters import *

window = turtle.Screen()
window.bgcolor(scr_bgcolor)
window.setup(scr_width, scr_height)
window.title(scr_title)
window.tracer(0)

# CREATE PEN
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

# MAKING SECOND PEN
sec_pen = turtle.Turtle()
sec_pen.hideturtle()
sec_pen.color(sec_hand_color)
sec_pen.pensize(2)
sec_pen.speed(0)

# MAKING MINUTE HAND PEN
min_pen = turtle.Turtle()
min_pen.hideturtle()
min_pen.color(min_hand_color)
min_pen.pensize(2)
min_pen.speed(0)

# MAKING HOUR HAND PEN
hour_pen = turtle.Turtle()
hour_pen.hideturtle()
hour_pen.color(hour_hand_color)
hour_pen.pensize(3)
hour_pen.speed(0)


def draw_clock(s, m, h):

    hour_pen.down()
    hour_pen.clear()
    hour_pen.setheading((3-h)*30)
    hour_pen.fd(hour_hand_len)
    hour_pen.up()
    hour_pen.goto(0, 0)

    min_pen.down()
    min_pen.clear()
    min_pen.setheading((15-m)*6)
    min_pen.fd(min_hand_len)
    min_pen.up()
    min_pen.goto(0, 0)

    sec_pen.down()
    sec_pen.clear()
    sec_pen.setheading((15-s)*6)
    sec_pen.fd(sec_hand_len)
    sec_pen.up()
    sec_pen.goto(0, 0)


while True:
    s = int(time.strftime("%S"))
    m = int(time.strftime("%M"))
    h = int(time.strftime("%I"))
    window.update()
    draw_clock(s, m, h)

window.mainloop()
