import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Clock")
root.geometry("350x300")

time_label = tk.Label(
    root ,
    font = ("Arial" , 35 , "bold") ,
    background = "black" , 
    foreground = "white"
)
time_label.pack(pady=50)

def update_clock():
    current_time = strftime("%I:%M:%S:%p")
    time_label.config(text = current_time)

    root.after(1000 , update_clock)

update_clock()

root.mainloop()