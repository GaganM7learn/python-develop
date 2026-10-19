import tkinter as tk

def say_hello():
    print("Hello , Bro")

root = tk.Tk()
root.title("Click Event")
root.geometry("400x250")

button = tk.Button(
    root , 
    text="Say Hello",
    command = say_hello
)

button.pack()
root.mainloop()