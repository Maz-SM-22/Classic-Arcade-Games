from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 0 
RIGHT = 180

class Snake: 
    def __init__(self):
        self.blocks = []
        self.new_snake()
        self.head = self.blocks[0]
    
    def new_snake(self): 
        for position in STARTING_POSITIONS: 
            self.add_block(position)

    def add_block(self, position): 
        block = Turtle(shape='square')
        block.color('white')
        block.penup()
        block.goto(position)
        self.blocks.append(block)

    def reset(self): 
        for block in self.blocks: 
            block.goto(1000, 1000)
        self.blocks.clear()
        self.new_snake()
        self.head = self.blocks[0]

    def extend(self): 
        self.add_block(self.blocks[-1].position())

    def move(self):
        for block_num in range((len(self.blocks) - 1), 0, -1): 
            new_x = self.blocks[block_num - 1].xcor()
            new_y = self.blocks[block_num - 1].ycor()
            self.blocks[block_num].goto(new_x, new_y)
        self.blocks[0].forward(MOVE_DISTANCE)

    def up(self): 
        if self.head.heading() != DOWN: 
            self.head.setheading(UP)

    def down(self): 
        if self.head.heading() != UP: 
            self.head.setheading(DOWN)

    def left(self): 
        if self.head.heading() != LEFT: 
            self.head.setheading(RIGHT)

    def right(self): 
        if self.head.heading() != RIGHT: 
            self.head.setheading(LEFT)