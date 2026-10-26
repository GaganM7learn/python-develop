import tkinter as tk

root = tk.Tk()
root.title("Addition Calculator")
root.geometry("350x300")

tk.Label(root , text="First Number").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root , text = "Second Number").pack(pady=10)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

result = tk.Label(root , text = "Result: ")
result.pack(pady=10)


def add_numbers():
    try:
        number1 = float(entry1.get())
        number2 = float(entry2.get())
        total = number1 + number2
        result.config(text=f"Result: {total}")

    except ValueError :
        result.config(text = "Please enter a valid numbers")


button = tk.Button(root , text= "Add" , command=add_numbers)
button.pack(pady=10)

root.mainloop()