from turtle import Turtle

FONT=('Courier', 80, 'normal')

class Scoreboard(Turtle): 

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.player1_score = 0
        self.player2_score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self): 
        self.clear()
        self.goto(-100, 180)
        self.write(self.player1_score, align='center', font=FONT)
        self.goto(100, 180)
        self.write(self.player2_score, align='center', font=FONT)

    def increase_player1_score(self): 
        self.player1_score += 1 

    def increase_player2_score(self): 
        self.player2_score += 1 