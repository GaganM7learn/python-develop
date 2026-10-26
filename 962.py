import tkinter as tk

root = tk.Tk()
root.title("Unique Letter Counter")
root.geometry("400x300")


entry = tk.Entry(root , width = 30)
entry.pack(pady=10)

result = tk.Label(root , text = "Unique letters : 0")
result.pack(pady=10)


def count_unique(*args):
    text = entry.get()
    unique = set()
    for character in text :
        if character.isalpha():
            unique.add(character)

    result.config(text = f"Unique letters : {len(unique)}")

entry.bind("<KeyRelease>" , count_unique)

root.mainloop()