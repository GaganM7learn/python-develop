import tkinter as tk

root = tk.Tk()
root.title("Reset Counter")
root.geometry("400x250")


count = tk.IntVar(value = 0)

label = tk.Label(root , textvariable = count , font=("Arial" , 20))
label.pack(pady=10)

def increase():
    count.set(count.get() +1 )

def reset():
    count.set(0)

button1 = tk.Button(root , text="Increase" , command= increase)
button1.pack(pady=10)

button2 = tk.Button(root , text = "Reset" , command=reset)
button2.pack(pady=10)

root.mainloop()