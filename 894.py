import tkinter as tk
root = tk.Tk()
root.title("Vertical Layput")
root.geometry("400x250")


label = tk.Label(root , text="Choose an option")

label.pack(pady = 10)

button1 = tk.Button(root , text="Option 1")
button1.pack(pady=5)

button2 = tk.Button(root , text="Option 2")
button2.pack(pady=5)

root.mainloop()