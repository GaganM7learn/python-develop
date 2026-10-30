
import tkinter as tk
import random

root = tk.Tk()
root.title("Guessing Game - 5 Attempts")
root.geometry("400x320")

secret_number = random.randint(1, 10)
attempts_left = 5
game_over = False

tk.Label(
    root,
    text="Guess a number from 1 to 10"
).pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

result = tk.Label(root, text="Make your first guess!")
result.pack(pady=10)

attempts_label = tk.Label(root, text="Attempts left: 5")
attempts_label.pack(pady=5)

def check_guess():
    global attempts_left, game_over

    if game_over:
        return

    try:
        guess = int(entry.get())

        if guess < 1 or guess > 10:
            result.config(text="Enter a number from 1 to 10")
            return

        attempts_left -= 1
        attempts_label.config(
            text=f"Attempts left: {attempts_left}"
        )

        if guess == secret_number:
            result.config(text="Correct! You win!")
            game_over = True
            guess_button.config(state="disabled")

        elif attempts_left == 0:
            result.config(
                text=f"Game over! The number was {secret_number}"
            )
            game_over = True
            guess_button.config(state="disabled")

        elif guess < secret_number:
            result.config(text="Too low!")

        else:
            result.config(text="Too high!")

    except ValueError:
        result.config(text="Enter a valid whole number")

guess_button = tk.Button(
    root,
    text="Guess",
    command=check_guess
)
guess_button.pack(pady=10)

root.mainloop()
