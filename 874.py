import tkinter as tk

def greet():
    username = username_entry.get().strip()
    if username :
        result.config(text = f"Welcome , {username}!")

    else:
        result.config(text = "Username required")

root = tk.Tk()
root.title("Login Form")
root.geometry("500x300")

username_entry = tk.Entry(root)
username_entry.pack()

button = tk.Button( root , text="Check Username" , command = greet)
button.pack()

result = tk.Label(root , text= "")
result.pack()

root.mainloop()
