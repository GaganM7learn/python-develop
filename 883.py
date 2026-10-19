import tkinter as tk

root = tk.Tk()
root.title("Full Width Buttons")
root.geometry("500x300")

button1 = tk.Button(root , text="Save")
button1.pack(fill = "x" , padx=20 , pady=10)


button2 = tk.Button(root , text="Cancel")
button2.pack(fill="x" , padx= 20 , pady=10)


root.mainloop()