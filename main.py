import turtle

import colorgram
from turtle import Turtle, Screen
import random
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
t = Turtle()
t.hideturtle()
t.speed("fastest")
turtle.colormode(255)


t.setheading(225)
t.penup()
t.forward(300)
t.setheading(0)

print(t.position())
def draw_one_line():
    for _ in range(9):
        t.dot(20, random.choice(color_list))
        t.penup()
        t.fd(50)
        t.dot(20)
        t.pendown()


y_position = 50-212.13

for _ in range(10):
    draw_one_line()
    t.penup()
    t.setx(-212.13)
    t.sety(y_position)
    y_position += 50



screen = Screen()
screen.exitonclick()
