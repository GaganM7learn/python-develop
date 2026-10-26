import tkinter as tk

root = tk.Tk()
root.title("Palindrome Pro")
root.geometry("400x300")

entry = tk.Entry(root , width = 30)
entry.pack(pady=10)

result1 = tk.Label( root , text = "Original : ")
result1.pack(pady=10)


result2 = tk.Label(root , text = "Result : ")
result2.pack(pady=10)

def update_result(*args):
    text = entry.get().strip().lower()
    text1 = entry.get()
    if text == text[::-1] and text != "":
        result1.config(text = f"Original : {text1}")
        result2.config(text = f"Result : Palindrome")

    else :
        result2.config(text = "Result : Not a palindrome")
        result1.config(text = f"Original : {text1}")
entry.bind("<KeyRelease>" , update_result)


root.mainloop()
