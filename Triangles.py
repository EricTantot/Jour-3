a = int(input("Entrer la longueur du côté A: "))
b = int(input("Entrer la longueur du côté B: "))
c = int(input("Entrer la longueur du côté C: "))

p = a + b + c
print(f"Voici le périmètre de votre triangle: {p}")

d = p / 2
carre = d * (d-a) * (d-b) * (d-c)
aire = carre ** 0.5

print(f"Voici l'aire de votre triangle: {aire:.2f}")
