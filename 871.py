import tkinter as tk

def show_name():
    name = name_entry.get()
    label.config(text=f"Hello, {name}!")

root = tk.Tk()
root.title("Name App")
root.geometry("400x250")

name_entry = tk.Entry(root)
name_entry.pack()

button=tk.Button(root , text= "Submit" , command = show_name)
button.pack()

label = tk.Label(root , text = "Enter your name")
label.pack()

root.mainloop()