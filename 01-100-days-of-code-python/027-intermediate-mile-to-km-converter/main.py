import tkinter as tk


def mile_to_km():
    # miles * 1.60934 = km
    km = float(miles_input.get()) * 1.60934
    km_label["text"] = f"{miles_input.get()} Mile(s) = {km:.2f} Kilometer(s)"


def clear():
    miles_input.delete(0, tk.END)
    km_label["text"] = "Enter the distance to calculate"


window = tk.Tk()
window.title("Mile to Km Converter")
window.config(padx=30, pady=30)

title_label = tk.Label(text="Mile to Kilometers Converter\n")
title_label.config(font=("Helvetica", 12, "bold"))
title_label.grid(row=0, column=0, columnspan=4, sticky="ew")

enter_distance_label = tk.Label(text="Enter the distance")
enter_distance_label.config(font=("Helvetica", 12))
enter_distance_label.grid(column=1, row=2)

miles_input = tk.Entry()
miles_input.config(font=("Helvetica", 12), width=8)
miles_input.grid(column=2, row=2)

miles_label = tk.Label(text="Miles")
miles_label.config(font=("Helvetica", 12))
miles_label.grid(column=3, row=2)

km_label = tk.Label(text="Enter the distance to calculate")
km_label.config(pady=20, font=("Helvetica", 12))
km_label.grid(row=3, column=0, columnspan=4, sticky="ew")

calc_btn = tk.Button(text="Calculate")
calc_btn.config(padx=20, font=("Helvetica", 12))
calc_btn.grid(row=4, column=1)
calc_btn["command"] = mile_to_km

clear_btn = tk.Button(text="Clear")
clear_btn.config(padx=30, font=("Helvetica", 12))
clear_btn.grid(row=4, column=2)
clear_btn["command"] = clear

window.mainloop()
