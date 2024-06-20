import math

a = int(input("Entrer la longueur du côté A: "))
b = int(input("Entrer la longueur du côté B: "))
c = int(input("Entrer la longueur du côté C: "))

if a + b > c:
    pass
else:
    print("Votre triangle ne peut pas être construit.")

if a + c > b:
    pass
else:
    print("Votre triangle ne peut pas être construit.")

if b + c > a:
    pass
else: 
    print("Votre triangle ne peut pas être construit.")

def check(a,b,c):
    if a == b == c:
        return"Votre triangle est équilatéral."
    elif a == b or b == c or a == c:
        return"Votre triangle est isocèle."
    else:
        return"Votre triangle est quelquonque."
    
def rec(a,b,c):
    sides = sorted([a,b,c])
    x = math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)
    return(x)

print(check(a,b,c))
print(f"{'Votre triangle est rectangle.' if rec(a,b,c) else ''}")
