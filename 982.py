import tkinter as tk

root = tk.Tk()
root.title("Tip Calculator")
root.geometry("350x250")


tk.Label(root , text = "Bill Amount").pack(pady=5)
bill_entry = tk.Entry(root)
bill_entry.pack(pady=5)

tk.Label(root , text = "Tip Percentage").pack(pady=5)
tip_entry = tk.Entry(root)
tip_entry.pack(pady=5)


result = tk.Label(root , text = "Total Bill: ")
result.pack(pady=5)

def calculate_tip():
    try :
        bill = float(bill_entry.get())
        tip_percent = float(tip_entry.get())

        if bill < 0 or tip_percent < 0 :
            result.config(text= "Enter non-negative values")
            return

        tip_amount = bill * tip_percent / 100
        total = bill + tip_amount

        result.config(text =f"Total Bill: {total:.2f}")

    except ValueError :
        result.config(text = "Please enter valid numbers")

tk.Button(
    root ,
    text = "Calculate Tip" , 
    command = calculate_tip
).pack(pady=5)

root.mainloop()