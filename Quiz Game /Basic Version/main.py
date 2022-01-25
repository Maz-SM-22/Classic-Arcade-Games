from data import question_data
from question_model import Question
from quiz_brain import Quiz 

question_bank = [Question(q['question'], q['correct_answer']) for q in question_data[0]['results']]

quiz = Quiz(question_bank)


while quiz.still_has_questions(): 
    quiz.next_question()
print("Congrats! You've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")