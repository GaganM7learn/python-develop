import tkinter as tk
def play_buttonfun():
    print("Starting Game...")

def settings_buttonfun():
    print("Opening settings...")

def exit_buttonfun():
    root.destroy()

root = tk.Tk()
root.title("Action Menu")
root.geometry("500x300")

play_button = tk.Button(
    root , 
    text="Play", 
    command = play_buttonfun
)
play_button.pack(pady=10)

settings_button = tk.Button(
    root , 
    text="Settings",
    command=settings_buttonfun
)
settings_button.pack(pady=10)


Exit_button = tk.Button(
    root ,
    text="Exit" ,
    command=exit_buttonfun
)
Exit_button.pack(pady=10)


root.mainloop()