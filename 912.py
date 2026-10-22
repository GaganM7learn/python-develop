import tkinter as tk

root = tk.Tk()
root.title("Clear Input")
root.geometry("400x250")

entry = tk.Entry(root)
entry.pack(pady=15)

def clear_input():
    entry.delete( 0 , tk.END)


button = tk.Button(
    root ,
    text="Clear",
    command=clear_input
)

button.pack(pady=10)

root.mainloop()