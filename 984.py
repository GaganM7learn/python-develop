
import tkinter as tk

root = tk.Tk()
root.title("Restaurant Bill Splitter")
root.geometry("400x350")

tk.Label(root, text="Bill Amount").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root, text="Tip Percentage").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

tk.Label(root, text="Number of People").pack(pady=5)
entry3 = tk.Entry(root)
entry3.pack(pady=5)

result1 = tk.Label(root, text="Total Bill: ")
result1.pack(pady=5)

result2 = tk.Label(root, text="Per Person: ")
result2.pack(pady=5)

def calculate_function():
    try:
        bill = float(entry1.get())
        tip_percent = float(entry2.get())
        people = int(entry3.get())

        if bill <= 0 or tip_percent <= 0 or people <= 0:
            result1.config(text="Enter positive values")
            result2.config(text="")
            return

        tip_amount = bill * tip_percent / 100
        total = bill + tip_amount
        share = total / people

        result1.config(text=f"Total Bill: {total:.2f}")
        result2.config(text=f"Per Person: {share:.2f}")

    except ValueError:
        result1.config(text="Please enter valid numbers")
        result2.config(text="")

button = tk.Button(
    root,
    text="Calculate Split",
    command=calculate_function
)
button.pack(pady=5)

root.mainloop()
