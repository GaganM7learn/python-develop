import tkinter as tk
root = tk.Tk()
root.title("Counter App")
root.geometry("400x250")

count = tk.IntVar()
count.set(0)

label = tk.Label(root , textvariable=count,
                 font=("Arial" , 20))

label.pack(pady=10)

def increase_count():
    count.set(count.get() + 1)

button = tk.Button(
    root,
    text="Increase",
    command= increase_count
)

button.pack(pady=10)

root.mainloop()