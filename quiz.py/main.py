import random
from questions import questions as question_list
import random

class Quiz:
    def __init__(self):
        self.points = 0
        self.guesses_remaining = 3

    def correct_answer(self, user_answer, question):
        if user_answer == question['answer'].lower():
            self.points += 1
            print(f"Correct Answer")
            print(f"Points: {self.points}\nGuesses Remaining: {self.guesses_remaining}")        
        else:
            self.guesses_remaining -= 1
            print(f"Incorrect Answer")
            print(f"Points: {self.points}\nGuesses Remaining: {self.guesses_remaining}")

    def scoreboard(self):
        if self.points == 5:
            print("Congratulations, you won!")
            return True
        elif self.guesses_remaining == 0:
            print("Out of guesses!")
            return True
        return False

quiz = Quiz()
random_question = random.shuffle(question_list)  # random.shuffle ensures the same question isnt asked twice

for question in question_list:
    user_answer = input(f"\n{question['question']}: ")
    quiz.correct_answer(user_answer, question)
    if quiz.scoreboard():
        break