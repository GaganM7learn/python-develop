import tkinter as tk
root = tk.Tk()

root.title("My Profile")
root.geometry("500x300")

label = tk.Label(
    root,
    text="Python Learner",
    fg="green",
    font=("Arial" , 20)
)

label.pack()

root.mainloop()