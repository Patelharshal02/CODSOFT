import tkinter as tk
from tkinter import messagebox
import random

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x400")
        self.root.configure(bg='#1d3557')  

        self.create_widgets()

    def create_widgets(self):
        header_label = tk.Label(self.root, text="WELCOME TO PASSWORD GENERATOR....👋", font=("Helvetica", 14, "bold"), bg='#1d3557', fg='#f1faee')
        header_label.pack(pady=20)
        
        input_frame = tk.Frame(self.root, bg='#1d3557')
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Enter number of letters:", bg='#1d3557', fg='#f1faee').grid(row=0, column=0, pady=5, sticky='e')
        self.letter_entry = tk.Entry(input_frame, width=5, bg='#a8dadc', fg='#000000')
        self.letter_entry.grid(row=0, column=1, pady=5, padx=10)

        tk.Label(input_frame, text="Enter number of numbers:", bg='#1d3557', fg='#f1faee').grid(row=1, column=0, pady=5, sticky='e')
        self.number_entry = tk.Entry(input_frame, width=5, bg='#a8dadc', fg='#000000')
        self.number_entry.grid(row=1, column=1, pady=5, padx=10)

        tk.Label(input_frame, text="Enter number of symbols:", bg='#1d3557', fg='#f1faee').grid(row=2, column=0, pady=5, sticky='e')
        self.symbol_entry = tk.Entry(input_frame, width=5, bg='#a8dadc', fg='#000000')
        self.symbol_entry.grid(row=2, column=1, pady=5, padx=10)

        self.generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password, bg='#457b9d', fg='#f1faee', font=("Helvetica", 10, "bold"))
        self.generate_button.pack(pady=20)

        self.password_label = tk.Label(self.root, text="Generated Password:", bg='#1d3557', fg='#f1faee', font=("Helvetica", 10, "bold"))
        self.password_label.pack(pady=5)

        self.password_display = tk.Entry(self.root, width=40, bg='#a8dadc', fg='#000000', font=("Helvetica", 10))
        self.password_display.pack(pady=5)

        self.copy_button = tk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard, bg='#457b9d', fg='#f1faee', font=("Helvetica", 10, "bold"))
        self.copy_button.pack(pady=10)

    def generate_password(self):
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numbers = '0123456789'
        symbols = '!@#$%*&( )'

        try:
            n_let = int(self.letter_entry.get())
            n_num = int(self.number_entry.get())
            n_sym = int(self.symbol_entry.get())

            if n_let < 0 or n_num < 0 or n_sym < 0:
                raise ValueError("Number of characters must be non-negative")

            password_list = []

            for _ in range(n_let):
                password_list.append(random.choice(letters))
            
            for _ in range(n_num):
                password_list.append(random.choice(numbers))
            
            for _ in range(n_sym):
                password_list.append(random.choice(symbols))

            random.shuffle(password_list)

            password = ''.join(password_list)
            self.password_display.delete(0, tk.END)
            self.password_display.insert(0, password)

        except ValueError as e:
            messagebox.showerror("Input Error", f"Invalid input: {e}")

    def copy_to_clipboard(self):
        password = self.password_display.get()
        self.root.clipboard_clear()
        self.root.clipboard_append(password)
        messagebox.showinfo("Clipboard", "Password copied to clipboard!")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
