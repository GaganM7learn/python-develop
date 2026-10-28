import tkinter as tk

root = tk.Tk()
root.title("BMI Category Calculator")
root.geometry("400x350")


tk.Label(root , text = "weight in kilograms").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root , text = "heigth in metres").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

result1 = tk.Label(root , text = "")
result1.pack(pady=5)

result = tk.Label(root , text = "BMI :")
result.pack(pady=5)


def calculate_bmi():
    try :
        weight = float(entry1.get())
        height = float(entry2.get())
        if weight <= 0 or height <= 0 :
            result1.config(text = "Please enter a valid number weight or height cannot be zero or lesser than zero ")


        elif weight < 18 :
            bmi = weight / (height**2)
            result1.config(text = "Underweight")
            result.config(text = f"BMI : {bmi:.2f}")

        elif weight < 25 :
            result1.config(text = "Normal")
            bmi = weight / (height**2)
            result.config(text = f"BMI : {bmi:.2f}")


        elif weight < 30 :
            bmi = weight / (height**2)
            result1.config(text = "Overweight")
            result.config(text = f"BMI : {bmi:.2f}")

        else :
            bmi = weight / (height**2)
            result1.config(text = "Obesity")
            result.config(text = f"BMI : {bmi:.2f}")

    except ValueError :
        result.config(text = "Please enter a valid number")


button1 = tk.Button(root , text = "Calculate BMI" , command = calculate_bmi)
button1.pack(pady=5)

root.mainloop()