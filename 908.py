import tkinter as tk

root = tk.Tk()
root.title("Message Toggle")
root.geometry("400x250")

visible = tk.BooleanVar(value=False)

label = tk.Label(
    root , 
    text="Hello , Bro!",
    font=("Arial" , 16)
)

def toggle_message():
    if visible.get():
        label.pack(pady=20)
    else :
        label.pack_forget()

checkbox = tk.Checkbutton(
    root ,
    text="Show message",
    variable =visible,
    command = toggle_message
)
checkbox.pack(pady=20)

root.mainloop()