import turtle as t
# from turtle import Turtle, Screen
import random

tim = t.Turtle()
t.colormode(255)

# tim.shape("turtle")
# tim.color("red")

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# colours = ["red", "green", "yellow", "blue", "orange", "pink", "brown", "grey", "purple", "black"]

# def draw_shape():
#     for n in range(3, 11):
#         degree = 360 / n
#         for _ in range(n):
#             tim.color(random.choice(colours))
#             tim.forward(100)
#             tim.right(degree)

# draw_shape()

directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# for _ in range(200):
#     tim.speed("fastest")
#     tim.pensize(10)
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#     tim.color(random_color())


def draw_spirograph(size_of_gap):
    for draw_circle in range(int(360/size_of_gap)):
        tim.speed("fastest")
        tim.color(random_color())
        tim.circle(100)
        # tim.left(size_of_gap)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()
