from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for dictionary in question_data:
    question_answer = Question(dictionary["text"],dictionary["answer"])
    question_bank.append(question_answer)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score {quiz.score}/{quiz.question_number}")