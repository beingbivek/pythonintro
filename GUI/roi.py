import tkinter as tk

def find_roi():
    invest = float(entry1.get())
    income = float(entry2.get())
    profit = income - invest
    result = profit / invest * 100
    resultlabel.config(text = f"The ROI is {result}%")

root = tk.Tk()
root.geometry("300x200")
root.title("ROI Finder")

label1 = tk.Label(root, text="Enter Investment")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()
label2 = tk.Label(root, text="Enter Income")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()
button = tk.Button(root, text="Calculate", command=find_roi)
button.pack()
resultlabel = tk.Label(root, text="Result")
resultlabel.pack()

root.mainloop()