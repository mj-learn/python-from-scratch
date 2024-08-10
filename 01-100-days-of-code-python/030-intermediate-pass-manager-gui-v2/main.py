import json
import tkinter as tk
from tkinter import messagebox
import pyperclip
from password_generator import PasswordGenerator

FONT_INPUT = ("Helvetica", 14, "normal")


# -- LOAD AND UPDATE JSON FILE ------------------------------------------------- #
def load_data():
    try:
        with open("data.json") as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {}


def save_new_data(new_data):
    data = load_data()
    data.update(new_data)
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)


# -- SEARCH IN JSON DATA -------------------------------------------------------- #
def search_in_data():
    url = website_input.get()
    if url:
        data = load_data()
        if url in data.keys():
            messagebox.showinfo(f"{url}", f"Username: {data[url]['username']}\nPassword: {data[url]['password']}")
        else:
            messagebox.showerror("Not found!", f"{url} is not in local data")
    else:
        messagebox.showerror("Error in search", "Website filed is empty")


# -- PASSWORD GENERATOR --------------------------------------------------------- #
def generate_password():
    pswrd = PasswordGenerator()
    password = pswrd.generate_password()
    pyperclip.copy(password)
    password_input.delete(0, tk.END)
    password_input.insert(0, password)


# -- SAVE PASSWORD -------------------------------------------------------------- #
def save_password():
    website = website_input.get().strip()
    username = username_input.get().strip()
    password = password_input.get().strip()
    try:
        if website and username and password:
            is_ok = messagebox.askyesno(
                title="Password Manager",
                message=f"Website: {website}\nEmail/Username: {username}\nPassword: {password}\nIs this ok?",
            )

            new_data = {
                website: {
                    "username": username,
                    "password": password,
                }
            }
        else:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Please don't leave any fields empty!")
    else:
        if is_ok:
            save_new_data(new_data)
            website_input.delete(0, tk.END)
            username_input.delete(0, tk.END)
            password_input.delete(0, tk.END)


# -- UI SETUP ------------------------------------------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)

logo_canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file="assets/logo.png")
logo_canvas.create_image(100, 100, image=logo_img)
logo_canvas.grid(row=1, column=0, columnspan=3)

website_label = tk.Label(text="Website:", width=10)
website_label.grid(row=2, column=0)

website_input = tk.Entry(width=17, font=FONT_INPUT)
website_input.focus()
website_input.grid(row=2, column=1)

search_btn = tk.Button(text="Search in vault", width=15, command=search_in_data)
search_btn.grid(row=2, column=2)

username_label = tk.Label(text="Username:")
username_label.grid(row=3, column=0)

username_input = tk.Entry(width=28, font=FONT_INPUT)
username_input.grid(row=3, column=1, columnspan=2, pady=10, padx=(0, 0))

password_label = tk.Label(text="Password:")
password_label.grid(row=4, column=0)

password_input = tk.Entry(width=17, font=FONT_INPUT)
password_input.grid(row=4, column=1)

generate_btn = tk.Button(text="Generate Password", command=generate_password)
generate_btn.config(bg="#379b46")
generate_btn.grid(row=4, column=2)

add_btn = tk.Button(text="Add password in local vault", font=FONT_INPUT, command=save_password)
add_btn.config(width=36, bg="#3f93a9")
add_btn.grid(row=5, column=0, columnspan=3, pady=(15, 0))

window.mainloop()
