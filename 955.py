import tkinter as tk

root = tk.Tk()
root.title("Palindrome Checker")
root.geometry("400x300")

entry = tk.Entry(root , width=30)
entry.pack(pady=10)

result = tk.Label(root , text = "Enter text to check")
result.pack(pady=10)

def check_palindrome(*args):
    text = entry.get().strip().lower()

    if text == text[::-1] :
        result.config(text = "It is palindrome!")
    else :
        result.config(text = "Not a palindrome.")

entry.bind("<KeyRelease>" , check_palindrome)

root.mainloop()
