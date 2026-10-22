import tkinter as tk

root = tk.Tk()
root.title("Temperature Adjuster")
root.geometry("500x300")

count = tk.IntVar(value=20)

label = tk.Label(
    root ,
    textvariable=count ,
    font=("Arial" , 20)

)

label.pack(pady=20)

def increasefun():
    count.set(count.get() + 1)

def decreasefun():
    count.set(count.get() - 1 )

button1 = tk.Button(
    root ,
    text = "Increase",
    command=increasefun
)
button1.pack(pady=5)

button2 = tk.Button(
    root ,
    text="Decrease",
    command = decreasefun
)
button2.pack(pady=5)


root.mainloop()