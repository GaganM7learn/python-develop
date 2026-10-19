import tkinter as tk

root = tk.Tk()
root.title("Position App")
root.geometry("500x300")

label = tk.Label(
    root , 
    text = "I'm on the right!"
)
label.pack(anchor="ne" , padx=20 , pady=20)

root.mainloop()