import tkinter as tk
def change_background():
    root.config(
        bg="Black"
    )
    background.config(
        bg="black",
        fg="white"
    )

root = tk.Tk()
root.title("My Theme App")
root.geometry("500x300")

background = tk.Label(
    root , 
    text = "Welcome to my app"
)
background.pack()

button = tk.Button(
    root,
    text="Dark Theme",
    command = change_background

)
button.pack()

root.mainloop()