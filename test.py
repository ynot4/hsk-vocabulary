import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, bg="black")
canvas.pack()
text = canvas.create_text((100,50),text="Hello", fill='white')

def clicked():
      res = "THANKYOU "
      canvas.itemconfig(text, text=res)

tk.Button(root, text="click", command=clicked).pack()
root.mainloop()