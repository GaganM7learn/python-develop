
import tkinter as tk

root = tk.Tk()
root.title("BMI Category Calculator")
root.geometry("400x350")

tk.Label(root, text="Weight in kilograms").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root, text="Height in metres").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

result1 = tk.Label(root, text="Category: ")
result1.pack(pady=5)

result = tk.Label(root, text="BMI: ")
result.pack(pady=5)

def calculate_bmi():
    try:
        weight = float(entry1.get())
        height = float(entry2.get())

        if weight <= 0 or height <= 0:
            result1.config(text="Enter positive values")
            result.config(text="BMI: ")
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obesity"

        result.config(text=f"BMI: {bmi:.2f}")
        result1.config(text=f"Category: {category}")

    except ValueError:
        result1.config(text="Please enter valid numbers")
        result.config(text="BMI: ")

button1 = tk.Button(
    root,
    text="Calculate BMI",
    command=calculate_bmi
)
button1.pack(pady=5)

root.mainloop()
