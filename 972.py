import tkinter as tk

root = tk.Tk()
root.title("Four-Operation Calculator")
root.geometry("400x400")

tk.Label(root , text="First Number").pack(pady=10)
entry1 = tk.Entry(root )
entry1.pack(pady=10)

tk.Label(root , text = "Second Number").pack(pady=10)
entry2 = tk.Entry(root)
entry2.pack(pady=10)

result = tk.Label(root , text = "Result: ")
result.pack(pady=10)

def add():
    number1 = float(entry1.get())
    number2 = float(entry2.get())
    try :

         added = number1 + number2
         result.config(text = f"Result: {added}")
    except ValueError :
        result.config(text = "Result: Please enter a valid number")


def subtract():
    number1 = float(entry1.get())
    number2 = float(entry2.get())
    try:
         subtracted = number1 - number2
         result.config(text = f"Result: {subtracted}")
    except ValueError :
        result.config(text = "Result: Please enter a valid number")


def multiply():
    number1 = float(entry1.get())
    number2 = float(entry2.get())
    try:

         multipled = number1 * number2
         result.config(text = f"Result: {multipled}")
    except ValueError :
        result.config(text = "Result: Please enter a valid number")


def divide():
    number1 = float(entry1.get())
    number2 = float(entry2.get())
    try:
         divided = number1/number2
         result.config(text = f"Result: {divided}")
    except ValueError :
        result.config(text = "Result: Cannot divide by zero")

add_button = tk.Button(root , text = "Add" , command = add)
add_button.pack(pady=10)

subtract_button = tk.Button(root , text = "Subtract" , command = subtract)
subtract_button.pack(pady=10)

multiply_button = tk.Button(root , text = "Multiply" , command = multiply)
multiply_button.pack(pady=10)

divide_button = tk.Button(root , text = "Divide" , command = divide)
divide_button.pack(pady=10)


root.mainloop()
