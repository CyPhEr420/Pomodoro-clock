# ---------------------------- CONSTANTS ------------------------------- #
from tkinter import *
import math

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
    window.after_cancel(timer)
    head_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    tick_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        head_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        head_label.config(text="Break", fg=PINK)
    else:
        head_label.config(text="Work")
        count_down(WORK_MIN * 60)


def count_down(count):
    count_minute = math.floor(count / 60)
    count_second = math.floor(count % 60)
    if count_second < 10:
        count_second = f"0{count_second}"
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        marks = ""
        start_timer()
        work_session = math.floor(reps / 2)
        print(work_session)
        for _ in range(work_session):
            marks += "✔"
        tick_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

head_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
head_label.grid(row=1, column=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 112, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=2, column=2)

# BUTTONS

start_button = Button(text="Start", width=7, highlightthickness=0, command=start_timer)
start_button.grid(row=3, column=1)

reset_button = Button(text="Reset", width=7, highlightthickness=0, command=reset_timer)
reset_button.grid(row=3, column=3)

tick_marks = Label(bg=YELLOW, fg=GREEN)
tick_marks.grid(row=4, column=2)

window.mainloop()
