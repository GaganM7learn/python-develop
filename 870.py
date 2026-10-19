import tkinter as tk

def change_label():
    label.config(text ="Status: Started")

root = tk.Tk()

root.title("Status App")
root.geometry("500x300")

label = tk.Label(root , text="Status: Waiting")

label.pack()

button = tk.Button( root , text="Start" , command=change_label)

button.pack()

root.mainloop()