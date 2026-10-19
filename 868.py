import tkinter as tk

def show_message():
    print("Welcome to Python !")

root = tk.Tk()

root.title("Greeting App")
root.geometry("500x300")

button = tk.Button(
    root,
    text="Greet Me",
    command = show_message
)

button.pack()

root.mainloop()