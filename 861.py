import tkinter as tk 
root = tk.Tk()

root.title("Welcome App")
root.geometry("400x250")

label = tk.Label(root , text="Welcome to Python !")

label.pack()
root.mainloop()