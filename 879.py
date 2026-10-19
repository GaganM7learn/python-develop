import tkinter as tk

root = tk.Tk()
root.title("Student Portal")
root.geometry("500x300")

label = tk.Label(root , text="Welcome, Student!")
label.pack(pady=20)

button = tk.Button(
    root,
    text="Continue",
    
)
button.pack(pady = 15 , padx=20)


root.mainloop()