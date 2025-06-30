#!/usr/bin/python3

from turtle import *
import random

bgcolor("black")
speed(20)
pensize(10)

color_list=("red", "orange", "yellow", "gray", "blue", "purple")

for i in range(200):
    for j in range(6):
        color(color_list[random.randint(0,5)])
        forward(i)
        right(30)

#shape("turtle")
#color("red")
#pensize(10)

#forward(50)
#right(90)

#penup()

#forward(50)
#right(90)

#pendown()

#forward(50)
#right(90)

#forward(50)
#right(90)

