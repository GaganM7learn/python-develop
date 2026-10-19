import tkinter as tk

root = tk.Tk()

root.title("Spacing App")
root.geometry("400x250")

label = tk.Label(root , text ="Welcome!")
label.pack(pady=20)


button = tk.Button(root , text = "Click Me")
button.pack(padx=30,pady=10)

root.mainloop()