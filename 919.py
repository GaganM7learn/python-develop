import tkinter as tk

root = tk.Tk()
root.title("PIN Length Checker")
root.geometry("400x300")

entry = tk.Entry(
    root ,
    width = 25 ,
    show = "*"
)
entry.pack(pady=10)

result = tk.Label(
    root ,
    text = ""
)
result.pack(pady=10)
def calculation():
    length = entry.get()

    if len(length) == 4 :
        result.config(text = "PIN length accepted!")
    else :
        result.config(text = "PIN must contain exactly 4 characters.")

button = tk.Button(
    root ,
    text = "Check PIN" , 
    command = calculation
)
button.pack(pady=10)

root.mainloop()