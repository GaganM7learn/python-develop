import tkinter as tk

root = tk.Tk()
root.title("Mini Navigation App")
root.geometry("400x300")

heading = tk.Label(root , text = "Choose a Page")
heading.pack(pady=10)

def show_home():
    heading.config(text = "Home Page")

def show_profile():
    heading.config(text = "Profile Page")

def show_settings():
    heading.config(text="Settings Page")
def show_reset():
    heading.config(text = "Choose a Page")    
    
home_button = tk.Button(root , text = "Home" , command = show_home)
home_button.pack(pady=10)

profile_button = tk.Button(root , text="Profile" , command = show_profile)
profile_button.pack(pady=10)

settings_button = tk.Button(root , text= "Settings" , command = show_settings)
settings_button.pack(pady=10)

reset_button = tk.Button(root , text = "Reset" , command = show_reset)
reset_button.pack(pady=10)

root.mainloop()