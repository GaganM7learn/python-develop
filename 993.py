import tkinter  as tk

import random
root = tk.Tk()
root.title("Random Number Calculator")
root.geometry("350x250")

result = tk.Label(root , text = "Click to generate a number")
result.pack(pady=20)


def generate_number():
    number = random.randint(1,10)
    result.config(text = f"Random number: {number}")

tk.Button(
    root ,
    text = "Generate" , 
    command = generate_number
)
root.mainloop()