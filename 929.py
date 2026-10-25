import tkinter as tk

root = tk.Tk()
root.title("Live Password Checker")
root.geometry("400x300")

entry = tk.Entry(
    root ,
    width = 25 ,
    show = "*"
)
entry.pack(pady=10)

result = tk.Label(
    root , 
    text = "Enter at least 8 characters" , 

)
result.pack(pady=10)

def password_check(*args):
    password = entry.get()

    if len(password) >= 8 :
        result.config(text="Password Length accepted!")

    else :
        result.config(text="Password is too short!")

entry.bind("<KeyRelease>" , password_check )

root.mainloop()