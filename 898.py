import tkinter as tk

def show_message():
    message_label.config(text="Button clicked!")

root = tk.Tk()
root.title("Message App")
root.geometry("400x250")

message_label = tk.Label(root , text="Waiting")
message_label.pack(pady=10)

button = tk.Button(
    root ,
    text="Click Me" , 
    command=show_message
)
button.pack(pady=10)

root.mainloop()