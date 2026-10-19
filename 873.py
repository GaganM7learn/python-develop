import tkinter as tk
def greet():
    name = name_entry.get().strip()

    if name:
        result.config(text = f"Hello,{name}!")
    else:
        result.config(text="Please enter your name .")

root = tk.Tk()
root.title("Input Validation")
root.geometry("400x250")

name_entry = tk.Entry(root)

name_entry.pack()

button = tk.Button(root , text="Greet", command=greet)
button.pack()

result = tk.Label(root , text="")
result.pack()

root.mainloop()