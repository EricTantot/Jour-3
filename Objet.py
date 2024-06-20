import os

def clear():
    os.system('cls')

a = int(input("Entrer les premieres coordonnées du point: "))
b = int(input("Entrer les secondes coordonnées du point: "))

point = (a,b)

clear()

choix = input("""Que voulez vous faire:
1. Afficher les coordonées du point
2. Calculer la distance de ce point par rapport à un autre point
              
Choix: """)

if choix == '1':
    print(f"Cordonnés du point: {point}")

if choix == '2':
    clear()
    c = int(input("Entrer les premieres coordonnées du point: "))
    d = int(input("Entrer les secondes coordonnées du point: "))
    clear()
    carre = (c-a)**2 + (d-b)**2
    distance = carre ** 0.5
    print(f"La distance séparant les deux points est de {distance:.3f}")
else: 
    print('Veuillez fournir un choix valide.')