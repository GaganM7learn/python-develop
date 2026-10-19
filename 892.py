import tkinter as tk
root = tk.Tk()
root.title("Grow")
root.geometry("500x300")

button = tk.Button(
    root ,
    text="Grow"
)
button.pack(fill="both" , expand=True  , padx=30 , pady=20)

root.mainloop()