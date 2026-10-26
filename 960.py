import tkinter as tk

root = tk.Tk()
root.title("Duplicate Checher Pro")
root.geometry("400x300")


entry = tk.Entry(root , width = 30)
entry.pack(pady=10)

result = tk.Label(root , text= "Text :")
result.pack(pady=10)

result1 = tk.Label(root , text = "Result : Enter text")
result1.pack(pady=10)

def check_duplicates(*args):
    text = entry.get().replace(" " , "").lower()

    if text != "" and len(text) != len(set(text)):
        result.config(text = f"Text : {text}" )
        result1.config(text = "Result : Duplicates Found")
    else :
        result.confid(text = f"Text : {text}")
        result1.config(text = "Result : No Duplicates")


entry.bind("<KeyRelease>" , check_duplicates)

root.mainloop()