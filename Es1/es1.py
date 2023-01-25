with open("Es1\proverbio.txt", "r") as f,open("Es1\proverbio.txt", "r") as w :
    w.write("ciao")
    proverb = f.read()
    print(proverb)

with open("Es1\proverbio_pari.txt", "w") as f1, open("Es1\proverbio_dispari.txt", "w") as f2:
    for i in range(len(proverb)):
        if i % 2 == 0:
            f1.write(proverb[i])
        else:
            f2.write(proverb[i])