import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Countdown Timer")
root.geometry("350x300")

clock_label = tk.Label(
    root ,
    font = ("Arial" , 35) ,
    foreground = "white" ,
    background = "black"

)
clock_label.pack( anchor = "center" , pady=30)


def update_timer():
    current_time = strftime("%H:%M:%S")
    clock_label.config(text = current_time)

    root.after(1000 , update_timer)

update_timer()
root.mainloop()