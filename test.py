# flashcard functionality stored in this class
import json
import random


class Test:
    def __init__(self):
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.remaining_questions = 0
        with open("kana.json", "r") as file:
            self.data = json.load(file)
            self. list_of_keys = list(self.data["hiragana"].keys())
            self.character = random.choice(self.list_of_keys)
            self.total_questions = len(self.list_of_keys)

    def process_answer(self, answer):
        if answer == self.data["hiragana"][self.character]:
            self.correct_answers += 1
            self.list_of_keys.remove(self.character)
            self.remaining_questions = self.total_questions - self.correct_answers
            return f"Correct! {self.remaining_questions}/{self.total_questions} characters remaining"
        else:
            self.incorrect_answers += 1
            self.remaining_questions = self.total_questions - self.correct_answers
            return f"Incorrect! the reading is for {self.character} is '{self.data['hiragana'][self.character]}'"

    def score(self):
        answered_correctly = self.total_questions - self.incorrect_answers
        accuracy_percentage = round((answered_correctly / self.total_questions) * 100, 2)
        return accuracy_percentage

    def check_if_finished(self):
        # Checking to see if list is empty
        if not self.list_of_keys:
            return True




