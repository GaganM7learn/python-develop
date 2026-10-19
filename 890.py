import tkinter as tk
root = tk.Tk()
root.title("Center Button")
root.geometry("500x300")


button = tk.Button(
    root ,
    text="Click Here"

)
button.pack(expand=True)

root.mainloop()