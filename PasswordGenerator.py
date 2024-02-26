import random
import string
import tkinter as tk
from tkinter import messagebox

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x250")

        self.label = tk.Label(root, text="Generate Strong Passwords", font=("Arial", 16))
        self.label.pack(pady=10)

        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack()
        self.length_entry = tk.Entry(root)
        self.length_entry.pack()

        self.num_passwords_label = tk.Label(root, text="Number of Passwords:")
        self.num_passwords_label.pack()
        self.num_passwords_entry = tk.Entry(root)
        self.num_passwords_entry.pack()

        self.generate_button = tk.Button(root, text="Generate Passwords", command=self.generate_passwords)
        self.generate_button.pack(pady=10)

    def generate_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def generate_passwords(self):
        try:
            length = int(self.length_entry.get())
            num_passwords = int(self.num_passwords_entry.get())
            if length <= 0 or num_passwords <= 0:
                raise ValueError("Password length and number of passwords must be positive")

            passwords = [self.generate_password(length) for _ in range(num_passwords)]
            passwords_text = "\n".join(passwords)
            messagebox.showinfo("Generated Passwords", f"Your passwords:\n{passwords_text}")

        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
