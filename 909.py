import tkinter as tk

root = tk.Tk()
root.title("Privacy Toggle")
root.geometry("400x250")

visible = tk.BooleanVar(value =False)

label = tk.Label(
    root ,
    text="your profile is visible" , 
    font=("Arial" , 16 )
)

def visiblefun():
    if visible.get():
        label.pack(pady=20)
    else :
        label.pack_forget()

checkbutton = tk.Checkbutton(
    root ,
    text = "Show profile status",
    variable = visible ,
    command = visiblefun
)
checkbutton.pack(pady=20)

root.mainloop()