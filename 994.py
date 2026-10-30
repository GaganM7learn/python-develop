import tkinter as tk

import random

### me

root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")

tk.Label(root , text = "Guess a random number 1 to 10").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

result = tk.Label(root , text = "")
result.pack(pady=5)

def generate_a_random_number():
    try :
            
       guess_number = float(entry1.get())
       number = random.randint(1,10)

       if number == guess_number :
          result.config(text = "Correct! you win! ")
       elif number > guess_number :
          result.config(text = "Too low!")

       elif number < guess_number :
          result.config(text = "Too high")


    except ValueError :
       result.config(text = "Enter a valid number")

tk.Button(root , text = "Guess" , command = generate_a_random_number ).pack(pady=5)


root.mainloop()

    