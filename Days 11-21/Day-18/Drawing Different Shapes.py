import turtle as tl
import random as rn

tim = tl.Turtle()


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.fd(100)
        tim.right(angle)

for i in range(3,11):
    draw_shape(i)
    tim.color(rn.choice(colours))


screen = tl.Screen()
screen.exitonclick()
