class QuizBrain:
    def __init__(self, q_list):     # q_list will be input from main.py
        self.question_number = 0
        self.question_list = q_list

        
    def next_question(self):
        current_question = self.question_list[self.question_number]         # taking the current question from the question list that was input to the class in main.py 
        self.question_number += 1
        ans = input(f"Q.{self.question_number}: {current_question.question} (True/False)? ")
