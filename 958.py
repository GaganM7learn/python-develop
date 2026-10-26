import tkinter as tk 

root = tk.Tk()
root.title("Anagram Pro")
root.geometry("450x400")

entry1 = tk.Entry(root , width = 30)
entry1.pack(pady=10)

entry2 = tk.Entry(root , width = 30)
entry2.pack(pady=10)

result1 = tk.Label(root , text = "First :")
result1.pack(pady=10)

result2 = tk.Label(root , text = "Second :")
result2.pack(pady=10)

result3 = tk.Label(root , text = "Result : Enter two words")
result3.pack(pady=10)

def changes_in_label(*args):
    text1 = entry1.get().replace(" " , "").lower()
    text2 = entry2.get().replace(" " , "").lower()
    if text1 != "" and text2 != "" and sorted(text1) == sorted(text2) :
        result1.config(text= f"First : {text1}")
        result2.config(text = f"Second : {text2}")
        result3.config(text = "Result : Amagrams")

    else :
        result1.config(text= f"First : {text1}")
        result2.config(text = f"Second : {text2}")
        result3.config(text = "Result : Not amagrams")

entry1.bind( "<KeyRelease>" , changes_in_label)
entry2.bind( "<KeyRelease>" , changes_in_label)

root.mainloop()