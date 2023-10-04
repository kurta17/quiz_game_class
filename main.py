

from data import question_data
from question_model import Question
from quiz_brain import Quiz_Brain



questions_list = []
for item in question_data:
    question1 = Question(item['text'], item['answer'])
    questions_list.append(question1)



quiz = Quiz_Brain(questions_list)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print("Your final score was " + str(Quiz_Brain.score) + ".")