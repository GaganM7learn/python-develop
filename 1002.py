import tkinter as tk

root = tk.Tk()
root.title("Countdown Timer")
root.geometry("350x300")

seconds = 0
running = False

time_entry = tk.Entry(root, font=("Arial", 14))
time_entry.pack(pady=10)

time_label = tk.Label(
    root,
    text="00:00",
    font=("Arial", 30)
)
time_label.pack(pady=15)

def update_timer():
    global seconds

    if running and seconds > 0:
        seconds -= 1

        mins = seconds // 60
        secs = seconds % 60

        time_label.config(text=f"{mins:02d}:{secs:02d}")

        root.after(1000, update_timer)

    elif seconds == 0:
        time_label.config(text="Time's Up!")

def start():
    global seconds, running

    if not running:
        try:
            seconds = int(time_entry.get())

            if seconds <= 0:
                time_label.config(text="Enter positive seconds!")
                return

            running = True
            update_timer()

        except ValueError:
            time_label.config(text="Enter a valid number!")

def stop():
    global running
    running = False

def reset():
    global seconds, running

    running = False
    seconds = 0
    time_entry.delete(0, tk.END)
    time_label.config(text="00:00")

start_button = tk.Button(root, text="Start", command=start)
start_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop", command=stop)
stop_button.pack(pady=5)

reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.pack(pady=5)

root.mainloop()