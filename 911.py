import tkinter as tk
root = tk.Tk()
root.title("Greeting App")
root.geometry("450x250")

entry = tk.Entry(root)
entry.pack(pady=20)

label = tk.Label(
    root ,
    text = "Enter your city :"

)
label.pack(pady=10)
def function1():
    name = entry.get().strip()

    if name :
        label.config(text = f"Welcome to {name}")

    else :
        label.config(text= "Please enter the city")

button = tk.Button(
    root ,
    text = "Submit" ,
    command = function1
)
button.pack(pady=10)

root.mainloop()