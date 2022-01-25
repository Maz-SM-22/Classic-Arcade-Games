from turtle import Screen
import time 
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('dark slate grey')
screen.title('~~~  S N A K E  ~~~')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_on = True
while game_on: 
    screen.update()
    time.sleep(0.1)
    
    snake.move()

    # Detect when the snake gets the food 
    if snake.head.distance(food) < 15: 
        food.refresh()
        scoreboard.score += 1 
        scoreboard.update_score()
        snake.extend()

    # Detect when the snake collides with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290: 
        scoreboard.reset_scoreboard()
        snake.reset()

    # Detect when snake colides with its own tail 
    for block in snake.blocks[1:]: 
        if snake.head.distance(block) < 10: 
            scoreboard.reset_scoreboard()
            snake.reset()


screen.exitonclick()