import tkinter as tk

root = tk.Tk()
root.title("Duplicate Character Checker")
root.geometry("400x300")

entry = tk.Entry(root , width =30)
entry.pack(pady=10)

result = tk.Label(root , text = "Enter some text")
result.pack(pady=10)


def check_dupliacted(*args):
    text = entry.get().replace(" " , "").lower()

    if len(text) != len(set(text)) and text != "":
        result.config(text = "Duplicate characters found")

    else :
        result.config(text = "No dupliacte characters")

entry.bind("<KeyRelease>" , check_dupliacted)

root.mainloop()