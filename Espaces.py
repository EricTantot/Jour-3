fichier = input("Entrer le nom du fichier: ")

if fichier : 
    file = open(fichier, 'rt')
    texte = file.read()
    file.close()

    out = open(fichier, 'wt')
    for i in texte:
        if i == " ":
            a = i * 3
            out.write(a)
        else:
            out.write(i)

else: 
    print("Fichier non trouvé.")

