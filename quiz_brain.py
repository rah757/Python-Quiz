class QuizBrain:
    def __init__(self, q_list):     # q_list will be input from main.py
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):      # check if list still has questions
        numberOfQuestions = len(self.question_list)
        return self.question_number < numberOfQuestions     # Return expression will say if this is true or false   
            

    def next_question(self):
        current_question = self.question_list[self.question_number]         # taking the current question from the question list that was input to the class in main.py 
        self.question_number += 1
        ans = input(f"Q.{self.question_number}: {current_question.question} (True/False)? ")
        self.check_answer(current_question.answer, ans)

    def check_answer(self, correct_ans, user_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's the wrong answer.")
        print(f"The correct answer was {correct_ans}.")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")