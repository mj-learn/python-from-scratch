import tkinter as tk
import pandas

BG_COLOR = "#B1DDC6"
LANG_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
START_BTN_FONT = ("Arial", 30, "normal")

data = None
random_word = None


# CARD FUNCTIONS
def get_random_word():
    try:
        return data.sample(n=1)
    except ValueError:
        raise


def update_card():
    card_canvas.itemconfig(canvas_img, image=card_img_back)
    card_canvas.itemconfig(lang_text, text="French", fill="#FFFFFF")
    card_canvas.itemconfig(word_text, text=random_word["French"].item(), fill="#FFFFFF")


def wrong():
    wrong_btn.grid_forget()
    right_btn.grid_forget()
    flip_btn.grid(row=2, column=2)
    global random_word
    random_word = get_random_word()
    update_card()


def right():
    wrong_btn.grid_forget()
    right_btn.grid_forget()
    flip_btn.grid(row=2, column=2)
    global data, random_word
    data = data.drop(random_word.index)
    try:
        random_word = get_random_word()
        update_card()
    except ValueError:
        end()


def flip_card():
    card_canvas.itemconfig(canvas_img, image=card_img_front)
    card_canvas.itemconfig(lang_text, text="English", fill="#000000")
    card_canvas.itemconfig(word_text, text=random_word["English"].item(), fill="#000000")
    flip_btn.grid_forget()
    wrong_btn.grid(row=2, column=1)
    right_btn.grid(row=2, column=3)


def end():
    card_canvas.itemconfig(canvas_img, image=card_img_back)
    card_canvas.itemconfig(lang_text, text="Finish", fill="#FFFFFF")
    card_canvas.itemconfig(word_text, text="Try again", fill="#FFFFFF")
    flip_btn.grid_forget()
    wrong_btn.grid_forget()
    right_btn.grid_forget()
    start_btn.grid(row=2, column=2)


def start():
    global data
    data = pandas.read_csv("data/french_words-demo.csv")
    start_btn.grid_forget()
    flip_btn.grid(row=2, column=2)
    global random_word
    random_word = get_random_word()
    update_card()


# UI
root = tk.Tk()
root.title("Flashy")
root.config(pady=30, padx=30, bg=BG_COLOR)

card_canvas = tk.Canvas(width=800, height=546, bg=BG_COLOR, highlightthickness=0)
card_img_front = tk.PhotoImage(file="images/card_front.png")
card_img_back = tk.PhotoImage(file="images/card_back.png")
canvas_img = card_canvas.create_image(400, 263, image=card_img_back)
lang_text = card_canvas.create_text(400, 150, text="Language", font=LANG_FONT, fill="#FFFFFF")
word_text = card_canvas.create_text(400, 300, text="Word", font=WORD_FONT, fill="#FFFFFF")
card_canvas.grid(row=1, column=1, columnspan=3)

wrong_img = tk.PhotoImage(file="images/wrong.png")
wrong_btn = tk.Button(width=100, height=100, image=wrong_img, bg=BG_COLOR, highlightthickness=0, border=0)
wrong_btn.config(command=wrong)

flip_img = tk.PhotoImage(file="images/flip.png")
flip_btn = tk.Button(width=97, height=95, image=flip_img, bg=BG_COLOR, highlightthickness=0, border=0)
flip_btn.config(command=flip_card)

start_btn = tk.Button(text="Start", font=START_BTN_FONT, command=start)
start_btn.grid(row=2, column=2)

right_img = tk.PhotoImage(file="images/right.png")
right_btn = tk.Button(width=100, height=100, image=right_img, bg=BG_COLOR, highlightthickness=0, border=0)
right_btn.config(command=right)

root.mainloop()
