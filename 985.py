import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title("Age Calculator")
root.geometry("350x250")

tk.Label(root , text = "Birth Year").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)


result = tk.Label(root , text = "Age:")
result.pack(pady=10)


def calculate_age():
    try :
        birth_year = int(entry.get())
        current_year = datetime.now().year

        if birth_year <= 0 or birth_year > current_year :
            result.config(text = "Enter a valid birth year")
            return

        age = current_year - birth_year
        result.config(text = f"Approximate age: {age}")

    except ValueError :
        result.config(text = "Enter a whole-number year")


tk.Button(
    root , 
    text = "Calculate Age" ,
    command = calculate_age
).pack(pady=5)

root.mainloop()