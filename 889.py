import tkinter as tk
root = tk.Tk()
root.title("Expand Layout")
root.geometry("400x250")

button = tk.Button(
    root ,
    text ="Center Me"
)
button.pack(expand=True)

root.mainloop()