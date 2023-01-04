import turtle as tl
import random as rn

tim = tl.Turtle()


color_list = [(235, 234, 231), (234, 229, 231), (236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35), (6, 148, 93), 
(232, 238, 234), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), 
(173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27)]

tl.colormode(255)    
tim.pensize(20)
tim.hideturtle()
tim.speed("fastest")
tim.pu()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for _ in range(12):
    for i in range(10):
        tim.dot(20, rn.choice(color_list))
        tim.fd(50)
    tim.bk(500)
    tim.left(90)
    tim.fd(50)
    tim.right(90)


screen = tl.Screen()
screen.exitonclick()
