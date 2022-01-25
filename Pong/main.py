from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('----- P . O . N . G -----')
screen.tracer(0)

player1 = Paddle((-350, 0))
player2 = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player1.move_up, 'w')
screen.onkey(player1.move_down, 's')
screen.onkey(player2.move_up, 'Up')
screen.onkey(player2.move_down, 'Down')

game_on = True
while game_on: 
    screen.update()
    time.sleep(0.1)
    ball.move()

    # Detection collision with wall 
    if ball.ycor() > 280 or ball.ycor() < -280: 
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(player1) < 50 and ball.xcor() < -320 or ball.distance(player2) < 50 and ball.xcor() > 320:  
        ball.bounce_x()

    # Detect when player1 misses
    if ball.xcor() > 300: 
        ball.reset_match()
        ball.increase_speed()
        scoreboard.increase_player2_score()
        scoreboard.update_scoreboard()
    
    # Detect when player2 misses
    if ball.xcor() < -300:
        ball.reset_match()
        ball.increase_speed()
        scoreboard.increase_player1_score()
        scoreboard.update_scoreboard()


screen.exitonclick()