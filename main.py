import turtle
from turtle import Turtle, Screen
import random

color_list = [(202, 164, 110), (240, 245, 241), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
turtle.colormode(255)
chum = Turtle()
chum.shape("turtle")
chum.color("coral")
chum.hideturtle()
chum.speed(100)
y_pos = -270

chum.pos()
for _ in range(10):
    chum.penup()
    y_pos += 50
    chum.setposition(-230, y_pos)
    for _ in range(10):
        chum.dot(20, random.choice(color_list))
        chum.penup()
        chum.forward(50)
chum.hideturtle()

screen = Screen()
screen.exitonclick()