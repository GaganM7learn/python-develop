import tkinter as tk

root = tk.Tk()
root.title("Character Counter")
root.geometry("400x300")

entry = tk.Entry(root , width = 30)
entry.pack(pady=10)

result = tk.Label(root , text = "Characters: 0")
result.pack(pady=10)

def count_characters(*args):
    text = entry.get()
    result.config(text = f"Characters : {len(text)}")

entry.bind("<KeyRelease>" , count_characters )

root.mainloop()
