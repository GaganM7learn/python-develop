import tkinter as tk
root = tk.Tk()
root.title("Score Counter")
root.geometry("500x300")

count = tk.IntVar()
count.set(0)

label = tk.Label(
    root , 
    textvariable=count,
    font=("Arial" , 20)
)
label.pack(pady=20)

def increase1():
    count.set(count.get() +1 )


button = tk.Button(
    root,
    text="Add Point",
    command=increase1
)

button.pack(pady=20)

root.mainloop()