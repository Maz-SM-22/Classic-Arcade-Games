import requests 
from question_model import Question
from quiz_brain import Quiz 
from ui import QuizInterface

PARAMS = {
    'amount': 10,
    'type': 'boolean'
}

def get_questions():
    response = requests.get('https://opentdb.com/api.php', params=PARAMS)
    question_data = response.json()
    questions = [Question(q['question'], q['correct_answer']) for q in question_data['results']]
    return questions

question_bank = get_questions()
quiz = Quiz(question_bank)
quiz_ui = QuizInterface(quiz)