import math

'''
To find a triangle's arear using heron's formula
'''

print("Enter values of sides")

'''a,b,c are sides of triangle'''

a = int(input("Side 1: "))
b = int(input("Side 2: "))
c = int(input("Side 3: "))

'''checking is sides are valid or not'''
if a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle sides")
    exit(0)

'''heron's formula'''

s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

'''printing area'''
print(f"Area: {area:.2f} square units")
