import tkinter as tk 

root = tk.Tk()
root.title("Click Counter")
root.geometry("300x200")


count =  0
result = tk.Label(root , text = "Click: 0")
result.pack(pady=5)

def increase_count():
    global count
    count += 1
    result.config(text = f"Clicks: {count}")


tk.Button(
    root , 
    text = "Click Me" , 
    command = increase_count
).pack(pady=10)

root.mainloop()