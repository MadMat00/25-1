import re
import json
def crea_dizionario(lines):
    posizioni = {}
    for i, line in enumerate(lines):
        for j, w in enumerate(line):
            parola = re.sub(r"[^a-zA-Z0-9\s]+", '', w)
            posizione = (i+1, j+1)
            if parola in posizioni:
                posizioni[parola].append(posizione)
            else:
                posizioni[parola] = [posizione]
    with open("Es2\words.json", "w") as file:
                json.dump(posizioni, file,indent=4)
    return posizioni

with open("Es2\\testo.txt", "r") as f:
    lines = [line.split(" ") for line in f.readlines()]
    posizioni = crea_dizionario(lines)
    while True:
        s = re.sub(r"[^a-zA-Z0-9]+", '', input("Parola da cercare: "))
        if s == 'q':
            break
        if s in posizioni:
            print(s, "trovata alle posizioni: ", posizioni[s])
        else:
            print(s, "Parola non presente")