import tkinter as tk
from tkinter import messagebox

main_color = "#87ceeb"

def calculate_sum():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 + num2
        messagebox.showinfo("Sum Result", f"The sum is: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def calculate_difference():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 - num2
        messagebox.showinfo("Difference Result", f"The difference is: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def calculate_product():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 * num2
        messagebox.showinfo("Product Result", f"The product is: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def calculate_quotient():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num2 != 0:
            result = num1 / num2
            messagebox.showinfo("Quotient Result", f"The quotient is: {result}")
        else:
            messagebox.showerror("Error", "Division by zero is not allowed.")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def clear():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)

# Create tkinter window
root = tk.Tk()
root.title("Pretty Calculator")
root.geometry("500x350")
root.config(bg=main_color)

# Create and style labels and entry widgets for input
label_num1 = tk.Label(root, text="Enter first number:", bg=main_color, font=("Helvetica", 12))
label_num1.pack(pady=10)

entry_num1 = tk.Entry(root, font=("Helvetica", 12), bd=2, relief="groove")
entry_num1.pack(pady=5)

label_num2 = tk.Label(root, text="Enter second number:", bg=main_color, font=("Helvetica", 12))
label_num2.pack(pady=10)

entry_num2 = tk.Entry(root, font=("Helvetica", 12), bd=2, relief="groove")
entry_num2.pack(pady=5)

# Create a frame to hold the buttons
button_frame = tk.Frame(root, bg=main_color)
button_frame.pack(pady=20)

# Create and style buttons with fixed sizes
button_width = 10  # fixed width
button_height = 2  # fixed height

sum_button = tk.Button(button_frame, text="Sum", command=calculate_sum, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), relief="raised", bd=3, width=button_width, height=button_height)
sum_button.pack(side=tk.LEFT, padx=5)

difference_button = tk.Button(button_frame, text="Difference", command=calculate_difference, bg="#FF9800", fg="white", font=("Helvetica", 12, "bold"), relief="raised", bd=3, width=button_width, height=button_height)
difference_button.pack(side=tk.LEFT, padx=5)

product_button = tk.Button(button_frame, text="Product", command=calculate_product, bg="#2196F3", fg="white", font=("Helvetica", 12, "bold"), relief="raised", bd=3, width=button_width, height=button_height)
product_button.pack(side=tk.LEFT, padx=5)

quotient_button = tk.Button(button_frame, text="Quotient", command=calculate_quotient, bg="#9C27B0", fg="white", font=("Helvetica", 12, "bold"), relief="raised", bd=3, width=button_width, height=button_height)
quotient_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(root, text="Clear", command=clear, bg="#f44336", fg="white", font=("Helvetica", 12, "bold"), relief="raised", bd=3, width=button_width, height=button_height)
clear_button.pack(pady=20)

# Run the tkinter main loop
root.mainloop()
