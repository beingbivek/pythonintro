import tkinter as tk
from tkinter import messagebox

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        entry.delete(0, tk.END)

# Create tkinter window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.resizable(0, 0)
root.config(bg="#f0f0f0")

# Entry widget to display calculations
entry = tk.Entry(root, font=("Helvetica", 20), bd=10, insertwidth=2, width=14, borderwidth=4, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, pady=20)

# Button text and position
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 1, 4)
]

# Create and position buttons
for button in buttons:
    text = button[0]
    row = button[1]
    col = button[2]
    rowspan = button[3] if len(button) > 3 else 1
    colspan = button[4] if len(button) > 4 else 1

    if text == '=':
        btn = tk.Button(root, text=text, padx=20, pady=20, font=("Helvetica", 18), command=calculate, bg="#4CAF50", fg="white")
    elif text == 'C':
        btn = tk.Button(root, text=text, padx=20, pady=20, font=("Helvetica", 18), command=clear_entry, bg="#f44336", fg="white")
    else:
        btn = tk.Button(root, text=text, padx=20, pady=20, font=("Helvetica", 18), command=lambda value=text: button_click(value), bg="#d3d3d3")

    # btn.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, sticky="nsew") # Sticky gives no space between buttons

# Configure grid weights to make buttons resizeable
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Run the tkinter main loop
root.mainloop()
