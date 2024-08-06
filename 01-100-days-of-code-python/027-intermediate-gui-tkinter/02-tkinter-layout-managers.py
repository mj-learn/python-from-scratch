import tkinter

# pack(): A geometry manager that organizes widgets in blocks before placing them in the parent widget.
# It automatically adjusts the size and position of the widgets based on the order of packing.

# place(): A geometry manager that positions widgets at an absolute location you specify.
# It allows precise control over the position and size of the widgets using x, y coordinates.

# grid(): A geometry manager that organizes widgets in a table-like structure with rows and columns.
# It makes it easy to create complex layouts by specifying the row and column for each widget.

window = tkinter.Tk()
window.geometry("700x700+1500+300")
window.config(padx=30, pady=30)  # windows padding

label_1 = tkinter.Label(text="Label 1", font=("Arial", 18, "bold"))
label_1.grid(column=1, row=1)
label_1.config(padx=20, pady=20)  # padding around this element

label_2 = tkinter.Label(text="Label 2", font=("Arial", 18, "bold"))
label_2.grid(column=3, row=1)
label_2.config(padx=20, pady=20)  # padding around this element

label_3 = tkinter.Label(text="Label 3", font=("Arial", 18, "bold"))
label_3.grid(column=2, row=2)
label_3.config(padx=20, pady=20)  # padding around this element

label_4 = tkinter.Label(text="Label 4", font=("Arial", 18, "bold"))
label_4.grid(column=4, row=3)
label_4.config(padx=20, pady=20)  # padding around this element

window.mainloop()
