from tkinter import *
from random import *
import pandas
from pandas import *

BACKGROUND_COLOR = "#B1DDC6"


try:
    data = pandas.read_csv("data/words_to_learn.csv.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

current_card = {}


def next_card():
    global current_card, flip_timer
    root.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_image)
    flip_timer = root.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back_image)


def is_known():
    to_learn.remove(current_card)
    to_learn_data = DataFrame(to_learn)
    to_learn_adata.to_csv("data/words_to_learn.csv", index=FALSE)
    next_card()


root = Tk()
root.title("Flash Card")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = root.after(3000, func=flip_card)

canvas = Canvas(width=800,  height=526)

card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")

canvas_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, relief=SOLID, border=0.5,
                        command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, relief=SOLID, border=0.5, command=is_known)
known_button.grid(row=1, column=1)

next_card()

root.mainloop()
