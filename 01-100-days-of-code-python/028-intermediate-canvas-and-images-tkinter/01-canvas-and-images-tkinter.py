# from tkinter import *  # Not like this import style
import tkinter as tk

windows = tk.Tk()
windows.config(bg="#CCCCCC")
windows.minsize(500, 500)

# Canvas Widget
my_canvas = tk.Canvas(width=300, height=300, bg="#999999")  # width & height of the canvas
placeholder_img = tk.PhotoImage(file="placeholder.png")
my_canvas.create_image(125, 125, image=placeholder_img)  # x & y from center of image
my_canvas.create_text(100, 150, text="placeholder", font=("Helvetica", 12, "bold"))  # x & y from center of text label
my_canvas.place(x=0, y=0)

# Canvas Widget 2
# highlightthickness=0 remove white border of the canvas widget
my_canvas_2 = tk.Canvas(width=300, height=300, bg="#666666", highlightthickness=0)  # This canvas will be on top
python_img = tk.PhotoImage(file="python.png")
my_canvas_2.create_image(125, 125, image=python_img)
my_canvas_2_text = my_canvas_2.create_text(
    100, 100, text="some text", fill="#fed140", font=("Helvetica", 12, "bold")
)  # x & y from center of text label
my_canvas_2.place(x=100, y=100)

my_canvas_2.itemconfig(my_canvas_2_text, text="Python")  # Reconfigure element of canvas later
windows.mainloop()
