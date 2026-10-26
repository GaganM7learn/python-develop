import tkinter as tk

root = tk.Tk()
root.title("Amagram Chech")
root.geometry("400x300")

entry1 = tk.Entry(root , width = 30)
entry1.pack(pady=10)
entry2 = tk.Entry(root , width = 30)
entry2.pack(pady=10)

result = tk.Label(root , text = "Enter two words")
result.pack(pady=10)

def check_anagram(*args):
    text1 = entry1.get().replace(' ' , "").lower()
    text2 = entry2.get().replace(" " , "").lower()

    if text1 !="" and text2 != "" and sorted(text1) == sorted(text2) :
        result.config(text = "They are anagrams!")

    else :
        result.config( text = "Not anagrams.")

entry1.bind("<KeyRelease>" , check_anagram)
entry2.bind("<KeyRelease>" , check_anagram)

root.mainloop()