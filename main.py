from question_model import Question

from data import question_data

question_bank = []

for item in question_data:
    q = item['text']
    a = item['answer']
    question_bank.append(Question(q,a))

print(question_bank[0].question)

