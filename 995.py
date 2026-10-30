
import tkinter as tk
import random

root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")

secret_number = random.randint(1, 10)

tk.Label(
    root,
    text="Guess a number from 1 to 10"
).pack(pady=5)

entry1 = tk.Entry(root)
entry1.pack(pady=5)

result = tk.Label(root, text="Guess a number from 1 to 10")
result.pack(pady=5)

def check_guess():
    try:
        guess_number = int(entry1.get())

        if guess_number < 1 or guess_number > 10:
            result.config(text="Enter a number from 1 to 10")
        elif guess_number == secret_number:
            result.config(text="Correct! You win!")
        elif guess_number < secret_number:
            result.config(text="Too low!")
        else:
            result.config(text="Too high!")

    except ValueError:
        result.config(text="Enter a valid whole number")

tk.Button(
    root,
    text="Guess",
    command=check_guess
).pack(pady=5)

root.mainloop()
