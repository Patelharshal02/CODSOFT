import tkinter as tk
import random

def play_game():
    user_choice = int(user_choice_entry.get())
    if user_choice < 0 or user_choice > 2:
        result_label.config(text="YOU ENTERED INVALID VALUE SORRY.. YOU LOSE", font=("Helvetica", 14))
    else:
        computer_choice = random.randint(0, 2)
        computer_choice_label.config(text=f"COMPUTER CHOICE IS: {computer_choice}", font=("Helvetica", 14))
        if computer_choice == user_choice:
            result_label.config(text="MATCH IS DRAW", font=("Helvetica", 14))
        elif computer_choice == 0 and user_choice == 2:
            result_label.config(text="YOU LOSE", font=("Helvetica", 14))
        elif user_choice == 0 and computer_choice == 2:
            result_label.config(text="YOU WIN", font=("Helvetica", 14))
        elif computer_choice > user_choice:
            result_label.config(text="YOU LOSE", font=("Helvetica", 14))
        elif user_choice > computer_choice:
            result_label.config(text="YOU WIN", font=("Helvetica", 14))

root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

user_choice_label = tk.Label(root, text="Enter your choice (0 for Rock, 1 for Paper, 2 for Scissors):", font=("Helvetica", 14))
user_choice_entry = tk.Entry(root)
play_button = tk.Button(root, text="Play", command=play_game)
computer_choice_label = tk.Label(root, text="COMPUTER CHOICE IS:", font=("Helvetica", 14))
result_label = tk.Label(root, text="", font=("Helvetica", 14))

user_choice_label.grid(row=0, column=0, padx=5, pady=5)
user_choice_entry.grid(row=0, column=1, padx=5, pady=5)
play_button.grid(row=0, column=2, padx=5, pady=5)
computer_choice_label.grid(row=1, column=0, padx=5, pady=5)
result_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
