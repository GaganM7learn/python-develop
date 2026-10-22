import tkinter as tk

root = tk.Tk()
root.title("Greeting App")
root.geometry("400x250")

entry = tk.Entry(root)
entry.pack(pady=20)

label = tk.Label (root , text="Enter your name")
label.pack(pady = 10)

def greet():
    name = entry.get().strip()

    if name:
        label.config(text=f"Hello , {name}!")

    else :
        label.config(text="Please enter you name")

button = tk.Button(root , text="Greet Me " , command=greet)
button.pack(pady=20)

root.mainloop()