import tkinter as tk
root = tk.Tk()
root.title("Expand and Fill")
root.geometry("400x250")


button = tk.Button(
    root ,
    text="Fill Space"

)
button.pack( fill="Both" ,expand=True , padx=20 , pady=20)

root.mainloop()