import tkinter as tk

def change_background():
    root.config(bg="lightblue")

root = tk.Tk()
root.title("Background Changer")
root.geometry("500x300")

button = tk.Button(
    root,
    text="Change Background",
    command=change_background
)

button.pack(pady=20)

root.mainloop()