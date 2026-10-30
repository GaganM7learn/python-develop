import tkinter as tk
## me

root = tk.Tk()
root.title('Monthly Savings Calculator Goal')
root.geometry("400x300")


tk.Label(root , text = "Monthly Savings").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)


tk.Label(root , text = "Savings Goal").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

result1 = tk.Label(root , text = "Months Needed: ")
result1.pack(pady=5)

def calculate_savings():
    try :
        monthly = float(entry1.get())
        goal = float(entry2.get())

        if monthly < 0 or goal <= 0 :
            result1.config(text = "Enter a valid positive value")

        total = goal/monthly
        ### use while loop to complete the form see next 991



        result1.config(text = f"Months Needed: {total} months")

    except ValueError :
        result1.config(text = "Please enter a valid numbers")


tk.Button(root , text = "Calculate Months" , command = calculate_savings).pack(pady=5)

root.mainloop()