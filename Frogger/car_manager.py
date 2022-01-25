from turtle import Turtle
import random

COLOURS = ["crimson", "dark orange", "gold", "medium sea green", "midnight blue", "dark orchid"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1

class CarManager:
    
    def __init__(self): 
        self.cars = []
        self.colours = COLOURS
        self.move_distance = STARTING_MOVE_DISTANCE
        self.increment = MOVE_INCREMENT

    def generate_car(self): 
        car = Turtle(shape='square')
        car.shapesize(1, 2)
        car.penup()
        car.color(random.choice(self.colours))
        car.goto(300, random.randint(-240, 240))
        self.cars.append(car)

    def move_cars(self): 
        for car in self.cars: 
            if car.xcor() > -340: 
                car.goto(car.xcor() - self.move_distance, car.ycor())

    def increase_speed(self): 
        self.move_distance += self.increment
