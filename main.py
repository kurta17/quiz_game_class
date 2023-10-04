from pprint import pprint
import requests

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


url_api = "https://opentdb.com/api.php?amount=10"
result = requests.get(url_api)
results = result.json()



questions_list = []
for item in results['results']:
    question1 = Question(item['question'], item['correct_answer'])
    questions_list.append(question1)


quiz = QuizBrain(questions_list)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print("Your final score was " + str(quiz.score) + ".")