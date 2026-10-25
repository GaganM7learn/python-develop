import tkinter as tk

root = tk.Tk()
root.title("Digit Counter")
root.geometry("400x300")


entry = tk.Entry(root , width = 30)
entry.pack(pady=10)

result = tk.Label(root , text = "Digits: 0" )
result.pack(pady=10)

def count_digits(*args):
    text = entry.get()
    num = "1234567890"
    count = 0

    for number in text:
        if number in num:
         count += 1

         result.config(text = f"Digits: {count}")

entry.bind("<KeyRelease>" , count_digits )

root.mainloop()