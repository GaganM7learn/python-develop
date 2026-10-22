import tkinter as tk
root = tk.Tk()
root.title("Message     Editor")
root.geometry("400x250")

entry = tk.Entry(root)
entry.pack(pady=15)

def functionclear():
    entry.delete( 0 , tk.END)

button = tk.Button(
    root ,
    text="Clear" , 
    command=functionclear
)
button.pack()

root.mainloop()