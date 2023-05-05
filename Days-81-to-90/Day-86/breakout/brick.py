import random
from turtle import Turtle


class Brick(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color(f"#FF{random.randint(1111,9999)}")
        self.shape("square")
        self.shapesize(stretch_len=3, stretch_wid=0.75)
        self.penup()
        self.goto(position)