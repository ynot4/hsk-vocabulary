import tkinter as tk
from PIL import Image, ImageTk

import random
from lists import eng, jyut, level, pinyin, simp, trad, yale, yalenum


class MainApp:
    def copy(self, chinese):  # assign this function to any button or any actions
        self.master.clipboard_clear()
        self.master.clipboard_append(chinese.cget("text"))

    @staticmethod
    def level_colour(level_number):
        if level_number == 1:
            level_colour = "#F8B51E"
        elif level_number == 2:
            level_colour = "#267F94"
        elif level_number == 3:
            level_colour = "#FD4F1C"
        elif level_number == 4:
            level_colour = "#BB1718"
        elif level_number == 5:
            level_colour = "#1B3E76"
        else:
            level_colour = "#6A3669"
        return level_colour

    def generate_new(self, trad_c, simp_c, jyutping, pinyin_c, border, hsk, number, english):
        rand = random.randrange(0, len(simp.l))

        trad_c.config(text=trad.l[rand])
        simp_c.config(text=simp.l[rand])
        jyutping.config(text=yalenum.l[rand])
        pinyin_c.config(text=pinyin.l[rand])
        number.config(text=level.l[rand])

        level_colour = self.level_colour(int(level.l[rand]))
        border.config(background=level_colour)
        hsk.config(bg=level_colour)
        number.config(bg=level_colour)

        english.config(state="normal")
        english.delete(1.0, "end")
        english.insert(1.0, eng.l[rand])
        english.config(state="disabled")

    def __init__(self, master):
        self.master = master
        self.master.title("HSK Vocabulary")
        self.master.geometry("900x600")

        self.master.update()
        self.header = tk.Canvas(self.master, height=100, width=self.master.winfo_width(), bg="#3298dc")
        self.header.create_text((300, 50), text="HSK Vocabulary", font=("Noto Sans", 35, "bold"), fill="white")

        self.temple = ImageTk.PhotoImage(Image.open("icons/chinese.png").resize((88, 88)))
        self.header.create_image(10, 10, anchor="nw", image=self.temple)
        self.header.pack()

        self.frame = tk.Frame(self.master)

        tk.Label(self.frame, text="Traditional: ", font=("Noto Sans", 25)).grid(row=0, column=0)
        tk.Label(self.frame, text="Simplified: ", font=("Noto Sans", 25)).grid(row=2, column=0)

        self.trad_c = tk.Label(self.frame, font=("Noto Sans HK", 60, "bold"))
        self.trad_c.grid(row=0, column=1, padx=20)
        self.simp_c = tk.Label(self.frame, font=("Noto Sans SC", 60, "bold"))
        self.simp_c.grid(row=2, column=1, padx=20)

        self.copy_icon = ImageTk.PhotoImage(Image.open("icons/copy.png").resize((40, 40)))
        self.play_icon = ImageTk.PhotoImage(Image.open("icons/play.png").resize((40, 40)))

        self.copy_trad = tk.Button(self.frame, font=("Noto Sans", 10),
                                   image=self.copy_icon, compound="center", command=lambda: self.copy(self.trad_c),
                                   borderwidth=0)
        self.copy_trad.grid(row=0, column=2, padx=10)
        self.play_trad = tk.Button(self.frame, font=("Noto Sans", 10),
                                   image=self.play_icon, compound="center", command=lambda: self.copy(self.trad_c),
                                   borderwidth=0)
        self.play_trad.grid(row=0, column=3)

        self.jyutping = tk.Label(self.frame, font=("Noto Serif", 20, "italic"))
        self.jyutping.grid(row=1, column=1)

        self.copy_simp = tk.Button(self.frame, font=("Noto Sans", 10),
                                   image=self.copy_icon, compound="center", command=lambda: self.copy(self.simp_c),
                                   borderwidth=0)
        self.copy_simp.grid(row=2, column=2, padx=10)
        self.play_simp = tk.Button(self.frame, font=("Noto Sans", 10),
                                   image=self.play_icon, compound="center", command=lambda: self.copy(self.simp_c),
                                   borderwidth=0)
        self.play_simp.grid(row=2, column=3)

        self.pinyin = tk.Label(self.frame, font=("Noto Serif", 20, "italic"))
        self.pinyin.grid(row=3, column=1)

        self.frame.pack()

        self.frame2 = tk.Frame(self.master)

        self.hsk_and_level = tk.Frame(self.frame2, bd=10)

        self.hsk_text = tk.Frame(self.hsk_and_level, width="80", height="25")
        self.hsk_text.pack_propagate(False)  # geometry information of slaves will not determine the size of frame
        self.hsk_label = tk.Label(self.hsk_text, text="HSK", font=("Noto Sans Blk", 25, "bold"), fg="white")
        self.hsk_label.pack(fill="both", expand=True)
        self.hsk_text.grid(row=0, column=0)

        self.level = tk.Frame(self.hsk_and_level, width="80", height="80")
        self.level.pack_propagate(False)  # geometry information of slaves will not determine the size of frame
        self.number = tk.Label(self.level, font=("Noto Sans Blk", 60)
                               , fg="white")
        self.number.pack(fill="both", expand=True)
        self.level.grid(row=1, column=0)

        self.english = tk.Text(self.frame2, font=("Noto Sans", 18), width=30, height=3, wrap="word", state="normal")

        self.scrollbar = tk.Scrollbar(self.frame2)
        self.scrollbar.grid(row=0, column=2, sticky="nse", padx=(0, 20))
        self.english.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.english.yview)

        self.hsk_and_level.grid(row=0, column=0)
        self.english.grid(row=0, column=1, padx=25, pady=20)

        self.new = tk.Button(self.frame2, command=lambda: self.generate_new(self.trad_c, self.simp_c, self.jyutping,
                                                                            self.pinyin, self.hsk_and_level,
                                                                            self.hsk_label, self.number, self.english),
                             text="new", font=("Noto Sans", 18))
        self.new.grid(row=0, column=3)

        self.frame2.pack()

        self.generate_new(self.trad_c, self.simp_c, self.jyutping, self.pinyin, self.hsk_and_level, self.hsk_label,
                          self.number, self.english)


if __name__ == '__main__':
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
