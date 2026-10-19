import tkinter as tk

root = tk.Tk()

root.title("My First Button")
root.geometry("500x300")

button = tk.Button(root , text="Start")

button.pack()

root.mainloop()