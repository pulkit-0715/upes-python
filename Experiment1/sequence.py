'''
To find a numbein an array
'''
seq = (10, 20, 56, 78, 89)

num = int(input("Enter the number: "))

found = False

for x in seq:
    if x == num:
        found = True
        break

if found:
    print("Present")
else:
    print("Not present")
