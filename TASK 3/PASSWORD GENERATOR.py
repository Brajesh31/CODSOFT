import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    char = string.ascii_letters + string.digits
    valid_punctuation = "@#$^&*_"
    allowed_chars = char + valid_punctuation
    password = ''.join(random.choices(allowed_chars, k=length))
    return password

def generate_password_button():
    try:
        len_value = int(length_entry.get())
        if len_value <= 0:
            messagebox.showerror("Error", "Password length must be greater than zero.")
            return
        
        password = generate_password(len_value)
        password_var.set(password)  # Update the password_var with the generated password
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for password length.")

root = tk.Tk()
root.title("Password Generator")
root.geometry("600x400")  # Increased window size
root.config(bg='light blue')
root.resizable(False, False)

# Custom Fonts
label_font = ('Arial', 14)
entry_font = ('Arial', 14)
button_font = ('Arial', 12, 'bold')

length_label = tk.Label(root, text="Password Length:", bg='light blue', font=label_font)
length_label.pack(pady=(20, 5))

length_entry = tk.Entry(root, width=30, font=entry_font)
length_entry.pack()

generate_btn = tk.Button(root, text="Generate Password", command=generate_password_button, font=button_font)
generate_btn.pack(pady=20)

password_label = tk.Label(root, text="Generated Password:", bg='light blue', font=label_font)
password_label.pack(pady=(20, 5))

password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, width=50, font=entry_font, state='readonly')
password_entry.pack()

root.mainloop()
