import tkinter as tk
from tkinter import messagebox

def get_sum():
    # Get value from textbox
    value1 = entry1.get()+"+"+entry2.get() # Get values from entry 1 textbox
    # value2 = float(entry2.get())
    result = eval(value1)
    messagebox.showinfo("Result",f"The sum is {result}")

def get_difference():
    # Get value from textbox
    value1 = float(entry1.get()) # Get values from entry 1 textbox
    value2 = float(entry2.get())
    result = value1 - value2
    messagebox.showinfo("Result",f"The difference is {result}")

def get_multiply():
    # Get value from textbox
    value1 = float(entry1.get()) # Get values from entry 1 textbox
    value2 = float(entry2.get())
    result = value1 * value2
    messagebox.showinfo("Result",f"The product is {result}")

def get_divide():
    # Get value from textbox
    value1 = float(entry1.get()) # Get values from entry 1 textbox
    value2 = float(entry2.get())
    result = value1 / value2
    messagebox.showinfo("Result",f"The quotient is {result}")

# Main screen
root = tk.Tk()
root.title("Python Calculator")
root.geometry("300x500")

# For First Number
label1 = tk.Label(root, text="Enter first number:")
label1.pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

# For Second Number
label2 = tk.Label(root, text="Enter second number:")
label2.pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Button
sum_button = tk.Button(root, text="Sum", command=get_sum)
sum_button.pack(pady=5)
dif_button = tk.Button(root, text="Difference", command=get_difference)
dif_button.pack(pady=5)
mul_button = tk.Button(root, text="Multiply", command=get_multiply)
mul_button.pack(pady=5)
div_button = tk.Button(root, text="Divide", command=get_divide)
div_button.pack(pady=5)

# Run the program
root.mainloop()