import tkinter as tk 
root = tk.Tk()
root.title("Live Message Checker")
root.geometry("400x300")

entry = tk.Entry(
    root , 
    width = 25 

)
entry.pack(pady=10)

result = tk.Label(root , text = "Type your message")
result.pack(pady=10)

def check_username(*args):
    username = entry.get()

    if len(username) < 5 :
        result.config(text = "Message is too short.")

    elif len(username) <= 20 :
        result.config(text = "Message is accepted!")

    else :
        result.config(text = "Message is too long .")

entry.bind("<KeyRelease>" ,  check_username )

root.mainloop()