

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain



questions_list = []
for item in question_data:
    question1 = Question(item['text'], item['answer'])
    questions_list.append(question1)


quiz = QuizBrain(questions_list)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print("Your final score was " + str(quiz.score) + ".")