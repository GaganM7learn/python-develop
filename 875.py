import tkinter as tk

def make_red():
    status_label.config(
        text="Color changed", 
        fg="red"
    )

root = tk.Tk()
root.title("Color Changer")
root.geometry("400x250")

status_label = tk.Label(
    root,
    text = "Original text",
    font = ("Arial" , 16)
)
status_label.pack()

button = tk.Button(
    root , 
    text = "Make Red",
    command = make_red
)
button.pack()

root.mainloop()