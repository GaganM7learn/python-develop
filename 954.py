import tkinter as tk

root = tk.Tk()
root.title("Text Reverser Pro")
root.geometry("400x300")

entry = tk.Entry(root , width = 30)
entry.pack(pady=10)

result_1 = tk.Label(root , text = f"Original: ")
result_1.pack(pady=10)
result2 = tk.Label(root , text = f"Reversed: ")
result2.pack(pady=10)

def reversed(*args):
    text = entry.get()
    reverse = text[::-1]
    result_1.config(text = f"Original: {text}")
    result2.config( text = f"Reversed: {reverse}")

entry.bind( "<KeyRelease>" , reversed)

root.mainloop()