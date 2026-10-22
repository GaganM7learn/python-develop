import tkinter as tk
def Connect_buttonfun():
    mesage_label.config(text="Status: Online")

root = tk.Tk()
root.title("Status App")
root.geometry("500x300")

mesage_label = tk.Label(
    root ,
    text="Status: Offline"

)

mesage_label.pack(pady=10)


connect_button = tk.Button(
    root ,
    text="Connect",
    command=Connect_buttonfun
)
connect_button.pack(pady=10)

root.mainloop()