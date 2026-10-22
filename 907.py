import tkinter as tk

root = tk.Tk()
root.title("Score Manager")
root.geometry("500x300")

count = tk.IntVar(value=0)

label = tk.Label(
    root , 
    textvariable = count 
)
label.pack(pady=10)

def increase():
    count.set(count.get() + 1)

def reset():
    count.set(0)


button1 = tk.Button(
    root ,
    text = "increase" ,
    command = increase
)
button1.pack(pady=10)

button2 = tk.Button(
    root ,
    text = "Reset" , 
    command = reset
)
button2.pack(pady=10)

root.mainloop()