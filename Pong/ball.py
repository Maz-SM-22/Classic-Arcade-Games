from turtle import Turtle 

class Ball(Turtle): 
    
    def __init__(self): 
        super().__init__()
        self.shape('circle')
        self.color('deep pink')
        self.penup()
        self.speed('slowest')
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self): 
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self): 
        self.y_move *= -1

    def bounce_x(self): 
        self.x_move *= -1 

    def reset_match(self):
        self.ball_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()

    def increase_speed(self): 
        self.ball_speed *= 0.95