import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    length = int(length_entry.get())
    use_digits = digits_var.get()
    use_special = special_var.get()

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits if use_digits else ''
    special = string.punctuation if use_special else ''

    all_chars = lower + upper + digits + special
    if not all_chars:
        messagebox.showerror("Error", "Select at least one character set!")
        return

    password = ''.join(random.choice(all_chars) for _ in range(length))
    password_var.set(password)

# Copy to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()
    messagebox.showinfo("Success", "Password copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Password Length:", font=("Arial", 12)).pack(pady=5)
length_entry = tk.Entry(root, width=5, font=("Arial", 12))
length_entry.pack()
length_entry.insert(0, "12")  # Default length

digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Digits", variable=digits_var, font=("Arial", 10)).pack()
tk.Checkbutton(root, text="Include Special Characters", variable=special_var, font=("Arial", 10)).pack()

tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12), bg="blue", fg="white").pack(pady=10)

password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, font=("Arial", 12), width=30, state="readonly").pack()

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 12), bg="green", fg="white").pack(pady=10)

# Run App
root.mainloop()
