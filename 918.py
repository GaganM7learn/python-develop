import tkinter as tk

root = tk.Tk()
root.title("Password Validator")
root.geometry("400x300")

entry = tk.Entry(
    root ,
    width = 25 ,
    show = "*"
)
entry.pack(pady=10)

result = tk.Label(root , text = "")
result.pack(pady=10)

def check_password():
    password = entry.get()
    if len(password) >= 8 :
        result.config(text = 'Password length accepted!')
    else :
        result.config(text = "Use at least 8 character.")


button = tk.Button(
    root ,
    text = "Check Password",
    command = check_password
)
button.pack(pady = 10)
root .mainloop()