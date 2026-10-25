import tkinter as tk


root = tk.Tk()
root.title("code validator")
root.geometry("400x300")

entry = tk.Entry(
    root ,
    width = 25 ,
    show = "*"
)
entry.pack(pady=10)

result = tk.Label(
    root ,
    text = ""
)
result.pack(pady=10)

def Password():
    password = entry.get()
    if len(password) == 4 and  password.isdigit() :
        result.config(text = "Valid four-digit PIN!")
    else :
        result.config(text = "Enter exactly 4 digit. ")

button = tk.Button(
    root ,
    text = "Check PIN" , 
    command = Password
)
button.pack(pady=10)

root.mainloop()