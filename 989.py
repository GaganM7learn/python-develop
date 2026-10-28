import tkinter as tk 

root = tk.Tk()
root.title("Monthly Savings Calculator")
root.geometry("350x250")

tk.Label(root , text = "Monthly Savings").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root , text = "Number of months ").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

result = tk.Label(root , text = "Total Savings:")
result.pack(pady=5)

def calculate_savings():
    try :
        monthly = float(entry1.get())
        months = int(entry2.get())

        if monthly < 0 or months <= 0 :
            result.config(text = "Enter valid positive values")
            return

        total = 0

        for month in range(months) :
            total += monthly

        result.config(text = f"Total Savings: {total:.2f}")

    except ValueError :
        result.config(text = "Please enter valid numbers")

tk.Button(
    root , 
    text = "Calculate Savings" ,
    command = calculate_savings
).pack(pady=5)


root.mainloop()