import tkinter as tk 
root = tk.Tk()
root.title("Username Status")
root.geometry("400x300")

entry = tk.Entry(root , width = 25 )
entry.pack(pady=10)

result = tk.Label( 
    root ,
    text = "Enter a username"
)
result.pack(pady=10)

def check_username(*args) :
    username = entry.get()
    if len(username) < 4 :
        result.config(text = "Username is too short .")
    elif len(username) <= 12:
        result.config(text = "username length accepted !")
    else :
        result.config(text = "Username is too long.")

entry.bind("<KeyRelease>" , check_username)


root.mainloop()
