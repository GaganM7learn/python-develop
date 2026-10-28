import tkinter as tk

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x300")

tk.Label(root , text = "Weight (Kg)").pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

tk.Label(root , text = "Height (metres)").pack(pady=5)
height_entry = tk.Entry(root)
height_entry.pack(pady=5)

result = tk.Label(root , text = "BMI:")
result.pack(pady=10)

def calculate_bmi():
    try :
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0 :
            result.config(text = "Value must be greater than zero")

        else :
            bmi = weight / (height** 2 )
            result.config(text = f"BMI: {bmi:.2f}")

    except ValueError :
        result.config(text = "Please enter a valid numbers")

tk.Button(
    root ,
    text = "Calculator BMI" , 
    command = calculate_bmi
).pack(pady=5)

root.mainloop()