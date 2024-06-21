import random

def ask(moins: int, plus, tested) -> int:
    while True:
        out = random.randint(moins, plus)
        if out not in tested:
            return out

def check_plus(plus, essai, z):
    if essai > plus or essai == (plus - 1):
        return 1
    return z

def check_moins(moins, essai, z):
    if essai < moins or essai == (moins + 1):
        return z + 1
    return z

print("Mémorisez un nombre entre 1 et 100, je vais essayer de le retrouver...")
input("Appuyer sur entrer quand vous êtes prêt et ne trichez pas ensuite.")

result = []
x = 0
plus = 100
moins = 0
z = 0

while True:
    test = ask(moins, plus, result)
    result.append(test)
    x += 1
    question = input(f"Je propose {test}... + / - / G: ")

    if question == "+":
        z = check_plus(plus, test, z)
        if z == 1:
            print(f"Tricheur !!! Quand j'ai proposé {plus} vous m'avez dis - donc {test} ne peut pas être + !!!")
            print(f"J'ai gagné par forfait en {x} coups !!!")
            break
        moins = test

    elif question == '-':
        z = check_moins(moins, test, z)
        if z == 1:
            print(f"Tricheur !!! Quand j'ai proposé {moins} vous m'avez dis + donc {test} ne peut pas être - !!!")
            print(f"J'ai gagné par forfait en {x} coups !!!")
            break
        plus = test

    elif question == "G":
        print(f"J'ai trouvé {test} en {x} coups !!!")
        break

    else:
        print("Veuillez fournir une entrée valide.")
        break