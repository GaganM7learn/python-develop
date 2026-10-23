import tkinter as tk

root = tk.Tk()
root.title("Name Validator")
root.geometry("400x300")

entry = tk.Entry ( root , width = 30)
entry.pack(pady=10)
result = tk.Label(root , text="")
result.pack(pady=10)

def submit_name():
    name = entry.get().strip()

    if name:
        result.config(text = f"Welcome , {name}!")

    else :
        result.config(text = "Please enter your name.")
button = tk.Button(
    root ,
    text = "Submit",
    command = submit_name
)

button.pack(pady=10)

root.mainloop()