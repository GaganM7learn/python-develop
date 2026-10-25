import tkinter as tk

root = tk.Tk()
root.title("Live Characters Counter")
root.geometry("400x300")

entry = tk.Entry(
    root ,
    width = 25
)
entry.pack(pady=10)

result = tk.Label(
    root ,
    text = "Length: 0 " , 

)
result.pack(pady=10)

def count_update(*args):
    text = entry.get()
    result.config(text= f"Length: {len(text)}")



root.mainloop()