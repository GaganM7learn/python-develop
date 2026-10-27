import tkinter as tk

root = tk.Tk()
root.title("Celsius to Fahrenheit")
root.geometry("350x250")

tk.Label(root , text="Temperature in celsius").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=10)

result = tk.Label(root , text = "Fahrenheit: ")
result.pack(pady=10)

def convert():
    try :
        celsius = float(entry.get())
        fahrenheit = (celsius * 9/5) + 32
        result.config(text = f"Fahrenheit: {fahrenheit:.2f}")

    except ValueError :
        result.config(text="Enter a valid temperature")

tk.Button(root , text = "Convert" , command = convert).pack(pady=5)

root.mainloop()