import tkinter as tk
import controller as c

user_text = '''
Welcome to Quotes Software
Enter
'1' for all quotes
'2' for random quote
'3' to find quote by number
'''

_isShowing = False

# Functions
def quote_id():
        q = c.showquotebyid(int(entry_id.get()))
        quotelabel.config(text=q.quote, wraplength=300)
        authorlabel.config(text=q.author, wraplength=300)

def removebuttonandentry():
     entry_id.pack_forget()
     id_button.pack_forget()

def showalldata():
     frame.pack(fill=tk.BOTH, expand=True)
     scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
     text.pack(fill=tk.BOTH, expand=True)
     scrollbar.config(command=text.yview)
     text.insert(tk.END, c.showallquotes())

def userselect():
    global _isShowing
    value = int(entry.get())
    if value == 1:
        if _isShowing:
            removebuttonandentry()
            _isShowing = False
        showalldata()
    elif value == 2:
        if _isShowing:
            removebuttonandentry()
            _isShowing = False
        randomquote = c.randomquotes()
        quotelabel.config(text=randomquote.quote, wraplength=300)
        authorlabel.config(text=randomquote.author, wraplength=300)
    elif value == 3:
        _isShowing = True
        entry_id.pack(pady=5)
        id_button.pack(pady=5)
        frame.pack_forget()
    else: quotelabel.config(text="Invalid Value"); authorlabel.config(text="")

# Initialize tkinter
root = tk.Tk()
root.title("Quotes")
root.geometry("300x400")

# View page
label = tk.Label(root, text=user_text)
label.pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)
button = tk.Button(root,text="Enter",command=userselect)
button.pack(pady=5)
quotelabel = tk.Label(root,text="")
quotelabel.pack(pady=5)
authorlabel = tk.Label(root,text="")
authorlabel.pack(pady=5)
entry_id = tk.Entry(root)
id_button = tk.Button(root,text="Enter",command=quote_id)
frame = tk.Frame(root)
scrollbar = tk.Scrollbar(frame)
text = tk.Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set, font=("Helvetica", 12), padx=10, pady=10)

# Run tkinter
root.mainloop()