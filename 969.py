import tkinter as tk

root = tk.Tk()
root.title("Simple Menu App")
root.geometry("350x250")

heading = tk.Label(root , text="Welcome!" , font=("Arial" , 18))
heading.pack(pady=10)

def show_home():
    heading.config(text="Home Page")

def show_about():
    heading.config(text="About Page")

def reset_page():
    heading.config(text = "Welcome!")

home_button = tk.Button(root , text="Home" , command=show_home)
home_button.pack(pady=10)

about_button = tk.Button(root , text = "About" , command=show_about)
about_button.pack(pady=10)

reset_button = tk.Button(root , text = "Reset" , command=reset_page)
reset_button.pack(pady=10)

root.mainloop()