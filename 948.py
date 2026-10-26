import tkinter as tk

root = tk.Tk()
root.title("Letter Counter")
root.geometry("400x300")


entry = tk.Entry(root , width = 30)
entry.pack(pady=10)

result = tk.Label(root , text = "Letters: 0")
result.pack(pady=10)

def count_letters(*args):
    text = entry.get()
    count = 0
    for character in text :
        if character.isalpha():
            count += 1
    result.config(text = f"Letters: {count}")
entry.bind("<KeyRelease>" , count_letters)
root.mainloop()