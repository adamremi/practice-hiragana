from tkinter import *
from test import *


def start_test():
    global test
    test = Test()
    question_label.config(text=test.character, font=("Arial", 100))
    submit_button.config(state=NORMAL)


def get_answer():
    test_finished = test.check_if_finished()
    if test_finished:
        test_results()
    else:
        answer = answer_entry.get().lower()
        feedback = test.process_answer(answer)
        if "Incorrect" in feedback:
            feedback_label.config(text=feedback, bg="#fa5252")
        else:
            feedback_label.config(text=feedback, bg="#8ce99a")
        # Checking to see if the test is done again in order to avoid an IndexError
        if test.check_if_finished():
            test_results()
        else:
            test.character = random.choice(test.list_of_keys)
            question_label.config(text=test.character)

        answer_entry.delete(0, END)


def test_results():
    question_label.config(text="You've finished!", font=("Arial", 40))
    feedback_label.config(text=f"{test.score()}% correct", bg="#fff0f6")
    submit_button.config(state=DISABLED)

# For binding the enter key to the same function as the submit button
def enter_key(event):
    get_answer()


# ------------- Window Object ------------------
root = Tk()
root.title("Practice Hiragana")
root.minsize(620, 500)
root.config(padx=100, pady=40, bg="#fff0f6")
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
