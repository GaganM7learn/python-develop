import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Countdown Timer")
root.geometry("350x300")

date_label = tk.Label(
    root ,
    font = ("Arial" , 18) ,
    foreground = "yellow" ,
    background = "black"
)
date_label.pack(pady=20)


time_Label = tk.Label(
    root ,
    font = ("Arial" , 35) , 
    foreground = "white" ,
    background = "black"
)
time_Label.pack()


def update_clock():
    current_time = strftime("%H:%M:%S")
    current_date = strftime("%d-%m-%Y")
    time_Label.config(text=current_time)
    date_label.config(text=current_date)

    root.after(1000 , update_clock)


update_clock()

root.mainloop()