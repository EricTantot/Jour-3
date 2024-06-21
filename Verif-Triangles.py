import math

def get_triangle_sides():
    sides = []
    while len(sides) < 3:
        side = int(input(f"Enter side {len(sides) + 1}: "))
        if side <= 0:
            print("Invalid input. Please enter a positive number.")
        else:
            sides.append(side)
    return sorted(sides)

def check_triangle(sides):
    a, b, c = sides
    if a + b <= c:
        print("Your triangle cannot be constructed.")
        return
    if a == b == c:
        return "Your triangle is equilateral."
    elif a == b or b == c or a == c:
        return "Your triangle is isosceles."
    else:
        return "Your triangle is scalene."

def is_rectangle(sides):
    a, b, c = sides
    return math.isclose(a**2 + b**2, c**2)

def main():
    sides = get_triangle_sides()
    print(check_triangle(sides))
    print(f"Your triangle is rectangle." if is_rectangle(sides) else "")

if __name__ == "__main__":
    main()