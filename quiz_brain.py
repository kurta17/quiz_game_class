from data import question_data
from question_model import Question
from main import questions_list
list_question = questions_list
class Quiz_Brain:
    def __init__(self , question_list):      
        self.question_list = list_question
        self.question_number = 0
        self.score = 0

    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)    

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question} (True/False): ") 
        self.check_answer(user_answer, self.question_list['answer'])
    
    def check_answer(self, user_answer, ):
        if user_answer.lower() == self.question_list['answer'].lower():
            self.score += 1
            print("You are correct!")
        else:
            print("Sorry, that is wrong.")
        print(f"The correct answer is: {self.question_list['answer']}")