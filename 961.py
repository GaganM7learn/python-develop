import tkinter as tk

root = tk.Tk()
root.title("Unique Character Counter")
root.geometry("400x300")

entry = tk.Entry(root , width = 30)
entry.pack(pady=10)

result = tk.Label(root , text = "Unique characters: 0")
result.pack(pady=10)

def count_unique(*args) :
    text = entry.get().replace(" " , "").lower()
    unique_characters = set(text)

    result.config(text = f"Unique characters : {len(unique_characters)}")

entry.bind("<KeyRelease>" , count_unique)

root.mainloop()