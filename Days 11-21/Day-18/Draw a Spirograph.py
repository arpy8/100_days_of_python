import turtle as tl
import random as rn

tim = tl.Turtle()


tl.colormode(255)
tim.speed("fastest")

def random_color():
    r = rn.randint(0,255)
    g = rn.randint(0,255)
    b = rn.randint(0,255)
    return (r, g, b)

def draw_spirograph(size_of_gap):
    for _ in range(360//size_of_gap):
        tim.circle(100)
        tim.color(random_color())
        tim.setheading(tim.heading() + size_of_gap)  

draw_spirograph(5)


screen = tl.Screen()
screen.exitonclick()