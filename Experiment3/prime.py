import math

nums = int(input("Enter a number: "))

if nums == 2:
    print("Prime")
    exit()

if nums < 2 or nums % 2 == 0:
    print("Not Prime")
    exit()

for i in range(3, int(math.sqrt(nums)) + 1, 2):
    if nums % i == 0:
        print("Not Prime")
        exit()

print("Prime")