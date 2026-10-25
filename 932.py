import tkinter as tk

root = tk.Tk()
root.title("Live Code Validator")
root.geometry("400x300")

entry = tk.Entry(
    root , 
    width = 25 , 
    show = "*"
)

entry.pack(pady=10)

result = tk.Label(root , text = "Enter your code")
result.pack(pady=10)

def check_password(*args):
    password = entry.get()

    if len(password) == 4 and password.isdigit():
        result.config(text = "Code accepted !")

    else :
        result.config(text = "Code must contain exactly 4c digits.")

entry.bind( "<KeyRelease>" , check_password )


root.mainloop()