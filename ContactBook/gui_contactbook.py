import tkinter as tk
from tkinter import messagebox
from main import create_connection

def create_contact():
    # Get value from textbox
    con = create_connection()
    cursor = con.cursor()
    name = entry1.get()
    phone = entry2.get()
    cursor.execute("INSERT INTO contacts (name,phone) VALUES (%s,%s)",(name,phone))
    con.commit()
    con.close()
    messagebox.showinfo("Dialog Box",f"Contact added Successfully!")

# Main screen
root = tk.Tk()
root.title("Contact Book")
root.geometry("300x500")

# For Principle
label1 = tk.Label(root, text="Enter Contact Name:")
label1.pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

# For Time
label2 = tk.Label(root, text="Enter Phone No.:")
label2.pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Button
add_contact_button = tk.Button(root, text="Create", command=create_contact)
add_contact_button.pack(pady=5)

# Run the program
root.mainloop()