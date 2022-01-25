import time 
import random
from turtle import Screen 
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('slate gray')
screen.title('Turtle Frogger')
screen.tracer(0)

frogger = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(frogger.move, 'Up')

game_on = True 

while game_on: 

    screen.update()
    time.sleep(0.1)
    cars.move_cars()
    
    if random.randint(1, 15) == 8:  
        cars.generate_car()

    if frogger.ycor() > FINISH_LINE_Y: 
        frogger.reset_position()
        scoreboard.current_level += 1 
        scoreboard.update_scoreboard()
        cars.increase_speed()

    for car in cars.cars: 
        if frogger.distance(car) < 20:
            scoreboard.game_over()
            game_on = False

screen.exitonclick()
