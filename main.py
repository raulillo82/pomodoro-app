from tkinter import *
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
    button_start.config(state="normal")
    button_reset.config(state="disabled")
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    button_start.config(state="disabled")
    button_reset.config(state="normal")
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    if reps % 2 != 0:
        count_down_secs = work_secs
        timer_label.config(text="Work", fg=GREEN)
    elif reps % 2 == 0:
        count_down_secs = short_break_secs
        timer_label.config(text="Break", fg=PINK)
    elif reps % 8 == 0:
        count_down_secs = long_break_secs
        timer_label.config(text="Break", fg=RED)
    else:
        count_down_secs = 0
    count_down(count_down_secs)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = count // 60 
    seconds = count % 60 
    if seconds < 10:
        seconds = "0" + str(seconds)

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if (count > 0):
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            check_label.config(text=check_label["text"] + "✔")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35,
                                                               "bold"))

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
check_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))

button_start = Button(text="Start", highlightthickness=0, command=start_timer,
                      state="normal")
button_reset = Button(text="Reset", highlightthickness=0, command=reset_timer,
                      state="disabled")

canvas.grid(row=1, column=1)
timer_label.grid(row=0, column=1)
check_label.grid(row=3, column=1)
button_start.grid(row=2, column=0)
button_reset.grid(row=2, column=2)

window.mainloop()
