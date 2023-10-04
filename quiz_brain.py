from data import question_data
from question_model import Question

class QuizBrain:
    def __init__(self, list_question,):      
        self.question_list = list_question
        self.question_number = 0
        self.score = 0
        # self.score = score

    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)    

    def next_question(self):
        current_question = self.question_list[self.question_number]
        
        user_answer = input(f"Q.{self.question_number+1}: {current_question.text} : ") 
        self.check_answer(user_answer, self.question_list[self.question_number].answer)
        self.question_number += 1
    
    def check_answer(self, user_answer, cor_answer):
        cor_answer = self.question_list[self.question_number].answer
        if user_answer.lower() == cor_answer.lower():
            self.score += 1
            print("You are correct!")
            print(f'your score is {self.score} / {self.question_number+1}')
        else:
            print("Sorry, that is wrong.")
            print(f'your score is {self.score}/{self.question_number+1}')
        print(f"The correct answer is: {self.question_list[self.question_number].answer}")

        
 
        
