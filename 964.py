import tkinter as tk

root = tk.Tk()
root.title("Letter Frequency Counter")
root.geometry("400x350")


entry = tk.Entry(root , width = 30)
entry.pack(pady=10)

entry1 = tk.Entry(root , width = 10)
entry1.pack(pady=10)

result = tk.Label(root , text = "Frequency : 0")
result.pack(pady=10)

def count_repeat(*args):
    text = entry.get().lower()
    target = entry1.get()

    if target == "" :
        result.config(text = "Enter a letter")

    else :

        count = text.count(target)
        result.config(text = f"Frequency : {count}")

entry.bind("<KeyRelease>" , count_repeat)
entry1.bind("<KeyRelease>" , count_repeat)


root.mainloop()
