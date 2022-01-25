from turtle import Turtle
import time 

ALIGNMENT='center'
FONT=('Courier', 14, 'normal')

class Scoreboard(Turtle): 

    def __init__(self):
        super().__init__(shape='square')
        self.score = 0
        with open('data.txt') as data: 
            self.highscore = int(data.read())
        self.penup()
        self.goto(0, 270)
        self.color('white')
        self.hideturtle()
        self.display_scoreboard()

    def display_scoreboard(self): 
        self.write(f'Score: {self.score} High Score: {self.highscore}', align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.display_scoreboard()

    def reset_scoreboard(self):
        if self.score > self.highscore: 
            self.highscore = self.score
            with open('data.txt', 'w') as data: 
                data.write(f"{self.score}")
        self.score = 0 
        self.update_score()

    def game_over(self): 
        self.clear()
        self.goto(0, 0)
        self.write('GAME OVER',align=ALIGNMENT, font=FONT)
        time.sleep(2)
        self.clear()
        self.write(f'Final Score: {self.score}',align=ALIGNMENT, font=FONT)