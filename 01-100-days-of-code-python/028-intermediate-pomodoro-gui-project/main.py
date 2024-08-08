import tkinter as tk

# CONSTANTS
PINK = "#E2979C"
RED = "#E7305B"
GREEN = "#9BDEAC"
YELLOW = "#F7F5DD"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = ""


# TIMER RESET
def reset_all():
    if timer:
        window.after_cancel(timer)

    global reps
    reps = 0
    pomodoro_label["text"] = "Timer"
    tomato_canvas.itemconfig(timer_text, text="00:00")
    check_marks["text"] = ""


# TIMER MECHANISM
def start_timer():
    reset_all()
    global reps
    reps = 1
    update_ui()


def update_ui():
    if reps > 8:
        return

    if reps == 8:
        pomodoro_label["text"] = "Long Break"
        check_marks["text"] = "✔✔✔✔"
        pomodoro_label.config(fg=PINK)
        count_down(LONG_BREAK_MIN)

    elif reps % 2 == 0:  # reps = 2, 4, 6
        check_str = ""
        for _ in range(reps // 2):
            check_str += "✔"
        pomodoro_label.config(fg=RED)
        pomodoro_label["text"] = f"Break"
        check_marks["text"] = check_str
        count_down(SHORT_BREAK_MIN)

    else:  # reps = 1, 3, 5, 7
        pomodoro_label.config(fg=GREEN)
        pomodoro_label["text"] = f"Work"
        count_down(WORK_MIN)


def update_timer(minutes, seconds):
    if seconds > 0:
        seconds -= 1
        count_down(minutes, seconds)
    elif minutes > 0:
        minutes -= 1
        seconds = 59
        count_down(minutes, seconds)


# COUNTDOWN MECHANISM
def count_down(minutes, seconds=0):
    tomato_canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")
    if minutes > 0 or seconds > 0:
        global timer
        timer = window.after(1000, update_timer, minutes, seconds)
    else:
        global reps
        reps += 1
        update_ui()


# UI SETUP
window = tk.Tk()
window.title("Pomodoro")
# window.minsize(600, 600)
window.config(padx=50, pady=50, bg=YELLOW)

pomodoro_label = tk.Label(font=(FONT_NAME, 40, "bold"), bg=YELLOW, foreground=GREEN)
pomodoro_label["text"] = "Timer"
pomodoro_label.grid(row=1, column=1, columnspan=3)

tomato_canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tk.PhotoImage(file="assets/tomato.png")
tomato_canvas.create_image(100, 112, image=tomato_image)
timer_text = tomato_canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
tomato_canvas.grid(row=2, column=2, pady=50)

start_btn = tk.Button(text="Start", font=(FONT_NAME, 20), bg=GREEN, foreground="#1b4e23", command=start_timer)
start_btn.grid(row=3, column=1)

check_marks = tk.Label(text="")
check_marks.config(fg=GREEN, font=(FONT_NAME, 25, "bold"), bg=YELLOW)
check_marks.grid(row=3, column=2)

reset_btn = tk.Button(text="Reset", font=(FONT_NAME, 20), bg=RED, fg="#4d101e", command=reset_all)
reset_btn.grid(row=3, column=3)


window.mainloop()
