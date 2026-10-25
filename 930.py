import tkinter as tk

root = tk.Tk()
root.title("Live PIN Checker")
root.geometry("400x300")

entry = tk.Entry(
    root ,
    width = 25 ,
    show = "*"
)
entry.pack(pady=10)

result = tk.Label(
    root ,
    text = "Enter a 4-digit PIN" 
)
result.pack(pady=10)

def password_check(*args):
    password = entry.get()

    if len(password) == 4 :
        result.config(text = "Pin length accepted")

    else :
        result.config(text= "Pin must contain exactly 4 characters")

entry.bind("<KeyRelease>" , password_check )

root.mainloop()