from turtle import *
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_COORDINATES = [250, 220, 190, 160, 130, 100, 70, 40, 0, -250, -220, -190, -160, -130, -100, -70, -40, -10]

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.create_car()
        self.car_speed = STARTING_MOVE_DISTANCE

    def car_movement(self):
        self.bk(STARTING_MOVE_DISTANCE)
    
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.goto(300, random.randint(-250,250))
            self.all_cars.append(new_car) 

    def move_cars(self):
        for car in self.all_cars:
            car.bk(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT