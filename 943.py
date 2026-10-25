import tkinter as tk

root = tk.Tk()
root.title("Vowel Counter")
root.geometry("400x300")

entry = tk.Entry(root , width= 30)
entry.pack(pady=15)

result = tk.Label(root , text = "Vowels: 0")
result.pack(pady=10)


def count_vowels(*args) :
    text = entry.get()
    vowels = "aeiou"
    count = 0

    for character in text :
        if character in vowels:
            count += 1
            result.config(text = f"Vowels: {count}")

entry.bind("<KeyRelease>" , count_vowels)

root.mainloop()