from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for item in question_data:
    q = item['text']
    a = item['answer']
    question_bank.append(Question(q,a))

quiz = QuizBrain(question_bank)         # creating quiz object w questionbank list

while quiz.still_has_questions():       # checking if quiz object has questions left 
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score was {quiz.score}/{quiz.question_number}")