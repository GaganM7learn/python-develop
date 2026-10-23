import tkinter as tk

root = tk.Tk()
root.title("Message Editor")
root.geometry("400x300")

entry = tk.Entry( root , width = 10)
entry.pack(pady =10)

result = tk.Label(
    root ,
    text = ""
)
result.pack(pady=10)

def show_message():
    message = entry.get()
    result.config( text = message)

def clear_message():
    entry.delete( 0 , tk.END)
    result.config(text = "")

show_button = tk.Button(
    root ,
    text = "Show Message",
    command = show_message
)
show_button.pack(pady=10)

clear_button = tk.Button(
    root ,
    text = "clear",
    command = clear_message
)
clear_button.pack(pady=10)

root.mainloop()