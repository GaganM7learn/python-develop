import tkinter as tk

def show_modify():
    city = city_entry.get()
    label.config(text= f"You live in {city}!")

root = tk.Tk()
root.title("Greeting Form")
root.geometry("500x300")

label = tk.Label(root , text = "Enter you city")
label.pack()

city_entry = tk.Entry(root)
city_entry.pack()


button = tk.Button(root , text = "Submit" , command = show_modify)
button.pack()



root.mainloop()