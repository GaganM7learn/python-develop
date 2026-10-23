import tkinter as tk

root = tk.Tk()
root.title("Username Validator")
root.geometry("400x300")

entry = tk.Entry(
    root ,
    width = 25
)
entry.pack()

result = tk.Label(
    root ,
    text = ""
)
result.pack(ipady = 10)

def check_user():
    name = entry.get().strip()

    if name :
        result.config( text = f" Username accepted : {name}")

    else :
        result.config( text = "PLease enter your username")

button = tk.Button(
    root ,
    text = "Check Username",
    command = check_user
)
button.pack(ipady = 10)


root.mainloop()