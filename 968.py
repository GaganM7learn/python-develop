import tkinter as tk

root = tk.Tk()

root.title("Text Statistics Pro")
root.geometry("450x350")

entry = tk.Entry(root , width=35)
entry.pack(pady=10)

result1 = tk.Label(root ,text = "Words: 0")
result1.pack(pady=10)

result2 = tk.Label(root , text = "Characters: 0")
result2.pack(pady=10)

result3 = tk.Label(root , text = "Unique letters: 0")
result3.pack(pady=10)

def update_label(*args):
    sentence = entry.get()
    words = sentence.lower().split()
    characters = len(sentence)
    unique_letter = set()
    for character in sentence.lower():

        if character.isalpha():
         unique_letter.add(character)

    result1.config(text= f"Words: {len(words)}")
    result2.config(text=f"Characters: {characters}")
    result3.config(text=f"Unique letters: {len(unique_letter)}")

entry.bind("<KeyRelease>" , update_label)

root.mainloop()