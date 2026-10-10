ru_en = {}

with open("en-ru.txt", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    if line == "":
        continue

    line = line.replace("--", "-")

    parts = line.split(" - ")
    en_word = parts[0]
    ru_words = parts[1].split(",")
#---------------
    for ru_word in ru_words:
        ru_word = ru_word.strip()
        if ru_word not in ru_en:
            ru_en[ru_word] = []
        ru_en[ru_word].append(en_word)
#------------
with open("ru-en.txt", "w", encoding="utf-8") as f:
    for ru_word in sorted(ru_en): # сортировка
        en_list = ", ".join(ru_en[ru_word])
        f.write(f"{ru_word} -- {en_list}\n")

print("Файл сделал сальто.")