import tkinter as tk

root = tk.Tk()
root.title("Secret Code Visibility")
root.geometry("400x300")

entry = tk.Entry(
    root ,
    width = 25 , 
    show = "*"
)
entry.pack(pady=10)

visible = tk.BooleanVar(value = False)


def code_function():
    if visible.get():
        entry.config(show="")
    else :
        entry.config(show = "*")
checkbutton = tk.Checkbutton(
    root ,
    text = "Show Secret Code",
    variable = visible ,
    command = code_function
)
checkbutton.pack(pady = 10)

root.mainloop()