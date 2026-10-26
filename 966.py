import tkinter as tk

root = tk.Tk()
root.title("Sentence Statistics")
root.geometry("450x300")

entry = tk.Entry(root , width = 35)
entry.pack(pady=10)

result = tk.Label(root , text = "Words: 0 | Characters: 0")
result.pack(pady=10)

def analyze_sentence(*args):
    text = entry.get()
    words = text.split()
    characters = len(text)

    result.config(text= f"Words: {len(words)} | Characters: {characters}")

entry.bind("<KeyRelease>" , analyze_sentence)

root.mainloop()