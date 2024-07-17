import tkinter as tk

root = tk.Tk()
root.title("Bivek Thapa")
root.geometry("750x400")

def on_button_click():
    label.config(text = "Button Clicked")

label = tk.Label(root, text="Welcome")
label.pack(pady=20)

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Run 
root.mainloop()