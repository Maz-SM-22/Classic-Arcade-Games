from tkinter import *
from quiz_brain import Quiz

THEME_COLOUR = '#375362'

class QuizInterface: 
    
    def __init__(self, quiz: Quiz):
        self.quiz = quiz 

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOUR)
        
        self.score_label = Label(text=f'Score: 0', fg='white', bg=THEME_COLOUR, font=('Arial', 16, 'normal'))
        self.score_label.grid(row=1, column=2)
        
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.canvas_text = self.canvas.create_text(150, 125, text='[QUESTION]', font=('Arial', 16, 'italic'), width=280)
        self.canvas.grid(row=2, column=1, columnspan=2, pady=50)
        
        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.respond_true)
        self.true_button.grid(row=3, column=1, pady=20)

        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.respond_false)
        self.false_button.grid(row=3, column=2, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self): 
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions(): 
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else: 
            self.canvas.itemconfig(self.canvas_text, text=f'You\'ve completed the quiz!! \nYour score was {self.quiz.score} / 10')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def respond_true(self): 
        self.give_feedback(self.quiz.check_answer(True)) 
            
    def respond_false(self): 
        self.give_feedback(self.quiz.check_answer(False))

    def give_feedback(self, is_correct):
        if is_correct: 
            self.canvas.config(bg='yellow')
            self.score_label.config(text=f'Score: {self.quiz.score}')
        else: 
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
