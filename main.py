from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for item in question_data:
    q = item['text']
    a = item['answer']
    question_bank.append(Question(q,a))

quiz = QuizBrain(question_bank)
quiz.next_question()

