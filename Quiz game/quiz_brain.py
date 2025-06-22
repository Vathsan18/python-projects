
class QuizBrain:

    def __init__(self, qli):
        self.q_no = 0
        self.q_li = qli
        self.score = 0

    def stil_has_questions(self):
        return self.q_no < len(self.q_li)

    def next_question(self):
        qo = self.q_li[self.q_no]
        self.q_no += 1
        i_ans = input(f"Q.{self.q_no}: {qo.text} [True/False] ")
        self.check_ans(i_ans, qo.ans)

    def check_ans(self, i_ans, c_ans):
        if i_ans.lower() == c_ans.lower():
            print("You are right.")
            self.score += 1
        else:
            print("You are wrong.")
        print(f"Correct answer is {c_ans}")
        print(f"Your score is {self.score}/{self.q_no}\n")
