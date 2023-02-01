from tkinter import *
from time import *
from math import *
# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    root.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1 
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps%8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg = RED)

    elif reps%2==0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg = PINK)
    
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg = GREEN)


    count_down(5*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_min = floor(count/60)
    count_sec = count % 60 
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count>0:
        timer = root.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(floor(reps/2)):
            mark += "✔"

# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.title("Pomodoro")
root.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img  = PhotoImage(file="C:/Users/asus/Desktop/repos/100_days_of_python/Day-28/tomato.png")

title_label = Label(text="Timer", font = (FONT_NAME, 45, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row = 0)

canvas.create_image(100, 112, image =  tomato_img)
timer_text = canvas.create_text(100, 130, text = "00:00", fill="white", font = (FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)


start_button = Button(text = "Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text = "Reset", command= reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(text="✔", fg=GREEN, bg=YELLOW)
check_label.grid(column=1,row=3)    

root.mainloop()
