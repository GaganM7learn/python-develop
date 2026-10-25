import tkinter as tk

root = tk.Tk()
root.title("Lowercase Counter")
root.geometry("400x300")

entry = tk.Entry(root , width = 30)
entry.pack(pady=10)

result = tk.Label(root , text = "Lowercase: 0")
result.pack(pady=10)

def count_lowercase(*args):
    text = entry.get()
    count = 0

    for character in text :
        if character.islower():
            count += 1 
    result.config(text = f"Lowercase: {count}")

entry.bind("<KeyRelease>" , count_lowercase)

root.mainloop()