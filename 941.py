import tkinter as tk
root = tk.Tk()
root.title("Word Counter")
root.geometry("400x300")
entry = tk.Entry(root , width =25 )
entry.pack(pady=10)

result = tk.Label(root , text = "Words : 0" )
result.pack(pady=10)

def count_words(*args):
    text = entry.get()

    words = text.split()

    result.config(text = f"Words : {len(words)}")

entry.bind("<KeyRelease>" , count_words)

root.mainloop()