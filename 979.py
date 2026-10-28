import tkinter as tk

root = tk.Tk()
root.title("Discount Calculator")
root.geometry("350x250")

tk.Label(root , text = "Original Price").pack(pady=5)
price_entry = tk.Entry(root)
price_entry.pack(pady=5)

tk.Label(root , text = "Discount (%)").pack(pady=5)
discount_entry = tk.Entry(root)
discount_entry.pack(pady=5)

result = tk.Label(root , text = "Final Price:")
result.pack(pady=10)

def calculate_discount():
    try :
        price = float(price_entry.get())
        discount = float(discount_entry.get())

        if price < 0 or discount < 0 or discount > 100 :
            result.config(text = "Enter valid price and discount")

            return
        final_price = price - ( price*discount / 100)

        result.config(text = f"Final Price : {final_price:2f}")

    except ValueError :
        result.config(text = "PLease enter a valid numbers")

tk.Button(
    root ,
    text = "Calculator" , 
    command = calculate_discount
).pack(pady=5)

root.mainloop()