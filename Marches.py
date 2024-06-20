def hauteurParcourue(a,b):
    x = ((a * b) * 2) * 7
    y = x / 100
    print(f"Pour {a} marches de {b} cm, il parcourt {y:.2f} m par semaine.")

a = int(input("Entrer le nombre de marches: "))
b = int(input("Entrer la hauteur d'une marche en cm: "))

hauteurParcourue(a,b)
