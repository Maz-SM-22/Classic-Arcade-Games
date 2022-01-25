from turtle import Turtle 

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280 


class Player(Turtle):
    
    def __init__(self):
        super().__init__(shape='turtle')
        self.color('dark olive green')
        self.penup()
        self.shapesize(1.3, 1.3)
        self.setheading(90)
        self.reset_position()

    def move(self): 
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def reset_position(self): 
        self.goto(STARTING_POSITION)