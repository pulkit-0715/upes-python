import math

print("Enter values of sides")

a = int(input("Side 1: "))
b = int(input("Side 2: "))
c = int(input("Side 3: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle sides")
    exit(0)

s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(f"Area: {area:.2f} square units")
