import tkinter as tk
root = tk.Tk()

root.title("Button App")
root.geometry("400x250")

button = tk.Button(root , text="Click Me")

button.pack()

root.mainloop()