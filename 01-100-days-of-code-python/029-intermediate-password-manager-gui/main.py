import tkinter as tk
from tkinter import messagebox
import pyperclip
from password_generator import PasswordGenerator


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
    if website and username and password:
        is_ok = messagebox.askyesno(
            title="Password Manager",
            message=f"Website: {website}\nEmail/Username: {username}\nPassword: {password}\n Is this ok?",
        )
        if is_ok:
            website_input.delete(0, tk.END)
            username_input.delete(0, tk.END)
            password_input.delete(0, tk.END)
            with open("passwords.csv", mode="a") as file:
                file.write(f"\n{website},{username},{password}")
    else:
        messagebox.showerror("Error", "Please don't leave any fields empty!")


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

website_input = tk.Entry(width=42)
website_input.focus()
website_input.grid(row=2, column=1, columnspan=2)

username_label = tk.Label(text="Email/Username:")
username_label.grid(row=3, column=0)

username_input = tk.Entry(width=42)
username_input.grid(row=3, column=1, columnspan=2, pady=10)

password_label = tk.Label(text="Password:")
password_label.grid(row=4, column=0)

password_input = tk.Entry(width=22)
password_input.grid(row=4, column=1)

generate_btn = tk.Button(text="Generate Password", command=generate_password)
generate_btn.config(bg="#379b46")
generate_btn.grid(row=4, column=2)

add_btn = tk.Button(text="Save password to CSV", command=save_password)
add_btn.config(width=36, bg="#3f93a9")
add_btn.grid(row=5, column=1, columnspan=2, pady=(10, 0))

window.mainloop()
