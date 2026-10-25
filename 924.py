import tkinter as tk

root = tk.Tk()
root.title("Password Manager")
root.geometry("400x300")

entry = tk.Entry(root , width = 25 , show = "*")
entry.pack(pady=10)

visible = tk.BooleanVar(value = False)

def toggle_passkword():
    if visible.get():
        entry.config(show = "")
    else :
        entry.config(show = "*")

def clear_password():
    entry.delete( 0 , tk.END)
    visible.set(False)
    entry.config(show="*")

check_button = tk.Checkbutton(
    root ,
    text = "Show password" ,
    variable = visible ,
    command = toggle_passkword
)
check_button.pack(pady=10)

clear_button = tk.Button(
    root ,
    text = "Clear" , 
    command = clear_password
)
clear_button.pack(pady = 10)

root.mainloop()

