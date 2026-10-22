import tkinter as tk
root = tk.Tk()
root.title("StringVar App")
root.geometry("400x250")

message = tk.StringVar()
message.set("waiting")

label = tk.Label(root , textvariable=message)
label.pack(pady=10)

def change_message():
    message.set("Message Updated!")

button = tk.Button(
    root ,
    text="Update",
    command=change_message
)

button.pack(pady=10)

root.mainloop()