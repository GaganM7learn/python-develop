import tkinter as tk
from datetime import datetime
## me

root = tk.Tk()
root.title("Age and Birth-Year Checker")
root.geometry("400x300")

tk.Label(root , text = "birth year").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

result1 = tk.Label(root , text = "Result:")
result1.pack(pady=5)

result2 = tk.Label(root , text = "Birth Year:")
result2.pack(pady=5)

def calculate_function():
    try :
        
        birth_year = int(entry1.get())
        current_year = datetime.now().year

        if birth_year <=0 or birth_year > current_year :
            result1.config(text = "Enter a valid birth year")
            result2.config(text = "")
            return

        age = current_year - birth_year
        result1.config(text = f"Result: {age:.2f}")
        result2.config(text = f"Birth Year: {birth_year:.0f}")

    except ValueError :
        result1.config(text = "Please enter a valid numbers")
        result2.config(text = "")

button = tk.Button(
    root ,
    text = "Check Age" , 
    command = calculate_function
)
button.pack(pady=5)


root.mainloop()