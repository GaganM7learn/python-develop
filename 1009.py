import tkinter as tk

from time import strftime

root = tk.Tk()
root.title("12 - Hour Digital Clock")
root.geometry("350x200")
root.configure(background= "black")


clock_label = tk.Label(
    root ,
    font = ("Arial" , 40 , "bold") ,
    foreground = "white" , 
    background = "black"
)
clock_label.pack(pady=50)

def update_clock():
    current_time = strftime("%I:%M:%S:%p")
    clock_label.config(text =current_time)
    root.after(1000 , update_clock)


update_clock()

root.mainloop()