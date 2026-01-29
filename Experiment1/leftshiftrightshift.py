'''
performing left and right shift(binary operators) a number
'''
num = int(input("Enter number: "))
n = int(input("Enter no. of shifts: "))

print(f"Left shift: {num * (2 ** n)}")
print(f"Right shift: {num // (2 ** n)}")