import tkinter as tk

root = tk.Tk()
root.title("Tall Button App")
root.geometry("500x300")

button = tk.Button(
    root ,
    text= "Start"
)
button.pack(pady=20 , padx=30 , ipady=20)


root.mainloop()