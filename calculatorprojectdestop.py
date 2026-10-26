
import tkinter as tk

root = tk.Tk()
root.title("Four-Operation Calculator")
root.geometry("400x400")

tk.Label(root, text="First Number").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root, text="Second Number").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

result = tk.Label(root, text="Result: ")
result.pack(pady=10)

def add():
    try:
        number1 = float(entry1.get())
        number2 = float(entry2.get())
        result.config(text=f"Result: {number1 + number2}")
    except ValueError:
        result.config(text="Please enter valid numbers")

def subtract():
    try:
        number1 = float(entry1.get())
        number2 = float(entry2.get())
        result.config(text=f"Result: {number1 - number2}")
    except ValueError:
        result.config(text="Please enter valid numbers")

def multiply():
    try:
        number1 = float(entry1.get())
        number2 = float(entry2.get())
        result.config(text=f"Result: {number1 * number2}")
    except ValueError:
        result.config(text="Please enter valid numbers")

def divide():
    try:
        number1 = float(entry1.get())
        number2 = float(entry2.get())

        if number2 == 0:
            result.config(text="Cannot divide by zero")
        else:
            result.config(text=f"Result: {number1 / number2}")

    except ValueError:
        result.config(text="Please enter valid numbers")

tk.Button(root, text="Add", command=add).pack(pady=5)
tk.Button(root, text="Subtract", command=subtract).pack(pady=5)
tk.Button(root, text="Multiply", command=multiply).pack(pady=5)
tk.Button(root, text="Divide", command=divide).pack(pady=5)

root.mainloop()
