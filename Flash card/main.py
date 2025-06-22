from tkinter import *
import pandas
import random
from mtoe import malayalam_words

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
# data_list = data.to_dict(orient="records")
data_list = malayalam_words
word_dict = {}

def next_card():
    global word_dict, window_timer
    window.after_cancel(window_timer)
    word_dict = random.choice(data_list)
    canvas.itemconfig(canvas_title, text="Malayalam", fill="black")
    canvas.itemconfig(canvas_word, text=word_dict["Malayalam"], fill="black")
    canvas.itemconfig(canvas_bg, image=front_image)
    window_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_bg, image=back_image)
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=word_dict["English"].title(), fill="white")


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_bg = canvas.create_image(400, 263, image=front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_title = canvas.create_text(400, 150, text="", font=("arial", 40, 'italic'))
canvas_word = canvas.create_text(400, 263, text="", font=("arial", 68, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, command=next_card, highlightthickness=0)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, command=next_card, highlightthickness=0)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()