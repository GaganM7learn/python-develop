import tkinter as tk

root = tk.Tk()
root.title("Text Reverser")

root.geometry("400x300")

entry = tk.Entry(root , width = 30)
entry.pack(pady=10)

result = tk.Label(root , text = "Reversed:")
result.pack(pady=10)

def reverse_text(*args):
    text = entry.get()
    reversed_text = text[::-1]
    result.config(text = f"Reversed: {reversed_text}")

entry.bind("<KeyRelease>" , reverse_text)

root.mainloop()