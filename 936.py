import tkinter as tk

root = tk.Tk()
root.title("Live Website Checker")
root.geometry("400x300")

entry = tk.Entry(
    root ,
    width = 25 
)
entry.pack(pady=10)

result = tk.Label(
    root ,
    text= "Enter a Website address containing a dot "
)
result.pack(pady=10)

def check_website(*args):
    address = entry.get().strip()
    if "." in address and len(address) >= 2 :
        result.config(text = "Website format accepted!")

    else :
        result.config(text = "Enter a website address containing a dot.")
entry.bind("<KeyRelease>" , check_website)

root.mainloop()