
import tkinter as tk

root = tk.Tk()
root.title("Savings Goal Calculator")
root.geometry("400x300")

tk.Label(root, text="Monthly Savings").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root, text="Savings Goal").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

result1 = tk.Label(root, text="Months Needed: ")
result1.pack(pady=5)

def calculate_savings():
    try:
        monthly = float(entry1.get())
        goal = float(entry2.get())

        if monthly <= 0 or goal <= 0:
            result1.config(text="Enter positive values")
            return

        total = 0
        months = 0

        while total < goal:
            total += monthly
            months += 1

        result1.config(text=f"Months Needed: {months}")

    except ValueError:
        result1.config(text="Please enter valid numbers")

tk.Button(
    root,
    text="Calculate Months",
    command=calculate_savings
).pack(pady=5)

root.mainloop()
