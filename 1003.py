import tkinter as tk


root = tk.Tk()
root.title("Countdown Timer")
root.geometry("350x300")

seconds = 0
going = False

time_Entry = tk.Entry(root , font = ("Arial" , 14))
time_Entry.pack(pady=10)

time_Label = tk.Label(root , text = "00:00")
time_Label.pack(pady=15)


def update_timer():
    global seconds , going
    try :
        if going and seconds >= 0 :
            seconds -= 1 

            mins = seconds // 60
            secs = seconds % 60

            time_Label.config(text = f"{mins:02d}:{secs:02d}")
            root.after(1000 , update_timer)

            if seconds == 0 :
                time_Label.config(text = "Time's Up!")


    except ValueError :
        time_Label.config(text = "Enter a valid number !")

def start():
    global seconds , going

    if not going :
        try :
            seconds = int(time_Entry.get())

            going = True
            update_timer()

        except ValueError :
            time_Label.config(text = "Enter a valid number !")

def stop():
    global going 

    going = False 

def reset():
    global seconds , going 

    going = False
    seconds = 0 
    time_Entry.delete(0 , tk.END)

    time_Label.config(text = "00:00")


start_button = tk.Button(root , text = "Start" , command = start)
start_button.pack(pady=5)

stop_button = tk.Button(root , text = "Stop" , command = stop)
stop_button.pack(pady=5)


reset_button = tk.Button(root , text = "Reset" , command = reset)
reset_button.pack(pady=5)


root.mainloop()