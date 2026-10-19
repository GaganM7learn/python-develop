import tkinter as tk
root = tk.Tk()
root.title("Fill Layout")
root.geometry("400x250")

button = tk.Button(root , text="Stretch Across")
button.pack(fill="x" , padx = 4 , pady = 10)

root.mainloop()