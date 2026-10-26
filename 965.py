import tkinter as tk

root = tk.Tk()
root.title("Word Frequency Pro")
root.geometry("400x350")

entry1 = tk.Entry(root , width = 30)
entry1.pack(pady=10)

entry2 = tk.Entry(root , width = 15)
entry2.pack(pady=10)

result1 = tk.Label(root , text = "Sentence: ")
result1.pack(pady=10)

result2 = tk.Label(root , text= "Result: Enter a word")
result2.pack(pady=10)

def label_change(*args):
    sentence = entry1.get()
    words = sentence.lower().strip()
    target = entry2.get().strip().lower()
    count = words.count(target)

    if target == "" :
        result1.config(text = f"Sentence: {sentence}")
        result2.config(text = "Result: Enter a word")
    else :
        result1.config(text=f"Sentence: {sentence}")
        result2.config(text = f"Result : {count}")


entry1.bind("<KeyRelease>" , label_change)
entry2.bind("<KeyRelease>" , label_change)
root.mainloop()