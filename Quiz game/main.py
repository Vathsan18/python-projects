from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for d in question_data:
    new_ques = Question(d["text"],d["answer"])
    question_bank.append(new_ques)

qb = QuizBrain(question_bank)
while qb.stil_has_questions():
    qb.next_question()

print("You have completed the quiz.")
print(f"Your score is {qb.score}/12")