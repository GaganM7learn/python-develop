import tkinter as tk
root = tk.Tk()
root.title("Button Height")
root.geometry("400x250")

button = tk.Button(root , text="Click Me")
button.pack(padx=20 , pady=20 , ipady=15)

root.mainloop()