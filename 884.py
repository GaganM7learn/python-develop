import tkinter as tk 

root = tk.Tk()

root.title("Anhor layout")
root.geometry("400x250")

label = tk.Label(root , text="Top Left")

label.pack(anchor="nw" , padx=30 , pady=20)

root.mainloop()

