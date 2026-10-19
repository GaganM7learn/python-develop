import tkinter as tk

root = tk.Tk()
root.title("Side Layout")
root.geometry("400x200")

button1 = tk.Button(root , text="left")
button1.pack(side="left" , padx=20)

button2 = tk.Button(root , text="right")
button2.pack(side="right" , padx=20)

root.mainloop()