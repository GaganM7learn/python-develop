import tkinter as tk

root = tk.Tk()
root.title("Character Frequency")
root.geometry("400x300")

entry = tk.Entry(root , width = 30)
entry.pack(pady=10)

result = tk.Label(root , text = "Enter text")
result.pack(pady=10)

def count_frequency(*args):
    text = entry.get().lower()
    target = "a" 
    count = text.count(target)

    result.config(text = f"Letter 'a' appears: {count} times")

entry.bind("<KeyRelease>" , count_frequency)

root.mainloop()