import tkinter as tk
# from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Scrollable Text Window")
root.geometry("400x300")

# Create a frame for the scrollbar and text widget
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Add a scrollbar to the frame
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Add a Text widget to the frame
text = tk.Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set, font=("Helvetica", 12), padx=10, pady=10)
text.pack(fill=tk.BOTH, expand=True)

# Configure the scrollbar
scrollbar.config(command=text.yview)

# Insert a long paragraph into the text widget
long_paragraph = """\
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus imperdiet, nulla et dictum interdum, nisi lorem egestas odio, vitae scelerisque enim ligula venenatis dolor. 
Maecenas nisl est, ultrices nec congue eget, auctor vitae massa. Fusce luctus vestibulum augue ut aliquet. Nunc sagittis dictum nisi, sed ullamcorper ipsum dignissim ac. 
In at libero sed nunc venenatis imperdiet sed ornare turpis. Donec vitae dui eget tellus gravida venenatis. Integer fringilla congue eros non fermentum. Sed dapibus pulvinar nibh tempor porta. 
Cras ac leo purus. Mauris quis diam velit.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus imperdiet, nulla et dictum interdum, nisi lorem egestas odio, vitae scelerisque enim ligula venenatis dolor. 
Maecenas nisl est, ultrices nec congue eget, auctor vitae massa. Fusce luctus vestibulum augue ut aliquet. Nunc sagittis dictum nisi, sed ullamcorper ipsum dignissim ac. 
In at libero sed nunc venenatis imperdiet sed ornare turpis. Donec vitae dui eget tellus gravida venenatis. Integer fringilla congue eros non fermentum. Sed dapibus pulvinar nibh tempor porta. 
Cras ac leo purus. Mauris quis diam velit.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus imperdiet, nulla et dictum interdum, nisi lorem egestas odio, vitae scelerisque enim ligula venenatis dolor. 
Maecenas nisl est, ultrices nec congue eget, auctor vitae massa. Fusce luctus vestibulum augue ut aliquet. Nunc sagittis dictum nisi, sed ullamcorper ipsum dignissim ac. 
In at libero sed nunc venenatis imperdiet sed ornare turpis. Donec vitae dui eget tellus gravida venenatis. Integer fringilla congue eros non fermentum. Sed dapibus pulvinar nibh tempor porta. 
Cras ac leo purus. Mauris quis diam velit.
"""

text.insert(tk.END, long_paragraph)

# Start the tkinter main loop
root.mainloop()
