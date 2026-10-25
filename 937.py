import tkinter as tk

root = tk.Tk()
root.title("Upper Converter")
root.geometry("400x300")

entry = tk.Entry(root , width = 25 )

entry.pack(pady=10)

result= tk.Label(root , text = "Type something")

result.pack(pady=10)

def convert_text(*args):
    text = entry.get()
    result.config(text = text.upper())
entry.bind("<KeyRelease>"  , convert_text)

root.mainloop()