import tkinter as tk

root = tk.Tk()
root.title("Username Length Counter")
root.geometry("400x300")

entry = tk.Entry(
    root ,
    width = 25
)
entry.pack(pady=10)

result = tk.Label(
    root ,
    text = "Length: 0"
)
result.pack(pady=10)


def check_characters():
    nochar = entry.get()
    result.config(text = f"Length: {len(nochar)}")

button = tk.Button(
    root ,
    text = "Check Length" ,
    command = check_characters
)
button.pack(pady=10)

root.mainloop()