from tkinter import *
import math

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
ticks = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def button_reset_clicked():
    global ticks
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    ticks = ""
    tick.config(text=ticks)
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def button_start_clicked():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global ticks
    count_min = math.floor(count / 60)
    count_sec = count % 60
    count_sec = ("0" + str(count_sec))[-2:]

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        button_start_clicked()
        if reps % 2 == 0:
            ticks += "✔"
            tick.config(text=ticks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN, padx=5, pady=5)
title.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

button_start = Button(text="Start", command=button_start_clicked, highlightthickness=0)
button_start.grid(row=2, column=0)
button_start.config(padx=5, pady=5)

button_reset = Button(text="Reset", command=button_reset_clicked, highlightthickness=0)
button_reset.grid(row=2, column=2)
button_reset.config(padx=5, pady=5)

tick = Label(font=(FONT_NAME, 12, "bold"), bg=YELLOW, fg=GREEN, padx=5, pady=5)
tick.grid(row=3, column=1)

window.mainloop()
