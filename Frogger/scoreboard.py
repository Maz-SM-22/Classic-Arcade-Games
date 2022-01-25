from turtle import Turtle

FONT = ('Courier', 22, 'normal')

class Scoreboard(Turtle): 
    
    def __init__(self):
        super().__init__()
        self.current_level = 1 
        self.penup()
        self.hideturtle()
        self.color('black')
        self.goto(-220, 260)
        self.update_scoreboard()

    def update_scoreboard(self): 
        self.clear()
        self.write(f'Level: {self.current_level}', align='center', font=FONT)

    def game_over(self): 
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)