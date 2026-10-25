import tkinter as tk

root = tk.Tk()
root.title("Email Formate Checker")
root.geometry("400x300")

entry = tk.Entry(root , width = 25 )
entry.pack(pady=10)

result = tk.Label(root , text = "Enter your Email")
result.pack(pady=10)

def check_email(*args):
    email = entry.get().strip()

    if "@" in email and "." in email :
        result.config(text = "Basic emial format accepted!")

    else :
        result.config(text = "Email must contain @ and . ")

entry.bind("<KeyRelease>" , check_email)

root.mainloop()