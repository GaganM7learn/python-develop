import tkinter as tk

root = tk.Tk()
root.title("Countdown Counter")
root.geometry("300x200")

result = tk.Label(root , text = "Ready!" , font = ("Arial" , 18))
result.pack(pady=5)

def countdown():
    number = 5