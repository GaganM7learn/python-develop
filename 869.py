import tkinter as tk
def change_text():
    label.config(text="Button clicked!")

root = tk.Tk()

root.title("Update Label")
root.geometry("400x250")

label = tk.Label(root , text = "Click the button below")
label.pack()

button = tk.Button(root , text = "Click Me" , command = change_text)

button.pack()
root.mainloop()