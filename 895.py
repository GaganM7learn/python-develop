import tkinter as tk

root = tk.Tk()
root.title("My Menu")
root.geometry("500x300")

label = tk.Label(root , text="Main Menu")
label.pack(pady=10)

button1 = tk.Button(root , text="Play")
button1.pack(pady=10)

button2 = tk.Button(root , text="Settings")
button2.pack(pady=10)

button3 = tk.Button(root , text="Exit")
button3.pack(pady=10)

root.mainloop()