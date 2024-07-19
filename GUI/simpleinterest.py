import tkinter as tk
from tkinter import messagebox

def get_si():
    # Get value from textbox
    value1 = float(entry1.get())# Get values from entry 1 textbox
    value2 = float(entry2.get())
    value3 = float(entry3.get())
    result = (value1*value2*value3)/100
    messagebox.showinfo("Result",f"The SI is {result}")

# Main screen
root = tk.Tk()
root.title("Python SI Calculator")
root.geometry("300x500")

# For Principle
label1 = tk.Label(root, text="Enter Principle:")
label1.pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

# For Time
label2 = tk.Label(root, text="Enter time (in yrs):")
label2.pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# For Rate
label3 = tk.Label(root, text="Enter rate:")
label3.pack(pady=5)
entry3 = tk.Entry(root)
entry3.pack(pady=5)

# Button
sum_button = tk.Button(root, text="Calculate", command=get_si)
sum_button.pack(pady=5)

# Run the program
root.mainloop()