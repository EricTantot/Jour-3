import random

print("Mémorisez un nombre entre 1 et 100, je vais essayer de le retrouver...")
a = input("Appuyer sur entrer quand vous êtes prêt et ne trichez pas ensuite.")

result = []

x = 0

plus = 100
moins = 0

def ask(moins, plus, tested):
    x = 0
    while x < 1:
        out = random.randint(moins,plus)
        if out in tested:
            x = x + 0
        else: 
            x = x + 1
    return out

    
z = 0

def check_plus(plus, essai, z):
    if essai > plus:
        z = 1
        return(z) 
    elif essai == (plus - 1):
        z = 1
        return(z)    
    else: 
        return(z)

def check_moins(moins, essai, z):
    if essai < moins:
        z = z + 1
        return(z)
    elif essai == (moins + 1):
        z = z + 1
        return(z)
    else:
        z = z + 0
        return(z)
    

while result != "G":
    test = ask(moins,plus, result)
    result.append(test)
    x = x + 1
    question = input(f"Je propose {test}... + / - / G: ")
    if question == "+":
        z = check_plus(plus, test, z)
        
        if z == 1:
            print(f"Tricheur !!! Quand j'ai proposé {plus} vous m'avez dis - donc {test} ne peut pas être + !!!")
            print(f"J'ai gagné par forfait en {x} coups !!!")
            break
        else : 
            moins = test
    elif question == '-':
        z = check_moins(moins,test,z)
        if z == 1:
            print(f"Tricheur !!! Quand j'ai proposé {moins} vous m'avez dis + donc {test} ne peut pas être - !!!")
            print(f"J'ai gagné par forfait en {x} coups !!!")
            break
        else: 
            plus = test
    elif question == "G": 
        print(f"J'ai trouvé {test} en {x} coups !!!") 
        break
    else: 
        print("Veuillez fournir une entrée valide.")
        break