import tkinter as tk

root = tk.Tk()
root.title("Character Counter")
root.geometry("400x300")

entry = tk.Entry(root , width=25)
entry.pack(pady=10)

result = tk.Label(root , text = "CharacterS: 0")
result.pack(pady=10)

def count_characters():
    text = entry.get()
    result.config(text=f"Characters: {len(text)}")


button = tk.Button(
    root ,
    text = "Count Characters" ,
    command = count_characters
)
button.pack(pady=10)


root.mainloop()