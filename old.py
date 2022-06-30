import csv

simp_l = []
pinyin_l = []
eng_l = []
trad_l = []
yalenum_l = []
jyut_l = []
yale_l = []
level_l = []

with open("csv/HSK Vocabulary - All Levels.csv", encoding="utf-8-sig") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        simp = row[0]
        pinyin = row[1]
        eng = row[2]
        trad = row[3]
        yalenum = row[4]
        jyut = row[5]
        yale = row[6]
        level = row[7]

        simp_l.append(simp)
        pinyin_l.append(pinyin)
        eng_l.append(eng)
        trad_l.append(trad)
        yalenum_l.append(yalenum)
        jyut_l.append(jyut)
        yale_l.append(yale)
        level_l.append(level)

with open("lists/simp.py", "w", encoding="utf-8-sig") as file:
    file.write(f"simp_l = {simp_l}")

with open("lists/pinyin.py", "w", encoding="utf-8-sig") as file:
    file.write(f"pinyin_l = {pinyin_l}")

with open("lists/eng.py", "w", encoding="utf-8-sig") as file:
    file.write(f"eng_l = {eng_l}")

with open("lists/trad.py", "w", encoding="utf-8-sig") as file:
    file.write(f"trad_l = {trad_l}")

with open("lists/yalenum.py", "w", encoding="utf-8-sig") as file:
    file.write(f"yalenum_l = {yalenum_l}")

with open("lists/jyut.py", "w", encoding="utf-8-sig") as file:
    file.write(f"jyut_l = {jyut_l}")

with open("lists/yale.py", "w", encoding="utf-8-sig") as file:
    file.write(f"yale_l = {yale_l}")

with open("lists/level.py", "w", encoding="utf-8-sig") as file:
    file.write(f"level_l = {level_l}")