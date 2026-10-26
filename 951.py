import tkinter as tk

root = tk.Tk()
root.title("Character Type Analyzer")
root.geometry("400x300")

entry = tk.Entry(root , width = 30)
entry.pack(pady= 10)

result = tk.Label(root , text = "Letters: 0 | Digits: 0 | Spaces: 0")
result.pack(pady=10)

def analzer_text(*args):
    text = entry.get()
    letters = 0
    digits = 0
    spaces = 0
    for character in text :
        if character.isalpha():
            letters += 1
        elif character.isdigit():
            digits += 1
        elif character == " " :
            spaces += 1

        result.config(text = f"Letters: {letters} | Digits: {digits} | Spaces: {spaces}")



entry.bind( "<KeyRelease>" , analzer_text)

root.mainloop()