import tkinter as tk

root = tk.Tk()
root.title("Password Visibility")
root.geometry("400x300")

entry = tk.Entry(root , width = 25 , show="*")
entry.pack(pady=15)

visible = tk.BooleanVar(value=False)

def toggle_password():
    if visible.get():
        entry.config(show="")
    else :
        entry.config(show = "*")

checkbox = tk.Checkbutton(
    root ,
    text = "Show password" , 
    variable = visible ,
    command = toggle_password
)
checkbox.pack(pady=10)

root.mainloop()