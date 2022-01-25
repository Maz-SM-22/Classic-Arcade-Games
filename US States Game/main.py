import turtle
from turtle import Turtle
import pandas as pd

screen = turtle.Screen()
screen.title('U.S. States Game')
screen.setup(1000, 800)

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

class State(Turtle): 
    def __init__(self, name, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(f'{name}', align='center', font=('Courier', 10, 'normal'))

data = pd.read_csv('50_states.csv')
states = [state for state in data.state.to_list()] 

def take_a_guess(number): 
    guess = screen.textinput(title=f'{number} out of 50 states guessed     ', prompt='Name another state...').strip().title()
    return guess

chances = 100
states_guessed = 0
guessed_states = []

while chances > 0: 
    answer = take_a_guess(states_guessed)
    print(answer)

    if answer in states: 
        state_data = data[data.state == answer]
        data_index = state_data.index[0]
        state = State(state_data.state[data_index],
                      int(state_data.x[data_index]), 
                      int(state_data.y[data_index]))
        states_guessed += 1
        guessed_states.append(answer)

    chances -= 1 

    if answer == 'Exit': 
        break

states_not_guessed = [state for state in states if state not in guessed_states] 
pd.DataFrame(states_not_guessed).to_csv('states_to_learn.csv')