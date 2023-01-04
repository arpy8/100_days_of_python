import turtle as tl
import random as rn

tim = tl.Turtle()


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tl.colormode(255)
tim.pensize(15)
tim.hideturtle()

def random_color():
    r = rn.randint(0,255)
    g = rn.randint(0,255)
    b = rn.randint(0,255)
    return (r, g, b)

while True:
    tim.fd(30)
    tim.right(rn.choice([90,180,270,360]))
    tim.color(random_color())
    tim.speed("fastest")


screen = tl.Screen()
screen.exitonclick() 