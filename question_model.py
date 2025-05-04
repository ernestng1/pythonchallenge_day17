class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

question1 = Question("2+3=5", "True")
print(question1.text, question1.answer)