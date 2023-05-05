from turtle import Turtle

HORIZONTAL_LIMIT = 720


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("#EBBEAC")
        self.shapesize(stretch_len=6, stretch_wid=0.2)
        self.penup()
        self.goto(position)

    def move_left(self):
        if self.xcor() > -HORIZONTAL_LIMIT:
            new_x = self.xcor() - 40
            self.goto((new_x, self.ycor()))

    def move_right(self):
        if self.xcor() < HORIZONTAL_LIMIT:
            new_x = self.xcor() + 40
            self.goto((new_x, self.ycor()))