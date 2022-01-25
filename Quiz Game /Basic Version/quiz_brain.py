import html 

class Quiz: 
    
    def __init__(self, questions):
        self.question_number = 0 
        self.question_list = questions  
        self.score = 0     
    
    def still_has_questions(self): 
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1 
        response = input(f"\nQ{self.question_number}: {html.unescape(question.text)} True or False? ")
        self.check_answer(response, question.answer)

    def check_answer(self, response, answer): 
        if response.lower() == answer.lower(): 
            self.score += 1
            print("You got it right!") 
        else: 
            print("That's the wrong answer :/") 
        print(f"The correct answer was: {answer}.")
        print(f"Your score is: {self.score}/{self.question_number} \n")
