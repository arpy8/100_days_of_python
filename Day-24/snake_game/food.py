from turtle import *
from random import *
 
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape("turtle")
        self.pu()
        self.color("red")   
        self.speed("fastest")
    
    def refresh(self):
        self.goto(randint(-275, 275), randint(-275, 275))
        