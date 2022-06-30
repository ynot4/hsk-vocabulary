import tkinter as tk

def resize_text(event):
    xview = event.widget.xview()
    yview = event.widget.yview()

    if xview != (0.0, 1.0) or yview != (0.0, 1.0):
        label.configure(text="it doesn't fit")
    else:
        label.configure(text="it fits")

root = tk.Tk()
label = tk.Label(root, text="")
text = tk.Text(root, wrap="none", height=4, width=20)
label.pack(side="top", fill="x")
text.pack(fill="both", expand=True)

text.bind("<Configure>", resize_text)

for i in range(10):
    if i % 4:
        text.insert("end", f"This is line {i}\n")
    else:
        text.insert("end", f"This is line {i}, and it is a little bit longer\n")
root.mainloop()