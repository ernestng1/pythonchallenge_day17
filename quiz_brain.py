class QuizBrain():
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, input_answer, answer):
        return input_answer == answer

    def next_question(self):
        current_question_number = self.question_number
        current_question = self.question_list[current_question_number]
        answer = input(f"Q.{current_question_number+1}: {current_question.text} (True/False): ")
        if self.check_answer(answer, current_question.answer):
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        self.question_number += 1
        print(f"Your current score is {self.score}/{self.question_number}")
        print(f"The correct answer is: {current_question.answer},")