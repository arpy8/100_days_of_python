from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

root = Tk()

wrong_image = "/images/wrong.png"
right_image = "/images/right.png"
wrong = PhotoImage(file=wrong_image)
right = PhotoImage(file=right_image)

wrong_button = Button(image=wrong, highlightthickness=0)
wrong_button.grid(row=0, column=0)
right_button = Button(image=right, highlightthickness=0)
wrong_button.grid(row=0, column=0)

root.mainloop()
