import tkinter as tk
from time import strftime


root = tk.Tk()
root.title("Countdown of Clock")
root.geometry("350x300")

date_label = tk.Label(
    root ,
    font = ("Arial" , 18) , 
    foreground = "yellow" ,
    background = "black"
)
date_label.pack(pady=20)


time_label = tk.Label(
    root ,
    font = ("Arial" , 35) , 
    background = "black" ,
    foreground = "white"
)
time_label.pack(pady=20)


def update_clock():
    current_time = strftime("%H:%M:%S")
    current_date = strftime("%d-%m-%Y")

    time_label.config(text = current_time)
    date_label.config(text = current_date)
    root.after(1000 , update_clock)

update_clock()
root.mainloop()