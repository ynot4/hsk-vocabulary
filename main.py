import tkinter as tk
import tkinter.messagebox
from PIL import Image, ImageTk
from save_dict import get_dict, save_location, get_canto_rom, get_mand

import random
from lists import eng, jyut, level, pinyin, simp, trad, yale, yalenum
from text_speech import speech


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

    def generate_new(self, trad_c, simp_c, jyutping, pinyin_c, border, hsk, number, english, selected_levels):
        checked_levels = list()
        for item in range(len(selected_levels)):
            if list(selected_levels.values())[item].get() == 1:  # if box is checked
                checked_levels.append(list(selected_levels.keys())[item][-1])  # add hsk level number to list

        rand = int()
        rand1 = rand2 = rand3 = rand4 = rand5 = rand6 = ""
        levels_selected = True
        if not checked_levels:
            levels_selected = False
            tk.messagebox.showerror(title="Error",
                                    message="Please select at least one HSK level to display words from.")

        if levels_selected:
            if "1" in checked_levels:
                pos = level.l.index('1')
                pos2 = level.l.index('2')
                rand1 = random.randrange(pos, pos2)
            if "2" in checked_levels:
                pos = level.l.index('2')
                pos2 = level.l.index('3')
                rand2 = random.randrange(pos, pos2)
            if "3" in checked_levels:
                pos = level.l.index('3')
                pos2 = level.l.index('4')
                rand3 = random.randrange(pos, pos2)
            if "4" in checked_levels:
                pos = level.l.index('4')
                pos2 = level.l.index('5')
                rand4 = random.randrange(pos, pos2)
            if "5" in checked_levels:
                pos = level.l.index('5')
                pos2 = level.l.index('6')
                rand5 = random.randrange(pos, pos2)
            if "6" in checked_levels:
                pos = level.l.index('6')
                rand6 = random.randrange(pos, len(level.l))

            rand_nums = [rand1, rand2, rand3, rand4, rand5, rand6]
            while not rand:
                rand = random.choice(rand_nums)
            rand = int(rand)

            trad_c.config(text=trad.l[rand])
            simp_c.config(text=simp.l[rand])

            global canto_rom
            if canto_rom == "Yale (Tone Numbers)":
                jyutping.config(text=yalenum.l[rand])
            elif canto_rom == "Yale (Tone Marks)":
                jyutping.config(text=yale.l[rand])
            else:
                jyutping.config(text=jyut.l[rand])

            pinyin_c.config(text=pinyin.l[rand])
            number.config(text=level.l[rand])

            level_colour = self.level_colour(int(level.l[rand]))
            border.config(background=level_colour)
            hsk.config(bg=level_colour)
            number.config(bg=level_colour)
            self.bg_colour(int(level.l[rand]))

            english.config(state="normal")
            english.delete(1.0, "end")
            english.insert(1.0, eng.l[rand])
            english.config(state="disabled")
        global rand_int
        rand_int = rand

    def bg_colour(self, level_number, *args):
        if level_number == 1:
            colour = "#fef8e9"
        elif level_number == 2:
            colour = "#e9f2f4"
        elif level_number == 3:
            colour = "#ffede8"
        elif level_number == 4:
            colour = "#f8e8e8"
        elif level_number == 5:
            colour = "#e8ecf1"
        else:
            colour = "#f0ebf0"
        self.master.config(bg=colour)
        self.frame.config(bg=colour)
        self.frame2.config(bg=colour)
        for wid in self.frame.winfo_children():
            wid.configure(bg=colour)
        for wid in self.frame3.winfo_children():
            wid.configure(bg=colour)
        self.frame3.config(bg=colour)
        self.done_button.config(bg="SystemButtonFace")

    def show_levels(self):
        if self.frame3.winfo_ismapped():
            self.frame3.place_forget()
        else:
            self.frame3.place(x=20, y=160)

    def __init__(self, master):
        self.master = master
        self.master.title("HSK Vocabulary")
        self.master.geometry("950x600")

        self.master.update()
        self.header = tk.Canvas(self.master, height=100, width=self.master.winfo_width(), bg="#3298dc")
        self.header.create_text((300, 50), text="HSK Vocabulary", font=("Noto Sans", 35, "bold"), fill="white")

        self.temple = ImageTk.PhotoImage(Image.open("icons/chinese.png").resize((88, 88)))
        self.header.create_image(10, 10, anchor="nw", image=self.temple)

        self.options = tk.Menubutton(self.header, text="Options", font=("Noto Sans SC", 25), relief="raised")
        self.options.menu = tk.Menu(self.options, tearoff=0)
        self.options["menu"] = self.options.menu
        self.options.menu.add_cascade(label="Choose HSK Levels", font=("Noto Sans", 14), command=self.show_levels)

        def set_roms(menu, index, rand, jyutping):
            global canto_rom
            canto_rom = menu.entrycget(index, "label")
            if canto_rom == "Yale (Tone Numbers)":
                jyutping.config(text=yalenum.l[rand])
            elif canto_rom == "Yale (Tone Marks)":
                jyutping.config(text=yale.l[rand])
            else:
                jyutping.config(text=jyut.l[rand])
            write_file()

        self.cantonese_roms = tk.Menu(self.header, tearoff=0)
        self.cantonese_roms.add_command(label="Jyutping", font=("Noto Sans", 10),
                                        command=lambda: set_roms(self.cantonese_roms, 0, rand_int, self.jyutping))
        self.cantonese_roms.add_command(label="Yale (Tone Numbers)", font=("Noto Sans", 10),
                                        command=lambda: set_roms(self.cantonese_roms, 1, rand_int, self.jyutping))
        self.cantonese_roms.add_command(label="Yale (Tone Marks)", font=("Noto Sans", 10),
                                        command=lambda: set_roms(self.cantonese_roms, 2, rand_int, self.jyutping))
        self.options.menu.add_cascade(label="Cantonese Romanisation", font=("Noto Sans", 14), menu=self.cantonese_roms)

        def set_mand(menu, index):
            global mand
            mand = menu.entrycget(index, "label")
            write_file()

        self.mandarin_variety = tk.Menu(self.header, tearoff=0)
        self.mandarin_variety.add_command(label="Standard Chinese", font=("Noto Sans", 10),
                                          command=lambda: set_mand(self.mandarin_variety, 0))
        self.mandarin_variety.add_command(label="Taiwanese", font=("Noto Sans", 10),
                                          command=lambda: set_mand(self.mandarin_variety, 1))
        self.options.menu.add_cascade(label="Mandarin Speech Variety", font=("Noto Sans", 14),
                                      menu=self.mandarin_variety)

        self.options.place(x=800, y=25)
        self.header.pack()

        self.frame = tk.Frame(self.master)

        tk.Label(self.frame, text="Traditional: ", font=("Noto Sans", 25)).grid(row=0, column=0, sticky="e")
        tk.Label(self.frame, text="Simplified: ", font=("Noto Sans", 25)).grid(row=2, column=0, sticky="e")

        self.trad_c = tk.Label(self.frame, font=("Noto Sans HK", 60, "bold"))
        self.trad_c.grid(row=0, column=1, padx=20)
        self.simp_c = tk.Label(self.frame, font=("Noto Sans SC", 60, "bold"))
        self.simp_c.grid(row=2, column=1, padx=20)

        self.copy_icon = ImageTk.PhotoImage(Image.open("icons/copy.png").resize((40, 40)))
        self.play_icon = ImageTk.PhotoImage(Image.open("icons/play.png").resize((40, 40)))

        self.copy_trad = tk.Button(self.frame, font=("Noto Sans", 10),
                                   image=self.copy_icon, compound="center", command=lambda: self.copy(self.trad_c),
                                   borderwidth=0)
        self.copy_trad.grid(row=0, column=3, padx=10)
        self.play_trad = tk.Button(self.frame, font=("Noto Sans", 10),
                                   image=self.play_icon, compound="center", command=lambda:
            speech(self.trad_c.cget("text"), "Cantonese", mand), borderwidth=0)
        self.play_trad.grid(row=0, column=2)

        tk.Label(self.frame, text="(Cantonese)", font=("Noto Serif", 12, "italic")).grid(row=1, column=2,
                                                                                         sticky="w")
        self.jyutping = tk.Label(self.frame, font=("Noto Serif", 20, "italic"))
        self.jyutping.grid(row=1, column=1)

        self.copy_simp = tk.Button(self.frame, font=("Noto Sans", 10),
                                   image=self.copy_icon, compound="center", command=lambda:
            self.copy(self.simp_c), borderwidth=0)
        self.copy_simp.grid(row=2, column=3, padx=10)
        self.play_simp = tk.Button(self.frame, font=("Noto Sans", 10),
                                   image=self.play_icon, compound="center", command=lambda:
            speech(self.simp_c.cget("text"), "Mandarin", mand), borderwidth=0)
        self.play_simp.grid(row=2, column=2)

        tk.Label(self.frame, text="(Mandarin)", font=("Noto Serif", 12, "italic")).grid(row=3, column=2,
                                                                                        sticky="w")
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

        self.english = tk.Text(self.frame2, font=("Noto Sans SC", 18), width=30, height=3, wrap="word", state="normal")

        self.scrollbar = tk.Scrollbar(self.frame2)
        self.scrollbar.grid(row=0, column=2, sticky="nse", padx=(0, 20))
        self.english.config(yscrollcommand=self.scrollbar.set, highlightthickness=0, borderwidth=0)
        self.scrollbar.config(command=self.english.yview)

        self.hsk_and_level.grid(row=0, column=0)
        self.english.grid(row=0, column=1, padx=25, pady=20)

        self.new = tk.Button(self.frame2, command=lambda: self.generate_new(self.trad_c, self.simp_c, self.jyutping,
                                                                            self.pinyin, self.hsk_and_level,
                                                                            self.hsk_label, self.number, self.english,
                                                                            self.dict),
                             text="new", font=("Noto Sans", 18))
        self.new.grid(row=0, column=3)

        self.frame2.pack()

        self.frame3 = tk.Frame(self.master)

        def write_file():
            self.saved_dict = "saved_dict = {"
            for item in range(len(self.dict)):
                self.saved_dict += f'"{self.hsk_levels[item]}": {list(self.dict.values())[item].get()},\n'
            self.saved_dict += "}"
            self.saved_dict += f'\ncanto_rom = "{canto_rom}"'
            self.saved_dict += f'\nmand = "{mand}"'
            with open(save_location, "w") as f:
                f.write(self.saved_dict)

        self.hsk_levels = ['HSK 1', 'HSK 2', 'HSK 3', 'HSK 4', 'HSK 5', 'HSK 6']
        self.dict_saved = get_dict()  # dictionary to store all the IntVars
        self.dict = dict()
        for option in range(len(self.hsk_levels)):
            o = self.hsk_levels[option]
            var = tk.IntVar()
            tk.Checkbutton(self.frame3, text=o, font=("Noto Sans", 15), variable=var, command=write_file).pack()
            var.set(list(self.dict_saved.values())[option])
            self.dict[o] = var  # add IntVar to the dictionary
        self.done_button = tk.Button(self.frame3, text="Done", font=("Noto Sans", 15),
                                     command=self.frame3.place_forget)
        self.done_button.pack(pady=(10, 0))
        self.frame3.place(x=20, y=160)

        self.generate_new(self.trad_c, self.simp_c, self.jyutping, self.pinyin, self.hsk_and_level, self.hsk_label,
                          self.number, self.english, self.dict)


if __name__ == '__main__':
    root = tk.Tk()
    canto_rom = get_canto_rom()
    mand = get_mand()
    rand_int = int()
    app = MainApp(root)
    root.mainloop()
