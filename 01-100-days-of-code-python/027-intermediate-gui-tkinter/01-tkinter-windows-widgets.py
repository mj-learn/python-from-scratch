import tkinter

window = tkinter.Tk()
window.title("My fist GUI Program")
window.geometry("500x500+1600+400")


# Label
my_label = tkinter.Label(text="Some label text")
my_label["text"] = 'Some label text from my_label["text"]'
my_label.config(text="Some label text from my_label.config()")
my_label.pack()


# Button
def button_clicked():
    my_label["text"] = my_input.get()


my_button = tkinter.Button(text="click me")
my_button["text"] = "Click me!"
my_button["command"] = button_clicked
my_button.pack()


# Input
my_input = tkinter.Entry()
my_input.pack()


# Text box
my_text_box = tkinter.Text(height=5, width=30)
my_text_box.focus()
my_text_box.insert(tkinter.END, "Placeholder text")
print(my_text_box.get("1.0", tkinter.END))
my_text_box.pack()


# Spinbox
def spinbox_used():
    print(my_spinbox.get())


my_spinbox = tkinter.Spinbox(from_=3, to=10, width=5, command=spinbox_used)
my_spinbox.pack()


# Scale
def scale_used(value):
    print(value)


my_scale = tkinter.Scale(from_=5, to=98, command=scale_used)
my_scale.pack()


# Check buttons
def check_box_used():
    print(checked_state.get())


checked_state = tkinter.IntVar()
my_check_box = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=check_box_used)
my_check_box.pack()


# Radio buttons
def radio_btn_used():
    print(radio_state.get())


radio_state = tkinter.IntVar()
my_radio_btn_1 = tkinter.Radiobutton(text="Option 1", value=3, variable=radio_state, command=radio_btn_used)
my_radio_btn_2 = tkinter.Radiobutton(text="Option 2", value=5, variable=radio_state, command=radio_btn_used)
my_radio_btn_1.pack()
my_radio_btn_2.pack()


# Listbox
def listbox_used(event):
    print(my_list_box.get(my_list_box.curselection()))


my_list_box = tkinter.Listbox(height=5)
fuits = ["Apple", "Banana", "Orange", "Grape", "Pineapple", "Kiwi", "Mango", "Strawberry", "Blueberry", "Watermelon"]

for item in fuits:
    my_list_box.insert(fuits.index(item), item)

my_list_box.bind("<<ListboxSelect>>", listbox_used)
my_list_box.pack()

window.mainloop()
