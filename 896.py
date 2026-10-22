import tkinter as tk 
def play_game():
    print("Game Started!")

def open_settings():
    print("Settings opened!")

root = tk.Tk()
root.title("Menu Actions")
root.geometry("400x250")

play_button = tk.Button(
    root ,
    text="Play",
    command=play_game
)

play_button.pack(pady=10)

settings_button = tk.Button(
    root ,
    text="Settings", 
    command=open_settings
)
settings_button.pack(pady=10)

root.mainloop()