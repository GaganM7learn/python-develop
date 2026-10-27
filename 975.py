import tkinter as tk

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x350")

tk.Label(root , text = "Temperature").pack(pady=10)

entry = tk.Entry(root , width=20)
entry.pack(pady=10)

result = tk.Label(root , text = "Result: ")
result.pack(pady=10)

def convert_C_to_F():
    try :
        celsius = float(entry.get())
        fahrenheit = (celsius*9/5)+ 32
        result.config(text= f"Result: {fahrenheit:.2f} ")

    except ValueError :
        result.config(text = "Please enter a valid input")

def convert_F_C():
    try :
        fahrenheit = float(entry.get())
        celsius = (fahrenheit - 32)*5/9
        result.config(text = f"Result: {celsius:.2f}")

    except ValueError :
        result.config(text = "Please enter a valid input")

cel_button = tk.Button(root , text = "convert to celsius" , command = convert_C_to_F)
cel_button.pack(pady=10)

fah_button = tk.Button (root , text = "convert to fahrenheit" , command = convert_F_C)
fah_button.pack(pady=10)

root.mainloop()

