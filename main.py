from tkinter import *
import json
import random

def start_test():
    global data
    global list_of_keys
    global character
    global correct_answers
    global total_questions
    with open("kana.json", "r") as file:
        data = json.load(file)
        list_of_keys = list(data["hiragana"].keys())
        character = random.choice(list_of_keys)
        question_label.config(text=character)
    correct_answers = 0
    total_questions = len(list_of_keys)
    feedback_label.config(text="", bg="#fff0f6")


def get_answer():
    global character
    global correct_answers
    global total_questions
    answer = answer_entry.get().lower()
    if answer == data["hiragana"][character]:
        correct_answers += 1
        list_of_keys.remove(character)
        remaining_questions = total_questions - correct_answers
        feedback_label.config(text=f"Correct! {remaining_questions}/{total_questions} characters remaining", bg="#8ce99a")
    else:
        remaining_questions = total_questions - correct_answers
        feedback_label.config(text=f"Incorrect! the reading is for {character} is '{data['hiragana'][character]}'", bg="#fa5252")
    answer_entry.delete(0, END)

    if list_of_keys == []:
        question_label.config(text="You've finished!")
        feedback_label.config(text=f"{calculate_score()}% correct")
        submit_button.config(state=DISABLED)
    else:
        character = random.choice(list_of_keys)
        question_label.config(text=character)

def calculate_score():
    global correct_answers
    global total_questions
    num = round(total_questions / correct_answers, 2)
    return num * 100

# For binding the enter key to the same function as the submit button
def enter_key(event):
    get_answer()


# ------------- Window Object ------------------
root = Tk()
root.title("Practice Hiragana")
root.minsize(600, 500)
root.config(padx=40, pady=40, bg="#fff0f6")
root.bind('<Return>', enter_key)

# Labels
header_label = feedback_label = Label(text="Hiragana", font=("Arial", 40), bg="#fff0f6")
header_label.grid(row=0, column=1, pady=10)
question_label = Label(text="", font=("Arial", 100), bg="#fff0f6")
question_label.grid(row=1, column=1, pady=10)
feedback_label = Label(text="", font=("Arial", 20), bg="#fff0f6")
feedback_label.grid(row=3, column=0, columnspan=3, pady=20)

# Entries
answer_entry = Entry(width=10, font=("Arial", 40), justify="center")
answer_entry.grid(row=2, column=1, pady=10)

# Buttons
submit_button = Button(text="Submit", width=10, font=("Arial", 24), command=get_answer)
submit_button.grid(row=4, column=0, pady=10)
reset_button = Button(text="Begin/Reset", width=10, font=("Arial", 24), command=start_test)
reset_button.grid(row=4, column=2, pady=10)

root.mainloop()

