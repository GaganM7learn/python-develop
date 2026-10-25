import tkinter as tk

root = tk.Tk()
root.title("Lower Converter")

root.geometry("400x300")

entry = tk.Entry(root , width = 25 )

entry.pack(pady=10)

result = tk.Label(root , text = "Type something")
result.pack(pady=10)

def convert_to_upper(*args):
    upperCharacter = entry.get().strip()
    result.config(text = upperCharacter.lower())

entry.bind("<KeyRelease>" , convert_to_upper)

root.mainloop()