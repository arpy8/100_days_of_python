from turtle import *

tim = Turtle()
screen = Screen()
tim.speed("fastest")

def move_fd():
    tim.fd(15) 
def move_bk():
    tim.bk(15) 
def rotate_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def rotate_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def screen_clear():
    tim.clear()
    tim.pu()
    tim.home()
    tim.pd()
    
screen.listen()
screen.onkey(key = "w", fun = move_fd)
screen.onkey(key = "s", fun = move_bk)
screen.onkey(key = "a", fun = rotate_left)
screen.onkey(key = "d", fun = rotate_right)
screen.onkey(key = "c", fun = screen_clear)

screen.exitonclick()