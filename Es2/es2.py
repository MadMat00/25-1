import re
def find_word(word, lines):
    posizioni = []
    for i, line in enumerate(lines):
        for j, w in enumerate(line):
            print(line)
            if word in re.sub(r"[^a-zA-Z0-9\s]+", '', w.lower()):
                if len(posizioni)==0:
                    posizioni=[[i+1,j+1]]
                else:
                    posizioni.append([i+1,j+1])
    return posizioni

with open("testo.txt", "r") as f:
    lines = [line.split(" ") for line in f.readlines()]
    while True:
        s = re.sub(r"[^a-zA-Z0-9]+", '', input("Parola da cercare: ")).lower()
        if s == 'q':
            break
        if len(find_word(s,lines))!=0:
            print("Parola trovata alle posizioni: ",find_word(s, lines))
        else:
            print("Parola non presente")


