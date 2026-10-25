import tkinter as tk 

root = tk.Tk()
root.title("Live Username Counter")
root.geometry("400x300")

entry = tk.Entry(
    root ,
    width = 25
)
entry.pack(pady=10)

result = tk.Label(
    root ,
    text = "Characters: 0"
)
result.pack(pady=10)


def length_fun(*args):
    length = entry.get()
    result.config(text = f"Characters: {len(length)}")

entry.bind( "<KeyRelease>" , length_fun )

root.mainloop()