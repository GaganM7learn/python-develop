import tkinter as tk
root = tk.Tk()

root.title("Styled Label")
root.geometry("400x250")

label = tk.Label(
    root,
    text="Learn Python!",
    fg="blue",
    font=("Arial" , 30)
)

label.pack()
root.mainloop()