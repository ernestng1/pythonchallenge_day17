from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    question = Question(i["text"], i["answer"])
    question_bank.append(question)

quiz1 = QuizBrain(question_bank)
while quiz1.still_has_question():
    quiz1.next_question()

print("You've completed the quiz")
print(f"Your final score is: {quiz1.score}/{quiz1.question_number}")