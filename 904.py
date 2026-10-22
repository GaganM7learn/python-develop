import tkinter as tk
root = tk.Tk()
root.title("Counter Controls")
root.geometry("400x250")

count = tk.IntVar(value=0)


label = tk.Label(
    root ,
    textvariable=count ,
    font=("Arial" , 20)
)
label.pack(pady=20)


def increase():
    count.set(count.get() + 1)

def decrease():
    count.set(count.get() - 1)

button1 = tk.Button(root , text = "increase" , command=increase)
button1.pack(pady=5)

button2 = tk.Button(root , text="Decrease" , command=decrease)
button2.pack(pady=5)

root.mainloop()