import math

def calculate_hypotenuse(a, b):
    """
    Calculate the length of hypotenuse using Pythagoras theorem
    c = sqrt(a² + b²)
    """
    return math.sqrt(a**2 + b**2)

side1, side2 = 3, 4
hypotenuse1 = calculate_hypotenuse(side1, side2)
print(f"Triangle with sides {side1} and {side2}:")
print(f"Hypotenuse: {hypotenuse1}")
