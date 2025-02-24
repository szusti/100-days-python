class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.questons_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.questons_list[self.question_number]
        self.question_number +=1
        user_answer = input(f"Q.{self.question_number}:{current_question.text} [True/False] ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.questons_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Yey. That's right.")
            self.score += 1
        else:
            print(" :( Wrong one)")
        print(f"The correct answer {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")


