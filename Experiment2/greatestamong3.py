import math
a=int(input("Enter 1st num"))
b=int(input("Enter 2nd num"))
c=int(input("Enter 3rd num"))

print(f"Max among 3:\t{max(a,b,c)}")
print(f"Min among 3:\t{min(a,b,c)}")
print(f"Middel among 3:\t{(a+b+c)-(max(a,b,c) + min(a,b,c))}")