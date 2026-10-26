import tkinter as tk

root = tk.Tk()
root.title("Special Character Counter")
root.geometry("400x300")

entry = tk.Entry(root , width = 30)
entry.pack(pady=10)

result = tk.Label(root , text = "Special Characters: 0")
result.pack(pady=10)

def count_special_characters(*args):
    text = entry.get()
    count = 0

    for character in text :
        if not character.isalnum() and character != " " :
            count += 1 

    result.config(text = f"Special Characters: {count}")
entry.bind("<KeyRelease>" , count_special_characters)
root.mainloop()