import tkinter as tk

root = tk.Tk()
root.title("Sentence Analzer ")

root.geometry("400x300")


entry = tk.Entry(root , width = 25)
entry.pack(pady=10)

result = tk.Label(root , text = "Words: 0 | Characters: 0")
result.pack(pady=10)

def count_wordscharacters(*args):
    text = entry.get()
    countword = text.split()

    result.config(text = f"Words: {len(countword)} | Characters: {len(text)}")

entry.bind("<KeyRelease>" , count_wordscharacters)

root.mainloop()