import tkinter as tk

import random

root = tk.Tk()
root.title("Guessiing Game- 5 Attempts")
root.geometry("400x320")


attempts_left = 5
guess_random_com  = random.randint(1,10)
game_over = False

tk.Label(root , text = "guess a number from 1 to 10").pack(pady=5)
entry = tk.Entry(root )
entry.pack(pady=5)

result = tk.Label(root , text = "Make your guess in number")
result.pack(pady=5)

def function_to_guess():
    global attempts_left , game_over   
    if game_over :
        return

    try :
        
        number_entered = int(entry.get())
        if number_entered > 10 or number_entered < 0 :
           result.config(text = "Enter a number from 1 to 10")
           return

        attempts_left -= 1
        result.config( text = f"Attempts Left : {attempts_left}")


        if number_entered == guess_random_com :
            result.config(text = "Correct ! You Win !")
            game_over = True
            guess_button.config(state = "disabled")

        elif attempts_left == 0 :
            result.config(text = f"Game Over! The number was {guess_random_com}")
            game_over = True
            guess_button.config(state = "disabled")

        elif number_entered > guess_random_com :
            result.config(text = "Too High!")

        else :
            result.config(text = "Too Low!")

    except ValueError :
        result.config(text = "Please enter a valid input")



guess_button = tk.Button(root , text = "Guess" , command = function_to_guess )
guess_button.pack(pady=5)


root.mainloop()
        

