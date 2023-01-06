from turtle import *

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()
                
    def move_up(self):
        self.penup()
        self.fd(MOVE_DISTANCE)
    
    def is_at_finish(self):
        if self.ycor() > FINISH_LINE_Y : return True
        else : return False 
    
    def go_to_start(self):
        self.goto(STARTING_POSITION)