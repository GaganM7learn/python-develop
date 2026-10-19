import tkinter as tk

root = tk.Tk()
root.title("Button Layout")
root.geometry("500x300")


button1 = tk.Button(root , text="first")
button1.pack(side="left" , padx=30)

button2 = tk.Button(root, text="Second")
button2.pack(side="right" , padx= 30)


root.mainloop()