import tkinter as tk

def find_square():
    value = float(entry.get())
    result = value * value
    resultlabel.config(text = result)

root = tk.Tk()
root.geometry("200x200")
root.title("Square Finder")

label = tk.Label(root, text="Enter Number to find square")
label.pack()
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="Calculate", command=find_square)
button.pack()
resultlabel = tk.Label(root, text="Result")
resultlabel.pack()

root.mainloop()