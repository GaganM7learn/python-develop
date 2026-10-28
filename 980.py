import tkinter as tk

root = tk.Tk()
root.title("Shopping Discount Calculator")
root.geometry("400x350")

tk.Label(root , text = "Original  Price").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root , text = "Discount Percentage").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

tk.Label(root , text = "Tax Percentage").pack(pady=5)
entry3 = tk.Entry(root)
entry3.pack(pady=5)

result = tk.Label(root , text = "Final Total:")
result.pack(pady=5)


def calculate_function():
    try :
            price = float(entry1.get())
            discount = float(entry2.get())
            tax = float(entry3.get())
            discount_amount = price * discount / 100
            discounted_price = price - discount_amount
            tax_amount = discounted_price * tax / 100
            final_total = discounted_price + tax_amount

            if price <= 0 or discount >= 100 or tax >= 100 :
               result.config(text = "Enter a valid price and discount ")
               return



            
            discount_amount = price * discount / 100
            discounted_price = price - discount_amount
            tax_amount = discounted_price * tax / 100
            final_total = discounted_price + tax_amount


            result.config(text = f"Final Total: {final_total:.2f}")

        


    except ValueError :
          result.config(root , text = "Please enter a valid numbers")        



button = tk.Button(root , text = "Calculate Total" , command = calculate_function )
button.pack(pady=5)


root.mainloop()