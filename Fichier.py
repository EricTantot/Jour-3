import os

def clear():
    os.system("cls")

def lire(fichier):
    clear()
    file = open(fichier,'rt')
    texte = file.read()
    print(texte)
    a = input()
    file.close()

def modif(fichier):
    file = open(fichier, 'at')
    while 0 < 1:
        clear()
        text = input("Entrer votre texte: (entrer pour aller à la ligne): ")
        if text == '':
            file.close()
            break
        else: 
            file.write(text + "\n")

fichier = input("Entrer le nom du fichier: ")

if fichier:
    clear()
    choix = input("""1. Lire le fichier
2. Modifier le fichier
                  
Choix: """)
    
    if choix == "1":
        lire(fichier)
    if choix == "2":
        modif(fichier)

else: 
    print("Fichier non trouvé.")