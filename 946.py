import tkinter as tk

root = tk.Tk()

root.title("Uppercase Counter")
root.geometry("400x300")

entry = tk.Entry(root , width = 30)
entry.pack(pady=10)

result = tk.Label(root , text ="Uppercase: 0" )
result.pack(pady=10)

def count_uppercase(*args):
    text = entry.get()
    count = 0

    for character in text :
        if character.isupper():
            count += 1

    result.config(text = f"Uppercase: {count}")

entry.bind("<KeyRelease>" , count_uppercase)

root.mainloop()