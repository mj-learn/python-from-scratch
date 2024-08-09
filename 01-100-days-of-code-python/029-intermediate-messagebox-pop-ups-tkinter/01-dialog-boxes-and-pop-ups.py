import tkinter as tk
from tkinter import messagebox

window = tk.Tk()

messagebox.showinfo("some title", "info message")

messagebox.showerror("some error title", "error message")

is_ok = messagebox.askokcancel("Some Title", "Lorem ipsum dolor sit amet consectetur adipiscing elit pharetra")

if is_ok:
    print("Ok")


window.mainloop()
