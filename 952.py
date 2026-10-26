import tkinter as tk 

root = tk.Tk()
root.title("Text Statistics")
root.geometry("400x300")

entry = tk.Entry(root , width = 35)
entry.pack(pady=10)

result = tk.Label(root , text = "Letters: 0 | Digits: 0 | Spaces: 0 | Special: 0")

result.pack(pady=10)

def count_thetypes(*args):
    text = entry.get()
    letters = 0
    digits = 0
    spaces = 0
    specials = 0

    for character in text :
        if not character.isalnum() and character != " ":
            specials += 1
        elif character.isalpha():
            letters += 1
        elif character.isdigit():
            digits += 1
        elif character == " " :
            spaces += 1

    result.config(text = f"Letters: {letters} | Digits: {digits} | Spaces: {spaces} | Special: {specials}")        

entry.bind("<KeyRelease>" , count_thetypes)


root.mainloop()