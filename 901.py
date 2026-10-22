import tkinter as tk

root = tk.Tk()
root.title("Dowload Status")
root.geometry("500x300")

message = tk.StringVar()
message.set("Dowload: 0%")

label = tk.Label( root , textvariable=message )

label.pack()

def change_message():
    message.set("Dowload: 100%")

button = tk.Button(
    root ,
    text="Complete",
    command=change_message
)
button.pack(pady=20)

root.mainloop()


