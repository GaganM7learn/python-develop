import tkinter as tk

root = tk.Tk()
root.title("Live PIN Digit Validator")
root.geometry("400x300")

entry = tk.Entry(root , width = 25 , show = "*")
entry.pack(pady=10)

result = tk.Label(root , text = "Enter a 4-digit PIN")
result.pack(pady=10)

def Validate_pin(*args):
    pin = entry.get()
    if len(pin) == 4 and pin.isdigit():
        result.config(text = "Valid PIN!")
    else :
        result.config(text="Enter exactly 4-digits.")

entry.bind("<KeyRelease>" , Validate_pin)

root.mainloop()