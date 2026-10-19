import tkinter as tk
root = tk.Tk()
root.title("Tall Button App")
root.geometry("500x300")

button = tk.Button(
    root,
    text = "Start"
)
button.pack(padx=30 , pady=15 , ipady=20)

root.mainloop()