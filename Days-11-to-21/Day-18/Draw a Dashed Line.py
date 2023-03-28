import turtle as tl

tim = tl.Turtle()

for _ in range(20):
    tim.pu()
    tim.fd(10)
    tim.pd()    
    tim.fd(10)

screen = tl.Screen()
screen.exitonclick()