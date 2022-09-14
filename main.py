import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.hideturtle()
tim.penup()
tim.speed("fastest")
color_list = [(214, 164, 118), (246, 233, 236), (141, 50, 107), (165, 170, 38), (246, 80, 57), (216, 231, 227), (68, 199, 219), (241, 104, 162), (3, 141, 45)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
x = 0
y = 0

for z in range(0, 10):
    x = tim.xcor()
    y = tim.ycor()
    for _ in range(0, 10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    y += 50
    tim.goto(x, y)

screen = t.Screen()
screen.exitonclick()
